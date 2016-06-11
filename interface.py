import numpy as np 
import cv2
import pickle
import kociemba
import serial

#port = "/dev/ttyACM0"
boundary = [
	[0,0],  #Red
	[0,0],  #Blue
	[0,0],  #orange
	[0,0],  #White
	[0,0],  #green
	[0,0],  #Yellow
]  

resolution = X,Y = 640 , 480

sqrs = [
	((Y/6)*5,(Y/6)*3),
	((Y/6)*4,(Y/6)*3),
	((Y/6)*3,(Y/6)*3),
	((Y/6)*5,(Y/6)*4),
	((Y/6)*4,(Y/6)*4),
	((Y/6)*3,(Y/6)*4),
	((Y/6)*5,(Y/6)*5),
	((Y/6)*4,(Y/6)*5),
	((Y/6)*3,(Y/6)*5)
]

sqrWidth = X/14
color_list = []
color_name = ['U','R','F','D','L','B']

#ser = serial.Serial(port,9600)

camera = cv2.VideoCapture(0)
if not(camera.isOpened()):
    camera.open()

def reset():
	t = 0
	print "Show :",color_name[0] 
	while t < 6:
		
		frame = camera.read()[1]
		frame = cv2.flip(frame,1)
		high = [0,0,0] 
		low = [256,256,256]
		for i in sqrs :
			x = int(i[0])
			y = int(i[1])
			w = int(sqrWidth)
			crop = frame[y:y+w,x:x+w]
			color = cv2.mean(crop)
			if(high[0] < color[0]):
				high = [color[0] + 30,color[1] + 30, color[2] + 30]
			if (low[0] > color[0]):
				low = [color[0] - 30,color[1] - 30, color[2] - 30]
			cv2.rectangle(frame,(x,y),(x+w,y+w),color,thickness=3)
		cv2.imshow("Callibration",frame)
		if cv2.waitKey(2) & 0xFF == ord('q'):
			boundary[t] = [high,low]
			t += 1
			if(t<6) : print "Show :", color_name[t]
	pickle.dump(boundary,open("Data","wb"))	
	cv2.destroyAllWindows()



while True:
	try:
		boundary = pickle.load(open("Data",'rb'))
		break
	except:
		reset()

def getCube():
	t = 0
	side_sequence = ""
	print "Scan side : ", color_name[0]
	while t < 6:
		data  = ""
		frame = camera.read()[1]
		frame = cv2.flip(frame,1)
		for i in sqrs :
			x = int(i[0])
			y = int(i[1])
			w = int(sqrWidth)
			crop = frame[y:y+w,x:x+w]
			color = cv2.mean(crop)
			color_list.append(color)
			flag = 0
			for [high,low] in boundary:
				if(low[0]<=color[0]<=high[0]):
					if(low[1]<=color[1]<=high[1]):
						if(low[2]<=color[2]<=high[2]):
							name = color_name[boundary.index([high,low])]
							data = data + name
							flag = 1
							break
			if flag == 1 :
				cv2.circle(frame,((x+sqrWidth/2),(y+sqrWidth/2)),sqrWidth/3,(285,285,285),thickness=2)
			cv2.rectangle(frame,(x,y),(x+w,y+w),color,thickness=3)
		cv2.imshow("Scaniing Cube",frame)
		if cv2.waitKey(2) & 0xFF == ord('q'):
			if(len(data)<6):
				print "Side incorrect: scan again"
				continue
			print data
			side_sequence = side_sequence + data
			t += 1
			if(t<6): print "Scan side : ", color_name[t]
		
		del color_list[:]
	return side_sequence
def calibrate():
	t = 0
	while t < 6 :
		ser.write("set value")
		k = 0
		while(k ==0):
			k = input("press '0' to start motor " + str(t)+ " : ")
			



while True:
	side_sequence = getCube()
	print "cube : " , side_sequence
	try :
		solve = kociemba.solve(side_sequence)
		break
	except :
		print "Error in cube, please re-scan"
solve = solve + " "
print solve
k = 0
calibrate()
while k == 1:
	k = input("Start solving ? :")

ser.write(solve.encode('ascii','ignore'))

cv2.destroyAllWindows()

