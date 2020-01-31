# sense-yeelight (in conjunction with sense-python)

## What is sense-yeelight?

This is a python example to control yeelight smart light bulb through sense API.  
Sense API provided by Cochlear.ai Ltd. is a powerful tool that enables machines to understand various sounds.  
Using this example, you can turn on and off the light bulb by whistling and change the color by finger snapping.  
Check the link below to see the demonstration:  
https://www.instagram.com/p/B75ewxdhdqD


## Environment setting

### 1. Portaudio

In order for sense-yeelight to get the audio stream from your microphone, port-audio is necessary.  
On MacOS, you can install it by
```
$ brew install portaudio
```

On Linux, 
```
$ apt-get update
$ apt-get install ffmpeg sox portaudio19-dev libssl-dev libcurl4-openssl-dev
```

### 2. Install python dependency

This repository was tested in python2.7 environment and the compatiblity check with python 3.x is still in progress.  
Make sure to have install `pip` before execute the following code.

```
$ pip install -r requirements.txt
```

### 3. Get your sense API key

You need to get a key to use sense API. Visit https://cochlear.ai/beta-subscription/ and sign up for free.  
Then put the key inside example_stream.py file.

## Launch example

Run
```
$ python example_stream.py
```

For further information, please refer to our API document: http://cochlear.ai/docs/.

## Reference
This repository is merely a combination of the two examples made by Cochlear.ai and Yeelight.  
For more information, please refer to the original sources.  

1. Yeelight developer demo for linux  
https://www.yeelight.com/en_US/developer

2. Sense API and the documentation by Cochlear.ai Ltd.  
https://github.com/cochlearai/sense-python  
http://cochlear.ai/docs/  


