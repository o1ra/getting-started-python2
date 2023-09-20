from selene.support.shared import browser
from selene import be, have

def test_search_yashaka():
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))
def test_no_results():
    browser.element('[name="q"]').clear().type('глрдроэошг98669700090').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))

