import pytest
from flask import json

from swagger_server.test import BaseTestCase
from swagger_server.models.restaurant import Restaurant  # noqa: E501
from swagger_server.models.address import Address  # noqa: E501


@pytest.allure.feature('Restaurants')
@pytest.allure.story('Add and get restaurants')
@pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
class TestDefaultController(BaseTestCase):

    def test_restaurants_get(self):

        query_string = [('id', 56), ('zipcode', 'zipcode_example')]

        with pytest.allure.step('1. Get restaurant with following parameters: {}'.format(query_string)):
            response = self.client.open(
                '/restaurants',
                method='GET',
                content_type='application/json',
                query_string=query_string)

        with pytest.allure.step('2. Check, that response code is 200'):
            self.assert200(response, 'Response body is : ' + response.data.decode('utf-8'))

    def test_restaurants_add(self):

        with pytest.allure.step('1. Create restaurant'):

            address = Address(zipcode='12345', city='Moscow', street='Lenina', latitude=1, longitude=1)
            restaurant = Restaurant(id=12345, name='MyRest1', address=address, owner='Me', emails=['rest@ya.ru'],
                                    phones=['+79123456789'])
            response = self.client.open(
                '/restaurants',
                method='POST',
                data=json.dumps(restaurant),
                content_type='application/json')

        with pytest.allure.step('2. Check, that response code is 200'):
            self.assert200(response, 'Response body is : ' + response.data.decode('utf-8'))
