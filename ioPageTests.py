from selenium import webdriver
import time

#Change base url according to your environment
base_url = "http://localhost:9966/petclinic/"

driver = webdriver.Firefox()
driver.implicitly_wait(5)
driver.get(base_url)

assert "PetClinic :: a Spring Framework demonstration" in driver.title
elem = driver.find_element_by_link_text("Find owners")
elem.click()

#searching owners
elem = driver.find_element_by_class_name("form-actions")
find_owners_btn = elem.find_elements_by_tag_name("button")
find_owners_btn[0].click()
#todo i need to slow down the webdriver to wait table is populated with data.
#todo change time.sleep() to wait command
time.sleep(2)


#switching to toolbar frame
driver.switch_to.frame(driver.find_element_by_id("__xrMenuFrame"))

#opening IO page
elem = driver.find_element_by_id("tool-queries").click()

# switching to IO frame
driver.switch_to.default_content()

ioFrame = driver.find_element_by_id("__xrIoFrame")
driver.switch_to.frame(ioFrame)

#searching IO name
header_elem = driver.find_element_by_tag_name("h1")
assert "Input / Output" in header_elem.text

#searching close button
close_btn = driver.find_element_by_id("mainClose")
close_btn.click()
assert "Input / Output" not in header_elem.text

driver.close()
print "\033[0;32mTest Passed!\033[0m"
