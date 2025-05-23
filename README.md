## Framework structure

The framework consists of a few folders. Below please the description of each folder:

	- base - probably the "main" folder where are located base page, working with locators, and the driver initialization class are located. The code and logic inside each file are easy to maintain and scale.
	- pages - here we have files with all product pages. One file = one page.
	- platform_capabilities - we can add as many platforms and devices as we want. All of them should be here.
	- result_screenshots - folder with test results screenshots.
	- tests - currently we have just test_starcraft.py.
	- utils - all the helpers that we need would be located here.


Also, there is conftest.py where we have additional --platform option and starting point fixture for each test. Here we are starting our driver depending on the platform and closing after the test is finished

## Environment setup

To start the test you should have: 

`appium server 2.17.1` 

`android simulator` - I'm using Pixel 6 Pro with 36 Google Api's (you can add it through Android Studio. Please find how to do it in internet as there would be to big instruction file)

I assume that Python 3+ version are already installed.

Then open project in your IDE and write your emulator name in **platform_capabilities/android.json**

**"appium:deviceName": "Your device name"**

Open cmd and start appium server by next command:

```bash
  appium --allow-insecure chromedriver_autodownload --base-path /wd/hub
```

Also do not forgot to **start your simulator.**


Then run next commands from project root (twich_task)

```bash
  pip install -r requirements.txt
  pytest --platform=android
```

## Demo

Please see the demo of text running in starcraft.gif file 
https://github.com/texnichnyi/twitch_task/blob/main/starcraft.gif

Or download starcraft.webm and run the video locally
https://github.com/texnichnyi/twitch_task/blob/main/starcraft.webm
