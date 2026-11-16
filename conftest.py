import pytest
from pathlib import Path
from playwright.sync_api import sync_playwright

TRACE_DIR = Path(__file__).resolve().parent / "traces"
TRACE_DIR.mkdir(exist_ok=True)


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture
def page(browser, request):
    context = browser.new_context(viewport={"width": 1440, "height": 900})
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()

    try:
        yield page
    finally:
        trace_name = f"{request.node.name}.zip"
        trace_path = TRACE_DIR / trace_name
        context.tracing.stop(path=str(trace_path))
        page.close()
        context.close()