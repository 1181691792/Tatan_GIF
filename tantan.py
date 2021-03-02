# coding=utf-8
import requests
import re
import time
import os
from bs4 import BeautifulSoup

class tantan():
    def ase(self):
        SEE=[]
        RTT=[]
        for i in range(0,21):
            url1 = 'https://fabiaoqing.com/search/bqb/keyword/印尼小胖tantan/type/bq/page/'
            url2 = str(i)
            url = url1+url2+'.html'
            S = requests.session()
            time.sleep(0.4)
            r = S.get(url=url)
            fg = (r.text.encode('GBK', 'ignore').decode('GBk'))
            DE = re.findall(r'data-original="(.*?)"', fg)
            alt = re.findall(r'alt="(.*?)"', fg)
            # print(DE)
            # print(alt)
            for j in range(0,len(DE)):
                SEE.append(DE[j])
                RTT.append(alt[j])
        # print(SEE)

        for z in  range(0,len(SEE)):
            print(SEE[z])
            # print(RTT[z])
            try:
                f = open("E:\\123\\"+RTT[z]+".gif", "w+") #注意地址
                time.sleep(0.4)
                with open("E:\\123\\"+RTT[z]+".gif", 'wb') as f:
                    f.write(requests.get(SEE[z]).content)
                print("下载"+RTT[z]+"成功")
            except:
                print("下载" + RTT[z] + "失败")


if __name__ == '__main__':
    tantan().ase()

