# General elements, variables and functions for Conduit application testing


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