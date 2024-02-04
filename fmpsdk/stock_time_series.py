import typing

from .general import __quotes
from .url_methods import __return_json_v3, __return_json_v4


def quote_short(apikey: str, symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /quote-short/ API.
    
    Get a simple quote for a stock, including the
    price, change, and volume. This endpoint can be
    used to get a quick snapshot of a stock's performance
    or to calculate its valuation.

    :param apikey: Your API key
    :param symbol: Company ticker.
    :return: A list of dictionaries.
    """
    path = f"quote-short/{symbol}"
    query_vars = {
        "apikey": apikey,
    }
    return __return_json_v3(path=path, query_vars=query_vars)


def exchange_realtime(
    apikey: str, exchange: str
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /quotes/ API.

    :param apikey: Your API key
    :param exchange: Exchange symbol.
    :return: A list of dictionaries.
    """
    return __quotes(apikey=apikey, value=exchange)


def historical_stock_dividend(
    apikey: str, symbol: str
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /historical-price-full/stock_divident/ API

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :return: A list of dictionaries.
    """
    path = f"historical-price-full/stock_dividend/{symbol}"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def historical_stock_split(
    apikey: str, symbol: str
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /historical-price-full/stock_divident/ API
    
    A list of historical dividend payments for publicly traded
    companies, including the date of the dividend payment, the
    ex-dividend date, and the dividend per share.

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :return: A list of dictionaries.
    """
    path = f"historical-price-full/stock_split/{symbol}"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def historical_survivorship_bias_free_eod(
    apikey: str, symbol: str, date: str
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /historical-price-full/<ticker>/<date> API
    
    The FMP Daily Chart endpoint provides a daily chart for a given
    company. The chart displays the opening price, high price, low price,
    and closing price of the company's stock for each day in a specified
    date range. By default the limit is 5 years of historical data, to get
    data prior to this date, please use the to & from parameters with a limit
    of 5 years.

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :param date: str YYYY-MM-DD
    :return: A list of dictionaries.
    """
    path = f"historical-price-full/{symbol}/{date}"
    query_vars = {"apikey": apikey}
    return __return_json_v4(path=path, query_vars=query_vars)
