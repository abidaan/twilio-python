# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base.domain import Domain
from twilio.rest.ip_messaging.v1 import V1


class IpMessaging(Domain):

    def __init__(self, twilio):
        """
        Initialize the IpMessaging Domain

        :returns: Domain for IpMessaging
        :rtype: IpMessaging
        """
        super(IpMessaging, self).__init__(twilio)

        self.base_url = 'https://ip-messaging.twilio.com'

        # Versions
        self._v1 = None

    @property
    def v1(self):
        """
        :returns: Version v1 of ip_messaging
        :rtype: V1
        """
        if self._v1 is None:
            self._v1 = V1(self)
        return self._v1

    @property
    def credentials(self):
        """
        :rtype: CredentialList
        """
        return self.v1.credentials

    @property
    def services(self):
        """
        :rtype: ServiceList
        """
        return self.v1.services

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.IpMessaging>'
