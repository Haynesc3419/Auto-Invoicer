import pandas as pd
import procare

from selenium import webdriver

dataframe = pd.read_excel(r"C:\Users\Hayne\Desktop\Invoices\Procare\InvoiceAutomation\procare_sheet.xlsx")
completedInvoices = []


def invoice():
    first = True
    invoices = []
    count = 0
    for index, row in dataframe.iterrows():

        if row[0] == 'nan':
            break;

        date = str(row[0])
        po = str(row[1])
        name = str(row[2])
        start = str(row[3])
        hours = str(row[4])
        h_rate = str(row[5])
        miles = str(row[6])
        m_rate = str(row[7])
        other_q = str(row[8])
        other_r = str(row[9])
        comments = str(row[10])

        if comments == 'nan':
            comments = ''

        row_list = [date, po, name, start, hours, h_rate, miles, m_rate, other_q, other_r, comments]
        print("Building invoice for: " + str(row_list))
        newInv = procare.Invoice(date, po, name, start, hours, h_rate, miles, m_rate, other_q, other_r, comments)
        invoices.append(newInv)

    print(str(len(invoices)) + " invoices created")
    driver = webdriver.Chrome()
    for inv in invoices:
        count += 1
        inv.create_invoice(driver)

    if count == len(invoices):
        print("Invoiced total of " + str(count) + " appointments")

    driver.quit()



invoice()
