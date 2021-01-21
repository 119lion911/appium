# **Appium**
## *Introduction*
<font size=2>
Appium為實現一套適用於移動端的WebDriver協議，基本上使用Appium時用的還是依賴於Selenium，和Web自動化測試的主要區別就在Driver不一樣。
ex:
如果用Selenium自動化測試Google Chrome，就需要一個ChromeDriver。如果要測試ID，就需要一個IEDriver。 <br>
如果要自動化測試Android，就只需要Appium，Appium就等於Driver的角色。Appium實現了一套標準的WebDriver。 \
只需要操作Appium，Appium會告訴裝置該做甚麼。這裡的裝置可以是iOS或者Android，甚至是Windows Phone 和Firefox OS。
</font><br>
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

---
## *start test*
#### 1. start android emulator
#### 2. cmd: appium
#### 3. execute AppData\Local\Android\Sdk\tools\bin\uiautomatorviewer.bat to find emulator element for test
#### 4. execute python script...
