import os, sys, inspect, thread, time, math
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
# Windows and Linux
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
# Mac
#arch_dir = os.path.abspath(os.path.join(src_dir, '../lib'))

import pygame
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture, Pointable, Finger

previousId = -1;
previousRgtId = -1;
#counter = 0;
prevProgress = 0;
curList = []
rightLst = []
timer_flag = 0 
t_start = 0;
t_end = 0;
err_counter = 0;
step_counter = 0;

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
		
		#logging file
		global outFile
		outFile = open('swipeLog.txt', 'a');
		
		#controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
		#controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
		#controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
		controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

	def on_discoonect(self, controller):
		print "Motion sensor Disconnected"

	def on_exit(self, controller):
		global err_counter
		global step_counter

		if counter != target_value:
			print "Target value not reached"
		else:
			print t_end - t_start
			outFile.write("Go from "+str(s_num)+" to "+str(target_value)+": ");
			outFile.write(str(t_end - t_start))
			err_counter = err_counter - 1;
			outFile.write(" Accuracy is: "+str(1-float(float(err_counter)/(err_counter+1))));
			outFile.write(" Expected step count: "+ str(abs(s_num - target_value)) +" Total step count: "+str(step_counter)+"\n");

		print "Motion Sensor Exit"
	
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
		global timer_flag
		global t_start
		global t_end
		global err_counter
		global step_counter

		if timer_flag == 0:
			timer_flag = 1;
			t_start = time.time();		

		#print "Types: "+self.finger_names[finger.type]+" ID: "+ str(finger.id)+" Length(mm): "+str(finger.length)
		
		
		for gesture in frame.gestures():
			
				
			if gesture.type == Leap.Gesture.TYPE_SWIPE:
				swipe = SwipeGesture(gesture);
				swipeDir = swipe.direction;
				point = swipe.pointable
				finger = Finger(swipe.pointable);
				#print "Finger: " + str(finger.type)
				
				if(swipeDir.x < 0 and math.fabs(swipeDir.x) > math.fabs(swipeDir.y)):
					if(previousId != swipe.id):
							if(len(curList) >= 12):
								lastSix = curList[-12:]
								oneCount = lastSix.count(1)
								twoCount = lastSix.count(2)
										
								if(swipeDir.x < 0 and math.fabs(swipeDir.x) > math.fabs(swipeDir.y)):
									if(oneCount == 12 and counter < 20):
										counter = counter + 1
										step_counter = step_counter + 1

										print "Counter: " + str(counter)
										# play audio
										fileName = str(counter).zfill(2)
										pygame.mixer.music.load(fileName + '.wav')
										pygame.mixer.music.play()
										if counter == target_value:
											t_end = time.time();
											print t_end - t_start
											err_counter = err_counter + 1;
								
							curList = []
							curList.append(finger.type)
							previousId = swipe.id
													
					if (previousId == swipe.id):
						curList.append(finger.type)
				
				if(swipeDir.x > 0 and math.fabs(swipeDir.x) > math.fabs(swipeDir.y)):
					if(previousRgtId != swipe.id):
						rightLst.append(finger.type)
						if(len(rightLst) >= 27):
							oneCount = rightLst.count(1)
							twoCount = rightLst.count(2)
							
							if(abs(twoCount - oneCount) <= 2 and counter > 1):
								counter = counter - 1
								step_counter = step_counter + 1

							print "Counter: " + str(counter)
							# play audio
							fileName = str(counter).zfill(2)
							pygame.mixer.music.load(fileName + '.wav')
							pygame.mixer.music.play()
							if counter == target_value:
								t_end = time.time();
								print t_end - t_start
								err_counter = err_counter + 1;
							rightLst = []
						previousRgtId = swipe.id
						
				
def main():

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    listener = LeapMotionListener()
    controller = Leap.Controller()

    controller.add_listener(listener)
	
	#initialize audio 
    pygame.mixer.init()
	
    print "Press enter on exit"
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        controller.remove_listener(listener)

if __name__ == "__main__":
    global counter
    global target_value
    global s_num
    counter = int(sys.argv[1]);
    s_num = counter;
    target_value = int(sys.argv[2]);
    main()