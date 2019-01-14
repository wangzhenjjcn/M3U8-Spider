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

domain="http://www.gg213.com"
flpg="?m=vod-type-id-16-pg-"
path="./gg213/"


print("Checking Files ...")
LIST_FILE = open(path+"LIST.txt","w",encoding='utf-8')
LIST_FILE.close()
print("Check Files ready!")



print("Reading Files ...")
LIST_FILE = open(path+"LIST.txt","r",encoding='utf-8')
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


LIST_FILE = open(path+"LIST.txt","a",encoding='utf-8')




LBPages=1
try:
        mainurl=domain
        pagelb=urllib.request.urlopen(mainurl)
        print (mainurl)
except Exception as e:
        print (str(e))
        pass
                                        
else:
        if pagelb:
                LBPageDetial=str(pagelb.read(),'GBK') 
                print("Checking Files ...")
                PAGE_FILE = open(path+"main.txt","w",encoding='utf-8')
                print("Check Files ready!")
                PAGE_FILE.write(str(LBPageDetial))
                PAGE_FILE.flush()                         
                PAGE_FILE.close()
                print(len(LBPageDetial))
                if ("<div class=\"videos\">") in LBPageDetial :
                        XQPagesUL=LBPageDetial[LBPageDetial.index("<div class=\"videos\">"):LBPageDetial.index("<div class=\"footer\">")]
                        XQPagesLIS=XQPagesUL.split( "<div class=\"video\">")
                        print("XQPagesLIS") 
                        print(len(XQPagesLIS))
 
                        for VPageNum in range(1,len(XQPagesLIS)):
                                print(VPageNum)
                                if  ("<a href=\"/video/") in  XQPagesLIS[VPageNum] :
                                        DetialPageLink=domain+XQPagesLIS[VPageNum][XQPagesLIS[VPageNum].index("<a href=")+9:XQPagesLIS[VPageNum].index(".html")+5] 
                                        print("DetialPageLink") 
                                        print(DetialPageLink) 

                                        try:
                                                xqurl=DetialPageLink
                                                xqpage=urllib.request.urlopen(xqurl)
                                                print (xqurl)
                                        except Exception as e:
                                                print (str(e))
                                                pass
                                                                                
                                        else:
                                                if xqpage:
                                                        XQPageDetial=str(xqpage.read(),'GBK') 
                                                        print("Checking Files ...")
                                                        MP4Detial=XQPageDetial[XQPageDetial.index("<source class=\"src\"")+25:XQPageDetial.index("Download video")]
                                                        MP4Detial=MP4Detial[0:MP4Detial.index("\"")]
                                                        MP4Title=XQPageDetial[XQPageDetial.index("<div class=\"a1\">")+16:XQPageDetial.index("<source class=\"src\"")]
                                                        MP4Title=MP4Title[0:MP4Title.index("</div>")]
                                                        print(MP4Title)
                                                        MP4Pic=XQPageDetial[XQPageDetial.index("<div class=\"a1\">")+16:XQPageDetial.index("Download video")]
                                                        MP4Pic=MP4Pic[MP4Pic.index("poster=\"")+8:MP4Pic.index("<source class=\"src\"")]
                                                        MP4Pic=MP4Pic[0:MP4Pic.index("\">")]
                                                        print(MP4Pic)


                                                        XQPAGE_FILE = open(path+str(VPageNum)+".txt","w",encoding='utf-8')
                                                        print("Check Files ready!")
                                                        XQPAGE_FILE.write(MP4Title+"\n"+MP4Pic+"\n"+MP4Detial)
                                                        XQPAGE_FILE.flush()                         
                                                        XQPAGE_FILE.close()
