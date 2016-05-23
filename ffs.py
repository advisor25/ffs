import urllib.request
import re

#Enter more websites in automatic
#filter their results by allowing characters that make up the ip
#add a checker where each address is tested

print('Fast Free Socks5 (ffs) v1.0')
print('- Coded by aseed9 irc.anonops.com:6697')
ans = True

while ans:

    headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)", "Referer": "https://bing.com"}
    print ("""
  - Menu Selection -
  1. Automatic 
  2. Manual
  3. Add to list
  4. Exit
           """)
    ans = input('Select Option : ')

    if ans =="1":
        try :
             print('Remember to refresh for newer proxies!')
             with urllib.request.urlopen('http://174.139.241.42/yahoo/lists/check/socks5.txt') as response: 
               html = response.read()
               html = str(html)
               html = re.sub('[^0-9.:]', " ", html)
               f = open('proxylist.txt','a')
               f.write(html)
               f.close()
               print('Data(1) saved.')
               ans = True
        except :
                print('##Error on first fetch.')
        try :
            with urllib.request.urlopen('http://www.proxylists.net/socks5.txt') as response: 
               html1 = response.read()
               html1 = str(html1)
               html1 = re.sub('[^0-9.:]', " ", html1)
               f = open('proxylist.txt','a')
               f.write(html1)
               f.close()
               print('Data(2) saved.')
               ans = True
        except :
                print('##Error on second fetch.')
        try :
            with urllib.request.urlopen('http://98.126.61.179/yahoo/lists/check/socks5.txt') as response: 
               html2 = response.read()
               html2 = str(html2)
               html2 = re.sub('[^0-9.:]', " ", html2)
               f = open('proxylist.txt','a')
               f.write(html2)
               f.close()
               print('Data(3) saved.')
               ans = True
        except :
                print('##Error on third fetch.')
        try :
            with urllib.request.urlopen('http://www.alexa.lr2b.com/socks5.txt') as response: 
               html3 = response.read()
               html3 = str(html3)
               html3 = re.sub('[^0-9.:]', " ", html3)
               f = open('proxylist.txt','a')
               f.write(html3)
               f.close()
               print('Data(4) saved.')
               ans = True
        except :
                print('##Error on fourth fetch.')
                
#Uncomment this section to add to automatic list
#To add more than one copy the following and adjust change variable names                
#        try :
#            with urllib.request.urlopen('YOURLINK') as response:
#                link2 = response.read()
#                link2 = str(link2)
#                link2 = re.sub('[^0-9.:]', " ", link2)
#                f = open('proxylist.txt','a')
#                f.write(link2)
#                f.close()
#                print('Data saved.')
#                ans = True
#
#        except :
#            print('Error in manually adding to list')

    if ans=="2":
            try:
                print('Remember to refresh for newer proxies!')
                link = input('Enter link : ')
                with urllib.request.urlopen(link) as response:
                     link = response.read()
                     link = str(link)
                     link = re.sub('[^0-9.:]', " ", link)
                     f = open('proxylist.txt','a+')
                     f.write(link)
                     f.close()
                     print('Dynamic Data saved.')
                     ans = True
            except:
                 print('##User Input Error')
                 ans = True

    if ans=="3":
         try:   
            print('1. Edit the program and remove comments(#) from the code.')
            print('2. Enter your server link at YOURLINK.')
            print('3. Rerun the script.')
            ans = True
         except :
             print('##Something went terribly wrong :S ')
        

    if ans=="4":
          quit()
    else:
          ans = True
            
        






