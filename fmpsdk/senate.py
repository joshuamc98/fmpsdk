"""
   https://site.financialmodelingprep.com/developer/docs/#Senate-trading
"""
import typing

from .url_methods import __return_json_v4


def senate_trading_rss(
    apikey: str, page: int = 0
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP API for recently reported Senate trades.
    
    Stay up-to-date on the trading activity of US Senators
    and identify potential conflicts of interest with the FMP Senate
    Trading RSS Feed. This feed provides real-time updates on all the
    trades that are made by US Senators, including the same information
    as the Senate Trading endpoint.

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"senate-trading-rss-feed"
    query_vars = {"apikey": apikey, "page": page}
    return __return_json_v4(path=path, query_vars=query_vars)


def senate_trading_symbol(
    apikey: str,
    symbol: str,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP API for recently reported Senate trades filtered by symbol.
    
    Track the trading activity of US Senators and identify potential conflicts
    of interest with the FMP Senate Trading endpoint. This endpoint provides a
    list of all the trades that have been made by US Senators, including the date
    of the trade, the asset traded, the amount traded, and the price per share.

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"senate-trading"
    query_vars = {"apikey": apikey, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)


def senate_disclosure_rss(
    apikey: str, page: int = 0
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP API for recently filed Senate disclosures.
    
    Stay up-to-date on the financial interests of House Representative
    and identify potential conflicts of interest with the FMP House Disclosure
    RSS Feed. This feed provides real-time updates on all the financial disclosures
    that are made by House Representative, including the same information as the House
    Disclosure endpoint.

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"senate-disclosure-rss-feed"
    query_vars = {"apikey": apikey, "page": page}
    return __return_json_v4(path=path, query_vars=query_vars)


def senate_disclosure_symbol(
    apikey: str,
    symbol: str,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP API for recently filed Senate disclosures filtered by symbol.

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"senate-disclosure"
    query_vars = {"apikey": apikey, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)
