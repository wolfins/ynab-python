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

from ynab.configuration import Configuration


class BudgetSettings(object):
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
        'date_format': 'DateFormat',
        'currency_format': 'CurrencyFormat'
    }

    attribute_map = {
        'date_format': 'date_format',
        'currency_format': 'currency_format'
    }

    def __init__(self, date_format=None, currency_format=None, _configuration=None):  # noqa: E501
        """BudgetSettings - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._date_format = None
        self._currency_format = None
        self.discriminator = None

        self.date_format = date_format
        self.currency_format = currency_format

    @property
    def date_format(self):
        """Gets the date_format of this BudgetSettings.  # noqa: E501


        :return: The date_format of this BudgetSettings.  # noqa: E501
        :rtype: DateFormat
        """
        return self._date_format

    @date_format.setter
    def date_format(self, date_format):
        """Sets the date_format of this BudgetSettings.


        :param date_format: The date_format of this BudgetSettings.  # noqa: E501
        :type: DateFormat
        """
        if self._configuration.client_side_validation and date_format is None:
            raise ValueError("Invalid value for `date_format`, must not be `None`")  # noqa: E501

        self._date_format = date_format

    @property
    def currency_format(self):
        """Gets the currency_format of this BudgetSettings.  # noqa: E501


        :return: The currency_format of this BudgetSettings.  # noqa: E501
        :rtype: CurrencyFormat
        """
        return self._currency_format

    @currency_format.setter
    def currency_format(self, currency_format):
        """Sets the currency_format of this BudgetSettings.


        :param currency_format: The currency_format of this BudgetSettings.  # noqa: E501
        :type: CurrencyFormat
        """
        if self._configuration.client_side_validation and currency_format is None:
            raise ValueError("Invalid value for `currency_format`, must not be `None`")  # noqa: E501

        self._currency_format = currency_format

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
        if issubclass(BudgetSettings, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BudgetSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BudgetSettings):
            return True

        return self.to_dict() != other.to_dict()
