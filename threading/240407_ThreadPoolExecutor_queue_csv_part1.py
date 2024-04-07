# С использованием пула потоков запросите у yahoo.finance данные по ценам.
# Тикеры в файле - источнике укажите на свой вкус, например: AAPL, MSFT, AMZN, NVDA, TSLA, GOOGL, META, BRK-B, UNH, JPM.

# В качестве параметров запроса укажите недельный таймфрейм, интервал времени запроса - с начала 2020 года по настоящий день.

# Структура решения должна быть следующей:
# - пул потоков выполняет целевую задачу: функцию получения данных по запросу.
# - по мере получения ответа, данные попадают в потокобезопасную очередь данных.
# - отдельным потоком из очереди выполняется сохранение данных в .csv файл.
# - главный поток является управляющим, он только запускает потоки.

# Как и что именно хранить в csv файле, как его называть, как выполнять преобразование данных из ответа сервиса в данные
# для заполнения csv файла, обоработка ошибок - все это остается на ваше усмотрение. Не забывайте только, что данные csv
# файла нам нужны для будущего постороения графиков скорректированных цен.



import concurrent.futures
import csv
import os
import queue
import requests
import threading
from datetime import datetime, timezone
from dateutil.parser import parse
from typing import Sequence, TypeAlias, Union

TickerData: TypeAlias = Union[Sequence[str], Sequence[float], Sequence[datetime]]

def get_history_data(ticker: str, start_date: str, end_date: str, interval: str = "1wk") -> TickerData:
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
    params = {
        "period1": int(parse(start_date).replace(tzinfo=timezone.utc).timestamp()),
        "period2": int(parse(end_date).replace(tzinfo=timezone.utc).timestamp()),
        "interval": interval,
        "includeAdjustedClose": "true"
    }
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Connection': 'keep-alive'
    }
    try:
        response = requests.get(url, headers=headers, params=params).json()
        result = [
            [response['chart']['result'][0]['meta']['symbol']] * len(response['chart']['result'][0]['timestamp']),
            response['chart']['result'][0]['indicators']['adjclose'][0]['adjclose'],
            [datetime.fromtimestamp(stamp).date() for stamp in response['chart']['result'][0]['timestamp']]
        ]
    except Exception:
        print(f'Failed to get data for {ticker}')
        raise ValueError
    return result


def csv_file_writer() -> None:
    os.makedirs('tickers_data', exist_ok=True)
    while True:
        data = tikers_data_queue.get()
        file_path = os.path.join('tickers_data', 'raw_data.csv')
        with open(file_path, 'a', encoding='utf-8', newline='') as fin:
            writer = csv.writer(fin, delimiter=';')
            writer.writerows(zip(*data))
        tikers_data_queue.task_done()


def results_handler(future: concurrent.futures.Future) -> None:
    exception = future.exception()
    if exception is not None:
        return
    try:
        data = future.result()
        tikers_data_queue.put(data)
    except Exception as err:
        print(f'Unknown error while handling data {err}')


tickers_to_load = ['AAPL', 'MSFT', 'AMZN', 'NVDA', 'TSLA', 'GOOGL', 'META', 'BRK-B', 'UNH', 'JPM']
tikers_data_queue = queue.Queue()

thr = threading.Thread(target=csv_file_writer, daemon=True)
thr.start()

with concurrent.futures.ThreadPoolExecutor() as executor:
    for ticker in tickers_to_load:
        future = executor.submit(get_history_data, ticker, '01/01/20', '01/04/24')
        future.add_done_callback(results_handler)

tikers_data_queue.join()