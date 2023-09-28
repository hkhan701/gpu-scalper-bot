
# importing all the libraries needed to enable accessing data from the html of a website
import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# importing a UserAgent in order to control the browser
from fake_useragent import UserAgent

# import time in order to add a small delay to prevent getting IP banned
import time

# importing libraries for the email to work
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart




# creates a user agent which allows selenium to control the web browser
ua = UserAgent()
opts = Options()
opts.add_argument("user-agent=" + ua.random)
driver = webdriver.Chrome(options=opts)

# loops this code forever
while True:
    # test link 1: https://www.memoryexpress.com/Category/Processors?FilterID=114c11d7-083a-0eed-060b-837a6600f02b&Search=ryzen
    # test link 2: https://www.memoryexpress.com/Category/VideoCards?FilterID=f1b0a6e4-f41e-5fea-c242-d1bac7b02bf2&Search=rtx
    # gets the webpage link, opens it and allows bs4 to parse through the html of the page using html.parser
    driver.get("https://www.memoryexpress.com/Category/Processors?FilterID=114c11d7-083a-0eed-060b-837a6600f02b&Search=ryzen")
    html = driver.page_source
    soup = bs4.BeautifulSoup(html, "html.parser")

    # initialize a list to store href link of items in stock
    in_stock = []

    # makes a list of all the items in the store with the class "c-shca-add-product-button c-shca-icon-item__summary-buy"
    items_in_store = soup.find_all("a", {"class":"c-shca-add-product-button c-shca-icon-item__summary-buy"})

    # using a for loop to go through all the items in the store on that specific page
    for i in items_in_store:
        if "Buy" in i['title']:
            # for every item in the store that is in stock (by checking if string "Buy" exists in the title)
            # and adds the href link to to the in_stock list
            # this link is conveniently also the one which automatically adds it to the cart from the main page
            in_stock.append(i['href'])

    # https://www.youtube.com/watch?v=YPiHBtddefI
    # declare and initialize the variables for sending an email.
    email = 'xxxxxxxx@gmail.com' 
    password = 'test123'
    send_to_email = 'xxxxxxxx@gmail.com'
    subject = 'FOUND NEW GPU!'
    message = ''

    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = send_to_email
    msg['Subject'] = subject



    urlCheck = ""
    # since the href link does not have the main url, we attach it to the front and print it to the console
    base_url = "https://www.memoryexpress.com/"
    print("GPUs in stock")
    for url in in_stock:
        url = base_url + url
        urlCheck = url
        # Concatenate the message with all the urls
        message = message + url + "\n"
        print(url)


    if "Checkout" in urlCheck:
        break
    # adds 8 second delay until it refreshes page
    time.sleep(8)
    # exits the code once there is items in your cart


# https://www.youtube.com/watch?v=YPiHBtddefI
# Attach the message to the MIMEMultipart object
msg.attach(MIMEText(message, 'plain'))
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)
text = msg.as_string()  # You now need to convert the MIMEMultipart object to a string to send
server.sendmail(email, send_to_email, text)
server.quit()

