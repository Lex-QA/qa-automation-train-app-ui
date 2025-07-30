import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.input import Input
from elements.text import Text


class TextBoxComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, '//div[@class="main-header"]', 'Text Box', is_xpath=True)

        self.full_name_input = Input(page, 'userName', 'Full Name')
        self.email_input = Input(page, 'userEmail', 'Email')
        self.current_address_input = Input(page, 'currentAddress', 'Permanent Address')
        self.permanent_address_input = Input(page, 'permanentAddress', 'Password')

    @allure.step("Fill text box form")
    def fill(self, full_name: str, email: str, current_address: str, permanent_address: str):
        self.full_name_input.fill(full_name)
        self.full_name_input.check_have_value(full_name)

        self.email_input.fill(email)
        self.email_input.check_have_value(email)

        self.current_address_input.fill(current_address)
        self.current_address_input.check_have_value(current_address)

        self.permanent_address_input.fill(permanent_address)
        self.permanent_address_input.check_have_value(permanent_address)

    @allure.step("Check visible text box form")
    def check_visible(self, title: str, full_name: str, email: str, current_address: str, permanent_address: str):
        self.title.check_have_text(title)

        self.full_name_input.check_visible()
        self.full_name_input.check_have_value(full_name)

        self.email_input.check_visible()
        self.email_input.check_have_value(email)

        self.current_address_input.check_visible()
        self.current_address_input.check_have_value(current_address)

        self.permanent_address_input.check_visible()
        self.permanent_address_input.check_have_value(permanent_address)
