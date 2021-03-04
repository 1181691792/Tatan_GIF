# coding=utf-8
import requests
import re
import time
import os


class tantan():
    def ase(self):
        SEE=[]
        RTT=[]
        for i in range(0,21):
            url1 = 'https://fabiaoqing.com/search/bqb/keyword/印尼小胖tantan/type/bq/page/'
            url2 = str(i)
            url = url1+url2+'.html'
            S = requests.session()
            time.sleep(0.5)
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
            RTY=RTT[z].split("（印尼小胖")[0].split("(印尼小胖")[0].split("(网红印尼小胖")[0].split("-印尼")[0].split("（网红印尼小胖")[0].replace(" ", "").replace("，", "").replace("!", "")
            try:
                path=str("E:\\123\\"+RTY+".gif")
                folder = os.path.isfile(path)
                if not folder:
                    with open("E:\\123\\"+RTY+".gif", 'wb') as f:
                        f.write(requests.get(SEE[z]).content)
                    print("下载"+RTY+"成功")
                else:
                    print("存在相同表情包"+RTY)
            except:
                print("下载" +RTY+ "失败")
                print("不做筛选，重新下载")
                try:
                    path = str("E:\\123\\" + RTT[z] + ".gif")
                    folder = os.path.isfile(path)
                    if not folder:
                        with open("E:\\123\\" + RTT[z] + ".gif", 'wb') as f:
                            f.write(requests.get(SEE[z]).content)
                        print("下载" + RTT[z] + "成功")
                    else:
                        print("存在相同表情包" + RTT[z])
                except:
                    print("再次下载失败，放弃下载")





if __name__ == '__main__':

    tantan().ase()

