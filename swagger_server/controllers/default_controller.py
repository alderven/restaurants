import connexion
import six

from swagger_server.models.restaurant import Restaurant  # noqa: E501
from swagger_server.models.restaurant_list_response import RestaurantListResponse  # noqa: E501
from swagger_server import util


def restaurants_get(id=None, zipcode=None):  # noqa: E501
    """restaurants_get

    Returns list of restaurants # noqa: E501

    :param id: Filter by restaurant id
    :type id: int
    :param zipcode: Filter by zipcode
    :type zipcode: str

    :rtype: RestaurantListResponse
    """
    return 'do some magic!'


def restaurants_post(restaurant):  # noqa: E501
    """restaurants_post

    Creates a new restaurant # noqa: E501

    :param restaurant: 
    :type restaurant: dict | bytes

    :rtype: Restaurant
    """
    if connexion.request.is_json:
        restaurant = Restaurant.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
