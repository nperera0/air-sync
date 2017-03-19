import os, sys, inspect, thread, time
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
# Windows and Linux
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
# Mac
#arch_dir = os.path.abspath(os.path.join(src_dir, '../lib'))

sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

previousId = -1;
counter = 0;
prevProgress = 0;

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
		controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
		controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
		controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
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
		
		for gesture in frame.gestures():
			if gesture.type == Leap.Gesture.TYPE_KEY_TAP:
				keyTap = KeyTapGesture(gesture)
				print "Key Tap ID: "+ str(gesture.id)+ " State: "+self.state_names[gesture.state]+ " Position: "+ str(keyTap.position) + " Direction: "+str(keyTap.direction)
				# if circle.pointable.direction.angle_to(circle.normal) <= Leap.PI/2:
					# clockwiseness = "clockwise"
					
					# if(previousId != circle.id):
						# prevProgress = 0
						# previousId = circle.id
						
						
					# if(previousId == circle.id):
						# if(int(circle.progress) - prevProgress == 1):
							# prevProgress = int(circle.progress)
							# if (counter < 20):
								# counter = counter + 1
							# print "Counter: " + str(counter)

				# else:
					# clockwiseness = "counter-clockwise"	
					# if(previousId != circle.id):
						# prevProgress = 0
						# previousId = circle.id
						
						
					# if(previousId == circle.id):
						# if(int(circle.progress) - prevProgress == 1):
							# prevProgress = int(circle.progress)
							# if (counter > 0):
								# counter = counter - 1
							# print "Counter: " + str(counter)

				
				# swept_angle = 0
				# if circle.state != Leap.Gesture.STATE_START:
					# previous = CircleGesture(controller.frame(1).gesture(circle.id))
					# swept_angle = (circle.progress - previous.progress)*2 * Leap.PI;
					
				#print "ID: "+str(circle.id)+" Progress: "+str(circle.progress)+" Radius: "+str(circle.radius)+" Swept Angle: "+str(swept_angle * Leap.RAD_TO_DEG)+" "+clockwiseness
				
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