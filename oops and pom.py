import time
from selenium import webdriver

class home_page():

    def __init__(self,from1,to,departure_month_and_year,departure_date,return_month_and_year,return_date):
        self.from1=from1
        self.to=to
        self.date1_month_year=departure_month_and_year
        self.date1=departure_date
        self.date2_month_year=return_month_and_year
        self.date2=return_date
        self.driver=webdriver.Chrome(r"C:\Users\vamsi\Desktop\automation\chromedriver.exe")
        self.date3 = self.date1 + " " + self.date1_month_year[:-4] + " " + self.date1_month_year[-4:]
        self.date4 = self.date2 + " " + self.date2_month_year[:-4] + " " + self.date2_month_year[-4:]

    def website(self):
        self.driver.get("https://www.makemytrip.com/flights/")
        self.driver.set_page_load_timeout(60)

    def maximize(self):
        self.driver.maximize_window()

    def trip_selector(self):
        round_trip = self.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div[1]/ul/li[2]")
        round_trip.click()

    def from_city(self):
        from_city = self.driver.find_element_by_id("fromCity")
        from_city.send_keys(self.from1)

    def to_city(self):
        to_city = self.driver.find_element_by_id("toCity")
        to_city.send_keys(self.to)
        time.sleep(1.5)
        first_item = self.driver.find_element_by_xpath('//*[@id="react-autowhatever-1-section-0-item-0"]')
        first_item.click()

    def date_picker(self):
        date_picker = self.driver.find_element_by_xpath("//span[text()='DEPARTURE']")
        date_picker.click()

    def departure_datepicker(self):
        for i in range(12):
            x = self.driver.find_element_by_xpath(
                '//*[@id="root"]/div/div[2]/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[1]/div')
            if x.text != self.date1_month_year:
                self.driver.find_element_by_xpath(
                    '//*[@id="root"]/div/div[2]/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[1]/span[2]').click()
            else:
                break
        x = self.driver.find_elements_by_xpath('//*[@class="dateInnerCell"]')
        for i in x:
            if i.text == self.date1:
                z = x.index(i) + 1
                break
        r = z / 7
        if r > z // 7:
            r = int(r) + 1
        else:
            int(r)
        c = z % 7

        x = '//*[@id="root"]/div/div[2]/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[3]/div[1]/div[4]/div'
        y = x[:-13] + str(r) + x[-12:-6] + str(c) + x[-5:]
        self.driver.find_element_by_xpath(y).click()

    def return_datepicker(self):
        for i in range(12):
            x = self.driver.find_element_by_xpath(
                '//*[@id="root"]/div/div[2]/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[1]/div')
            if x.text != self.date2_month_year:
                self.driver.find_element_by_xpath(
                    '//*[@id="root"]/div/div[2]/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[1]/span[2]').click()
            else:
                break
        x = self.driver.find_elements_by_xpath('//*[@class="dateInnerCell"]')
        for i in x:
            if i.text == self.date2:
                z = x.index(i) + 1
                break
        r = z / 7
        if r > z // 7:
            r = int(r) + 1
        else:
            int(r)
        c = z % 7
        x = '//*[@id="root"]/div/div[2]/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[3]/div[1]/div[4]/div'
        y = x[:-13] + str(r) + x[-12:-6] + str(c) + x[-5:]
        self.driver.find_element_by_xpath(y).click()

    def search(self):
        search = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[2]/p/a')
        search.click()

class results_page(home_page):
    def wait_time(self):
        time.sleep(5)

    def departure_times1(self):
        self.times = self.driver.find_elements_by_xpath('//*[@class="dept-time"]')

    def return_times(self):
        self.times1 = self.driver.find_elements_by_xpath('//*[@class="reaching-time append_bottom3"]')

    def prices(self):
        self.prices = self.driver.find_elements_by_xpath('//*[@class="actual-price"]')

    def durations(self):
        self.durations = self.driver.find_elements_by_xpath('//*[@class="fli-duration"]')

    def airlines(self):
        self.airlines = self.driver.find_elements_by_xpath('//*[@class="airlineInfo-sctn"]')

    def wait1(self):
        time.sleep(5)

class data_processing(results_page):
    def data(self):
        self.departure_times = [self.times[i].text for i in range(len(self.times) // 2)]
        self.arrival_times = [self.times1[i].text for i in range(len(self.times1) // 2)]

        self.return_departure_times = [self.times[i].text for i in range(len(self.times) // 2, len(self.times))]
        self.return_arrival_times = [self.times1[i].text for i in range(len(self.times1) // 2, len(self.times1))]

        for i in range(2):
            self.prices.pop()
            self.airlines.pop()

        self.price = [self.prices[i].text for i in range(len(self.prices) // 2)]
        self.return_price = [self.prices[i].text for i in range(len(self.prices) // 2, len(self.prices))]

        self.departure_duration = [self.durations[i].text for i in range(len(self.durations) // 2)]
        self.return_duration = [self.durations[i].text for i in range(len(self.durations) // 2, len(self.durations))]

        self.departure_airlines = [self.airlines[i].text for i in range(len(self.airlines) // 2)]
        self.return_airlines = [self.airlines[i].text for i in range(len(self.airlines) // 2, len(self.airlines))]

        self.cheap = ["".join(i[2:].split(",")) for i in self.price]
        self.cheap1 = ["".join(i[2:].split(",")) for i in self.return_price]

        self.min, self.min1, self.a, self.b = 100000, 100000, [], []

        for i in range(len(self.cheap)):
            if int(self.cheap[i]) <= self.min:
                self.min = int(self.cheap[i])
                self.a.append(i)
            if int(self.cheap1[i]) <= self.min1:
                self.min1 = int(self.cheap1[i])
                self.b.append(i)

    def printer(self):

        for i in self.a:
            print("the cheapest flight from " + self.from1 + " to " + self.to + " on " + self.date3 + " is:", end=" ")
            print(self.departure_airlines[i], self.departure_times[i], self.departure_duration[i], self.arrival_times[i], self.price[i], sep=" ")
        print(
            "-------------------------------------------------------------------------------------------------------------------------------")
        for i in self.b:
            print("the cheapest flight from " + self.to + " to " + self.from1 + " on " + self.date4 + " is:", end=" ")
            print(self.return_airlines[i], self.return_departure_times[i], self.return_duration[i], self.return_arrival_times[i],
              self.return_price[i], sep=" ")

    def sleep_time(self):
        time.sleep(20)

    def driver_quit(self):
        self.driver.quit()

a=data_processing("delhi","mumbai","October2019","10","October2019","14")
a.website()
a.maximize()
a.trip_selector()
a.from_city()
a.to_city()
a.date_picker()
a.departure_datepicker()
a.return_datepicker()
a.search()
a.wait_time()
a.departure_times1()
a.return_times()
a.durations()
a.prices()
a.airlines()
a.wait1()
a.data()
a.printer()
a.sleep_time()
a.driver_quit()