﻿#coding=utf-8
import sys,time,datetime,os,urllib.request
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
hdr = {
       'Host':"w------ap------p8.co------m",
       'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
       'Accept-Charset': 'utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'gzip, deflate, br',
       'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
       'Connection': 'keep-alive'
       }

domain="http://w------ap------p8.co------m/"
flpg="?m=vod-type-id-16-pg-1.html"
 

try:
        ejurl=domain+flpg
        pagelb=urllib.request.urlopen(ejurl)
        print (ejurl)
except Exception as e:
        print (str(e))
        pass
                                        
else:
        if pagelb:
                LBPageDetial=str(pagelb.read(),'utf8') 
                LBPages=0
                LBLink=""
                print(str(LBPageDetial))            
                if ("下一页") in LBPageDetial and ("尾页") in LBPageDetial:
                        LBPages=LBPageDetial[LBPageDetial.index("下一页"):LBPageDetial.index("尾页")]0
                        LBLink=LBPages[LBPages.index("href=")+6:LBPages.index("pg-")+3]                        
                        LBPages=LBPages[LBPages.index("pg-")+3:LBPages.index(".html")]
                        print (LBPages)
                        print ((domain+LBLink+LBPages+".html").replace(".com//",".com/"))
				 