import csv
import settings
import standard_functions


# Navigates to the proper pages where changes are to be made / information is to be read.

def navigate():

    input_file = csv.DictReader(open(settings.file))

    for row in input_file:
        expense_type_key = str(row["expense_type_key"])
        project_type_key = str(row["project_type_key"])
        account = str(row["account"])

        webPage = settings.URL + "/admin/setup/expense/expense_types/cost_account/list?expensetypekey=" + expense_type_key
        settings.driver.get(webPage)
        xpathId = '//*[@id="k_' + project_type_key + '"]/td[1]/img'
        settings.driver.find_element_by_xpath(xpathId).click()
        if settings.direction == "import":
            standard_functions.fileImport(account)
        elif settings.direction == "export":
            standard_functions.fileExport(account)
