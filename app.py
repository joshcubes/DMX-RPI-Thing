from stupidArtnet import StupidArtnet
import time
import random

# THESE ARE MOST LIKELY THE VALUES YOU WILL BE NEEDING
target_ip = '192.168.0.201'		# typically in 2.x or 10.x range
universe = 0 										# see docs
packet_size = 512								

# CREATING A STUPID ARTNET OBJECT
# SETUP NEEDS A FEW ELEMENTS
# TARGET_IP   = DEFAULT 127.0.0.1
# UNIVERSE    = DEFAULT 0
# PACKET_SIZE = DEFAULT 512
# FRAME_RATE  = DEFAULT 30
# ISBROADCAST = DEFAULT FALSE
a = StupidArtnet(target_ip, universe, packet_size, 30, True, True)

# MORE ADVANCED CAN BE SET WITH SETTERS IF NEEDED
# NET         = DEFAULT 0
# SUBNET      = DEFAULT 0

# CHECK INIT

# YOU CAN CREATE YOUR OWN BYTE ARRAY OF PACKET_SIZE
packet = bytearray(packet_size)		# create packet for Artnet
for i in range(packet_size):			# fill packet with sequential values
    packet[i] = (i % 256)

# ... AND SET IT TO STUPID ARTNET
a.set(packet)						# only on changes

# ALL PACKETS ARE SAVED IN THE CLASS, YOU CAN CHANGE SINGLE VALUES
a.set_single_value(1, 255)			# set channel 1 to 255

# ... AND SEND
a.show()							# send data

# OR USE STUPIDARTNET FUNCTIONS
a.flash_all()						# send single packet with all channels at 255

time.sleep(1)						# wait a bit, 1 sec

a.blackout()						# send single packet with all channels at 0
a.see_buffer()

rate = 50
sleep = 1/rate
channel = 1
while True:
    try:
        channel = random.randint(1,512)
            
        y = random.randint(0,255)
        
        a.set_single_value(channel,y)
        a.show()
        time.sleep(sleep)
    
    
    except KeyboardInterrupt:
        break

    
# CLEANUP IN THE END
del a