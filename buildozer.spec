[app]
title = Beyond 9
package.name = beyond9
package.domain = org.reality

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0.0

requirements = python3,kivy,pillow,android,pyjnius

orientation = portrait
fullscreen = 0

android.permissions = CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,RECORD_AUDIO,INTERNET,ACCESS_NETWORK_STATE

android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a,armeabi-v7a

p4a.bootstrap = sdl2
android.gradle_dependencies = androidx.appcompat:appcompat:1.3.1

icon.filename = icon.png
presplash.filename = presplash.png

[buildozer]
log_level = 2
warn_on_root = 1
