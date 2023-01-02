# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ynab.api_client import ApiClient


class PayeeLocationsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_payee_location_by_id(self, budget_id, payee_location_id, **kwargs):  # noqa: E501
        """Single payee location  # noqa: E501

        Returns a single payee location  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payee_location_by_id(budget_id, payee_location_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str budget_id: The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget). (required)
        :param str payee_location_id: id of payee location (required)
        :return: PayeeLocationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_payee_location_by_id_with_http_info(budget_id, payee_location_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_payee_location_by_id_with_http_info(budget_id, payee_location_id, **kwargs)  # noqa: E501
            return data

    def get_payee_location_by_id_with_http_info(self, budget_id, payee_location_id, **kwargs):  # noqa: E501
        """Single payee location  # noqa: E501

        Returns a single payee location  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payee_location_by_id_with_http_info(budget_id, payee_location_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str budget_id: The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget). (required)
        :param str payee_location_id: id of payee location (required)
        :return: PayeeLocationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['budget_id', 'payee_location_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_payee_location_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'budget_id' is set
        if self.api_client.client_side_validation and ('budget_id' not in params or
                                                       params['budget_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `budget_id` when calling `get_payee_location_by_id`")  # noqa: E501
        # verify the required parameter 'payee_location_id' is set
        if self.api_client.client_side_validation and ('payee_location_id' not in params or
                                                       params['payee_location_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `payee_location_id` when calling `get_payee_location_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'budget_id' in params:
            path_params['budget_id'] = params['budget_id']  # noqa: E501
        if 'payee_location_id' in params:
            path_params['payee_location_id'] = params['payee_location_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/budgets/{budget_id}/payee_locations/{payee_location_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PayeeLocationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_payee_locations(self, budget_id, **kwargs):  # noqa: E501
        """List payee locations  # noqa: E501

        Returns all payee locations  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payee_locations(budget_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str budget_id: The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget). (required)
        :return: PayeeLocationsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_payee_locations_with_http_info(budget_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_payee_locations_with_http_info(budget_id, **kwargs)  # noqa: E501
            return data

    def get_payee_locations_with_http_info(self, budget_id, **kwargs):  # noqa: E501
        """List payee locations  # noqa: E501

        Returns all payee locations  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payee_locations_with_http_info(budget_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str budget_id: The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget). (required)
        :return: PayeeLocationsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['budget_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_payee_locations" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'budget_id' is set
        if self.api_client.client_side_validation and ('budget_id' not in params or
                                                       params['budget_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `budget_id` when calling `get_payee_locations`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'budget_id' in params:
            path_params['budget_id'] = params['budget_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/budgets/{budget_id}/payee_locations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PayeeLocationsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_payee_locations_by_payee(self, budget_id, payee_id, **kwargs):  # noqa: E501
        """List locations for a payee  # noqa: E501

        Returns all payee locations for a specified payee  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payee_locations_by_payee(budget_id, payee_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str budget_id: The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget). (required)
        :param str payee_id: id of payee (required)
        :return: PayeeLocationsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_payee_locations_by_payee_with_http_info(budget_id, payee_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_payee_locations_by_payee_with_http_info(budget_id, payee_id, **kwargs)  # noqa: E501
            return data

    def get_payee_locations_by_payee_with_http_info(self, budget_id, payee_id, **kwargs):  # noqa: E501
        """List locations for a payee  # noqa: E501

        Returns all payee locations for a specified payee  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payee_locations_by_payee_with_http_info(budget_id, payee_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str budget_id: The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget). (required)
        :param str payee_id: id of payee (required)
        :return: PayeeLocationsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['budget_id', 'payee_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_payee_locations_by_payee" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'budget_id' is set
        if self.api_client.client_side_validation and ('budget_id' not in params or
                                                       params['budget_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `budget_id` when calling `get_payee_locations_by_payee`")  # noqa: E501
        # verify the required parameter 'payee_id' is set
        if self.api_client.client_side_validation and ('payee_id' not in params or
                                                       params['payee_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `payee_id` when calling `get_payee_locations_by_payee`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'budget_id' in params:
            path_params['budget_id'] = params['budget_id']  # noqa: E501
        if 'payee_id' in params:
            path_params['payee_id'] = params['payee_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/budgets/{budget_id}/payees/{payee_id}/payee_locations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PayeeLocationsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)