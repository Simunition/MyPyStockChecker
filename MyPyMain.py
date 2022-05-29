from StockChecker import StockChecker
from SendNotifications import SendNotifications
import time

class MyPyMain():
    
    ##Distro List
    distroList = [""] # list of emails/phone numbers to notify
    
    ##create items
    itemOne = "ASUS ROG STRIX Radeon RX 6800 XT"
    websitesOne = ["newegg"]
    URLsOne = ["https://www.newegg.com/asus-radeon-rx-6800-xt-rog-strix-lc-rx6800xt-o16g-gaming/p/N82E16814126475?Description=radeon%206800&cm_re=radeon_6800-_-14-126-475-_-Product"]
    
    itemTwo = "ASUS ROG STRIX Radeon RX 6800"
    websitesTwo = ["newegg"]
    URLsTwo = ["https://www.newegg.com/asus-radeon-rx-6800-rog-strix-rx6800-o16g-gaming/p/N82E16814126477?Description=radeon%206800&cm_re=radeon_6800-_-14-126-477-_-Product&quicklink=true"]
    
    itemThree = "ASUS ROG Strix NVIDIA GeForce RTX 3080 OC"
    websitesThree = ["newegg", "bestbuy", "amazon"]
    URLsThree = ["https://www.newegg.com/asus-geforce-rtx-3080-rog-strix-rtx3080-o10g-gaming/p/N82E16814126457?Description=asus%20rog%20strix%203080&cm_re=asus_rog%20strix%203080-_-14-126-457-_-Product&quicklink=true",
                 "https://www.bestbuy.com/site/asus-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-strix-graphics-card-black/6432445.p?skuId=6432445",
                 "https://www.amazon.com/ASUS-Graphics-DisplayPort-Axial-tech-2-9-Slot/dp/B08J6F174Z?ref_=ast_sto_dp"]
    
    itemFour = "ASUS ROG Strix GeForce RTX 3070"
    websitesFour = ["newegg", "bestbuy", "amazon"]
    URLsFour = ["https://www.newegg.com/asus-geforce-rtx-3070-rog-strix-rtx3070-o8g-gaming/p/N82E16814126458?Description=rog%20strix%203070&cm_re=rog_strix%203070-_-14-126-458-_-Product",
                "https://www.bestbuy.com/site/asus-rog-strix-rtx3070-8gb-gddr6-pci-express-4-0-graphics-card-black/6439127.p?skuId=6439127",
                "https://www.amazon.com/NVIDIA-Graphics-DisplayPort-Dual-BIOS-Axial-tech/dp/B08N9VTCWG/ref=sr_1_2?dchild=1&keywords=rog+strix+3070&qid=1608146832&sr=8-2#customerReviews"]
    
#     itemFive = "5"
#     websitesFive = ["does", "", ""]
#     URLsFive = ["",
#                 "it",
#                 ""]
#     
#     itemSix = "6"
#     websitesSix = ["", "", "get"]
#     URLsSix = ["",
#                "",
#                "here"]
    
    items = [itemOne, itemTwo, itemThree, itemFour]
    websites = [websitesOne, websitesTwo, websitesThree, websitesFour]
    URLs = [URLsOne, URLsTwo, URLsThree, URLsFour]
    StockObjects = []
    tic = 0
    toc = 0
    
    
    for item, website, URL in zip (items, websites, URLs):
        for site, link in zip(website, URL):
            StockObjects.append(StockChecker(item, site, link))
            
    count = 0
            
    while True:    
        print("Checking {} Items...".format(len(StockObjects)))
        
        for item in StockObjects:
            itemBool = item.stockCheck()
            print("{} in stock on {}: {}".format(item.getItem(), item.getWebsite().title(), itemBool))
            if itemBool:
                message = item.toMessage()
                notification = SendNotifications(distroList, message)
                notification.send()
                
        count += 1
        print("Check Count: {}".format(count))
        
        tic = time.perf_counter()
        lap = tic - toc
        toc = tic
        print("Time Elapsed: {}".format(time.strftime("%Hh %Mm %Ss", time.gmtime(tic))))
        print("Time this Lap: {}".format(time.strftime("%Hh %Mm %Ss", time.gmtime(lap))))
        print("\n\n")
