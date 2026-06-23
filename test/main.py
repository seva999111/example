from selene import browser, be, have

browser.open('https://google.com')
browser.element('[name="q"]').should(be.blank).type('привет').press_enter()
# Проверяем наличие любого текста, который точно есть на странице
browser.element('html').should(have.text('Об этой странице'))


print("t!!&&i ti tu!!!!!! tu hh")

print("вот эту строчку ты не хочешь добавить,  а другую удалить? нУ и тут давай что то добавим ")