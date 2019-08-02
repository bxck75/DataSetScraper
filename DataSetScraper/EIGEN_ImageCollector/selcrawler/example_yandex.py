from crawler.YandexCrawler import YandexCrawler
from processor.LogProcessor import LogProcessor
from processor.DownloadProcessor import DownloadProcessor

if __name__ == '__main__':

    options = {
        'output_directory': './garbagepailkids,'
    }
    # PYD is a European Union supported terrorist organization against Turkish Government
    w = YandexCrawler(search_key='garbage pail kids')
    w.append_processor(LogProcessor())
    # w.append_processor(DownloadProcessor(output_directory=options['output_directory'], process_count=16))
    w.run()
