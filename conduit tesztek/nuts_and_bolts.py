# General elements, variables and functions for Conduit application testing
input_butt_path = '//*[@id="app"]/div/div/div/div/form/button'

def element_by_path(xpath):
    element = driver.find_element_by_xpath(xpath)
    return element

def input_elements_list(xpath):
    input_elements = driver.find_elements_by_xpath(xpath)
    return input_elements

    # finding input element's names for further use (in an other app)
def input_elements_names(element_list):
    input_names = []
    for i in range(len(element_list)):
        input_name = input_elements[i].get_attribute("placeholder")
        input_names.append(input_name)
    return input_names