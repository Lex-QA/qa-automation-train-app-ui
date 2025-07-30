from typing import Pattern

import allure
from playwright.sync_api import Page, expect

from tools.logger import get_logger

logger = get_logger("BASE_PAGE")


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        step = f'Opening the url "{url}"'

        with allure.step(step):
            logger.info(step)
            self.page.goto(url, wait_until='networkidle')

    def visit_by_click(self, url, section: str, item: str):
        step = f'Opening page by clicking on sidebar item: {section} -> {item.value}'

        with allure.step(step):
            logger.info(step)
            self.page.goto(" http://85.192.34.140:8081", wait_until='networkidle')

            # Исправленный локатор для категории (используем XPath вместо CSS)
            category_locator = self.page.locator(
                f'xpath=//div[@class="card mt-4 top-card"][{section.value}]'
            )
            category_locator.click()
            self.page.wait_for_load_state('networkidle')

            # Локатор для пункта меню
            menu_item = self.page.locator(
                f'xpath=//span[text()="{item.value}"]'
            )

            # Кликаем по пункту меню
            menu_item.click()
            self.page.wait_for_load_state('networkidle')

    def reload(self):
        step = f'Reloading page with url "{self.page.url}"'

        with allure.step(step):
            logger.info(step)
            self.page.reload(wait_until='networkidle')

    def check_current_url(self, expected_url: Pattern[str]):
        step = f'Checking that current url matches pattern "{expected_url.pattern}"'

        with allure.step(step):
            logger.info(step)
            expect(self.page).to_have_url(expected_url)
