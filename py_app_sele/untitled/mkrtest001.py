#Usage:monkeyrunner drag_monkeyrunner_test.py
#Import the monkeyrunner modules

import sys
from com.android.monkeyrunner import MonkeyRunner ,MonkeyDevice ,MonkeyImage
#param
submit_x=900
submit_y=1300
button1_x=500
button1_y=1100

guanzhu1_x=500
guanzhu1_y=600

fanhui1_x=100
fanhui1_y=200

fanhui2_x=100
fanhui2_y=200

type = 'DOWN_AND_UP'
seconds = 3
#package and activity
package = "com.hesc.escle.sheng.localserver"
activity = "com.hesc.escle.sheng.module.login.LoginActivity"
component = package + '/' + activity
#connect device
device = MonkeyRunner.waitForConnection()

#lauch app   component="com.hesc.escle.sheng.localserver/com.hesc.escle.sheng.module.login.LoginActivity"
device.startActivity(component)
print("app lauch")

MonkeyRunner.sleep(seconds)

device.touch(submit_x,submit_y,type)

MonkeyRunner.sleep(seconds)

#Get snapshot
picture = device.takeSnapshot()
picture.writeToFile('./monkeytest.png','png')
print("picture")

#guanzhu
device.touch(button1_x,button1_y,type)
MonkeyRunner.sleep(seconds)
print("dianji guanzhu ")

#xiangqing
device.touch(guanzhu1_x,guanzhu1_y,type)
MonkeyRunner.sleep(seconds)
print("chakan xiangqing")

#fanhui1
device.touch(fanhui1_x,fanhui1_y,type)
MonkeyRunner.sleep(seconds)
print("fanhui1")

#fanhui2
device.touch(fanhui2_x,fanhui2_y,type)
MonkeyRunner.sleep(seconds)
print("fanhui2")

