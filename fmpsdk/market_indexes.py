import logging
import typing

import requests

from .general import __quotes
from .settings import (
    DOWJONES_CONSTITUENTS_FILENAME,
    NASDAQ_CONSTITUENTS_FILENAME,
    SP500_CONSTITUENTS_FILENAME,
    BASE_URL_v3,
)
from .url_methods import __return_json_v3


def indexes(apikey: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /quotes/index/ API.
    
    The FMP Market Index endpoint provides a list of all
    the major stock market indices, such as the S&P 500,
    the Dow Jones Industrial Average, and the Nasdaq Composite
    Index. This information can be used by investors to track
    the performance of the overall stock market and to identify
    sectors and industries that are outperforming or underperforming
    the market.

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"index"
    return __quotes(apikey=apikey, value=path)


def sp500_constituent(
    apikey: str,
    download: bool = False,
    filename: str = SP500_CONSTITUENTS_FILENAME,
) -> typing.Union[typing.List[typing.Dict], None]:
    """
    Query FMP /sp500_constituent/ API
    
    Provides historical data for all companies that are included in the S&P 500 index.

    :param apikey: Your API key.
    :param download: True/False
    :param filename: Name of saved file.
    :return: A list of dictionaries.
    """
    path = f"sp500_constituent"
    query_vars = {"apikey": apikey}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL_v3}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving SP500 Constituents as {filename}.")
    else:
        return __return_json_v3(path=path, query_vars=query_vars)


def historical_sp500_constituent(
    apikey: str,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /historical/sp500_constitnuet/ API.
    
    Provides historical data for all companies that are
    included in the S&P 500 index.

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"historical/sp500_constituent"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def nasdaq_constituent(
    apikey: str,
    download: bool = False,
    filename: str = NASDAQ_CONSTITUENTS_FILENAME,
) -> typing.Union[typing.List[typing.Dict], None]:
    """
    Query FMP /nasdaq_constituent/ API
    
    Provides a list of all companies that are
    listed on the NASDAQ stock exchange.

    :param apikey: Your API key.
    :param download: True/False
    :param filename: Name of saved file.
    :return: A list of dictionaries.
    """
    path = f"nasdaq_constituent"
    query_vars = {"apikey": apikey}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL_v3}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving NASDAQ Constituents as {filename}.")
    else:
        return __return_json_v3(path=path, query_vars=query_vars)


def historical_nasdaq_constituent(
    apikey: str,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /historical/nasdaq_constitnuet/ API.
    
    Provides a list of all companies that are listed
    on the NASDAQ stock exchange.

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"historical/nasdaq_constituent"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def dowjones_constituent(
    apikey: str,
    download: bool = False,
    filename: str = DOWJONES_CONSTITUENTS_FILENAME,
) -> typing.Union[typing.List[typing.Dict], None]:
    """
    Query FMP /dowjones_constituent/ API
    
    Provides a list of all companies that are included
    in the Dow Jones Industrial Average.

    :param apikey: Your API key.
    :param download: True/False
    :param filename: Name of saved file.
    :return: A list of dictionaries.
    """
    path = f"dowjones_constituent"
    query_vars = {"apikey": apikey}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL_v3}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving DOWJONES Constituents as {filename}.")
    else:
        return __return_json_v3(path=path, query_vars=query_vars)


def historical_dowjones_constituent(
    apikey: str,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /historical/dowjones_constitnuet/ API.
    
    Provides a list of all companies that are included
    in the Dow Jones Industrial Average.
    
    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"historical/dowjones_constituent"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def available_indexes(apikey: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /symbol/available-indexes/ API
    
    The FMP Available Indexes endpoint provides a list
    of all available indexes. The list includes the index's
    symbol, name, and exchange.

    :param apikey: Your API key
    :return: A list of dictionaries.
    """
    path = f"symbol/available-indexes"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)
