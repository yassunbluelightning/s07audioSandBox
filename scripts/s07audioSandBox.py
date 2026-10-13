#s07audioSandBox.py
import pj
import pjTkInter as tk
import pjSound as sound
from logStdErr import logStdErrClass
lse=logStdErrClass()
lse.setProjectName("s07audioSandBox")
lse.errToFile()
###
tk.stopTkTimer() ####Avoid influence from the OtherApp Which Uses Timer in the Same Project;YassunAdd;2025-1001;;
tk.updateMainLabel("s07audioSandBox")
tk.title("This shows how to play SoundEffects and BGM from SandBox.")
###
seSrcAbsPath=lse.bundleAppPath + \
"/PeterJohnAudios/pickup.mp3"
seDestAbsPath=lse.sandBoxProjDirPath + \
"/audios/pickup.mp3"
import os
import shutil
if os.path.isfile( seSrcAbsPath ) and not os.path.isfile( seDestAbsPath ):
  shutil.copy2( seSrcAbsPath, seDestAbsPath )
if os.path.isfile( seDestAbsPath ) :
  sound.playSoundEffects( seDestAbsPath )
####
bgmSrcAbsPath=lse.bundleAppPath + \
"/PeterJohnAudios/2014-0710-0332PM-YassunSnewYorkAdventure(just2seconds).mp3"
bgmDestAbsPath=lse.sandBoxProjDirPath + \
"/audios/2014-0710-0332PM-YassunSnewYorkAdventure(just2seconds).mp3"
if os.path.isfile( bgmSrcAbsPath ) and not os.path.isfile( bgmDestAbsPath ):
  shutil.copy2( bgmSrcAbsPath, bgmDestAbsPath )
if os.path.isfile( bgmDestAbsPath ) :
  sound.prepareBgm( bgmDestAbsPath )
sound.playBGM()
#sound.stopBGM()

##tk.bindKeyPressFunction("s07audioSandBox:s07audioSandBox.keyPress")

##tk.bindButtonFunction("s07audioSandBox:s07audioSandBox.button")

##tk.bindMotionFunction("s07audioSandBox:s07audioSandBox.motion")

##tk.bindMotionCanvasFunction("s07audioSandBox:s07audioSandBox.motionCanvas")

##tk.startTimerFunctionAfter("s07audioSandBox:s07audioSandBox.gameLoop", 0.2)
