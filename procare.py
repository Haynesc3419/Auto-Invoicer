from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import testprocare

# XPATHS
DatePath = '/html/body/div[3]/section/div[3]/div[2]/div/div/div/div/div/div/form/div[2]/div[1]/div[1]/ul/li[2]/div/input'
poPath = '/html/body/div[3]/section/div[3]/div[2]/div/div/div/div/div/div/form/div[2]/div[1]/div[1]/ul/li[3]/div/input'
PatientPath = '/html/body/div[3]/section/div[3]/div[2]/div/div/div/div/div/div/form/div[2]/div[1]/div[1]/ul/li[4]/div/input'
start_hour_path = '/html/body/div[3]/section/div[3]/div[2]/div/div/div/div/div/div/form/div[2]/div[1]/div[1]/ul/li[9]/div/div/div[1]/input'
start_minute_path = '/html/body/div[3]/section/div[3]/div[2]/div/div/div/div/div/div/form/div[2]/div[1]/div[1]/ul/li[9]/div/div/div[2]/input'
end_hour_path = '/html/body/div[3]/section/div[3]/div[2]/div/div/div/div/div/div/form/div[2]/div[1]/div[1]/ul/li[10]/div/div/div[1]/input'
end_minute_path = '/html/body/div[3]/section/div[3]/div[2]/div/div/div/div/div/div/form/div[2]/div[1]/div[1]/ul/li[10]/div/div/div[2]/input'

Completed_Drop_Down_Path = '/html/body/div[3]/section/div[3]/div[2]/div/div/div/div/div/div/form/div[2]/div[1]/div[1]/ul/li[5]/div/div/div[3]/div/ul/li[2]'
Completed_Button = '/html/body/div[3]/section/div[3]/div[2]/div/div/div/div/div/div/form/div[2]/div[1]/div[1]/ul/li[5]/div/div/div[2]/b'

Start_Drop_Down_Path_PM = '/html/body/div[3]/section/div[3]/div[2]/div/div/div/div/div/div/form/div[2]/div[1]/div[1]/ul/li[9]/div/div/div[3]/div/div[3]/div/ul/li[2]'
Start_Button = '/html/body/div[3]/section/div[3]/div[2]/div/div/div/div/div/div/form/div[2]/div[1]/div[1]/ul/li[9]/div/div/div[3]/div/div[2]/b'

End_Drop_Down_Path_PM = '/html/body/div[3]/section/div[3]/div[2]/div/div/div/div/div/div/form/div[2]/div[1]/div[1]/ul/li[10]/div/div/div[3]/div/div[3]/div/ul/li[2]'
End_Button = '/html/body/div[3]/section/div[3]/div[2]/div/div/div/div/div/div/form/div[2]/div[1]/div[1]/ul/li[10]/div/div/div[3]/div/div[2]/b'

Parking_Path = '/html/body/div[3]/section/div[3]/div[2]/div/div/div/div/div/div/form/div[2]/div[1]/div[1]/ul/li[17]/div[1]/div/div[3]/div/ul/li[2]'
Parking_Button = '/html/body/div[3]/section/div[3]/div[2]/div/div/div/div/div/div/form/div[2]/div[1]/div[1]/ul/li[17]/div[1]/div/div[2]/b'

hours_path = '/html/body/div[3]/section/div[3]/div[2]/div/div/div/div/div/div/form/div[2]/div[1]/div[1]/ul/li[11]/div/input'
hour_rate_path = '/html/body/div[3]/section/div[3]/div[2]/div/div/div/div/div/div/form/div[2]/div[1]/div[1]/ul/li[12]/div/input'
miles_path = '/html/body/div[3]/section/div[3]/div[2]/div/div/div/div/div/div/form/div[2]/div[1]/div[1]/ul/li[13]/div/input'
miles_rate_path = '/html/body/div[3]/section/div[3]/div[2]/div/div/div/div/div/div/form/div[2]/div[1]/div[1]/ul/li[14]/div/input'
other_q_path = '/html/body/div[3]/section/div[3]/div[2]/div/div/div/div/div/div/form/div[2]/div[1]/div[1]/ul/li[15]/div/input'
other_rate_path = '/html/body/div[3]/section/div[3]/div[2]/div/div/div/div/div/div/form/div[2]/div[1]/div[1]/ul/li[16]/div/input'

Next_Page_Path = '/html/body/div[3]/section/div[3]/div[2]/div/div/div/div/div/div/form/div[2]/div[1]/div[2]/input'

providerID_path = '/html/body/div[3]/section/div[3]/div[2]/div/div/div/div/div/div/form/div[2]/div[2]/div[1]/ul/li[2]/div/input'
providerEmail_path = '/html/body/div[3]/section/div[3]/div[2]/div/div/div/div/div/div/form/div[2]/div[2]/div[1]/ul/li[5]/div/input'
additional_comments_path = '/html/body/div[3]/section/div[3]/div[2]/div/div/div/div/div/div/form/div[2]/div[2]/div[1]/ul/li[7]/div/textarea'

Submit_Path = '/html/body/div[3]/section/div[3]/div[2]/div/div/div/div/div/div/form/div[2]/div[2]/div[2]/input[2]'


class Invoice:
    def __init__(self, date, po_number, patient_name,
                 start_time, hours, hour_rate, miles, mile_rate,
                 other_quantity, other_rate, additional_comments):

        self.providerID = '9543' #9543
        self.providerEmail = 'jaklinehaynes@gmail.com'
        self.hours = hours

        start_t = testprocare.get_time_makeup(start_time)
        self.start_hour = start_t[0]
        self.start_minute = start_t[1]
        self.start_AM = start_t[2]

        end_t = testprocare.add_time(start_time, hours)
        self.end_hour = end_t[0]
        self.end_minute = end_t[1]
        self.end_AM = end_t[2]
        self.other_quantity = other_quantity

        self.patient_name = patient_name
        self.po_number = po_number
        self.date = date

        self.attr_list_one = [date, po_number, patient_name, self.start_hour, self.start_minute, self.end_hour, self.end_minute]
        self.path_list_one = [DatePath, poPath, PatientPath, start_hour_path, start_minute_path, end_hour_path, end_minute_path]

        self.attr_list_two = [hours, hour_rate, miles, mile_rate, other_quantity, other_rate]
        self.path_list_two = [hours_path, hour_rate_path, miles_path, miles_rate_path, other_q_path, other_rate_path]

        self.attr_list_three = [self.providerID, self.providerEmail, additional_comments]
        self.path_list_three = [providerID_path, providerEmail_path, additional_comments_path]


    def create_invoice(self, driver):
        print("Invoicing " + self.patient_name + " " + self.po_number + " " + self.date)
        driver.get('https://theprocare.com/interpreter-invoice-form/')

        WebDriverWait(driver, 2);
        Completed_Drop_Down_Button = driver.find_element(By.XPATH, Completed_Button)
        Completed_Drop_Down_Button.click()
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, Completed_Drop_Down_Path))).click()
        driver.execute_script("window.scrollTo(0, 400)")

        # Click Start AM_PM Drop Down Button and Click PM if it is PM
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, Start_Button))).click()
        if self.start_AM == "PM":
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Start_Drop_Down_Path_PM))).click()

        # Click End AM_PM Drop Down Button and Click PM if it is PM
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, End_Button))).click()
        if self.end_AM == "PM":
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, End_Drop_Down_Path_PM))).click()

        # Other Description Box
        if int(self.other_quantity) > 0:
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, Parking_Button))).click()
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Parking_Path))).click()

        # Goes through attributes and pastes them to their Xpaths
        for index in range(0,len(self.path_list_one)):
            path = self.path_list_one[index]
            attr = self.attr_list_one[index]
            form_element = driver.find_element(By.XPATH, path)
            form_element.send_keys(attr)

        for index in range(0,len(self.path_list_two)):
            path = self.path_list_two[index]
            attr = self.attr_list_two[index]
            form_element = driver.find_element(By.XPATH, path)
            form_element.send_keys(attr)

        # Click Next Page Button
        driver.execute_script("window.scrollTo(0, 450)")
        driver.execute_script('jQuery("#gform_target_page_number_4").val("2"); jQuery("#gform_4").trigger("submit",[true]);')

        # Second Page info
        for index in range(0, len(self.path_list_three)):
            path = self.path_list_three[index]
            attr = self.attr_list_three[index]
            form_element = driver.find_element(By.XPATH, path)
            form_element.send_keys(attr)

        # Click Submit Button
        driver.execute_script("window.scrollBy(0, 600)")
        driver.execute_script("""jQuery("#gform_4").trigger("submit",[true]);""")
        print("Invoice Completed")

