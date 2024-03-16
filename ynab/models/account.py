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


class Account(object):
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
        'type': 'str',
        'on_budget': 'bool',
        'closed': 'bool',
        'note': 'str',
        'balance': 'float',
        'cleared_balance': 'float',
        'uncleared_balance': 'float'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'on_budget': 'on_budget',
        'closed': 'closed',
        'note': 'note',
        'balance': 'balance',
        'cleared_balance': 'cleared_balance',
        'uncleared_balance': 'uncleared_balance'
    }

    def __init__(self, id=None, name=None, type=None, on_budget=None, closed=None, note=None, balance=None, cleared_balance=None, uncleared_balance=None):  # noqa: E501
        """Account - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._type = None
        self._on_budget = None
        self._closed = None
        self._note = None
        self._balance = None
        self._cleared_balance = None
        self._uncleared_balance = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.type = type
        self.on_budget = on_budget
        self.closed = closed
        self.note = note
        self.balance = balance
        self.cleared_balance = cleared_balance
        self.uncleared_balance = uncleared_balance

    @property
    def id(self):
        """Gets the id of this Account.  # noqa: E501


        :return: The id of this Account.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Account.


        :param id: The id of this Account.  # noqa: E501
        :type: str
        """
        if id is None:
            id = ''

        self._id = id

    @property
    def name(self):
        """Gets the name of this Account.  # noqa: E501


        :return: The name of this Account.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Account.


        :param name: The name of this Account.  # noqa: E501
        :type: str
        """
        if name is None:
            name = ''

        self._name = name

    @property
    def type(self):
        """Gets the type of this Account.  # noqa: E501


        :return: The type of this Account.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Account.


        :param type: The type of this Account.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["checking", "savings", "creditCard", "cash", "lineOfCredit", "merchantAccount", "payPal", "investmentAccount", "mortgage", "otherAsset", "otherLiability", "autoLoan"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def on_budget(self):
        """Gets the on_budget of this Account.  # noqa: E501

        Whether this account is on budget or not  # noqa: E501

        :return: The on_budget of this Account.  # noqa: E501
        :rtype: bool
        """
        return self._on_budget

    @on_budget.setter
    def on_budget(self, on_budget):
        """Sets the on_budget of this Account.

        Whether this account is on budget or not  # noqa: E501

        :param on_budget: The on_budget of this Account.  # noqa: E501
        :type: bool
        """
        if on_budget is None:
            on_budget = ''

        self._on_budget = on_budget

    @property
    def closed(self):
        """Gets the closed of this Account.  # noqa: E501

        Whether this account is closed or not  # noqa: E501

        :return: The closed of this Account.  # noqa: E501
        :rtype: bool
        """
        return self._closed

    @closed.setter
    def closed(self, closed):
        """Sets the closed of this Account.

        Whether this account is closed or not  # noqa: E501

        :param closed: The closed of this Account.  # noqa: E501
        :type: bool
        """
        if closed is None:
            closed = ''

        self._closed = closed

    @property
    def note(self):
        """Gets the note of this Account.  # noqa: E501


        :return: The note of this Account.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this Account.


        :param note: The note of this Account.  # noqa: E501
        :type: str
        """
        self._note = note

    @property
    def balance(self):
        """Gets the balance of this Account.  # noqa: E501

        The current balance of the account in milliunits format  # noqa: E501

        :return: The balance of this Account.  # noqa: E501
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this Account.

        The current balance of the account in milliunits format  # noqa: E501

        :param balance: The balance of this Account.  # noqa: E501
        :type: float
        """
        if balance is None:
            balance = ''

        self._balance = balance

    @property
    def cleared_balance(self):
        """Gets the cleared_balance of this Account.  # noqa: E501

        The current cleared balance of the account in milliunits format  # noqa: E501

        :return: The cleared_balance of this Account.  # noqa: E501
        :rtype: float
        """
        return self._cleared_balance

    @cleared_balance.setter
    def cleared_balance(self, cleared_balance):
        """Sets the cleared_balance of this Account.

        The current cleared balance of the account in milliunits format  # noqa: E501

        :param cleared_balance: The cleared_balance of this Account.  # noqa: E501
        :type: float
        """
        if cleared_balance is None:
            cleared_balance = ''

        self._cleared_balance = cleared_balance

    @property
    def uncleared_balance(self):
        """Gets the uncleared_balance of this Account.  # noqa: E501

        The current uncleared balance of the account in milliunits format  # noqa: E501

        :return: The uncleared_balance of this Account.  # noqa: E501
        :rtype: float
        """
        return self._uncleared_balance

    @uncleared_balance.setter
    def uncleared_balance(self, uncleared_balance):
        """Sets the uncleared_balance of this Account.

        The current uncleared balance of the account in milliunits format  # noqa: E501

        :param uncleared_balance: The uncleared_balance of this Account.  # noqa: E501
        :type: float
        """
        if uncleared_balance is None:
            uncleared_balance = ''

        self._uncleared_balance = uncleared_balance

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
        if not isinstance(other, Account):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
