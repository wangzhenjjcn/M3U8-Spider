#coding=utf-8
import sys,time,datetime,os,urllib.request
import io
import sys
import hashlib

print("System loading!")

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

print("System ready!")
hdr = {
       'Host':"www.gg213.com",
       'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
       'Accept-Charset': 'utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'gzip, deflate, br',
       'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
       'Connection': 'keep-alive'
       }

domain="http://www.gg213.com"
path="./gg213/"


print("Checking Files ...")
LIST_FILE = open(path+"LIST.txt","w",encoding='utf-8')
LIST_FILE.close()
READED_FILE = open(path+"READED.txt","w",encoding='utf-8')
READED_FILE.close()
print("Check Files ready!")
print("Reading Files ...")
LIST_FILE = open(path+"LIST.txt","r",encoding='utf-8')
LIST=[]
linenum=0
for lines in LIST_FILE:
        print(linenum+":"+lines)
        linenum+=1
        linesdata = lines.strip("\n")				
        LIST.append(linesdata)
LIST_FILE.close()
print("LIST_FILE Success...")


READED_FILE = open(path+"READED.txt","r",encoding='utf-8')
READED=[]
for lines in READED_FILE:
        linesdata = lines.strip("\n")				
        READED.append(linesdata)
READED_FILE.close()
print("READED_FILE Success...")


print("ALL Success...")

LIST_FILE = open(path+"LIST.txt","a",encoding='utf-8')
READED_FILE = open(path+"READED.txt","a",encoding='utf-8')






def getPage(PAGEURL):
        LIST.append(PAGEURL)
        LIST_FILE.write(PAGEURL+"\n")
        LIST_FILE.flush()
        try:
                mainurl=PAGEURL
                if mainurl=="" or len(mainurl)<3 : return ""
                pagelb=urllib.request.urlopen(mainurl)
        except Exception as e:
                print (str(e))
                return ""
        else:
                if pagelb:
                        PAGEDATA=str(pagelb.read(),'GBK')
                        READED.append(PAGEURL)
                        READED_FILE.write(PAGEURL+"\n")
                        READED_FILE.flush()
                        return PAGEDATA
        return ""




def getVideoPages(PAGEINFO):
        pages=[]
        if ("<div class=\"videos\">") in PAGEINFO :
                if ("<div class=\"footer\">") in PAGEINFO :
                        XQPagesUL=PAGEINFO[PAGEINFO.index("<div class=\"videos\">"):PAGEINFO.index("<div class=\"footer\">")]
                else:
                        XQPagesUL=PAGEINFO[PAGEINFO.index("<div class=\"videos\">"):]
                XQPagesLIS=XQPagesUL.split( "<div class=\"video\">")
                for VNum in range(1,len(XQPagesLIS)):
                        if  ("<a href=\"/video/") in  XQPagesLIS[VNum] :
                                DetialPageLink=domain+XQPagesLIS[VNum][XQPagesLIS[VNum].index("<a href=")+9:XQPagesLIS[VNum].index(".html")+5] 
                                pages.append(DetialPageLink)
                                pass
                        pass
        return pages
                       




def getLinkList(LINKPAGEINFO):
        links=[]
         #<a href="/diao/se56.html" rel="" class="se async" title="All">欧美</a>
        if ("<a href=\"") in LINKPAGEINFO :
                print("12333")
                LINKPagesDATA=LINKPAGEINFO
                LINKPagesDATAs=LINKPagesDATA.split( "<a href=\"")
                for VNum in range(1,len(LINKPagesDATAs)):
                        print(VNum)
                        if  ("\"") in  LINKPagesDATAs[VNum] and (".html") in LINKPagesDATAs[VNum]  :
                                DetialPageLink=LINKPagesDATAs[VNum][0:LINKPagesDATAs[VNum].index(".html")+5] 
                                print(DetialPageLink)
                                if ("\"") in  DetialPageLink or ("http") in  DetialPageLink or ("javascript") in  DetialPageLink or (":") in  DetialPageLink:
                                        pass
                                else:
                                        links.append(domain+DetialPageLink)
                                        print("++++Read new Link:"+domain+DetialPageLink)
                        elif ("\"") in  LINKPagesDATAs[VNum]:
                                DetialPageLink=LINKPagesDATAs[VNum][0:LINKPagesDATAs[VNum].index("\"")] 
                                print(DetialPageLink)
                                if ("\"") in  DetialPageLink or ("http") in  DetialPageLink or ("javascript") in  DetialPageLink or (":") in  DetialPageLink:
                                        pass
                                else:
                                        links.append(domain+DetialPageLink)
                                        print("++++Read new Link:"+domain+DetialPageLink)
        return links
                       





def deCodeXQPage(XQURL):
        LIST.append(XQURL)
        LIST_FILE.write(XQURL+"\n")
        LIST_FILE.flush()

        if XQURL in READED: return

        try:
                xqpage=urllib.request.urlopen(XQURL)
        except Exception as e:
                print("ERR")
                print (str(e))
                deCodeXQPage(XQURL)
                pass            
        else:
                if xqpage:
                        XQPageDetial=str(xqpage.read(),'GBK') 
                        MP4Detial=XQPageDetial[XQPageDetial.index("<source class=\"src\"")+25:XQPageDetial.index("Download video")]
                        MP4Detial=MP4Detial[0:MP4Detial.index("\"")]
                        MP4ID=MP4Detial[MP4Detial.index("xml/")+4:MP4Detial.index(".m")]                                                        
                        print("......")
                        print(MP4ID)
                        MP4Title=XQPageDetial[XQPageDetial.index("<div class=\"a1\">")+16:XQPageDetial.index("<source class=\"src\"")]
                        MP4Title=MP4Title[0:MP4Title.index("</div>")]
                        print(MP4Title)
                        MP4Pic=XQPageDetial[XQPageDetial.index("<div class=\"a1\">")+16:XQPageDetial.index("Download video")]
                        MP4Pic=MP4Pic[MP4Pic.index("poster=\"")+8:MP4Pic.index("<source class=\"src\"")]
                        MP4Pic=MP4Pic[0:MP4Pic.index("\">")]
                        print(MP4Pic)
                        XQPAGE_FILE = open(path+MP4ID+".txt","w",encoding='utf-8')
                        print(" ")
                        XQPAGE_FILE.write(MP4Title+"\n"+MP4Pic+"\n"+MP4Detial)
                        XQPAGE_FILE.flush()                         
                        XQPAGE_FILE.close()
                        READED.append(XQURL)
                        READED_FILE.write(XQURL+"\n")
                        READED_FILE.flush()
 



 





def READPAGE(URL):
        pageurl=URL

        LIST.append(URL)
        LIST_FILE.write(URL+"\n")
        LIST_FILE.flush()
        print("Loading reading....")

        if len(pageurl)<3 : pageurl=domain
        
        if URL in READED: 
                print("++URL readed:"+URL)
                return


        print("Loading "+pageurl+" .....")
        MAINPAGE=getPage(pageurl)
        

         
      




        print("++Reading "+pageurl+" .....")
        videoPages=getVideoPages(MAINPAGE)
        
        for videoPage in videoPages:
                print("++Reading videoPage "+videoPage+" ----------------------------")
                deCodeXQPage(videoPage)
                print("++++Finish videoPage "+videoPage+" -------------------------------")
                print(" ")
                pass

        links=getLinkList(MAINPAGE)
        
        
        
        print(links)
        for link in links:
                print("++Reading link "+link+" ++++++++++++++++++++++++")
                READPAGE(link)
                print("++++Finish link "+link+" +++++++++++++++++++++++++")
                print(" ")
                pass
        print("URL"+URL+" +++++++++++++++++++++++++")
        print(" ")


        READED.append(URL)
        READED_FILE.write(URL+"\n")
        READED_FILE.flush()


READPAGE("")
LIST_FILE.close()
READED_FILE.close()


