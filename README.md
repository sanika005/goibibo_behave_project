# To run the project go to terminal and run the command
    - behave

# To see the allure reports
    - behave -f allure_behave.formatter:AllureFormatter -o reports/ features
    - brew install allure
    - allure serve reports/# goibibo_behave_project
