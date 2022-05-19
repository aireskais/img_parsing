import csv

results = []
with open('minobr_scrape_list.csv') as File:
    reader = csv.DictReader(File)
    for row in reader:
        results.append(row)
