# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from bs4 import BeautifulSoup as bs #v4.11.1
import requests
import os
from pathlib import Path, WindowsPath

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


def get_team_list(root_page_addr: str) -> list:
    # go to basically any pcs page and get the team list:
    team_list = []
    sp = get_soup(root_page_addr)
    var = sp.html.body.find_all('li')

    for li in var:
        if len(li.contents) > 0 and li.contents[0].string == 'Teams':
            new_li = li
            break

    var = new_li.find_all('a')
    for li in var:
        if li.string != 'Teams' and not 'class' in li.attrs:
            team_list.append(li.string)

    print(team_list)
    return team_list


def get_team_list_test():
    # chat-gpt's unit test for this!
    team_list = get_team_list('https://www.pcsoweb.com/g5-bin/client.cgi?G5genie=8&school_id=1')
    assert len(team_list) == 10
    assert 'Boys Varsity' in team_list
    assert 'Girls Varsity' in team_list
    assert 'Boys JV' in team_list
    assert 'Girls JV' in team_list
    assert 'Boys Freshman' in team_list
    assert 'Girls Freshman' in team_list
    assert 'Boys Middle School' in team_list
    assert 'Girls Middle School' in team_list
    assert 'Boys Elementary' in team_list
    assert 'Girls Elementary' in team_list


def get_soup(address_str):

    page = requests.get(address_str)
    return bs(page.content, features="html.parser")

def get_and_save_raw_html_soup(address_str, dir):
    # function to save the raw scraped pages as reference
    file_name = address_str.split('/')[-1] + '.html'
    page = requests.get(address_str)
    page.encoding = page.apparent_encoding
    with open(os.path.join(dir, file_name), 'w', encoding="utf-8") as fd:
        fd.write(page.text)
    success = True
    return success

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    repo_dir = Path.cwd()
    storage_dir = repo_dir.parent.joinpath(WindowsPath('ProCyclingDE_Data'))
    riders_storage_dir = storage_dir.joinpath(WindowsPath('riders'))
    misc_storage_dir = storage_dir.joinpath(WindowsPath('misc'))

    root_page_addr = 'https://www.procyclingstats.com/'
    addr = 'https://www.procyclingstats.com/rider/wout-van-aert'
    soup = get_soup(addr)

    get_team_list(root_page_addr)



    #get_and_save_raw_html_soup(root_page_addr, misc_storage_dir)
    #if not misc_storage_dir.is_dir():
        #misc_storage_dir.mkdir()

    #data_dir = Path("../ProCyclingDEP_Data/Riders/")


    #stat = get_and_save_raw_html_soup(addr, misc_storage_dir)
    #print_hi('PyCharm')
    #init_scrape_site(address_str)
    #get_rider_websites(soup)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
