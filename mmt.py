#imports
import time
from selenium import webdriver

#details
from1="delhi"
to="mumbai"
departure_month_and_year="October2019"  # enter the month and year in this format
departure_date="10" #enter date
return_month_and_year="October2019" #enter the month and year in this format
return_date="14"    #enter return date
date=departure_date+" "+ departure_month_and_year[:-4] + " "+departure_month_and_year[-4:]
date1=return_date+" "+ return_month_and_year[:-4]+" "+return_month_and_year[-4:]

#to open chrome
driver= webdriver.Chrome(r"C:\Users\vamsi\Desktop\automation\chromedriver.exe")
driver.set_page_load_timeout(60)

#website
driver.get("https://www.makemytrip.com/flights/")

#to maximize
driver.maximize_window()

#trip selector
round_trip=driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div[1]/ul/li[2]")
round_trip.click()

#from city
from_city=driver.find_element_by_id("fromCity")
from_city.send_keys(from1)

#to city
to_city=driver.find_element_by_id("toCity")
to_city.send_keys(to)
time.sleep(1.5)
first_item=driver.find_element_by_xpath('//*[@id="react-autowhatever-1-section-0-item-0"]')
first_item.click()


#datepicker
date_picker=driver.find_element_by_xpath("//span[text()='DEPARTURE']")
date_picker.click()

#departure date
for i in range(12):
    x = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[1]/div')
    if x.text!=departure_month_and_year:
        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[1]/span[2]').click()
    else:
        break
x=driver.find_elements_by_xpath('//*[@class="dateInnerCell"]')
for i in x:
    if i.text==departure_date:
        z=x.index(i)+1
        break
r=z/7
if r>z//7:
    r=int(r)+1
else:
    int(r)
c=z%7

x='//*[@id="root"]/div/div[2]/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[3]/div[1]/div[4]/div'
y=x[:-13]+str(r)+x[-12:-6]+str(c)+x[-5:]
departure_date = driver.find_element_by_xpath(y).click()

#return date
for i in range(12):
    x = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[1]/div')
    if x.text!=return_month_and_year:
        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[1]/span[2]').click()
    else:
        break
x=driver.find_elements_by_xpath('//*[@class="dateInnerCell"]')
for i in x:
    if i.text==return_date:
        z=x.index(i)+1
        break
r=z/7
if r>z//7:
    r=int(r)+1
else:
    int(r)
c=z%7
x='//*[@id="root"]/div/div[2]/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[3]/div[1]/div[4]/div'
y=x[:-13]+str(r)+x[-12:-6]+str(c)+x[-5:]
return_date = driver.find_element_by_xpath(y).click()

#search button
search=driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[2]/p/a')
search.click()

#wait time for loading the page
time.sleep(5)

#departure times
times=driver.find_elements_by_xpath('//*[@class="dept-time"]')

#return times
times1=driver.find_elements_by_xpath('//*[@class="reaching-time append_bottom3"]')

#prices
prices=driver.find_elements_by_xpath('//*[@class="actual-price"]')

#durations
durations=driver.find_elements_by_xpath('//*[@class="fli-duration"]')

#airlines
airlines=driver.find_elements_by_xpath('//*[@class="airlineInfo-sctn"]')

#processing data
departure_times=[times[i].text for i in range(len(times)//2)]
arrival_times=[times1[i].text for i in range(len(times1)//2)]

return_departure_times=[times[i].text for i in range(len(times)//2,len(times))]
return_arrival_times=[times1[i].text for i in range(len(times1)//2,len(times1))]

for i in range(2):
    prices.pop()
    airlines.pop()

price=[prices[i].text for i in range(len(prices)//2)]
return_price=[prices[i].text for i in range(len(prices)//2,len(prices))]

departure_duration=[durations[i].text for i in range(len(durations)//2)]
return_duration=[durations[i].text for i in range(len(durations)//2,len(durations))]

departure_airlines=[airlines[i].text for i in range(len(airlines)//2)]
return_airlines=[airlines[i].text for i in range(len(airlines)//2,len(airlines))]

cheap=["".join(i[2:].split(",")) for i in price]
cheap1=["".join(i[2:].split(",")) for i in return_price]

min,min1,a,b=100000,100000,[],[]

for i in range(len(cheap)):
    if int(cheap[i])<=min:
        min=int(cheap[i])
        a.append(i)
    if int(cheap1[i])<=min1:
        min1=int(cheap1[i])
        b.append(i)

#printing data
print(len(departure_airlines),len(return_airlines),len(departure_duration),len(return_duration))
for i in a:
    print("the cheapest flight from " + from1 + " to " + to +" on " + date +" is:",end=" ")
    print(departure_airlines[i],departure_times[i],departure_duration[i],arrival_times[i],price[i],sep=" ")
print("-------------------------------------------------------------------------------------------------------------------------------")
for i in b:
    print("the cheapest flight from "+ to+ " to "+ from1 +" on " + date1 + " is:",end=" ")
    print(return_airlines[i],return_departure_times[i],return_duration[i],return_arrival_times[i],return_price[i],sep=" ")

time.sleep(20)
driver.quit()
