String cron_string = BRANCH_NAME == "master" ? "H H/12 * * *" : ""

pipeline {
  options {
    buildDiscarder(logRotator(daysToKeepStr: '10', numToKeepStr: '20'))
    disableConcurrentBuilds()
  }
  triggers{
    bitbucketPush()
    cron(cron_string)
  }
  agent { label 'pf' }
  stages {
    stage('Git') {
      steps {
        hipchatSend(color: 'GRAY', message: 'Build <a href="$BLUE_OCEAN_URL">${BUILD_DISPLAY_NAME}</a> on <a href="$JOB_URL">${JOB_NAME}</a><BR>$HIPCHAT_CHANGES_OR_CAUSE', room: 'Automation - Jenkins', v2enabled: false, sendAs: 'build0')
        // checkout scm
        checkout([$class: 'GitSCM', branches: [[name: '**']], doGenerateSubmoduleConfigurations: false, extensions: [[$class: 'LocalBranch', localBranch: "**"]], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'zlorberbaum', url: 'http://zlorberbaum@bitbucket.qumu.com/scm/qa/qe.git']]])
      }
    }
    stage('Install') {
      steps {
        withPythonEnv('python') {
          pysh(script: 'rm -rf report/*.* || true', returnStatus: false, returnStdout: false)
          pysh(script: './install.sh', returnStatus: false, returnStdout: false)
        }
      }
    }
    stage('Pre-test Sanity') {
      steps {
        withPythonEnv('python') {
          pysh(script: './run.sh -m "init or sanity" functional/init_PF_test.py functional/setup_PF_test.py functional/Stand_Alone_PFE/setup_PFEs_test.py functional/PF_sanity_test.py', returnStatus: false, returnStdout: false)
        }
      }
    }
    stage('Upgrade SUT') {
      steps {
        withPythonEnv('python') {
          pysh(script: './run.sh -m "init or upgrade" functional/init_PF_test.py functional/setup_PF_test.py functional/Stand_Alone_PFE/setup_PFEs_test.py functional/Components/setup_components_prerequisites_test.py', returnStatus: false, returnStdout: false)
        }
      }
    }
    stage('Post-upgrade Sanity') {
      steps {
        withPythonEnv('python') {
          pysh(script: './run.sh -m "init or sanity" functional/init_PF_test.py functional/setup_PF_test.py functional/Stand_Alone_PFE/setup_PFEs_test.py functional/PF_sanity_test.py', returnStatus: false, returnStdout: false)
        }
      }
    }
    stage('Broadcast & Distribution') {
      steps {
        withPythonEnv('python') {
          pysh(script: './run.sh -m "init or broadcast or distribution" functional/init_PF_test.py functional/setup_PF_test.py functional/Stand_Alone_PFE/', returnStatus: false, returnStdout: false)
        }
      }
    }
    stage('Component Tests (non-draft)') {
      steps {
        script {
          try {
            echo("Start component POST tests.")
            withPythonEnv('python') {
              pysh(script: './run.sh -m "init or (components and not draft and POST)" functional/init_PF_test.py functional/setup_PF_test.py functional/Components/', returnStatus: false, returnStdout: false, propagate: false)
            }
          }
          catch (error) {
            echo("First round component POST tests failed")
            echo("Re-running failed component POST tests.")
            catchError {
              withPythonEnv('python') {
                pysh(script: './run.sh --lf -m "init or (components and not draft and POST)" functional/init_PF_test.py functional/setup_PF_test.py functional/Components/', returnStatus: false, returnStdout: false)
              }
            }
            currentBuild.result = 'FAILURE'
            // throw error
          }
          try {
            echo("Start component GET tests.")
            withPythonEnv('python') {
              pysh(script: './run.sh -m "init or (components and not draft and GET)" functional/init_PF_test.py functional/setup_PF_test.py functional/Components/', returnStatus: false, returnStdout: false, propagate: false)
            }
          }
          catch (error) {
            echo("First round component GET tests failed")
            echo("Re-running failed component GET tests.")
            catchError {
              withPythonEnv('python') {
                pysh(script: './run.sh --lf -m "init or (components and not draft and GET)" functional/init_PF_test.py functional/setup_PF_test.py functional/Components/', returnStatus: false, returnStdout: false)
              }
            }
            currentBuild.result = 'FAILURE'
            // throw error
          }
          try {
            echo("Start component PATCH tests.")
            withPythonEnv('python') {
              pysh(script: './run.sh -m "init or (components and not draft and PATCH)" functional/init_PF_test.py functional/setup_PF_test.py functional/Components/', returnStatus: false, returnStdout: false, propagate: false)
            }
          }
          catch (error) {
            echo("First round component PATCH tests failed")
            echo("Re-running failed component PATCH tests.")
            catchError {
              withPythonEnv('python') {
                pysh(script: './run.sh --lf -m "init or (components and not draft and PATCH)" functional/init_PF_test.py functional/setup_PF_test.py functional/Components/', returnStatus: false, returnStdout: false)
              }
            }
            currentBuild.result = 'FAILURE'
            // throw error
          }
          try {
            echo("Start component other tests.")
            withPythonEnv('python') {
              pysh(script: './run.sh -m "init or (components and not draft and not GET and not POST and not PATCH and not DELETE)" functional/init_PF_test.py functional/setup_PF_test.py functional/Components/', returnStatus: false, returnStdout: false, propagate: false)
            }
          }
          catch (error) {
            echo("First round component other tests failed")
            echo("Re-running failed component other tests.")
            catchError {
              withPythonEnv('python') {
                pysh(script: './run.sh --lf -m "init or (components and not draft and not GET and not POST and not PATCH and not DELETE)" functional/init_PF_test.py functional/setup_PF_test.py functional/Components/', returnStatus: false, returnStdout: false)
              }
            }
            currentBuild.result = 'FAILURE'
            // throw error
          }
          try {
            echo("Start component DELETE tests.")
            withPythonEnv('python') {
              pysh(script: './run.sh -m "init or (components and not draft and DELETE)" functional/init_PF_test.py functional/setup_PF_test.py functional/Components/', returnStatus: false, returnStdout: false, propagate: false)
            }
          }
          catch (error) {
            echo("First round component DELETE tests failed")
            echo("Re-running failed component DELETE tests.")
            catchError {
              withPythonEnv('python') {
                pysh(script: './run.sh --lf -m "init or (components and not draft and DELETE)" functional/init_PF_test.py functional/setup_PF_test.py functional/Components/', returnStatus: false, returnStdout: false)
              }
            }
            currentBuild.result = 'FAILURE'
            // throw error
          }
          if (currentBuild.result == 'FAILURE') {
              throw error
          }
        }
      }
    }
  }
  post {
    always {
        echo sh(returnStdout: true, script: 'env')
        script {
        def GIT_COMMIT = sh(returnStdout: true, script: 'git log -1 --pretty=%B').trim()
        }
        echo("GIT_COMMIT: ${GIT_COMMIT}")
        script {
            try {
              if (env.CHANGE_TITLE == null) {
                  env.CHANGE_TITLE = ''
              }
            }
            catch (error) {
              env.CHANGE_TITLE = ''
            }
        }
        echo("CHANGE_TITLE: ${CHANGE_TITLE}")
      withPythonEnv('python') {
        allure(includeProperties: false, jdk: '', properties: [[key: 'allure.issues.tracker.pattern', value: 'https://jira.qumu.com/browse/%s'], [key: 'allure.tests.management.pattern', value: 'https://jira.qumu.com/browse/%s']], results: [[path: 'allure']])
        junit(healthScaleFactor: 1.0, testResults: 'report/report*.xml')
      }
    }
    success {
        hipchatSend(color: 'GREEN', notify: true, message: '<a href="$JOB_URL">${JOB_NAME}</a> build <a href="$BLUE_OCEAN_URL">${BUILD_DISPLAY_NAME}</a>, <a href="$TEST_REPORT_URL">passed successfuly</a> after $BUILD_DURATION.<BR>Branch / pull-request: <a href="${CHANGE_URL}">${BRANCH_NAME}</a>', room: 'Automation - Jenkins', v2enabled: false, sendAs: 'build0')
    }
    unstable {
        hipchatSend(color: 'YELLOW', notify: true, message: '<a href="$JOB_URL">${JOB_NAME}</a> build <a href="$BLUE_OCEAN_URL">${BUILD_DISPLAY_NAME}</a>, <a href="$TEST_REPORT_URL">was unstable</a> after $BUILD_DURATION.<BR>Branch / pull-request: <a href="${CHANGE_URL}">${BRANCH_NAME}</a>', room: 'Automation - Jenkins', v2enabled: false, sendAs: 'build0')
    }
    failure {
        hipchatSend(color: 'RED', notify: true, message: '<a href="$JOB_URL">${JOB_NAME}</a> build <a href="$BLUE_OCEAN_URL">${BUILD_DISPLAY_NAME}</a>, <a href="$TEST_REPORT_URL">has failed</a> after $BUILD_DURATION.<BR>Branch / pull-request: <a href="${CHANGE_URL}">${BRANCH_NAME}</a>', room: 'Automation - Jenkins', v2enabled: false, sendAs: 'build0')
    }
    // changed {
    //     hipchatSend(color: 'YELLOW', notify: true, message: '<a href="$JOB_URL">${JOB_NAME}</a> build <a href="$BLUE_OCEAN_URL">${BUILD_DISPLAY_NAME}</a>, <a href="$TEST_REPORT_URL">status changed</a> after $BUILD_DURATION.<BR>Branch / pull-request: <a href="${CHANGE_URL}">${BRANCH_NAME}</a>', room: 'Automation - Jenkins', v2enabled: false, sendAs: 'build0')
    // }
    aborted {
        hipchatSend(color: 'PURPLE', notify: true, message: '<a href="$JOB_URL">${JOB_NAME}</a> build <a href="$BLUE_OCEAN_URL">${BUILD_DISPLAY_NAME}</a>, <a href="$TEST_REPORT_URL">was aborted</a> after $BUILD_DURATION.<BR>Branch / pull-request: <a href="${CHANGE_URL}">${BRANCH_NAME}</a>', room: 'Automation - Jenkins', v2enabled: false, sendAs: 'build0')
    }
  }
}
