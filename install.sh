#!/bin/bash

# آپدیت سیستم
sudo apt-get update -y
sudo apt-get upgrade -y

# نصب پایتون و پیش‌نیازها
sudo apt-get install python3-pip python3-dev git -y

# دانلود کدهای پنل از GitHub
git clone https://github.com/yourusername/SvM.git

# وارد پوشه پروژه
cd SvM

# نصب کتابخانه‌های پایتون
pip3 install -r requirements.txt

# اجرای پنل
python3 panel.py
