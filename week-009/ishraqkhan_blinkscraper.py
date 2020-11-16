from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

URL = 'https://www.blinkfitness.com/locations/'
PATH = "/Users/ishraqkhan/bin/chromedriver"

# initialize web driver with eager page loading strategy
options = Options()
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(executable_path=PATH, options=options)
driver.get(URL)

# get all Areas web element
element = WebDriverWait(driver, timeout=15).until(lambda d: d.find_element_by_xpath('//*[@id="layout-first-page"]/div/div/bw-locations/bw-location-list[2]/div'))

areas = element.find_elements_by_class_name('area')
#print(len(areas))


gyms = []
for area in areas:
    # find area location
    location = area.find_element_by_class_name('area__header').text
    
    # list of facilities per area
    facilities = area.find_elements_by_class_name('area__item')
    for facility in facilities:      
        branch = facility.find_element_by_class_name('facility__header').text # facility name
        
        # save gym information as dictionary
        if branch != '':
            gym = {} 
            gym['area'] = location 
            gym['branch'] = branch # 
            gym['status'] = facility.find_element_by_class_name('facility__indicator').text # open, closed, etc
            gym['address'] = facility.find_element_by_class_name('facility__address').text # facility address
            gyms.append(gym)
            
# for gym in gyms:
#     print(gym)