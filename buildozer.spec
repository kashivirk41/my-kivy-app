[app]

# (str) Title of your application
title = My Kivy App

# (str) Package name
package.name = mykivyapp

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source files where the let of data is (relative to directory of spec)
source.dir = .

# (list) Source files to include (let of extensions)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
# यहाँ हमने kivy का बिल्कुल स्टेबल और टेस्टेड वर्जन 2.2.1 फिक्स कर दिया है ताकि pip कोई ढूंढने में गलती न करे
requirements = python3,kivy==2.2.1

# (list) Permissions
android.permissions = INTERNET

# Target API and NDK configuration to prevent errors
android.api = 33
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# लाइसेंस को पक्का स्वीकार करने के लिए
android.accept_sdk_license = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
