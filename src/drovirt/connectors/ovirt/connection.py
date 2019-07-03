
import logging

import ovirtsdk4 as sdk

logger = logging.getLogger(__name__)


def get_connection(api_url, username, password, allow_insecure):
    connection = sdk.Connection(
        url=api_url,
        username=username,
        password=password,
        ca_file='ca.pem',
        debug=True,
        insecure=allow_insecure,
        log=logger,
    )
    return connection
