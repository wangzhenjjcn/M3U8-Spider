#coding=utf-8
import sys,time,datetime,os,urllib.request

hdr = {
       'Host':"wapp8.com",
       'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
       'Accept-Charset': 'utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'gzip, deflate, br',
       'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
       'Connection': 'keep-alive'
       }


    
 

try:
        ejurl=
        pagelb=urllib.request.urlopen(ejurl)
        print (ejurl)
except Exception as e:
        print (str(e))
        pass
                                        
else:
        if pagelb:
                LBPageDetial=str(pagelb.read()).encode('utf8').decode("gb2312")
                LBPages=0
                print(LBPageDetial)            
                if ("下一页".encode('utf8')) in LBPageDetial and ("尾页".encode('utf8')) in LBPageDetial:
                        print("00000000000")
                        LBPages=LBPageDetial[LBPageDetial.index("下一页"):LBPageDetial.index("尾页")]
                
                
                print (LBPages)
        print ('6+56+5+6ioyhuyhuiyhui')				
				 