import os, sys, inspect, thread, time
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
# Windows and Linux
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
# Mac
#arch_dir = os.path.abspath(os.path.join(src_dir, '../lib'))

import pygame
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import logging
import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

previousId = -1;
#counter = 0;
prevProgress = 0;
timer_flag = 0
t_start = 0;
t_end = 0;
outFile = 0;
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
		outFile = open('circleLog.txt', 'a');
		controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
		controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
		controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
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
		#global logger
		#logger.info('Log time');
		frame = controller.frame();
		#global previousId ;

		#pass
		global previousId
		global counter
		global prevProgress
		global timer_flag
		global t_start
		global t_end
		global err_counter
		global step_counter
		
		if timer_flag == 0:
			timer_flag = 1;
			t_start = time.time();
			
		for gesture in frame.gestures():
			if gesture.type == Leap.Gesture.TYPE_CIRCLE:
				circle = CircleGesture(gesture)		
				if circle.pointable.direction.angle_to(circle.normal) <= Leap.PI/2:
					clockwiseness = "clockwise"
					
					if(previousId != circle.id):
						prevProgress = 0
						previousId = circle.id
						
						
					if(previousId == circle.id):
						if(int(circle.progress) - prevProgress == 1):
							prevProgress = int(circle.progress)
							if (counter < 20):
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

				else:
					clockwiseness = "counter-clockwise"	
					if(previousId != circle.id):
						prevProgress = 0
						previousId = circle.id
						
						
					if(previousId == circle.id):
						if(int(circle.progress) - prevProgress == 1):
							prevProgress = int(circle.progress)
							if (counter > 1):
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
				
				swept_angle = 0
				if circle.state != Leap.Gesture.STATE_START:
					previous = CircleGesture(controller.frame(1).gesture(circle.id))
					swept_angle = (circle.progress - previous.progress)*2 * Leap.PI;
					
				#print "ID: "+str(circle.id)+" Progress: "+str(circle.progress)+" Radius: "+str(circle.radius)+" Swept Angle: "+str(swept_angle * Leap.RAD_TO_DEG)+" "+clockwiseness
				
def main():

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    listener = LeapMotionListener()
    controller = Leap.Controller()
	
	#initialize audio 
    pygame.mixer.init()

    controller.add_listener(listener)
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