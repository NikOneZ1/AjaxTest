class Page:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, id):
        element = self.driver.find_element_by_id(id)
        return element

    def click_element(self, element):
        element.click()
