import os
import csv
import settings
import standard_functions

# Used in case of export
output_file = []


# Navigates to the proper pages where changes are to be made / information is to be read, then kicks off the Import /
# Export function

def navigate():
    input_file = csv.DictReader(open(os.path.join(os.environ["HOMEPATH"], "Desktop",settings.file)))

    for row in input_file:
        expense_type = str(row["expense_type"])
        project_type = str(row["project_type"])
        expense_type_key = str(row["expense_type_key"])
        project_type_key = str(row["project_type_key"])
        account = str(row["account"])

        # Navigates to the URL for the given Expense Type, then clicks the edit pencil for the given Project Type

        webPage = settings.URL + "/admin/setup/expense/expense_types/cost_account/list?expensetypekey=" + expense_type_key
        settings.driver.get(webPage)
        xpathId = '//*[@id="k_' + project_type_key + '"]/td[1]/img'
        settings.driver.find_element_by_xpath(xpathId).click()

        # Determines whether or not information is being imported or exported

        # If importing, proceed to import function
        if settings.direction == "Import":

            standard_functions.fileImport(account)

        # If exporting, create a dictionary containing the values from Unanet
        elif settings.direction == "Export":

            account = str(settings.driver.find_element_by_xpath('//*[@id="ac-input"]').get_attribute("value"))

            output_file_row = {"expense_type": expense_type, "expense_type_key": expense_type_key,
                               "project_type": project_type, "project_type_key": project_type_key, "account": account}
            output_file.append(output_file_row)

        row["account"] = account
        print(row)

    # If exporting, send dictionary to export function when it is finished being created.
    if settings.direction == "Export":
        standard_functions.fileExport(output_file)
