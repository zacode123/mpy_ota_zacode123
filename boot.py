import os, machine
import gc
import webrepl
import PyModules.gemini_agent as agent
import Tools.ota_updater as ota
ota.auto_update()
webrepl.start()
agent.connectWIFI()
gc.collect()
