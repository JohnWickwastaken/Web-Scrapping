from bs4 import BeautifulSoup
import requests


html_text = requests.get('https://www.iomfsa.im/enforcement/disqualified-directors/').text
soup = BeautifulSoup(html_text, 'lxml')
def function1():
    directors = soup.find_all('section', class_='accordion-item')
    for director in directors:
        director_list = director.find('div', class_='rte').text
        print(f'{director_list}')

function1()

# directors = soup.find('section', class_='accordion-item')
# name = directors.find('div', class_ = 'rte').text
# print(f'{name}')


Name: John Trevor Roche Baines
Address (at date of disqualification): c/o Isle of Man Prison, Jurby, Isle of Man
Date of Birth: 19 Dec 1939
Period of Disqualification: 15 Years 0 Months 0 Days
Dates of Disqualification: From 15 Jul 2010 To 15 Jul 2025
Particulars of Disqualification Order or Undertaking: Section 2 Company Officers (Disqualification) Act 2009
Notes: Leave granted on 18 November 2010 to be reappointed as director of LB Investments Limited (IOM company no. 2629C) for the sole purpose of executing a Power of Attorney materially identical to the form of the draft Power of Attorney annexed hereto marked "A", to enable any attorney so appointed, inter alia, to convey and distribute the proceeds of sale of the assets of LB Investments Limited. [A copy of the leave form and annex are attached to the register entry held at the office for the registration of companies. Copies may also be obtained by contacting the Enforcement Division of the Financial Supervision Commission.]
 


Name: Ralph Stephen Brunswick
Address (at date of disqualification): Valdfrieden, Ballaugh Glen, Ballaugh, Isle of Man IM7 5JB
Date of Birth:
Period of Disqualification: 13 Years 6 Months 0 Days
Dates of Disqualification: From 4 Mar 2009 To 4 Sep 2022
Particulars of Disqualification Order or Undertaking: S.26(1) Companies Act 1992
