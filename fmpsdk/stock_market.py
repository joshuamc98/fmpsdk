import typing

from .settings import DEFAULT_LIMIT
from .url_methods import __return_json_v3


def actives(apikey: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /actives/ API
    
    The FMP Market Most Active endpoint provides a list
    of the stocks that have the highest trading volume on
    a given day. This information can be used by investors
    to identify stocks that are liquid and to potential trading
    opportunities.The FMP Market Most Active endpoint provides a
    list of the stocks that have the highest trading volume on a
    given day. This information can be used by investors to identify
    stocks that are liquid and to potential trading opportunities.

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"actives"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def gainers(apikey: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /gainers/ API
    
    The FMP Market Biggest Gainers endpoint provides a list
    of the stocks that have gained the most value on a given day.
    This information can be used by investors to identify stocks
    that are momentum and to potential investment opportunities.

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"gainers"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def losers(apikey: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /losers/ API
    
    The FMP Market Biggest Losers endpoint provides a list
    of the stocks that have lost the most value on a given day.
    This information can be used by investors to identify stocks
    that are underperforming and to potential trading opportunities.

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"losers"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def market_hours(apikey: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /market-hours/ API
    
    

    :param apikey: Your API key.
    :return: A list of dictionaries.
    """
    path = f"market-hours"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def sectors_performance(
    apikey: str, limit: int = DEFAULT_LIMIT
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /sectors_performance/ API
    
    The FMP Sector Performance endpoint provides the performance
    of each sector of the stock market over a specified period of
    time. This information can be used by investors to identify
    sectors that are outperforming or underperforming the market.

    :param apikey: Your API key.
    :param limit: Number of rows to return
    :return: A list of dictionaries.
    """
    path = f"sectors-performance"
    query_vars = {"apikey": apikey, "limit": limit}
    return __return_json_v3(path=path, query_vars=query_vars)
