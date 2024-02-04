import logging
import typing

import requests

from .settings import DEFAULT_LIMIT, SEC_RSS_FEEDS_FILENAME, BASE_URL_v3
from .url_methods import __return_json_v3, __return_json_v4


def institutional_holders(
    apikey: str, symbol: str
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /institutional-holder/ API.
    
    Provides the stock ownership of individual holders,
    including institutional and individual investors.

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :return: A list of dictionaries.
    """
    path = f"institutional-holder/{symbol}"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def mutual_fund_holders(
    apikey: str, symbol: str
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /mutual-fund-holder/ API.
    
    The FMP Mutual Fund Holder endpoint provides a list of all the institutional
    investors that own shares of a particular mutual fund. This information can be
    used by investors to track the ownership of a mutual fund and to identify potential
    trends. For example, an investor may want to know which institutions are buying or
    selling shares of a particular mutual fund.

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :return: A list of dictionaries.
    """
    path = f"mutual-fund-holder/{symbol}"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def etf_holders(apikey: str, symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /etf-holder/ API.
    
    The FMP ETF Holder endpoint provides a list of all
    the institutional investors that own shares of an ETF.
    For example, an investor may want to know which institutions
    are buying or selling shares of a particular ETF.

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :return: A list of dictionaries.
    """
    path = f"etf-holder/{symbol}"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def etf_sector_weightings(
    apikey: str, symbol: str
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /etf-sector-weightings/ API.
    
    The FMP ETF Sector Weighting endpoint provides
    a breakdown of the percentage of an ETF's assets
    that are invested in each sector. For example, an
    investor may want to invest in an ETF that has a high
    exposure to the technology sector if they believe that
    the technology sector is poised for growth.


    :param apikey: Your API key.
    :param symbol: Company ticker.
    :return: A list of dictionaries.
    """
    path = f"etf-sector-weightings/{symbol}"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def etf_country_weightings(
    apikey: str, symbol: str
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /etf-country-weightings/ API.
    
    The FMP ETF Country Weighting endpoint provides a breakdown 
    of the percentage of an ETF's assets that are invested in
    each country. For example, an investor may want to invest
    in an ETF that has a high exposure to China if they believe
    that the Chinese economy is poised for growth.

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :return: A list of dictionaries.
    """
    path = f"etf-country-weightings/{symbol}"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def sec_rss_feeds(
    apikey: str,
    limit: int = DEFAULT_LIMIT,
    download: bool = False,
    filename: str = SEC_RSS_FEEDS_FILENAME,
) -> typing.Union[typing.List[typing.Dict], None]:
    """
    Query FMP /rss_feed/ API.
    
    A real-time feed of SEC filings from publicly traded companies,
    including the filing type, link to SEC page, and direct link to
    the filing. This endpoint can be used to stay up-to-date on the
    latest SEC filings for all companies or for a specific set of companies.

    :param apikey: Your API key.
    :param limit: Number of rows to return.
    :param download: True/False
    :param filename: Name of saved file.
    :return: A list of dictionaries.
    """
    path = f"rss_feed"
    query_vars = {"apikey": apikey}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL_v3}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving SEC RSS Feeds as {filename}.")
    else:
        query_vars["limit"] = limit
        return __return_json_v3(path=path, query_vars=query_vars)


def cik_list(apikey: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /cik_list/ API.

    Complete list of all institutional investment managers by cik
    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"cik_list"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def cik_search(apikey: str, name: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /cik-search/ API.
    
    Our CIK List provides a comprehensive database of CIK
    numbers for SEC-registered entities. A CIK number is a
    unique identifier assigned to each SEC-registered entity,
    and it is required for many financial transactions. Our CIK
    List is a valuable resource for businesses and individuals who
    need to quickly and easily find CIK numbers

    FORM 13F cik search by name
    :param apikey: Your API key.
    :param name: Name
    :return: A list of dictionaries.
    """
    path = f"cik-search/{name}"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def cik(apikey: str, cik_id: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /cik/ API.
    
    Quickly find registered company names linked to
    SEC-registered entities using their CIK Number with
    our CIK Search..

    FORM 13F get company name by cik
    :param apikey: Your API key.
    :param cik_id: CIK value
    :return: A list of dictionaries.
    """
    path = f"cik/{cik_id}"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def form_13f(
    apikey: str, cik_id: str, date: str = None
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /form-thirteen/ API.
    
    Provides quarterly reports on the equity holdings
    of institutional investment managers with over $100
    million in assets under management.

    FORM 13F statements provides position-level report of all institutional investment managers with more than $100m
    in assets under management.
    :param apikey: Your API key.
    :param cik_id: CIK value
    :param date: 'YYYY-MM-DD'
    :return: A list of dictionaries.
    """
    path = f"form-thirteen/{cik_id}"
    query_vars = {"apikey": apikey}
    if date:
        query_vars["date"] = date
    return __return_json_v3(path=path, query_vars=query_vars)


def cusip(apikey: str, cik_id: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /cusip/ API.
    
    Access information about financial instruments and securities
    by simply entering their unique CUSIP (Committee on Uniform Securities
    Identification Procedures) numbers with our CUSIP Search.

    Cusip mapper
    :param apikey: Your API key.
    :param cik_id: CIK value
    :return: A list of dictionaries.
    """
    path = f"cusip/{cik_id}"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def institutional_symbol_ownership(
    apikey: str,
    symbol: str,
    limit: int,
    includeCurrentQuarter: bool = False,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /institutional-ownership/symbol-ownership API.
    
    Provides the institutional ownership of individual stocks.

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :param limit: up to how many quarterly reports to return.
    :param includeCurrentQuarter: Whether to include any available data in the current quarter.
    :return: A list of dictionaries.
    """
    path = f"institutional-ownership/symbol-ownership"
    query_vars = {
        "symbol": symbol,
        "apikey": apikey,
        "includeCurrentQuarter": includeCurrentQuarter,
        "limit": limit,
    }
    return __return_json_v4(path=path, query_vars=query_vars)
