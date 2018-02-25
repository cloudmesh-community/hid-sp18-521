import connexion
import six
import imp

pds_functions = imp.load_source('pds_functions', '/home/scs811s/Github/hid-sp18-521/swagger/pds_functions.py')

from swagger_server.models.inline_response400 import InlineResponse400  # noqa: E501
from swagger_server.models.provider import Provider  # noqa: E501
from swagger_server import util


def create_provider(provider=None):  # noqa: E501
    """create_provider

    User can insert a new provider record. # noqa: E501

    :param provider: Creates a new medical provider record.
    :type provider: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        #provider = Provider.from_dict(connexion.request.get_json())  # noqa: E501
        provider = connexion.request.get_json()

        return pds_functions.provider_insert(provider)


def delete_provider(npi):  # noqa: E501
    """delete_provider

    Delete a single provider based on NPI supplied. # noqa: E501

    :param npi: NPI of provider to delete
    :type npi: int

    :rtype: None
    """
    return pds_functions.provider_delete(npi)


def get_provider(npi):  # noqa: E501
    """get_provider

    Returns medical provider of the speicifed provider NPI # noqa: E501

    :param npi: Provider type of providers to return
    :type npi: int

    :rtype: List[Provider]
    """
    return Provider(pds_functions.provider_query_npi(npi))


def get_providers():  # noqa: E501
    """get_providers

    Returns all medical providers in the system. # noqa: E501


    :rtype: List[Provider]
    """
    return Provider(pds_functions.provider_query_all())


def update_provider(npi, provider=None):  # noqa: E501
    """update_provider

    Update a providers information based on NPI supplied # noqa: E501

    :param npi: NPI of provider to update
    :type npi: int
    :param provider: Data for update
    :type provider: dict | bytes

    :rtype: List[Provider]
    """
    if connexion.request.is_json:
        provider = connexion.request.get_json()

    return pds_functions.provider_update(npi, provider)