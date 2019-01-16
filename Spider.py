#coding=utf-8
import sys,time,datetime,os,urllib.request
import io
import sys
import hashlib
import threading
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

DOMAIN="http://www.gg213.com"
PATH="./gg213/"
ALLTHREADS = 1

print("Checking Files ...")
LIST_FILE = open(PATH+"LIST.txt","w",encoding='utf-8')
LIST_FILE.close()
READED_FILE = open(PATH+"READED.txt","w",encoding='utf-8')
READED_FILE.close()
print("Check Files ready!")
print("Reading Files ...")
LIST_FILE = open(PATH+"LIST.txt","r",encoding='utf-8')
LIST=[]
linenum=0
for lines in LIST_FILE:
        print(linenum+":"+lines)
        linenum+=1
        linesdata = lines.strip("\n")				
        LIST.append(linesdata)
LIST_FILE.close()
print("LIST_FILE Success...")


READED_FILE = open(PATH+"READED.txt","r",encoding='utf-8')
READED=[]
for lines in READED_FILE:
        linesdata = lines.strip("\n")				
        READED.append(linesdata)
READED_FILE.close()
print("READED_FILE Success...")


print("ALL Success...")

LIST_FILE = open(PATH+"LIST.txt","a",encoding='utf-8')
READED_FILE = open(PATH+"READED.txt","a",encoding='utf-8')





def getPage(PAGEURL):     
        global ALLTHREADS   
        PAGEDATA=""
        ALLTHREADS=ALLTHREADS+1           
        while ALLTHREADS >50:
                time.sleep(5)
        LIST.append(PAGEURL)
        R=threading.Lock()
        R.acquire()
        LIST_FILE.write(PAGEURL+"\n")
        LIST_FILE.flush()
        R.release()
        # LIST_FILE.write(PAGEURL+"\n")
        # LIST_FILE.flush()
        try:
                mainurl=PAGEURL
                if mainurl=="" or len(mainurl)<3 : 
                        ALLTHREADS=ALLTHREADS-1
                        return PAGEDATA
                pagelb=urllib.request.urlopen(mainurl)
        except Exception as e:
                print (str(e))
                ALLTHREADS=ALLTHREADS-1
                return PAGEDATA
        else:
                if pagelb:
                        PAGEDATA=str(pagelb.read(),'GBK')
 
        ALLTHREADS=ALLTHREADS-1
        return PAGEDATA




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
                                DetialPageLink=DOMAIN+XQPagesLIS[VNum][XQPagesLIS[VNum].index("<a href=")+9:XQPagesLIS[VNum].index(".html")+5] 
                                pages.append(DetialPageLink)
                                pass
                        pass
        return pages
                       




def getLinkList(LINKPAGEINFO):
        links=[]
        
        if ("<a href=\"") in LINKPAGEINFO :

                LINKPagesDATA=LINKPAGEINFO
                LINKPagesDATAs=LINKPagesDATA.split( "<a href=\"")
                for VNum in range(1,len(LINKPagesDATAs)):
                       
                        if  ("\"") in  LINKPagesDATAs[VNum] and (".html") in LINKPagesDATAs[VNum]  :
                                DetialPageLink=LINKPagesDATAs[VNum][0:LINKPagesDATAs[VNum].index(".html")+5] 

                                if ("\"") in  DetialPageLink or ("http") in  DetialPageLink or ("javascript") in  DetialPageLink or (":") in  DetialPageLink or ("www") in  DetialPageLink or ("#") in  DetialPageLink:
                                        pass
                                else:
                                        links.append(DOMAIN+DetialPageLink)
                                        
                                        
                        elif ("\"") in  LINKPagesDATAs[VNum]:
                                DetialPageLink=LINKPagesDATAs[VNum][0:LINKPagesDATAs[VNum].index("\"")] 

                                if ("\"") in  DetialPageLink or ("http") in  DetialPageLink or ("javascript") in  DetialPageLink or (":") in  DetialPageLink or ("www") in  DetialPageLink or ("#") in  DetialPageLink:
                                        pass
                                else:
                                        links.append(DOMAIN+DetialPageLink)
                                        
                                       
        return links
                       





def deCodeXQPage(XQURL):
        global ALLTHREADS
        ALLTHREADS=ALLTHREADS+1
        while ALLTHREADS >50:
                time.sleep(5)
        LIST.append(XQURL)
        R=threading.Lock()
        R.acquire()
        LIST_FILE.write(XQURL+"\n")
        LIST_FILE.flush()
        R.release()
        # LIST_FILE.write(XQURL+"\n")
        # LIST_FILE.flush()
        if XQURL in READED: 
         
                ALLTHREADS=ALLTHREADS-1
                return ""

        try:
                xqpage=urllib.request.urlopen(XQURL)
        except Exception as e:
                print("ERR")
                print (str(e))
                
                ALLTHREADS=ALLTHREADS-1
                return ""           
        else:
                if xqpage:
                        XQPageDetial=str(xqpage.read(),'GBK') 
                        MP4Detial=XQPageDetial[XQPageDetial.index("<source class=\"src\"")+25:XQPageDetial.index("Download video")]
                        MP4Detial=MP4Detial[0:MP4Detial.index("\"")]
                        MP4ID=MP4Detial[MP4Detial.index("xml/")+4:MP4Detial.index(".m")]                                                        
                        print(str(ALLTHREADS)+ "   "+MP4ID)
                        MP4Title=XQPageDetial[XQPageDetial.index("<div class=\"a1\">")+16:XQPageDetial.index("<source class=\"src\"")]
                        MP4Title=MP4Title[0:MP4Title.index("</div>")]
                        MP4Pic=XQPageDetial[XQPageDetial.index("<div class=\"a1\">")+16:XQPageDetial.index("Download video")]
                        MP4Pic=MP4Pic[MP4Pic.index("poster=\"")+8:MP4Pic.index("<source class=\"src\"")]
                        MP4Pic=MP4Pic[0:MP4Pic.index("\">")]
                        XQPAGE_FILE = open(PATH+MP4ID+".txt","w",encoding='utf-8')
                        XQPAGE_FILE.write(MP4Title+"\n"+MP4Pic+"\n"+MP4Detial)
                        XQPAGE_FILE.flush()                         
                        XQPAGE_FILE.close()
                        READED.append(XQURL)
                        R=threading.Lock()
                        R.acquire()
                        READED_FILE.write(XQURL+"\n")
                        READED_FILE.flush()
                        R.release()
        ALLTHREADS=ALLTHREADS-1
        return
 



 





def READPAGE(URL,LEVEL):
        global ALLTHREADS
        levle_this=int(LEVEL)+1
        print("reading level:"+str(levle_this)+"    "+URL+" ..")
        pageurl=URL
        LIST.append(URL)
        R=threading.Lock()
        R.acquire()
        LIST_FILE.write(URL+"\n")
        LIST_FILE.flush()
        R.release()


        # LIST_FILE.write(URL+"\n")
        # LIST_FILE.flush()
        if len(pageurl)<3 : 
                pageurl=DOMAIN        
        if URL in READED: 
                return
        threads = []
        MAINPAGE=getPage(pageurl)
        videoPages=getVideoPages(MAINPAGE)
        links=getLinkList(MAINPAGE)
        for videoPage in videoPages:
                if videoPage in READED:
                        pass
                else:
                        threads.append( threading.Thread(target=deCodeXQPage,args=(videoPage,)) )
                        pass
        for link in links:
                LIST.append(link)
                print("NewLinkAdded:"+link)
                if link in READED:
                        pass
                else:
                        threads.append(threading.Thread(target=READPAGE,args=(link,levle_this,)) )
                        pass
        for t in threads: 
                t.setDaemon(True)
                while threading.activeCount()  >3:
                        print("threading.activeCount():"+str(threading.activeCount())+"        LEVEL:"+str(levle_this))
                        for t in threads: 
                                if len(t._args)>0:
                                        print(t._args)
                                pass



                        time.sleep(5)
                t.start()
        done=False

        while done==False:
                done=True

                for t in threads: 
                        if  t.isAlive() :
                                done=False
                time.sleep(2)
                print("UNDONE")


        print("DONEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
        print(URL)
        R=threading.Lock()
        R.acquire()
        READED.append(URL)
        READED_FILE.write(URL+"\n")
        for link in links:
                 READED.append(link)
                 READED_FILE.write(link+"\n")
        READED_FILE.flush()
        R.release()

        

threading.Semaphore(5)  

if len(LIST)>0:
        for link in LIST:
                READPAGE(link,1)
                pass
else:
        READPAGE("",1)
        pass




LIST_FILE.close()
READED_FILE.close()

