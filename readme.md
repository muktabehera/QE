Installation
============

Basics
------

Install [Python](https://www.python.org/downloads/) for your operating
system environemnt. This framework have been tested with latest Python
version 2.7.x and Python 3.x versions. It is recommended to use latest
Python 3.x for future upgradability and compatibility.

On a command prompt run the following (you may have to run the shell
with elevated privelages: *run-as-administrator* ; *sudo -H ...* ; or
other, depending on the OS):

    python -m ensurepip --upgrade

Clone Code Repository
---------------------

You should (already) have **git** client installed on your system. While
UI-based clients exist and can be used, it is recommended that git
command line is used.

-   Fork this [automation
    project](http://bitbucket.qumu.com/projects/QA/repos/qe/browse), to
    your user space:

        http://bitbucket.qumu.com/projects/QA/repos/qe?fork

-   Clone your fork to the local machine:

        git clone --recursive http://<username>@bitbucket.qumu.com/scm/~<username>/qe.git

-   Get into the directory cloned.

-   Add reference to the original remote code:

        git remote add upstream http://<username>@bitbucket.qumu.com/scm/qa/qe.git

<div class="admonition note">

See [Confluence GIT
Guide](https://confluence.qumu.com/display/auto/Git+Guidance) for basic
GIT reference and pointers to additional documentation.

</div>

Continue with the project docs
------------------------------

After checking out the code, please navigate to your qe for folder on your PC, and go to the **qe/docs/_build** folder.
The **index.html** file is the root page for all the documentation.

Please open **installation.html** in your browser, for details on how to continue this installation.
Please don't forget to check also the introduction and getting-started pages.
