from collections import defaultdict
from csv import DictWriter
from datetime import datetime as dt
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent / 'results'


class PepParsePipeline:

    def open_spider(self, spider):
        self.dict = defaultdict(int)

    def process_item(self, item, spider):
        self.dict[item['status']] += 1
        return item

    def close_spider(self, spider):
        self.dict['Total'] = sum(self.dict.values())

        date = dt.now().strftime('%Y-%m-%d_%H-%M-%S')
        BASE_DIR.mkdir(exist_ok=True)
        filename = BASE_DIR / f'status_summary_{date}.csv'

        with open(filename, 'w', newline='') as csvfile:
            status, count = 'Status', 'Count'
            writer = DictWriter(csvfile, fieldnames=[status, count])
            writer.writeheader()

            dict_status = []
            for key, value in self.dict.items():
                dict_status.append({status: key, count: value})

            writer.writerows(dict_status)
