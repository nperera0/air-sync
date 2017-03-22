import os, sys, inspect, thread, time, signal
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
# Windows and Linux
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
# Mac
#arch_dir = os.path.abspath(os.path.join(src_dir, '../lib'))

import pygame
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import Leap
import time
import msvcrt
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture, Finger

previousId = -1;
#counter = 0;
prevProgress = 0;
curList = []
timer_flag = 0 
t_start = 0;
t_end = 0;
err_counter = 0;
step_counter = 0;

#def sigint_handler(signal, frame):
#    print 'Interrupted !!'
	
#signal.signal(signal.SIGINT, sigint_handler)


def findIndexOf(item, list):
		index = 0;
		for curItem in list:
			if(curItem == item):
				return index
			index = index + 1
		return -1


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
		outFile = open('screentapLog.txt', 'a');
		
		controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
		controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
		controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
		controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);
		while msvcrt.kbhit():
			msvcrt.getch()

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
		global timer_flag
		global t_start
		global t_end
		global err_counter
		global step_counter

		if timer_flag == 0:
			timer_flag = 1;
			t_start = time.time();
			
		for gesture in frame.gestures():
			if gesture.type == Leap.Gesture.TYPE_SCREEN_TAP:
				keyTap = ScreenTapGesture(gesture)
				#swipeDir = swipe.direction;
				point = keyTap.pointable
				finger = Finger(keyTap.pointable);
				#print "Finger: " + str(finger.type)
				
				curList.append(finger.type);
				#print len(frame.gestures());
				
				#print "Key Tap ID: "+ str(gesture.id)+ " State: "+self.state_names[gesture.state]+ " Position: "+ str(keyTap.position) + " Direction: "+str(keyTap.direction)
					
				#print "ID: "+str(circle.id)+" Progress: "+str(circle.progress)+" Radius: "+str(circle.radius)+" Swept Angle: "+str(swept_angle * Leap.RAD_TO_DEG)+" "+clockwiseness
				oneCount = curList.count(1);
				twoCount = curList.count(2);
				gestures = frame.gestures()
				if ((abs(twoCount - oneCount) >= 1) and findIndexOf(gesture, frame.gestures()) == (len(frame.gestures()) - 1)):
					if(counter < 20):
						counter = counter + 1
						step_counter = step_counter + 1
						print "Counter: " + str(counter)
						# play audio
						fileName = str(counter).zfill(2)
						pygame.mixer.music.load(fileName + '.wav')
						pygame.mixer.music.play()
						curList = []
						if counter == target_value:
							t_end = time.time();
							print t_end - t_start
							err_counter = err_counter + 1;

						
				elif ((abs(twoCount - oneCount) < 1) and findIndexOf(gesture, frame.gestures()) == (len(frame.gestures()) - 1)):
					if(counter > 1):
						counter = counter - 1
						step_counter = step_counter + 1
						print "Counter: " + str(counter)
						# play audio
						fileName = str(counter).zfill(2)
						pygame.mixer.music.load(fileName + '.wav')
						pygame.mixer.music.play()
						curList = []
						if counter == target_value:
							t_end = time.time();
							print t_end - t_start
							err_counter = err_counter + 1;
									
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