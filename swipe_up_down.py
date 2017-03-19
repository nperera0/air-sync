import os, sys, inspect, thread, time, math
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
# Windows and Linux
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
# Mac
#arch_dir = os.path.abspath(os.path.join(src_dir, '../lib'))

sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture, Pointable, Finger

previousId = -1;
previousRgtId = -1;
counter = 0;
prevProgress = 0;
curList = []
rightLst = []

class LeapMotionListener(Leap.Listener):
	finger_names = ['Thumb', 'Index','Middle','Ring','Pinky']
	bone_names = ['Metacarpal','Proximal','Intermediate','Distal']
	state_names = ['STATE_INVALID','STATE_START','STATE_UPDATE','STATE_END']
	#previousId = -1;
	#counter = 0;

	def on_init(self, controller):
		print "Initialized"

	def on_connect(self, controller):
		print "Motion Sensor Connected!"
		#controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
		#controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
		#controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
		controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

	def on_discoonect(self, controller):
		print "Motion sensor Disconnected"

	def on_exit(self, controller):
		print "Motion Sensor Disconnected"
	
	def on_frame(self, controller):
		frame = controller.frame();
		#global previousId ;

		#pass
		global previousId
		global counter
		global prevProgress
		global curList
		global rightLst
		global previousRgtId
		#print "Types: "+self.finger_names[finger.type]+" ID: "+ str(finger.id)+" Length(mm): "+str(finger.length)
		
		for gesture in frame.gestures():
			
			if gesture.type == Leap.Gesture.TYPE_SWIPE:
				swipe = SwipeGesture(gesture);
				swipeDir = swipe.direction;
				point = swipe.pointable
				finger = Finger(swipe.pointable);
				#print "Finger: " + str(finger.type)
				
				if(swipeDir.y > 0 and math.fabs(swipeDir.x) < math.fabs(swipeDir.y)):
					if(previousId != swipe.id):
							#print curList
							if(len(curList) >= 6):
								lastSix = curList[-6:]
								oneCount = lastSix.count(1)
										
								if(swipeDir.y > 0 and math.fabs(swipeDir.x) < math.fabs(swipeDir.y)):
									if(oneCount == 6 and counter < 20):
										counter = counter + 1
										print "Counter: " + str(counter)
									#print "Swiped up"
								
							curList = []
							curList.append(finger.type)
							previousId = swipe.id
													
					if (previousId == swipe.id):
						curList.append(finger.type)
						
					#print isinstance(finger.type, list)			
					#if(swipeDir.x > 0 and math.fabs(swipeDir.x) > math.fabs(swipeDir.y)):
					#	if(curList.count(1)
					#	print "Swiped right"
				# elif(swipeDir.x < 0 and math.fabs(swipeDir.x) > math.fabs(swipeDir.y)):
					# print "Swiped left"
				# elif(swipeDir.y > 0 and math.fabs(swipeDir.x) < math.fabs(swipeDir.y)):
					# print "Swiped up"
				# elif(swipeDir.y < 0 and math.fabs(swipeDir.x) < math.fabs(swipeDir.y)):
					# print "Swiped down"
				# #else:
				# #	print "Swiped left"
					
				#print "Swipe ID: "+str(swipe.id)+ "Direction: "+ str(swipe.direction)
				# #"State: "+ self.state_names[gesture.state]+ "Position: "+str(swipe.position)+ 
				#" Direction: "+ str(swipe.direction)
				#+"Speed: "+ str(swipe.speed)
				
				if(swipeDir.y < 0 and math.fabs(swipeDir.x) < math.fabs(swipeDir.y)):
					if(previousRgtId != swipe.id):
						rightLst.append(finger.type)
						if(len(rightLst) >= 12):
							oneCount = rightLst.count(1)
							twoCount = rightLst.count(2)
							
							if(abs(twoCount - oneCount) <= 3 and counter > 0):
								counter = counter - 1
							print "Counter: " + str(counter)
							#print "Swiped down: " + str(abs(twoCount - oneCount))
							rightLst = []
						previousRgtId = swipe.id

				#print "Swipe ID: "+str(swipe.id)+ "Direction: "+ str(swipe.direction)
				















				
				
def main():

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    listener = LeapMotionListener()
    controller = Leap.Controller()

    controller.add_listener(listener)
    print "Press enter on exit"
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        controller.remove_listener(listener)

if __name__ == "__main__":
    main()