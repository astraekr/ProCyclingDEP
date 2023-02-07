# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from bs4 import BeautifulSoup as bs
import requests
import os

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def init_scrape_site(addr):
    page = requests.get(addr)
    soup = bs(page.content)
    #print(soup)
    #print(soup.html.head)
    #print(soup.title)
    #print(soup.html.head.script)
    #print(soup.find_all('script')[0].contents)
    #var = soup.find_all('script')[0]
    #print(var.children)
    print(soup.html.body)
    var = soup.html.body.find_all('div')

def get_rider_websites(tin_of_soup):

    var = tin_of_soup.html.body.find_all('ul', class_="list horizontal sites")
    for div in var:
        print('success?')
        print(div)
        print('')
    """
    var = soup.html.body.find_all('div')
    for div in var:
        print(div)
        print('')
    var = soup.html.body.find_all('div', 'rdr-img-cont')
    for div in var:
        print(div)
        print('')
    """

def get_rider_info(tin_of_soup):
    # function to get rider info
    var = tin_of_soup


def get_team_list():
    #go to basically any pcs page and get the team list:
    """
    <li class="more4"><a class="reg" href="teams.php">Teams</a><a class="more4 toggleNavDropdown" href="">▼</a><ul class="hide"><li><a href="team/bora-hansgrohe-2023">BORA - hansgrohe</a></li>
    <li><a href="team/cofidis-2023">Cofidis </a></li>
    <li><a href="team/ef-education-easypost-2023">EF Education-EasyPost</a></li>
    <li><a href="team/groupama-fdj-2023">Groupama - FDJ</a></li>
    <li><a href="team/ineos-grenadiers-2023">INEOS Grenadiers</a></li>
    <li><a href="team/intermarche-circus-wanty-2023">Intermarché - Circus - Wanty </a></li>
    <li><a href="team/team-jumbo-visma-2023">Jumbo-Visma</a></li>
    <li><a href="team/movistar-team-2023">Movistar Team</a></li>
    <li><a href="team/soudal-quick-step-2023">Soudal - Quick Step</a></li>
    <li><a href="team/team-arkea-samsic-2023">Team Arkéa Samsic</a></li>
    <li><a href="team/team-jayco-alula-2023">Team Jayco AlUla</a></li>
    <li><a href="team/team-dsm-2023">Team DSM</a></li>
    <li><a href="team/trek-segafredo-2023">Trek - Segafredo</a></li>
    <li><a href="team/ag2r-citroen-team-2023">AG2R Citroën Team</a></li>
    <li><a href="team/uae-team-emirates-2023">UAE Team Emirates</a></li>
    <li><a href="team/alpecin-deceuninck-2023">Alpecin-Deceuninck</a></li>
    <li><a href="team/astana-qazaqstan-team-2023">Astana Qazaqstan Team</a></li>
    <li><a href="team/bahrain-victorious-2023">Bahrain - Victorious</a></li>
    </ul></li>

    :return:
    """

def get_soup(address_str):

    page = requests.get(address_str)
    print(type(page))
    print(page)
    return bs(page.content)

def get_and_save_raw_html_soup(address_str, dir):
    #function to save the raw scraped pages as reference
    file_name = address_str.split('/')[-1] + '.txt'
    page = requests.get(address_str)
    page.encoding = page.apparent_encoding
    print(page.apparent_encoding)
    #print(os.listdir(dir))
    page.encoding = "utf-8"
    with open(os.path.join(dir, file_name), 'w', encoding="utf-8") as fd:
        fd.write(page.text)
    success = True
    return success

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data_dir = "../ProCyclingDEP_Data/Riders/"
    addr = 'https://www.procyclingstats.com/rider/wout-van-aert'
    soup = get_soup(addr)
    stat = get_and_save_raw_html_soup(addr, data_dir)
    print_hi('PyCharm')
    #init_scrape_site(address_str)
    get_rider_websites(soup)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
