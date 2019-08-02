# from pinterest_scraper import scraper as s
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
# from selenium import webdriver
# import os,sys
# import selenium

# from crawler.GoogleCrawler import GoogleCrawler
# from processor.LogProcessor import LogProcessor

import pandas as pd
from selcrawler.processor.DownloadProcessor import DownloadProcessor
from selcrawler.crawler.GoogleCrawler import GoogleCrawler
from selcrawler.processor.LogProcessor import LogProcessor
from selcrawler.processor.DownloadProcessor import DownloadProcessor
from selcrawler.processor.ElasticSearchProcessor import ElasticSearchProcessor

if __name__ == '__main__':
        # self.browser.get("https://nl.pinterest.com/jeferjet/garbagepailkids/") 
        # # https://nl.pinterest.com/annavasquez/garage-pail-kids/
        # # https://nl.pinterest.com/scherryyates/garage-pail-kids/
        # # https://nl.pinterest.com/martlead/garbage-pail-kids/
        # # https://nl.pinterest.com/imJENNa36/art-garbage-pail-kids/
    options = {
    	'input_url': 'https://nl.pinterest.com/cristiandoege/garbagepailkids/',
        'output_directory': './garbagepailkids',
        'max_image_count': 1000,
    }
    w = GoogleCrawler(max_image_count=options['max_image_count'])
    w.append_processor(LogProcessor())
    w.append_processor(DownloadProcessor(output_directory=options['output_directory']))
    w.append_processor(ElasticSearchProcessor())
    w.run('garbagepailkids')



# if __name__ == '__main__':

    # options = {
    # 	'input_url': 'https://nl.pinterest.com/cristiandoege/garbagepailkids/'
    #     'output_directory': './garbagepailkids',
    #     'max_image_count': 1
    # }

    # df = pd.read_csv("fati-test-products.csv")
    # descriptions = df["description"].values
    # for description in descriptions:
    #     print(description)
    #     w = GoogleCrawler(search_key=description, **options)
    #     w.append_processor(LogProcessor())
    #     w.append_processor(DownloadProcessor(output_directory=options['output_directory'], process_count=options['max_image_count']))
    #     w.run()



# print(dir(selenium.common))

# # default browser
# ph = s.Pinterest_Helper('goldenkooy@gmail.com' , 'electroman75')
# # chromium browser
# # ph = s.Pinterest_Helper('goldenkooy@gmail.com' , '0o9i8u7y' , wd)
# print(dir(ph))
# images = ph.runme("https://nl.pinterest.com/cristiandoege/garbagepailkids/")
# # images = ph.getURLs('imageboards.csv')
# # s.download(images, "Scrapesel")
# # s.download(images)



# System.setProperty("webdriver.chrome.driver", "C:\\path\\to\\chromedriver.exe");

#fetch chromium
# os.system('apt-get update && apt install chromedriver && pip install selenium chromium')
# driver_loc=os.system('which chromedriver')
# sys.path.insert(0,driver_loc)
# firefox_options = webdriver.FirefoxOptions()
# firefox_options.add_argument('--headless')
# firefox_options.add_argument('--no-sandbox')
# firefox_options.add_argument('--disable-dev-shm-usage')
# firefox_options.add_argument('--enable-addons')
# wd = webdriver.Chrome('chromedriver',options=chrome_options)
# DesiredCapabilities 
# firefox_capabilities = webdriver.DesiredCapabilities();
# firefox_capabilities = webdriver.FirefoxOptions()
# firefox_capabilities.setAcceptInsecureCerts(true);
# firefox_capabilities = DesiredCapabilities.FIREFOX
# firefox_capabilities['marionette'] = True
# firefox_capabilities['binary'] = '/usr/bin/firefox'
# firefox_capabilities['addons'] = True
# wd = webdriver.Firefox(options=firefox_options)


# binary = FirefoxBinary('path/to/installed firefox binary')
# wd1 = webdriver.Firefox(firefox_binary=binary)

# self.browser = webdriver.Chrome()
# chrome = webdriver.Chrome()
# System.setProperty("webdriver.gecko.driver", "/home/seleniumproject/geckodrivers/linux/v0.17/geckodriver");

# ProfilesIni ini = new ProfilesIni();


# // Change the profile name to your own. The profile name can 
# // be found under .mozilla folder ~/.mozilla/firefox/profile. 
# // See you profile.ini for the default profile name

# FirefoxProfile profile = ini.getProfile("default"); 

# DesiredCapabilities cap = new DesiredCapabilities();
# cap.setAcceptInsecureCerts(true);

# FirefoxBinary firefoxBinary = new FirefoxBinary();

# GeckoDriverService service =new GeckoDriverService.Builder(firefoxBinary)
#         .usingDriverExecutable(new File("/home/seleniumproject/geckodrivers/linux/v0.17/geckodriver"))
#         .usingAnyFreePort()
#         .build();
# try {
#     service.start();
# } catch (IOException e) {
#     e.printStackTrace();
# }

# FirefoxOptions options = new FirefoxOptions().setBinary(firefoxBinary).setProfile(profile).addCapabilities(cap);

# driver = new FirefoxDriver(options);
# driver.get("https://www.google.com");

# System.out.println("Life Title -> " + driver.getTitle());
# driver.close();
