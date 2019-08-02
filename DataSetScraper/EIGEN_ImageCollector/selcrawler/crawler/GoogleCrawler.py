import time
from .BaseCrawler import BaseCrawler


class GoogleCrawler(BaseCrawler):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # google search specific url parameters
        self.search_url_prefix = kwargs.get('search_url_prefix', 'https://www.google.com.sg/search?q=')
        self.search_url_suffix = kwargs.get('search_url_suffix','&source=lnms&tbm=isch&sa=X&ei=0eZEVbj3IJG5uATalICQAQ&ved=0CAcQ_AUoAQ&biw=939&bih=591')

        # show more options
        # options : 'id','class'
        self.show_more_find_type = kwargs.get('show_more_find_type', 'id')
        self.show_more_find_value = kwargs.get('show_more_find_value', 'smb')

        # image options
        self.preview_image_class = kwargs.get('preview_image_class', 'rg_ic')
        self.original_image_class = kwargs.get('original_image_class', 'rg_l')

    def get_search_url_prefix(self):
        return self.search_url_prefix

    def get_search_url_suffix(self):
        return self.search_url_suffix

    def extract_pic_url(self, driver):
        """ extract all the raw pic url in list
        """
        original_tag_list = driver.find_elements_by_class_name(self.original_image_class)
        # original image

        for tag in original_tag_list:
            original_image_url = tag.get_attribute('href')
            preview_image_url = tag.find_element_by_class_name(self.preview_image_class).get_attribute('src')
            self.pic_url_list.append((preview_image_url, original_image_url))
            if self.max_image_count == len(self.pic_url_list):
                break
        driver.quit()

    def load_page(self, driver, target_url):
        driver.get(target_url)
        try:
            doc_height = driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            # driver.save_screenshot('out.png')
            button_load_rest = driver.find_element_by_id(self.show_more_find_value)

            counter = 0
            while (button_load_rest is None) or (not button_load_rest.is_displayed()):
                time.sleep(0.1)
                doc_height_new = driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                button_load_rest = driver.find_element_by_id(self.show_more_find_value)
                if button_load_rest and button_load_rest.is_displayed():
                    button_load_rest.click()
                    time.sleep(0.5)
                    doc_height_new = driver.execute_script(
                        "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                if doc_height == doc_height_new:
                    button_load_rest = driver.find_element_by_id(self.show_more_find_value)
                    if button_load_rest is None:
                        break
                    else:
                        counter += 1
                        if counter > 10:
                            break
                else:
                    doc_height = doc_height_new
                    counter = 0

        except Exception as e:
            print(e)
