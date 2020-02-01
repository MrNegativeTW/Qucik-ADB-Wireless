<div align="center">

# Quick ADB Wireless

**A simple python script let you connect/disconnect adb over WiFi.**

![](https://img.shields.io/badge/Platform-macOS-important)
![](https://img.shields.io/badge/Python-3.5%20Above-success)
![](https://img.shields.io/badge/License-GNU%20GPLv3-blue)<br>

</div>

## Demo

**Connect**<br>
![](https://raw.githubusercontent.com/MrNegativeTW/Qucik-ADB-Wireless/master/Demo_Pics/Demo_Connect.gif)
**Disconnect**
![](https://raw.githubusercontent.com/MrNegativeTW/Qucik-ADB-Wireless/master/Demo_Pics/Demo_Disconnect.gif)


## Getting Started
### Prerequisites
- macOS<br>
- Python 3.5 and above<br>
- ADB installed (Usually comes w/ Android Stduio)<br>

### Installation
1. Add ADB path to bash profile.
```
echo 'export ANDROID_HOME=/Users/$USER/Library/Android/sdk' >> ~/.bash_profile

echo 'export PATH=${PATH}:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools' >> ~/.bash_profile

source ~/.bash_profile
```
2. Clone/Download project.

## Usage
1. cd to project folder
2. Run `python3 WADB.py` in terminal

## License
GNU GPLv3
