import allure
from playwright.sync_api import Page, expect, Locator
from ui_coverage_tool import ActionType, SelectorType

from elements.ui_coverage import tracker
from tools.logger import get_logger

logger = get_logger("BASE_ELEMENT")


class BaseElement:
    def __init__(self, page: Page, locator: str, name: str, is_xpath: bool = False):
        self.page = page
        self.name = name
        self.locator = locator
        self.is_xpath = is_xpath

    @property
    def type_of(self) -> str:
        return "base element"

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        """Возвращает Playwright Locator (поддерживает ID и XPath)."""
        locator = self.locator.format(**kwargs)
        step = f'Getting locator "{locator}" at index "{nth}"'

        with allure.step(step):
            logger.info(step)
            if self.is_xpath:
                return self.page.locator(f'xpath={locator}').nth(nth)
            return self.page.locator(f'#{locator}').nth(nth)

    def get_raw_locator(self, nth: int = 0, **kwargs) -> str:
        """Возвращает сырой XPath (для трекинга покрытия)."""
        if self.is_xpath:
            formatted_locator = self.locator.format(**kwargs)
            # Если locator уже XPath, добавляем индекс (если nth > 0)
            if nth > 0:
                return f"({formatted_locator})[{nth + 1}]"
            return formatted_locator
        return f"//*[@id='{self.locator.format(**kwargs)}'][{nth + 1}]"

    def get_custom_locator(self, custom_xpath: str, nth: int = 0, **kwargs) -> Locator:
        """Возвращает Locator для произвольного XPath (не только ID)."""
        formatted_xpath = custom_xpath.format(**kwargs)
        step = f'Getting custom XPath locator "{formatted_xpath}" at index "{nth}"'

        with allure.step(step):
            logger.info(step)
            return self.page.locator(f'xpath={formatted_xpath}').nth(nth)

    def track_coverage(self, action_type: ActionType, nth: int = 0, **kwargs):
        tracker.track_coverage(
            selector=self.get_raw_locator(nth, **kwargs),
            action_type=action_type,
            selector_type=SelectorType.XPATH
        )

    def click(self, nth: int = 0, **kwargs):
        step = f'Clicking {self.type_of} "{self.name}"'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            locator.click()

        self.track_coverage(ActionType.CLICK, nth, **kwargs)

    def check_visible(self, nth: int = 0, **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" is visible'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_be_visible()

        self.track_coverage(ActionType.VISIBLE, nth, **kwargs)

    def check_have_text(self, text: str, nth: int = 0, **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" has "{text}"'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_have_text(text)

        self.track_coverage(ActionType.TEXT, nth, **kwargs)

    def check_contain_text(self, text: str, nth: int = 0, **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" has "{text}"'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_contain_text(text)

        self.track_coverage(ActionType.TEXT, nth, **kwargs)