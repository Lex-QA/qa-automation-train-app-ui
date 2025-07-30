import allure
import pytest
from allure_commons.types import Severity

from config import settings
from pages.elements.text_box_page import TextBoxPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.routes import SidebarSection, SidebarItem, AppRoute


@pytest.mark.regression
@allure.tag(AllureTag.ELEMENTS, AllureTag.ELEMENTS)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.ELEMENTS)
@allure.story(AllureStory.TEXT_BOX)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.ELEMENTS)
@allure.sub_suite(AllureStory.TEXT_BOX)
class TestTextBox:
    @allure.title('Fill text box with correct data')
    @allure.severity(Severity.CRITICAL)
    def test_successful_submit_text_bot(self, text_box_page: TextBoxPage):
        text_box_page.visit_by_click(url=AppRoute.MAIN, section=SidebarSection.ELEMENTS, item=SidebarItem.TEXT_BOX)
        text_box_page.text_box_form.fill(
            full_name=settings.test_text_box.full_name,
            email=settings.test_text_box.email,
            current_address=settings.test_text_box.current_address,
            permanent_address=settings.test_text_box.permanent_address
        )
        text_box_page.click_submit_button()
        text_box_page.validate_new_values(
            full_name=settings.test_text_box.full_name,
            email=settings.test_text_box.email,
            current_address=settings.test_text_box.current_address,
            permanent_address=settings.test_text_box.permanent_address
        )

