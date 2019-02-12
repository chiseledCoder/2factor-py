import os
import requests
import urls
from Configure2Factor import Configure2Factor
import json


# class _2Factor(object):
#
# 	def __init__(self, api_key=None, endpoint=None):
# 		self.api_key = api_key
# 		self.endpoint = endpoint
#
# 	def check_sms_otp_balance(self):
# 		response = call_api(method='get', )
#
# 	def request(self, method, data, **options):
# 		pass
#
# 	def get_api_key():
# 		return self.api_key


class TwoFactorSMS(object):
    """ Contains methods for SMS realted Requests """

    def check_sms_otp_balance(self):
        # Get the URL
        url = urls.SmsOtpUrls.check_sms_otp_balance

        # Required Parameter is: API Key
        url = url.format(Configure2Factor.get_api_key())
        r = requests.get(url=url)
        response = r.json()
        # Check for Invalid API Key Error
        return response

    def send_sms_otp(self, custom_template=None, custom_otp=None):
        """ Chosse different requests for custom template vs no custom template
            Autogenerated : Default True (If server should automatically generate the OTP for you)
            (If false, custom_otp should be provided)
        """

        if custom_template is None and custom_otp is None:
            url = urls.SmsOtpUrls.send_auto_generated_otp

        if custom_template is None and custom_otp is not None:
            url = urls.SmsOtpUrls.send_custom_otp.format(Configure2Factor.get_api_key(), custom_otp)

        if custom_template is not None and custom_otp is None:
            url = urls.SmsOtpUrls.send_auto_generated_otp_custom_template.format(Configure2Factor.get_api_key(),
                                                                                 custom_template)

        if custom_template is not None and custom_otp is not None:
            url = urls.SmsOtpUrls.send_custom_otp_custom_template.format(Configure2Factor.get_api_key(), custom_otp,
                                                                         custom_template)

        r = requests.get(url=url)
        response = r.json()
        return response


    def verify_sms_otp_input(self, session_id=None, otp_input=None):
        """ This endpoint is useful in verifying user entered OTP with sent OTP """
        # session_id can be retrieved from 'Details' field of Send OTP endpoint response
        assert session_id is not None and otp_input is not None, " Session ID and OTP should not be Null"

        url = urls.SmsOtpUrls.verify_sms_otp_input.format(Configure2Factor.get_api_key(),
                                                          session_id, otp_input)
        r = requests.get(url)

        response = r.json()

        return response
