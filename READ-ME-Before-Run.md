# screenshot.py
create your first screenshot application for windows in python within less than 5 minutes

![screenshot](https://user-images.githubusercontent.com/47782249/79207679-a34d5000-7e5e-11ea-982d-d13f3d21f506.png)

**How to Take a Screenshot using Python ?** 

_You may use the following template to take a screenshot using Python:_

import pyautogui

myScreenshot = pyautogui.screenshot()
myScreenshot.save(r'Path to save screenshot\file name.png')

In the next section, I’ll show you the complete steps to take a screenshot using Python. I’ll also include the code to create a GUI to take screenshots:

GUI to take Screenshots

- Steps to Take a Screenshot using Python

- Step 1: Install the pyautogui package

To start, you’ll need to install the pyautogui package using the following command (under Windows):

- pip install pyautogui

You may check this guide for the instructions to install a package using pip for Windows users.

- Step 2: Capture the path to save the screenshot

Next, capture the full path where the screenshot will be saved on your computer.

In my case, I decided to save the screenshot under the following path:

C:\Users\BJ\Desktop\Test\screenshot1.png

Here, the file name is screenshot1, while the file type is png (alternatively, you can set the file type to jpg).

Step 3: Take the screenshot using Python
For the final step, you’ll need to use the template below in order to take the screenshot using Python:

import pyautogui

myScreenshot = pyautogui.screenshot()
myScreenshot.save(r'Path to save screenshot\file name.png')
For our example, I applied the following code to take the screenshot (note that you’ll need to change the path to reflect the location where the screenshot will be saved on your computer):

import pyautogui

myScreenshot = pyautogui.screenshot()
myScreenshot.save(r'C:\Users\BJ\Desktop\Test\screenshot1.png')
Run the code in Python (adjusted to your path), and the screenshot will saved at your specified location.


![logo-python-png-6](https://user-images.githubusercontent.com/47782249/79207188-025e9500-7e5e-11ea-9f9a-5b235452882f.png)
