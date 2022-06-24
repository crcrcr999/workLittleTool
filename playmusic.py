import datetime
import random
import time
import worktime
import os
import playsound


def play(filename):
    try:
        playsound.playsound(filename)
    except Exception as ide:
        print(f'Error: {ide}')

### 定义文件名获取函数
def data_needed(filePath):
    import os        #引入os
    file_name = list()        #新建列表
    for i in os.listdir(filePath):        #获取filePath路径下所有文件名
    	if i.endswith(".mp3"):
        	data_collect = ''.join(i)        #文件名字符串格式
        	file_name.append(data_collect)        #将文件名作为列表元素填入
    return(file_name)        #返回列表

#isworktime = lambda x,y: True if (x>=y[0] and x<y[1]) else False
upanPath="/media/cr/MUSIC/"
endMusicPath="end/huijia.mp3"
playEndMusic=False
#workrange=[13,20]
string="";
while True:
	if os.path.exists(upanPath):
		if worktime.timecalendar():
		#if nowminute<23:
			playEndMusic=False
			musiclist=data_needed(upanPath)
			randomint=random.randint(0,len(musiclist)-1)
			speakpath = upanPath+musiclist[randomint]
			print ("\033[A\033[K\33[K\33[A")
			string="\033[32;1m现在播放\033[0m:\033[33;1m:"+musiclist[randomint]+"\033[0m"
			print(string)
			play(speakpath)
			time.sleep(1)
		else:
			if playEndMusic==False:
				play(upanPath+endMusicPath)
				playEndMusic=True
			time.sleep(60)
	
