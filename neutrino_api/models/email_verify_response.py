# -*- coding: utf-8 -*-

"""
    neutrino_api

    This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io ).
"""


class EmailVerifyResponse(object):

    """Implementation of the 'Email Verify Response' model.

    TODO: type model description here.

    Attributes:
        valid (bool): Is this a valid email address (syntax and domain is
            valid)
        verified (bool): True if this address has passed SMTP verification.
            Check the smtp-status and smtp-response fields for specific
            verification details
        email (string): The full email address (this could be different to the
            supplied address if typos-fixed is true)
        typos_fixed (bool): True if typos have been fixed
        syntax_error (bool): True if this address has a syntax error
        domain_error (bool): True if this address has a domain error (e.g. no
            valid mail server records)
        domain (string): The email domain
        provider (string): The email service provider domain
        is_freemail (bool): True if this address is a free-mail address
        is_disposable (bool): True if this address is a disposable, temporary
            or darknet related email address
        is_personal (bool): True if this address is for a person. False if
            this is a role based address, e.g. admin@, help@, office@, etc.
        smtp_status (string): The SMTP verification status for the
            address:<br/><ul><li>ok - SMTP verification was successful, this
            is a real address that can receive mail</li><li>invalid - this is
            not a valid email address (has either a domain or syntax
            error)</li><li>absent - this address is not registered with the
            email service provider</li><li>unresponsive - the mail server(s)
            for this address timed-out or refused to open an SMTP
            connection</li><li>unknown - sorry, we could not reliably
            determine the real status of this address (this address may or may
            not exist)</li></ul>
        smtp_response (string): The raw SMTP response message received during
            verification
        is_catch_all (bool): True if this email domain has a catch-all policy
            (it will accept mail for any username)
        is_deferred (bool): True if the mail server responded with a temporary
            failure (either a 4xx response code or unresponsive server). You
            can retry this address later, we recommend waiting at least 15
            minutes before retrying

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "valid":'valid',
        "verified":'verified',
        "email":'email',
        "typos_fixed":'typosFixed',
        "syntax_error":'syntaxError',
        "domain_error":'domainError',
        "domain":'domain',
        "provider":'provider',
        "is_freemail":'isFreemail',
        "is_disposable":'isDisposable',
        "is_personal":'isPersonal',
        "smtp_status":'smtpStatus',
        "smtp_response":'smtpResponse',
        "is_catch_all":'isCatchAll',
        "is_deferred":'isDeferred'
    }

    def __init__(self,
                 valid=None,
                 verified=None,
                 email=None,
                 typos_fixed=None,
                 syntax_error=None,
                 domain_error=None,
                 domain=None,
                 provider=None,
                 is_freemail=None,
                 is_disposable=None,
                 is_personal=None,
                 smtp_status=None,
                 smtp_response=None,
                 is_catch_all=None,
                 is_deferred=None):
        """Constructor for the EmailVerifyResponse class"""

        # Initialize members of the class
        self.valid = valid
        self.verified = verified
        self.email = email
        self.typos_fixed = typos_fixed
        self.syntax_error = syntax_error
        self.domain_error = domain_error
        self.domain = domain
        self.provider = provider
        self.is_freemail = is_freemail
        self.is_disposable = is_disposable
        self.is_personal = is_personal
        self.smtp_status = smtp_status
        self.smtp_response = smtp_response
        self.is_catch_all = is_catch_all
        self.is_deferred = is_deferred


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        valid = dictionary.get('valid')
        verified = dictionary.get('verified')
        email = dictionary.get('email')
        typos_fixed = dictionary.get('typosFixed')
        syntax_error = dictionary.get('syntaxError')
        domain_error = dictionary.get('domainError')
        domain = dictionary.get('domain')
        provider = dictionary.get('provider')
        is_freemail = dictionary.get('isFreemail')
        is_disposable = dictionary.get('isDisposable')
        is_personal = dictionary.get('isPersonal')
        smtp_status = dictionary.get('smtpStatus')
        smtp_response = dictionary.get('smtpResponse')
        is_catch_all = dictionary.get('isCatchAll')
        is_deferred = dictionary.get('isDeferred')

        # Return an object of this model
        return cls(valid,
                   verified,
                   email,
                   typos_fixed,
                   syntax_error,
                   domain_error,
                   domain,
                   provider,
                   is_freemail,
                   is_disposable,
                   is_personal,
                   smtp_status,
                   smtp_response,
                   is_catch_all,
                   is_deferred)


