# General information

This project contains simple API test and [Allure Report](https://cdn.rawgit.com/alderven/restaurants/master/allure-report/index.html) based on [Swagger doc](https://gist.github.com/catherine-v/12a723fc2247a4bdaf8c275dd64421ed)

Swagger server generated manually using [Swagger Editor](https://editor.swagger.io). It can also be integrated into CI by using [Swagger Server Stub Generator](https://github.com/swagger-api/swagger-codegen/wiki/server-stub-generator-howto).

# Test Case and Test Result:
№ | Test Script                                                                                                           | Test description        | Run Result                                                                                                       
--| -----------------------------------------------------------------------------------------------------------------------| ------------------------|-------------------------------------------------------------------------------------------------------------------------- 
1 | [test_restaurants_add_and_get.py](https://github.com/alderven/restaurants/blob/master/test_restaurants_add_and_get.py) | Add restaurant          | [Passed](https://cdn.rawgit.com/alderven/restaurants/master/allure-report/index.html#behaviors/3148d55dcb6490d60b498a03b4e46cc6/769e1442434ef5e6/)
1 | [test_restaurants_add_and_get.py](https://github.com/alderven/restaurants/blob/master/test_restaurants_add_and_get.py) | Get restaurant          | [Passed](https://cdn.rawgit.com/alderven/restaurants/master/allure-report/index.html#behaviors/3148d55dcb6490d60b498a03b4e46cc6/a9c132eb634a248f/)

# How to install
1. Download and unzip [current project](https://github.com/alderven/restaurants/archive/master.zip)
1. Install [Python 3.6 or higher](https://www.python.org/downloads)
1. Install following Python libs:
   * [pytest](https://docs.pytest.org/en/latest/getting-started.html)
   * [allure-pytest](https://pypi.python.org/pypi/allure-pytest)
   * [Flask-Testing](https://pythonhosted.org/Flask-Testing)
1. Install [Allure Framework](https://docs.qameta.io/allure/latest)


# How to run tests
Execute following line in CMD in the project folder:
```
python -m swagger_server
python -m pytest --alluredir /full/path/to/report/folder
```

# How to generate Allure report
Execute following line in CMD in the project folder:
```
allure serve /full/path/to/report/folder
```
