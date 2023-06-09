# Dashboard app

A very basic dashboard app with the following functionalities:

    Add User
    Update User
    Delete User
    View Users

# Project setup

## Requirements

- [npm](https://www.npmjs.com/package/npm)

## Install needed packages

In the project directory, you can run:

    npm install
     or
    yarn install

# Run project

The app can be compiled and hot-reloaded for development on your local machine by running in the project directory:

    npm run dev
     or
    yarn run dev

The app will open in your browser. In case it doesn't, open your browser and go to http://localhost:3000 to view it in the browser.

NOTE: The page will reload if you make edits to the app codebase.


# Assignment

The assignment has been devised with manual and automation testers in mind in order to assess your testing knowledge, attention to details and how you architecture the code.

Please carefully read what you need to do and what not to do. The assignment consists of two parts, backend automation and frontend automation.

## Frontend and Backend tasks

- [ ] Perform some Exploratory Testing sessions against the application to familiarize with it and report any bugs or mismatching behavior between the app and its specifications. You don't need to report every issue you find, and neither browser nor mobile compatibility issues. Please only report the ones you find most important, but at most 5 issues;
- [ ] Update the README.md file and explain how the tests can be ran locally;

## Frontend only tasks

- [ ] Cover 2 [requirements](docs/requirements.md) from the specifications with **End-to-End tests**. Choose the ones you find most important. Pick a testing framework you feel most comfortable with;

## Backend only tasks

- [ ] Cover 2 [requirements](docs/requirements.md) from the specifications with **API tests**. Choose the ones you find most important. Pick a testing framework you feel most comfortable with;


# How to run the tests loocally

- [ ] Solution: https://github.com/antoniahoro/wolters-kluwer-qa-assignment.git
- [ ] Branch: test-antonia

## Frontend and Backend tasks - Exploratory testing

Issues discovered during exploratory testing cand be found here: src/exploratory_testing.
This folder contains:
- [ ] a description of the issues: src/exploratory_testing/exploratory_testing_issues.xlsx
- [ ] attachments for each issue (.png files)

## Frontend only tasks - solution

**End-to-End tests** can be found here: src/frontend_testing.
Check src/frontend_testing/requirements.txt before executing the code.

- Open a Pytho IDE (eg. Pycharm).
- Open the project src.
- [Configure a Python virtual environmnet](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#python_create_virtual_env).
- Open src/frontend_testing/tests/add_user_test.py.
- Make sure you have Chrome browser installed.
- Run the tests from class AddUserTest.


## Backend only tasks - solution

**API tests** can be found here: src/backend_testing.postman_collection.json.

Setup:
- Download the collection from src/backend_testing.postman_collection.json
- Install Postman desktop app. See [Installing and updating Postman](https://learning.postman.com/docs/getting-started/installation-and-updates/). You cand also use the [Postman web app](https://web.postman.co/home) if you don't want to install it.
- In Postman > Create your own workspace .
- Import backend_testing.postman_collection.json into your workspace. the request can be found in Collections section.
- Go to Environments section and select Create Environment.
- Give an environment name and create an environment variable:
    - Variable = base_url
    - Initial Value = http://127.0.0.1:3003
- Save the variable using Save button.
- Return to the Collections section.
- Select the getUsersListResponse request.
- From No Environment tab select your environment.
- Send the request.
- Results can be found in Test Results.
