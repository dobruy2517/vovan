from selenium import webdriver

driver = webdriver.Chrome('/home/ihor/chromedriver')
driver.maximize_window()

for url in open("url_file.txt"):
    driver.get(url)
    title_tegs = driver.find_elements_by_css_selector('[title]')
    for title_value in title_tegs:
        text = title_value.get_attribute('title')
        titles = open('titles_values.txt', 'a')
        titles.write((text + '\n').encode('utf8'))

    alt_tags = driver.find_elements_by_tag_name('alt')
    for alt_value in alt_tags:
        alt_text = alt_value.get_attribute('alt')
        titles = open('alts_values.txt', 'a')
        titles.write((alt_text + '\n').encode('utf8'))
    driver.close()
