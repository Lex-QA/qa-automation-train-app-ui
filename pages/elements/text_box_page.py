from playwright.sync_api import Page, expect

from elements.button import Button
from elements.text import Text
from pages.base_page import BasePage
from components.elements.text_box_form_component import TextBoxComponent


class TextBoxPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.text_box_form = TextBoxComponent(page)

        self.submit_button = Button(page, 'submit', 'Submit')

        self.new_name = Text(page, 'name', 'Name')
        self.new_email = Text(page, 'email', 'Email')
        self.new_current_address = Text(page, '//p[@id="currentAddress"]', 'Current Address', is_xpath=True)
        self.new_permanent_address = Text(page, '//p[@id="permanentAddress"]', 'Permanent Address', is_xpath=True)


    def click_submit_button(self):
        self.submit_button.click()

    def validate_new_values(self, full_name: str, email: str, current_address: str, permanent_address: str):
        self.new_name.check_contain_text(full_name)
        self.new_email.check_contain_text(email)
        self.new_current_address.check_contain_text(current_address)
        self.new_permanent_address.check_contain_text(permanent_address)



