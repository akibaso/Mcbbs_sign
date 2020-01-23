# coding:utf-8
import requests
from bs4 import BeautifulSoup
import re  

cookie = '''Hm_lvt_affdf09dddabcdf2d681acefa474b973=1573371748,1573376807,1575193919; ccdefend=e06b1f7f78966c983f4b02136f76f598; ZxYQ_8cea_pc_size_c=0; ZxYQ_8cea_lastvisit=1579747263; ZxYQ_8cea_sendmail=1; ZxYQ_8cea_saltkey=IoU1J117; ZxYQ_8cea_lastact=1579750882%09member.php%09logging; ZxYQ_8cea_ulastactivity=1579750882%7C0; ZxYQ_8cea_auth=0715uuxw2pQHeeVHAlsFjFsqNiTVE9NYLQ5mY2vCuWVDOdcIGZ7szLriCWoCB1k%2FYi%2FinT71x8VVMdy5W7KL8AcxhrvY; ZxYQ_8cea_lastcheckfeed=2387880%7C1579750882; ZxYQ_8cea_checkfollow=1; ZxYQ_8cea_lip=183.221.109.20%2C1579750882'''
header = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
'Connection': 'keep-alive',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Cookie': cookie}
url = 'https://www.mcbbs.net/forum.php'
wbdata = requests.get(url,headers=header).text
soup = BeautifulSoup(wbdata,'lxml')
print(soup)
html = str(soup)
if __name__ == '__main__':  
    p = re.compile('<[^>]+>')  
    print p.sub("", html)  
    
