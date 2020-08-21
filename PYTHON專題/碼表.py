import time

print("按下回车开始计时，按下 Ctrl + C 停止计时。")

while  True:
    
    input("")
    starttime=time.time()
    print("start")
    try:
        while True:
            print("计时:",round(time.time()-starttime,0),"秒",end="\r")
            
            time.sleep(1)
    except KeyboardInterrupt:
        print("end")
        endtime=time.time()
        print("total time is :",round(endtime-starttime,2),"sec")
        break