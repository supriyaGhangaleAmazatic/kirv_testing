from selenium.webdriver.common.by import By


class AddProduct(object):

        products_link = (By.XPATH, '//a[@class ="add-product"]')
        product_search_bar = (By.XPATH, '//input[@placeholder="Enter Product Name"]')
        product_type = (By.XPATH, '//input[@placeholder="Enter Product Type"]/ul/li[1]')
        sku_number = (By.XPATH, "//input[@placeholder='Enter SKU Number']")
        warranty = (By.XPATH, "//input[@placeholder='Enter Warranty']")
        brand = (By.XPATH, "//input[@placeholder='Enter Brand']/ul/li[3]")
        sub_category = (By.XPATH, "//input[@placeholder='Enter Category']/ul/li[3]")
        color = (By.XPATH, "//input[@placeholder='Enter Color']/ul/li[3]")
        model_number = (By.XPATH, "//input[@placeholder='Enter Model Number']")
        dim_uom = (By.XPATH, "//label[contains(text(),'Product Dim. UOM')]/../field/div/label/div/input/ul/li")
        product_length = (By.XPATH, "//input[@placeholder='Enter Length']")

        product_width = (By.XPATH, "//div[@class='row no-gutters-5']//div[3]//field[1]//div[1]//label[1]//input[1]")
        weight_uom = (By.XPATH, "//label[contains(text(),'Product Weight UOM')]/../field/div/label/div/input")
        product_weight = (By.XPATH, "//div[@class='row no-gutters-5']//input[@placeholder='Enter Weight']")
        description = (By.XPATH, "cke_editable cke_editable_themed cke_contents_ltr cke_show_borders")
        product_img = (By.XPATH, "//div[@id='myDrop']")
        msrp = (By.XPATH, "//input[@placeholder='Enter MSRP']")
        wholesale_price = (By.XPATH, "//input[@placeholder='Enter Wholesale Price']")
        retail_price = (By.XPATH, "//input[@placeholder='Enter Retail Price']")
        grade_New = (By.XPATH, "//label[contains(text(),'New')]")
        grade_premium = (By.XPATH, "//label[contains(text(),'Premium')]")

        grade_Refurbished = (By.XPATH, "//label[contains(text(),'Refurbished')]")
        grade_Scratch = (By.XPATH, "//label[contains(text(),'Scratch & Dent')]")
        grade_Liquidation = (By.XPATH, "//label[contains(text(),'Liquidation')]")
        new_Cost = (By.XPATH, "//div[@class='row mb-4']//div[2]//fieldset[1]//div[1]//div[1]//field[1]//div[1]//label[1]//input[1]")
        new_SellingPrice = (By.XPATH, "//div[@class='row mb-4']//div[2]//fieldset[1]//div[1]//div[2]//field[1]//div[1]//label[1]//input[1]")
        premium_Cost = (By.XPATH, "//div[@class='row mb-4']//div[3]//fieldset[1]//div[1]//div[1]//field[1]//div[1]//label[1]//input[1]")
        premium_SellingPrice = (By.XPATH, "//div[@class='row mb-4']//div[3]//fieldset[1]//div[1]//div[2]//field[1]//div[1]//label[1]//input[1]")
        refurbished_Cost = (By.XPATH, "//div[@class='row mb-4']//div[4]//fieldset[1]//div[1]//div[1]//field[1]//div[1]//label[1]//input[1]")
        refurbished_SellingPrice = (By.XPATH, "//div[@class='row mb-4']//div[4]//fieldset[1]//div[1]//div[2]//field[1]//div[1]//label[1]//input[1]")

        scratchDent_Cost = (By.XPATH, "//div[@class='row mb-4']//div[5]//fieldset[1]//div[1]//div[1]//field[1]//div[1]//label[1]//input[1]")
        scratchDent_SellingPrice = (By.XPATH, "//div[@class='row mb-4']//div[5]//fieldset[1]//div[1]//div[2]//field[1]//div[1]//label[1]//input[1]")
        liquidation_Cost = (By.XPATH, "//div[@class='row mb-4']//div[6]//fieldset[1]//div[1]//div[1]//field[1]//div[1]//label[1]//input[1]")
        liquidation_SellingPrice = (By.XPATH, "//div[@class='row mb-4']//div[6]//fieldset[1]//div[1]//div[2]//field[1]//div[1]//label[1]//input[1]")
        add_Competitor = (By.XPATH, "//button[contains(text(),'Add Competitor')]")
        add_Property = (By.XPATH, "//button[contains(text(),'Add Property')]")  
        shipping_dim_uom_dd = (By.XPATH, "//div[@class='row no-gutters-5 mt-4']//div[1]//field[1]//div[1]//label[1]//div[1]//input[1]")
        shipping_Length = (By.XPATH, "//div[@class='row no-gutters-5 mt-4']//input[contains(@placeholder,'Enter Length')]")
        shipping_width = (By.XPATH, "//div[@class='row no-gutters-5 mt-4']//input[@placeholder='Enter Width']")
        shipping_Height = (By.XPATH, "//input[@placeholder='Enter Height']")
        shipping_Weight_uom_dd = (By.XPATH, "//div[@class='row no-gutters-5 mt-4']//div[5]//field[1]//div[1]//label[1]//div[1]//input[1]")
        shipping_Weight = (By.XPATH, "//div[@class='row no-gutters-5 mt-4']//input[@placeholder='Enter Weight']")
