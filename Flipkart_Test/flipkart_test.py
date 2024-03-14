from joblib import Parallel, delayed
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from browserstack.local import Local
from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


bs_local = Local()
bs_local_args = {
    "key": "xMtQqxgpztGYscyuXZ8E",
    "v": "true", # Enable verbose logging
    "localIdentifier": "my_local_identifier",
    "port": "45691"
}
bs_local.start(**bs_local_args)

def run_test(browser_name):
    if browser_name == 'Chrome':
        options = ChromeOptions()
    elif browser_name == 'Firefox':
        options = FirefoxOptions()
        # Add Firefox-specific options here
    elif browser_name == 'Edge':
        options = EdgeOptions()
        # Add Edge-specific options here
    elif browser_name == 'Safari':
        options = SafariOptions()
        # Add Safari-specific options here
    elif browser_name == 'ChromeW8':
        options = ChromeOptions()
        options.set_capability("os", "Windows")
        options.set_capability("os_version", "8.1")
        options.set_capability("browser_version", "109.0")

    driver = webdriver.Remote(
        command_executor='https://adilshaikh_yfq8GJ:xMtQqxgpztGYscyuXZ8E@hub.browserstack.com/wd/hub',
        options=options)
    
    
    # Your Selenium code to interact with the Flipkart website goes here
    service = Service('D:\\ChromeDriver\\chromedriver-win64\\chromedriver.exe')

    # Initialize the WebDriver with the specified service
    driver = webdriver.Chrome(service=service)

    #Load Flipkart Home Page
    driver.get("https://www.flipkart.com")
    # driver.fullscreen_window()

    # Search for "Samsung Galaxy S10"
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Samsung Galaxy S10")
    search_box.send_keys(Keys.RETURN)



    # Click on "Mobiles" in Categories
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Mobiles"))).click()


    #Apply Filters
    # Brand: Samsung
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, "//section[@class='_167Mu3 _2hbLCH']//div[@class='_3FPh42']//div[@class='_2d0we9']//div[@title='SAMSUNG']//div[@class='_1Y4Vhm _4FO7b6']//label[@class='_2iDkf8 t0pPfW']//div[@class='_24_Dny']")))
    element.click()


    # Sort by Price -> High to Low
    wait = WebDriverWait(driver, 10) # Wait up to 10 s
    driver.find_element(By.XPATH, "//div[normalize-space()='Price -- High to Low']").click()
    
    # Select Flipkart Assured
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, "//section[@class='_2hbLCH _24gLJx']//label[@class='_2iDkf8 shbqsL']//div[@class='_24_Dny _3tCU7L']")))
    element.click()



    driver.implicitly_wait(5)


    #Read and Print Product Details
    # Wait for search results to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//body/div[@id='container']/div/div[@class='_36fx1h _6t1WkM _3HqJxg']/div[@class='_1YokD2 _2GoDe3']/div[@class='_1YokD2 _3Mn1Gg']/div[@class='_1AtVbE col-12-12']/div[@class='_13oc-S']")))

    # Read and print product details
    products = driver.find_elements(By.XPATH, "//body/div[@id='container']/div/div[@class='_36fx1h _6t1WkM _3HqJxg']/div[@class='_1YokD2 _2GoDe3']/div[@class='_1YokD2 _3Mn1Gg']/div[@class='_1AtVbE col-12-12']/div[@class='_13oc-S']")
    for product in products:
        name = product.find_element(By.CSS_SELECTOR, "._4rR01T").text
        price = product.find_element(By.CSS_SELECTOR, "._30jeq3").text
        link = product.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
        print(f"Product Name: {name}, \nDisplay Price: {price}, \nLink: {link} \n\n\n")
        message = f"Product Name: {name}, Display Price: {price}, Link: {link}"
    
        # Execute JavaScript to print the message in the browser's console
        driver.execute_script(f"console.log('{message}');")

    # Step 8: Close the Browser
    driver.quit() 




# Example usage
browsers = ['Chrome', 'Firefox','Edge', 'Safari' , 'ChromeW8']

# Run tests in parallel
Parallel(n_jobs=-1)(delayed(run_test)(browser) for browser in browsers)

bs_local.stop()





# # List of desired capabilities for different browser/OS combinations
# desired_caps_list = [
#     {
#         'os': 'Windows',
#         'os_version': '10',
#         'browser': 'Chrome',
#         'browser_version': 'latest',
#         'name': 'BStack-[Python] Sample Test'
#     },
#     {
#         'os': 'Windows',
#         'os_version': '10',
#         'browser': 'Firefox',
#         'browser_version': 'latest',
#         'name': 'BStack-[Python] Sample Test'
#     },
#     # Add more combinations as needed
# ]


# # options = Options()
# # options.set_capability("os", "Windows")
# # options.set_capability("os_version", "10")
# # options.set_capability("browser", "Chrome")
# # options.set_capability("browser_version", "latest")
# # options.set_capability("name", "BStack-[Python] Sample Test")

# # driver = webdriver.Remote(
# #     command_executor='https://adilshaikh_yfq8GJ:xMtQqxgpztGYscyuXZ8E@hub.browserstack.com/wd/hub',
# #     options=options)



# # Iterate over the list and run the test for each combination
# for desired_cap in desired_caps_list:
#     driver = webdriver.Remote(
#         command_executor='https://adilshaikh_yfq8GJ:xMtQqxgpztGYscyuXZ8E@hub.browserstack.com/wd/hub',
#         desired_capabilities=desired_cap)
    
#     # Your existing Selenium code to interact with the Flipkart website goes here


# #Initializing WebDriver

# service = Service('D:\\ChromeDriver\\chromedriver-win64\\chromedriver.exe')

# # Initialize the WebDriver with the specified service
# driver = webdriver.Chrome(service=service)

# #Load Flipkart Home Page
# driver.get("https://www.flipkart.com")
# # driver.fullscreen_window()

# # Search for "Samsung Galaxy S10"
# search_box = driver.find_element(By.NAME, "q")
# search_box.send_keys("Samsung Galaxy S10")
# search_box.send_keys(Keys.RETURN)



# # Click on "Mobiles" in Categories
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Mobiles"))).click()


# #Apply Filters
# # Brand: Samsung
# wait = WebDriverWait(driver, 10)
# element = wait.until(EC.element_to_be_clickable((By.XPATH, "//section[@class='_167Mu3 _2hbLCH']//div[@class='_3FPh42']//div[@class='_2d0we9']//div[@title='SAMSUNG']//div[@class='_1Y4Vhm _4FO7b6']//label[@class='_2iDkf8 t0pPfW']//div[@class='_24_Dny']")))
# element.click()


# # Sort by Price -> High to Low
# driver.find_element(By.XPATH, "//div[normalize-space()='Price -- High to Low']").click()
# wait = WebDriverWait(driver, 10) # Wait up to 10 s


# # Select Flipkart Assured
# wait = WebDriverWait(driver, 10)
# element = wait.until(EC.element_to_be_clickable((By.XPATH, "//section[@class='_2hbLCH _24gLJx']//label[@class='_2iDkf8 shbqsL']//div[@class='_24_Dny _3tCU7L']")))
# element.click()


# driver.implicitly_wait(5)


# #Read and Print Product Details
# # Wait for search results to load
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//body/div[@id='container']/div/div[@class='_36fx1h _6t1WkM _3HqJxg']/div[@class='_1YokD2 _2GoDe3']/div[@class='_1YokD2 _3Mn1Gg']/div[@class='_1AtVbE col-12-12']/div[@class='_13oc-S']")))

# # Read and print product details
# products = driver.find_elements(By.XPATH, "//body/div[@id='container']/div/div[@class='_36fx1h _6t1WkM _3HqJxg']/div[@class='_1YokD2 _2GoDe3']/div[@class='_1YokD2 _3Mn1Gg']/div[@class='_1AtVbE col-12-12']/div[@class='_13oc-S']")
# for product in products:
#     name = product.find_element(By.CSS_SELECTOR, "._4rR01T").text
#     price = product.find_element(By.CSS_SELECTOR, "._30jeq3").text
#     link = product.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
#     print(f"Product Name: {name}, \nDisplay Price: {price}, \nLink: {link} \n\n\n")

# # Step 8: Close the Browser
# driver.quit()
