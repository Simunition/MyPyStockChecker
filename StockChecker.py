from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class StockChecker():
    
    def __init__(self, item, website, url):
        self.item = item
        self.website = website
        self.url = url

    def stockCheck(self):
        ##Checks the stock and returns boolean 
        
        #Set driver options to hidden
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        
        #Open driver
        driver = webdriver.Chrome('chromedriver.exe', options=options)
        #driver = webdriver.PhantomJS('phantomjs.exe')
        
        #Get the webpage
        driver.get(self.url)
        #driver.minimize_window() #optional
        
        try:
            #parse webpage
            soup=BeautifulSoup(driver.page_source,'html.parser')
            #close driver
            driver.close()
            
            if self.website.lower()=="newegg":
                link = soup.find("div",{"class":"product-inventory"})
                stockCheckString = ""
                for i in link:
                    stockCheckString += i.text
                isItStocked = ("In stock" in stockCheckString)
                
            elif self.website.lower()=="bestbuy":
                link = soup.find("div",{"class":"fulfillment-add-to-cart-button"})
                stockCheckString = ""
                for i in link:
                    stockCheckString += i.text
                isItStocked = ("Sold Out" not in stockCheckString)
            
            elif self.website.lower()=="amazon":
                link = soup.find("div",{"id":"buybox"})
                testFor = "In Stock"
                stockCheckString =""
                for i in link:
                    stockCheckString += str(i)
                isItStocked = ("In Stock" in stockCheckString)
          
            return isItStocked
            
        except: 
            return "Error"

    
    def toMessage(self):
        
        return """\
        Subject:{item} In Stock!
        The {item} is in stock on {website}
        {url}""".format(item = self.item, website = self.website, url = self.url)
    
    def getItem(self):
        return self.item
    
    def getWebsite(self):
        return self.website
        


#newegg testers
#in stock
#a = StockChecker(item = "AIO Cooler", website = "newegg", url = "https://www.newegg.com/enermax-liqtech-ii-360-liquid-cooling-system/p/N82E16835214093?Item=N82E16835214093&quicklink=true")
#out of stock
#a = StockChecker(item = "Radeon",website = "newegg",url = "https://www.newegg.com/asus-radeon-rx-6800-xt-rog-strix-lc-rx6800xt-o16g-gaming/p/N82E16814126475")
#print(a.stockCheck())
#print(a.toMessage())
        
        
#bestbuy testers
#in stock
#b = StockChecker(item = "Playstation 5 Controller", website = "bestbuy", url = "https://www.bestbuy.com/site/sony-playstation-5-dualsense-wireless-controller/6430163.p?skuId=6430163")
#out of stock
#b = StockChecker(item = "Asus RTX 3080", website = "bestbuy", url = "https://www.bestbuy.com/site/asus-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-strix-graphics-card-black/6432445.p?skuId=6432445")
#print(b.stockCheck())
#print(b.toMessage())

#amazon tester
#instock
#c = StockChecker(item = "Spice Rack", website = "amazon", url = "https://www.amazon.com/Kamenstein-30020-Revolving-Countertop-Refills/dp/B00008WQ3L/?_encoding=UTF8&pd_rd_w=T3nMQ&pf_rd_p=58f68c27-9bf4-466f-b1c8-101a062bcc82&pf_rd_r=PT73H2YNT4XM7MV2TJKN&pd_rd_r=858bd3de-f316-4f5c-a97a-268e255abcee&pd_rd_wg=DSSbA&ref_=pd_gw_wish")
#out of stock
#c = StockChecker(item = "ASUS RTX 3080", website = "amazon", url = "https://www.amazon.com/ASUS-Graphics-DisplayPort-Axial-tech-2-9-Slot/dp/B08J6F174Z?ref_=ast_sto_dp")
#print(c.stockCheck())
#print(c.toMessage())
        
        
        
        
        
        
        
        