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


class Payee(object):
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
        'name': 'str',
        'transfer_account_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'transfer_account_id': 'transfer_account_id'
    }

    def __init__(self, id=None, name=None, transfer_account_id=None):  # noqa: E501
        """Payee - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._transfer_account_id = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.transfer_account_id = transfer_account_id

    @property
    def id(self):
        """Gets the id of this Payee.  # noqa: E501


        :return: The id of this Payee.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Payee.


        :param id: The id of this Payee.  # noqa: E501
        :type: str
        """
        if id is None:
            id = ''

        self._id = id

    @property
    def name(self):
        """Gets the name of this Payee.  # noqa: E501


        :return: The name of this Payee.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Payee.


        :param name: The name of this Payee.  # noqa: E501
        :type: str
        """
        if name is None:
            name = ''

        self._name = name

    @property
    def transfer_account_id(self):
        """Gets the transfer_account_id of this Payee.  # noqa: E501

        If a transfer payee, the account_id to which this payee transfers to  # noqa: E501

        :return: The transfer_account_id of this Payee.  # noqa: E501
        :rtype: str
        """
        return self._transfer_account_id

    @transfer_account_id.setter
    def transfer_account_id(self, transfer_account_id):
        """Sets the transfer_account_id of this Payee.

        If a transfer payee, the account_id to which this payee transfers to  # noqa: E501

        :param transfer_account_id: The transfer_account_id of this Payee.  # noqa: E501
        :type: str
        """
        if transfer_account_id is None:
            transfer_account_id = ''

        self._transfer_account_id = transfer_account_id

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
        if not isinstance(other, Payee):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
