# Welcome to the Linux Video Conferencing Audio Tools

This repository provides a collection of tools that help with your audio set-up
when tele- or video conferencing on Linux.

# Dependencies

The following dependencies need to be installed to be able to use these scripts:

## Debian / Ubuntu packages:

The following packages need to be installed on your system:

* Pulse audio

To install:

```
sudo apt install pulseaudio
```

## Python Package Index packages:

The scripts depend on the following PIP packages being installed on your system:

* pick
* pulsectl
* setuptools

To install:

```
pip3 install --upgrade pick pulsectl setuptools
```

# Included tools

## `create-combined-source.py`

Helps you create a virtual audio source that combines a number of other audio
sources. This is very useful when you would like to share your desktop audio in
addition to your mic with teleconferencing software that does not support it
on Linux.

How to use:

1. On the command-line, run:
   ```
   ./create-combined-source.py
   ```
1. You will be presented with a list of audio sources. Select a number of them
   with the spacebar and arrow keys. Once you are happy with the selection, press
   'Enter'.
1. A virtual audio source named `VirtualCombinedAudioSource` will be created that
   you can connect to your video conferencing software with the Pulse Audio Volume
   Control.

To remove the virtual audio source, run the script a second time, but do not select
any audio sources.
