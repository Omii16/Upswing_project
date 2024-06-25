from selenium.webdriver.common.by import By


class Paths:

    def __init__(self, driver):
        self.driver= driver

    # Signup_process
    signup_btn = (By.XPATH, "//a[text()='Sign up']")
    signup_user = (By.XPATH, "//input[@id='sign-username']")
    signup_pass = (By.XPATH, "//input[@id='sign-password']")
    signup_click = (By.XPATH, "//button[@onclick='register()']")

    # Login
    login_btn = (By.XPATH, "//a[text()='Log in']")
    login_user = (By.XPATH, "//input[@id='loginusername']")
    login_pass = (By.XPATH, "//input[@id='loginpassword']")
    login_click = (By.XPATH, "//button[@onclick='logIn()']")

    # HomePage
    home_page = (By.XPATH, "//div[@id='navbarExample']/ul/li[7]")
    home_page_btn = (By.XPATH, "//div[@id='navbarExample']/ul/li[1]")
    home_page_cart = (By.XPATH, "//div[@id='navbarExample']/ul/li[4]")

    # Product browsing
    product_phone = (By.XPATH, "//div[@class='list-group']/a[2]")
    phone_list = (By.XPATH, "//a[@class='hrefch']")
    product_samsung_phone = (By.XPATH, "//a[normalize-space()='Samsung galaxy s6']")
    product_nextpage = (By.XPATH,"//h2[normalize-space()='Samsung galaxy s6']")

    # Shopping cart
    shopping_select_product = (By.XPATH, "//a[normalize-space()='MacBook Pro']")
    add_Product = (By.XPATH, "//a[normalize-space()='Add to cart']")
    check_product = (By.XPATH, "//td[normalize-space()='MacBook Pro']")


    def signup_button(self):
        return self.driver.find_element(*Paths.signup_btn)

    def signup_username(self):
        return self.driver.find_element(*Paths.signup_user)

    def signup_password(self):
        return self.driver.find_element(*Paths.signup_pass)

    def signup_click_btn(self):
        return self.driver.find_element(*Paths.signup_click)

    def login_button(self):
        return self.driver.find_element(*Paths.login_btn)

    def login_username(self):
        return self.driver.find_element(*Paths.login_user)

    def login_password(self):
        return self.driver.find_element(*Paths.login_pass)

    def login_click_btn(self):
        return self.driver.find_element(*Paths.login_click)

    def home_page_text(self):
        return self.driver.find_element(*Paths.home_page)

    def home_page_button(self):
        return self.driver.find_element(*Paths.home_page_btn)

    def product_phone_btn(self):
        return self.driver.find_element(*Paths.product_phone)

    def product_phone_list(self):
        return self.driver.find_element(*Paths.phone_list)

    def product_select_phone(self):
        return self.driver.find_element(*Paths.product_samsung_phone)

    def product_display_nextpage(self):
        return self.driver.find_element(*Paths.product_nextpage)

    def shopping_cart_product(self):
        return self.driver.find_element(*Paths.shopping_select_product)

    def add_to_cart_product(self):
        return self.driver.find_element(*Paths.add_Product)

    def home_page_cart_button(self):
        return self.driver.find_element(*Paths.home_page_cart)

    def check_cart_product(self):
        return self.driver.find_element(*Paths.check_product)


