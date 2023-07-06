from pathlib import Path
from datetime import datetime as dt

BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:

    def open_spider(self, spider):
        self.results = {}

    def process_item(self, item, spider):
        status = item['status']

        if self.results.get(status):
            self.results[status] += 1
        else:
            self.results[status] = 1

        return item

    def close_spider(self, spider):
        self.results['Total'] = sum(self.results.values())

        downloads_dir = BASE_DIR / 'results'
        date = dt.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = downloads_dir / f'status_summary_{date}.csv'

        with open(filename, mode='w', encoding='utf-8') as f:
            f.write('Status,Count\n')
            for key, value in self.results.items():
                f.write(f'{key},{value}\n')
