# **Appium**
---
## *environment set up*
#### 1. install java 8: jdk1.8.0_281, jre1.8.0_281 \
add the system environment variables: \
JAVA_HOME: C:\Program Files\Java\jdk1.8.0_281 \
Path: %JAVA_HOME%\bin \
(cause java 9 & 10 do not support the uiautomatorviewer of android)
#### 2. install android studio \
add the system environment variables: \
ANDROID_HOME: C:\Users\xxxx\AppData\Local\Android\Sdk \
Path: %ANDROID_HOME%\tools \
Path: %ANDROID_HOME%\platform-tools
#### 3. install node.js
#### 4. install appium with node.js
cmd: npm install -g appium \ 
or \ 
cmd: npm --registry http://registry.cnpmjs.org install -g  appium
#### 5. install python
#### 6. pip install Appium-Python-Client

## *start test*
#### 1. start android emulator
#### 2. cmd: appium
#### 3. execute AppData\Local\Android\Sdk\tools\bin\uiautomatorviewer.bat to find emulator element for test
#### 4. execute python script...
