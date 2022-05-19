import csv

from selenium import webdriver as wd
from selenium.webdriver.common.by import By

options = wd.ChromeOptions()
options.add_argument('--start-maximized')
page = wd.Chrome(options=options)
page.get('https://minobrnauki.gov.ru/about/deps/ad/')

persons = page.find_elements(
    by=By.CSS_SELECTOR,
    value='.administration-card-title'
)
images = page.find_elements(
    by=By.CSS_SELECTOR,
    value='.administration-card-image'
)
rows = []

with open('minobr_scrape_list.csv') as File:
    reader = csv.DictReader(File)
    [rows.append(row) for row in reader]

if images:
    for image in images:
        for person in persons:
            for i in range(len(rows)):
                if rows[i]['family_name'] in person.text.split():
                    name = rows[i]['person_id'] + '.jpg'
                    image.location_once_scrolled_into_view
                    image.screenshot(name)
                    rows.remove(rows[i])
                    break
page.close()
# if images:
#     for image in images:
#         with open('minobr_scrape_list.csv') as File:
#             reader = csv.DictReader(File)
#             for row in reader:
#                 break_flag = False
#                 for person in persons:
#                     if row['family_name'] in person.text.split():
#                         name = row['person_id'] + '.jpg'
#                         image.location_once_scrolled_into_view
#                         image.screenshot(name)
#                         break_flag = True
#                         break

# with open("family.txt", 'w', encoding='utf-8') as file:
#     if not persons:
#         print('no_images_here', file=file)
#         file.close()
#         exit()
#     print(*[image.text for image in persons], sep='\n', file=file)
#     file.close()
