###############################################################################
# Copyright 2019 Cochlear.ai Ltd. All Rights Reserved.                        #
#                                                                             #
# This is an example to control yeelight smart light bulb through sense API.  #
# Human-generating sound events such as whistling or finger snapping sounds   #
# can be interpreted by sense API. In this example, you can turn on and off   #
# the light bulb by whistling and change the color by finger snapping.        #
# Check this link below to see the demonstration:                             #
# https://www.instagram.com/p/B75ewxdhdqD                                     #
###############################################################################

import json
import pprint

from common.sense import SenseStreamer
from common.sense import sense_stream_request
from common.sense import sense_stream_response
from YeelightWifiBulbLanCtrl import *
import numpy as np

def switch_color(color):
    if color ==  16777215: # White
        color_new = 16711680
    elif color == 16711680: # Red
        color_new = 65280
    elif color == 65280: # Green
        color_new = 255
    elif color == 255: # Blue
        color_new = 16777215
    return color_new

# Sense API-related parameters
apikey = 'Your API-key here'
task = 'event'
prev_tag = ''
color = 16777215


# Yeelight control setting
detection_thread = Thread(target=bulbs_detection_loop)
detection_thread.start()
# give detection thread some time to collect bulb info
sleep(0.2)


# Select the yeelight light bulb to control
print('Choose the light bulb to control.')
display_bulbs()
lb_index = int(raw_input('Type the index : '))


# Streaming begins
with SenseStreamer(task) as stream:
    audio_generator = stream.generator()
    requests = sense_stream_request(audio_generator,apikey,task)
    responses = sense_stream_response(requests)
    print('Listening...')
    
    for i in responses:
        mytag = json.loads(i.outputs)['result']['frames'][0]['tag']
        print('Detected event: {}'.format(mytag))

        # Action definition
        if prev_tag != mytag:
            if mytag == 'Whistling':
                # Turn on/off the light
                toggle_bulb(lb_index)
                operate_on_bulb(lb_index, "set_rgb", str(color))
            elif mytag == 'Finger_snap':
                # Change the color (white -> r -> g -> b -> white ...)
                color = switch_color(color)
                operate_on_bulb(lb_index, "set_rgb", str(color))
        prev_tag = mytag

# user interaction end, tell detection thread to quit and wait
RUNNING = False
detection_thread.join()



