# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    OpenAPI spec version: 1.0.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PayeeLocation(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'payee_id': 'str',
        'latitude': 'str',
        'longitude': 'str'
    }

    attribute_map = {
        'id': 'id',
        'payee_id': 'payee_id',
        'latitude': 'latitude',
        'longitude': 'longitude'
    }

    def __init__(self, id=None, payee_id=None, latitude=None, longitude=None):  # noqa: E501
        """PayeeLocation - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._payee_id = None
        self._latitude = None
        self._longitude = None
        self.discriminator = None

        self.id = id
        self.payee_id = payee_id
        self.latitude = latitude
        self.longitude = longitude

    @property
    def id(self):
        """Gets the id of this PayeeLocation.  # noqa: E501


        :return: The id of this PayeeLocation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PayeeLocation.


        :param id: The id of this PayeeLocation.  # noqa: E501
        :type: str
        """
        if id is None:
            id = ''

        self._id = id

    @property
    def payee_id(self):
        """Gets the payee_id of this PayeeLocation.  # noqa: E501


        :return: The payee_id of this PayeeLocation.  # noqa: E501
        :rtype: str
        """
        return self._payee_id

    @payee_id.setter
    def payee_id(self, payee_id):
        """Sets the payee_id of this PayeeLocation.


        :param payee_id: The payee_id of this PayeeLocation.  # noqa: E501
        :type: str
        """
        if payee_id is None:
            payee_id = ''

        self._payee_id = payee_id

    @property
    def latitude(self):
        """Gets the latitude of this PayeeLocation.  # noqa: E501


        :return: The latitude of this PayeeLocation.  # noqa: E501
        :rtype: str
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this PayeeLocation.


        :param latitude: The latitude of this PayeeLocation.  # noqa: E501
        :type: str
        """
        if latitude is None:
            latitude = ''

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this PayeeLocation.  # noqa: E501


        :return: The longitude of this PayeeLocation.  # noqa: E501
        :rtype: str
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this PayeeLocation.


        :param longitude: The longitude of this PayeeLocation.  # noqa: E501
        :type: str
        """
        if longitude is None:
            longitude = ''

        self._longitude = longitude

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PayeeLocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
