from Plugins.SystemPlugins.Hotplug.plugin import hotplugNotifier
from Components.Label import Label
from Components.ActionMap import ActionMap
from Components.MenuList import MenuList
from Components.FileList import FileList
from Components.Task import Task, Job, job_manager, Condition
from Components.Sources.StaticText import StaticText
from Components.SystemInfo import SystemInfo
from Screens.Console import Console
from Screens.MessageBox import MessageBox
from Screens.ChoiceBox import ChoiceBox
from Screens.Screen import Screen
from Screens.Console import Console
from Screens.HelpMenu import HelpableScreen
from Screens.TaskView import JobView
from Tools.Downloader import downloadWithProgress
from enigma import fbClass
import urllib2
import os
import shutil
import math
from boxbranding import getBoxType,  getImageDistro, getMachineName, getMachineBrand, getImageVersion, getMachineKernelFile, getMachineRootFile
distro =  getImageDistro()
ImageVersion = getImageVersion()
ROOTFSBIN = getMachineRootFile()
KERNELBIN = getMachineKernelFile()

#############################################################################################################
image = 0 # 0=openATV / 1=openMips
if distro.lower() == "openmips":
	image = 1
elif distro.lower() == "openatv":
	image = 0
feedurl_atv = 'http://images.mynonpublic.com/openatv/%s' %ImageVersion

if ImageVersion == '5.3':
	ImageVersion2= '5.4'
else:
	ImageVersion2= '5.3'
feedurl_atv2= 'http://images.mynonpublic.com/openatv/%s' %ImageVersion2
feedurl_om = 'http://image.openmips.com/5.3'
imagePath = '/media/hdd/images'
flashPath = '/media/hdd/images/flash'
flashTmp = '/media/hdd/images/tmp'
ofgwritePath = '/usr/bin/ofgwrite'
#############################################################################################################


