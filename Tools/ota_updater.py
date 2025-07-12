from PyModules.ota import OTAUpdater
from Config.config import STA_SSID, STA_PASS, GIT_URL

ota_updater = OTAUpdater(STA_SSID, STA_PASS, GIT_URL)

def auto_update():
  ota_updater.download_and_install_update_if_available()
