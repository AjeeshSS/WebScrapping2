import requests
from bs4 import BeautifulSoup

website_url = 'https://infopark.in/companies/jobs'

ouput_file = open('jobs.txt', 'w')

# Disable SSL verification
res = requests.get(website_url, verify=False)

# soup object
soup = BeautifulSoup(res.text,'lxml')
jobs = soup.find_all("div",{'class':"row company-list joblist"})

print(jobs)


for job in jobs:
    title_element = job.find('a')
    title = title_element.text
    link = title_element['href']
    
    company_name  = job.find('div',{'class':'jobs-comp-name'}).text
    last_date  = job.find('div',{'class':'job-date'}).text
    
    ouput_file.write(title + '\n' + company_name + '\n' + last_date + '\n' + link + '\n\n\n')

    # print(title, company_name, last_date)

    
