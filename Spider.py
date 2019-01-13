#coding=utf-8
import sys,time,datetime,os,urllib.request
import io
import sys

print("System loading!")

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

print("System ready!")
hdr = {
       'Host':"wapp8.com",
       'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
       'Accept-Charset': 'utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'gzip, deflate, br',
       'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
       'Connection': 'keep-alive'
       }

domain="http://wapp8.com/"
flpg="?m=vod-type-id-16-pg-"


print("Checking Files ...")
LIST_FILE = open("./"+"WAPP8"+"/"+"LIST.txt","w",encoding='utf-8')
LIST_FILE.close()
print("Check Files ready!")



print("Reading Files ...")
LIST_FILE = open("./"+"WAPP8"+"/"+"LIST.txt","r",encoding='utf-8')
LIST_DATA = LIST_FILE.read()
print("Read Files success!")
LIST={}
print(LIST_FILE.encoding)
linenum=0
for lines in LIST_FILE:
        print (linenum)
        linenum+=1
        linesdata = lines.strip("\n")				
        LIST[linenum]=linesdata
LIST_FILE.close()
print(linenum)
print(LIST)
print(LIST_FILE)


LIST_FILE = open("./"+"WAPP8"+"/"+"LIST.txt","a",encoding='utf-8')




LBPages=1
try:
        ejurl=domain+flpg+str(LBPages)+".html"
        pagelb=urllib.request.urlopen(ejurl)
        print (ejurl)
except Exception as e:
        print (str(e))
        pass
                                        
else:
        if pagelb:
                LBPageDetial=str(pagelb.read(),'utf8') 
                LBLink=""
                #print(str(LBPageDetial))            
                if ("下一页") in LBPageDetial and ("尾页") in LBPageDetial:
                        LBPages=LBPageDetial[LBPageDetial.index("下一页"):LBPageDetial.index("尾页")]
                        LBLink=LBPages[LBPages.index("href=")+6:LBPages.index("pg-")+3]                        
                        LBPages=LBPages[LBPages.index("pg-")+3:LBPages.index(".html")]                        
                        print ((domain+LBLink+LBPages+".html").replace(".com//",".com/"))
print (LBPages)					
						
						 
						
for LBPage in range(int(LBPages)):
        try:
                ejurl=domain+flpg+str(LBPage)+".html"
                pagelb=urllib.request.urlopen(ejurl)
                print (ejurl)
        except Exception as e:
                print (str(e))
                pass
                                                
        else:
                if pagelb:
                        LBPageDetial=str(pagelb.read(),'utf8') 
                        LBLink=""
                        LBLinkNum=0
                        if ("<ul class=\"videos\">") in LBPageDetial and ("尾页") in LBPageDetial:
                                XQPagesUL=LBPageDetial[LBPageDetial.index("<ul class=\"videos\">"):LBPageDetial.index("尾页")]
                                XQPagesUL=XQPagesUL[0:XQPagesUL.index("</ul>")] 
                                if ("</ul>") in XQPagesUL  :               
                                        XQPagesUL=XQPagesUL[0:XQPagesUL.index("</ul>")]  
                                        if ("</ul>") in XQPagesUL  :               
                                                XQPagesUL=XQPagesUL[0:XQPagesUL.index("</ul>")] 
                                XQPagesLIS=XQPagesUL.split( "</li>")
                                print("XQPagesLIS") 
                                print(len(XQPagesLIS))

                                for XQPageNum in range(len(XQPagesLIS)-1):
                                        XQPageData=XQPagesLIS[XQPageNum]
                                        if ("<a href=") in XQPageData :
                                                XQPageLink=domain+XQPageData[XQPageData.index("<a href=")+9:XQPageData.index(".html")+5]  
                                                print(XQPageNum)
                                                print(XQPageLink)
                                                print("")
                                                LBLink+=XQPageLink+"\n"
                                                LBLinkNum+=1
                        LBLink.replace("\r\n\r\n","\r\n")
                        print("Checking Files ...")
                        PAGE_FILE = open("./"+"WAPP8"+"/"+"LIST"+str(LBPage)+".txt","w",encoding='utf-8')
                        print("Check Files ready!")
                        PAGE_FILE.write(str(LBLink))
                        PAGE_FILE.flush()                         
                        PAGE_FILE.close()
                        print(len(LBLink))
        print (LBPage)	
 
        	
				