# -*- coding: utf-8 -*-

"""
    neutrino_api

    This file was automatically generated for NeutrinoAPI by APIMATIC v2.0 ( https://apimatic.io ).
"""


class EmailValidateResponse(object):

    """Implementation of the 'Email Validate Response' model.

    TODO: type model description here.

    Attributes:
        valid (bool): Is this a valid email
        syntax_error (bool): True if this address has a syntax error
        domain (string): The email domain
        domain_error (bool): True if this address has a domain error (e.g. no
            valid mail server records)
        is_freemail (bool): True if this address is a free-mail address
        email (string): The email address. If you have used the fix-typos
            option then this will be the fixed address
        is_disposable (bool): True if this address is a disposable, temporary
            or darknet related email address
        typos_fixed (bool): True if typos have been fixed
        is_personal (bool): True if this address belongs to a person. False if
            this is a role based address, e.g. admin@, help@, office@, etc.
        provider (string): The email service provider domain

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "valid":'valid',
        "syntax_error":'syntaxError',
        "domain":'domain',
        "domain_error":'domainError',
        "is_freemail":'isFreemail',
        "email":'email',
        "is_disposable":'isDisposable',
        "typos_fixed":'typosFixed',
        "is_personal":'isPersonal',
        "provider":'provider'
    }

    def __init__(self,
                 valid=None,
                 syntax_error=None,
                 domain=None,
                 domain_error=None,
                 is_freemail=None,
                 email=None,
                 is_disposable=None,
                 typos_fixed=None,
                 is_personal=None,
                 provider=None):
        """Constructor for the EmailValidateResponse class"""

        # Initialize members of the class
        self.valid = valid
        self.syntax_error = syntax_error
        self.domain = domain
        self.domain_error = domain_error
        self.is_freemail = is_freemail
        self.email = email
        self.is_disposable = is_disposable
        self.typos_fixed = typos_fixed
        self.is_personal = is_personal
        self.provider = provider


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
        syntax_error = dictionary.get('syntaxError')
        domain = dictionary.get('domain')
        domain_error = dictionary.get('domainError')
        is_freemail = dictionary.get('isFreemail')
        email = dictionary.get('email')
        is_disposable = dictionary.get('isDisposable')
        typos_fixed = dictionary.get('typosFixed')
        is_personal = dictionary.get('isPersonal')
        provider = dictionary.get('provider')

        # Return an object of this model
        return cls(valid,
                   syntax_error,
                   domain,
                   domain_error,
                   is_freemail,
                   email,
                   is_disposable,
                   typos_fixed,
                   is_personal,
                   provider)


