Installation
============

Basics
------

Install `Python <https://www.python.org/downloads/>`_ for your operating system environemnt.
This framework have been tested with latest Python version 2.7.x and Python 3.x versions.
It is recommended to use latest Python 3.x for future upgradability and compatibility.

On a command prompt run the following (you may have to run the shell with elevated privelages:
*run-as-administrator* ; *sudo -H ...* ; or other, depending on the OS)::

    python -m ensurepip --upgrade

Clone Code Repository
---------------------
You should (already) have **git** client installed on your system.
While UI-based clients exist and can be used, it is recommended that git command line is used.

For Windows clients you can `get git for Windows <https://git-for-windows.github.io/>`_ distribution,
make sure to install ssh and coreutils, as part of the installation, and enable command shell integrations.

* Fork this `automation project <http://bitbucket.qumu.com/projects/QA/repos/qe/browse>`_, to your user space::

    http://bitbucket.qumu.com/projects/QA/repos/qe?fork

* Clone your fork to the local machine::

    git clone --recursive http://<username>@bitbucket.qumu.com/scm/~<username>/qe.git

* Get into the directory cloned.
* Add reference to the original remote code::

    git remote add upstream http://<username>@bitbucket.qumu.com/scm/qa/qe.git

.. note:: See `Confluence GIT Guide <https://confluence.qumu.com/display/auto/Git+Guidance>`_ for basic GIT reference and pointers to additional documentation.

Python Virtual Environment
--------------------------

.. important:: **Highly recommended** - Use `python virtual environment <http://docs.python-guide.org/en/latest/dev/virtualenvs/>`_.

Install (with elevated privileges) **virtualenv**, and use it for the reminder of the installation process::

    pip install --upgrade virtualenv

and then, activate the virtual environment::

    cd <my_qe_automation_project_folder>
    virtualenv .

or::

    virtualenv <my_qe_automation_project_folder>

on Linux / Unix / MAC::

    source <my_qe_automation_project_folder>/bin/activate

on Windows::

    <my_qe_automation_project_folder>/Scripts/activate.bat

.. note:: To exit the virtual environment, run *deactivate* from the command prompt.

Continue the installation, inside a virtualized environmet and/or with elevated priveleges, and install the following dependencies::

    pip install --upgrade -r requirements.txt

Patch bravado-core:

on Linux / Unix / MAC (please note to pick the path for your python version)::

    cp -v bravado-core-patch/*.py lib/python2.7/site-packages/bravado_core/

or::

    cp -v bravado-core-patch/*.py lib/python3.6/site-packages/bravado_core/

on on Windows::

    copy bravado-core-patch\*.py Lib\site-packages\bravado_core\


.. todo:: Add video validation installation items.


Highly Recommended & Optional Add-ons
-------------------------------------

* Interactive python shell::

    pip install --upgrade ptpython

  ... and see `ptpython <https://github.com/jonathanslenders/ptpython>`_ website for details about its features.
  The interactive shell can be used to test the automation code, while providing auto-completion, interactive documentation, and easy introspection of objects.

* To build documentation::

    pip install --upgrade -r docs/requirements.txt

  ... and then run the make file in the docs folder.

* To generate test report, install `allure <https://github.com/allure-framework/allure2>`_ on supported platforms, per the instructions on the allure website.


Test Environment Setup
----------------------

Setup SUT Components
====================

.. warning:: This must never be done to a production environment of any test environemnt open to external networks.

On PathFinder and PathFinderEdge servers:

* Allow applianceadmin sudo without password, by editing ``/etc/sudoers``::

    PFE
     
    # applianceadmin   ALL=(ALL:ALL) NOPASSWD: ALL
     
    PF
     
    # %sudo   ALL=(ALL:ALL) NOPASSWD: ALL

* `Generate private SSH <https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/#platform-mac>`_
  keys for the test client (machine running the automation code),
  and add the public key to .ssh/authorized_keys for PathFinder user1 and PFE applianceadmin.

* Last step has to be applied to continuous integration slaves. These slaves should have python and virtualenv installed as a prerequisite.

Configure SUT Components
========================

* Make a copy of ``data/qed_env.yml`` under the same folder (or subfolder of data).
* Edit to match your environemnt.
* When running the py.test tests, specify the file using --env argument. For example::

    py.test --html=report/report.html --junitxml=report/report.xml --alluredir allure --disable-pytest-warnings --disable-warnings --env data/qed_env.yml functional/
