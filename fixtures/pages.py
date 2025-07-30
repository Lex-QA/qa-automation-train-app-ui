import pytest
from playwright.sync_api import Page

from pages.elements.text_box_page import TextBoxPage


@pytest.fixture
def text_box_page(page: Page) -> TextBoxPage:
    return TextBoxPage(page=page)
