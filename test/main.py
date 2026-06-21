from selene import browser, be, have

browser.open('https://google.com')
browser.element('[name="q"]').should(be.blank).type('привет').press_enter()
# Проверяем наличие любого текста, который точно есть на странице
browser.element('html').should(have.text('Об этой странице'))

print("hello world")