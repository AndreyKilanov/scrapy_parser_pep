from collections import defaultdict
from csv import writer, excel
from datetime import datetime as dt
from pathlib import Path

from pep_parse.settings import DOWNLOAD_DIR

BASE_DIR = Path(__file__).parent.parent / DOWNLOAD_DIR


class PepParsePipeline:
    def __init__(self):
        BASE_DIR.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.dict = defaultdict(int)

    def process_item(self, item, spider):
        self.dict[item['status']] += 1
        return item

    def close_spider(self, spider):
        self.dict['Total'] = sum(self.dict.values())

        date = dt.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = BASE_DIR / f'status_summary_{date}.csv'

        with open(filename, 'w', newline='') as csvfile:
            writer(csvfile, dialect=excel).writerows(
                (('Status', 'Count'), *self.dict.items())
            )
