# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class SigningKeyList(ListResource):

    def __init__(self, version, account_sid):
        """
        Initialize the SigningKeyList

        :param Version version: Version that contains the resource
        :param account_sid: A 34 character string that uniquely identifies this resource.

        :returns: SigningKeyList
        :rtype: SigningKeyList
        """
        super(SigningKeyList, self).__init__(version)

        # Path Solution
        self._solution = {
            'account_sid': account_sid,
        }
        self._uri = '/Accounts/{account_sid}/SigningKeys.json'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams SigningKeyInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: generator
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists SigningKeyInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: generator
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of SigningKeyInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SigningKeyInstance
        :rtype: Page
        """
        params = values.of({
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return SigningKeyPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a SigningKeyContext

        :param sid: The sid

        :returns: SigningKeyContext
        :rtype: SigningKeyContext
        """
        return SigningKeyContext(
            self._version,
            account_sid=self._solution['account_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a SigningKeyContext

        :param sid: The sid

        :returns: SigningKeyContext
        :rtype: SigningKeyContext
        """
        return SigningKeyContext(
            self._version,
            account_sid=self._solution['account_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.SigningKeyList>'


class SigningKeyPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the SigningKeyPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_sid: A 34 character string that uniquely identifies this resource.

        :returns: SigningKeyPage
        :rtype: SigningKeyPage
        """
        super(SigningKeyPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of SigningKeyInstance

        :param dict payload: Payload response from the API

        :returns: SigningKeyInstance
        :rtype: SigningKeyInstance
        """
        return SigningKeyInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.SigningKeyPage>'


class SigningKeyContext(InstanceContext):

    def __init__(self, version, account_sid, sid):
        """
        Initialize the SigningKeyContext

        :param Version version: Version that contains the resource
        :param account_sid: The account_sid
        :param sid: The sid

        :returns: SigningKeyContext
        :rtype: SigningKeyContext
        """
        super(SigningKeyContext, self).__init__(version)

        # Path Solution
        self._solution = {
            'account_sid': account_sid,
            'sid': sid,
        }
        self._uri = '/Accounts/{account_sid}/SigningKeys/{sid}.json'.format(**self._solution)

    def fetch(self):
        """
        Fetch a SigningKeyInstance

        :returns: Fetched SigningKeyInstance
        :rtype: SigningKeyInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return SigningKeyInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            sid=self._solution['sid'],
        )

    def update(self, friendly_name=values.unset):
        """
        Update the SigningKeyInstance

        :param unicode friendly_name: The friendly_name

        :returns: Updated SigningKeyInstance
        :rtype: SigningKeyInstance
        """
        data = values.of({
            'FriendlyName': friendly_name,
        })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return SigningKeyInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the SigningKeyInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.SigningKeyContext {}>'.format(context)


class SigningKeyInstance(InstanceResource):

    def __init__(self, version, payload, account_sid, sid=None):
        """
        Initialize the SigningKeyInstance

        :returns: SigningKeyInstance
        :rtype: SigningKeyInstance
        """
        super(SigningKeyInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'friendly_name': payload['friendly_name'],
            'date_created': deserialize.rfc2822_datetime(payload['date_created']),
            'date_updated': deserialize.rfc2822_datetime(payload['date_updated']),
        }

        # Context
        self._context = None
        self._solution = {
            'account_sid': account_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: SigningKeyContext for this SigningKeyInstance
        :rtype: SigningKeyContext
        """
        if self._context is None:
            self._context = SigningKeyContext(
                self._version,
                account_sid=self._solution['account_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def friendly_name(self):
        """
        :returns: The friendly_name
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def date_created(self):
        """
        :returns: The date_created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date_updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    def fetch(self):
        """
        Fetch a SigningKeyInstance

        :returns: Fetched SigningKeyInstance
        :rtype: SigningKeyInstance
        """
        return self._proxy.fetch()

    def update(self, friendly_name=values.unset):
        """
        Update the SigningKeyInstance

        :param unicode friendly_name: The friendly_name

        :returns: Updated SigningKeyInstance
        :rtype: SigningKeyInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
        )

    def delete(self):
        """
        Deletes the SigningKeyInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.SigningKeyInstance {}>'.format(context)
