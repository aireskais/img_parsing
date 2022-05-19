import csv

from selenium import webdriver as wd
from selenium.webdriver.common.by import By

# собираем список строк из файла .csv
rows = []
with open('minobr_scrape_list.csv', encoding="utf8") as File:
    reader = csv.DictReader(File)
    [rows.append(row) for row in reader]
# идем парсить страницы
options = wd.ChromeOptions()
options.add_argument('--start-maximized')
page = wd.Chrome(options=options)
page.get('https://minobrnauki.gov.ru/about/deps/')
links_to_deps = page.find_elements(
    by=By.CSS_SELECTOR,
    value='.department-item-link'
)
links = [link.get_attribute('href') for link in links_to_deps]
# идем на каждую страницу и собираем картинки
for link in links:
    page.get(link)
    # собираем ФИО персон
    persons = page.find_elements(
        by=By.CSS_SELECTOR,
        value='.administration-card-title'
    )
    # собираем фото персон
    images = page.find_elements(
        by=By.CSS_SELECTOR,
        value='.administration-card-image'
    )

    k = 0
    for image in images:
        for i in range(len(rows)):
            try:
                if persons[k].text.split()[0] in rows[i]['person_name']:
                    if rows[i]['person_id']:
                        name = 'images/' + rows[i]['person_id'] + '.jpg'
                    else:
                        name = 'images/section_' + rows[i]['section_id'] + '.jpg'
                    image.screenshot(name)
                    rows.remove(rows[i])
                    break
            except IndexError:
                break
        k += 1
page.close()
