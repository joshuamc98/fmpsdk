import typing

from .url_methods import (
    __return_json_v3,
    __validate_statistics_type,
    __validate_technical_indicators_time_delta,
)


def technical_indicators(
    apikey: str,
    symbol: str,
    period: int = 10,
    statistics_type: str = "SMA",
    time_delta: str = "daily",
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /technical_indicator/ API.
    
    Technical indicators are mathematical calculations applied to historical
    market data, like price and volume, to assist traders and analysts in
    predicting future price movements. They provide visual representations
    and signals, helping traders make informed decisions about buying or selling
    assets. However, they are based on past data, have limitations, and should be
    used alongside other forms of analysis for more accurate trading strategies.

    :param apikey: Your API key
    :param symbol: Company ticker
    :param period: I don't know.  10 is my only example.
    :param statistics_type: sma, ema, wma, dema, tema, williams, rsi, adx, standarddeviation 
    :param time_delta: 'daily' or intraday: 1min, 5min, 15min, 30min, 1hour, 4hour, 1day
    :return:
    """
    path = f"technical_indicator/{__validate_technical_indicators_time_delta(time_delta)}/{symbol}"
    query_vars = {
        "apikey": apikey,
        "period": period,
        "type": __validate_statistics_type(statistics_type),
    }
    return __return_json_v3(path=path, query_vars=query_vars)
