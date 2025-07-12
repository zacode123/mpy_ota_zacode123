import network
import urequests
import os
import json
import machine
from time import sleep

class OTAUpdater:
    """OTA updater: auto-downloads & installs multiple files from GitHub based on version.json"""

    def __init__(self, ssid, password, base_url):
        self.ssid = ssid
        self.password = password
        self.base_url = base_url
        self.version_url = self.base_url + "version.json"

        if 'version.json' in os.listdir():
            with open('version.json') as f:
                self.current_version = int(json.load(f).get('version', 0))
        else:
            self.current_version = 0
            with open('version.json', 'w') as f:
                json.dump({'version': self.current_version}, f)

    def connect_wifi(self):
        sta_if = network.WLAN(network.STA_IF)
        if not sta_if.isconnected():
            print("Connecting to WiFi...", end="")
            sta_if.active(True)
            sta_if.connect(self.ssid, self.password)
            while not sta_if.isconnected():
                print(".", end="")
                sleep(0.3)
            print(f"\nConnected: {sta_if.ifconfig()[0]}")

    def check_for_updates(self):
        self.connect_wifi()
        print(f"Fetching version.json from {self.version_url}")
        try:
            response = urequests.get(self.version_url)
            data = response.json()
            self.latest_version = int(data.get("version", 0))
            self.files_to_update = data.get("files", [])
            print(f"Remote version: {self.latest_version}, Current version: {self.current_version}")
            return self.latest_version > self.current_version
        except Exception as e:
            print(f"Failed to check version: {e}")
            return False

    def download_and_save_file(self, filepath):
        url = self.base_url + filepath
        print(f"Downloading: {filepath} from {url}")
        try:
            response = urequests.get(url)
            if response.status_code == 200:
                # Create folders if needed
                folders = filepath.split('/')[:-1]
                path = ""
                for folder in folders:
                    path = path + "/" + folder if path else folder
                    if folder not in os.listdir(path[:path.rfind(folder)] or '/'):
                        try:
                            os.mkdir(path)
                        except:
                            pass
                # Write file
                with open(filepath, 'w') as f:
                    f.write(response.text)
                print(f"Updated: {filepath}")
            else:
                print(f"Failed to fetch {filepath}: status {response.status_code}")
        except Exception as e:
            print(f"Error downloading {filepath}: {e}")

    def update_all_files(self):
        for file in self.files_to_update:
            self.download_and_save_file(file)

        # Save new version
        with open('version.json', 'w') as f:
            json.dump({'version': self.latest_version}, f)

    def download_and_install_update_if_available(self):
        if self.check_for_updates():
            print("New version available. Updating...")
            self.update_all_files()
            print("Update completed. Restarting...")
            machine.reset()
        else:
            print("No updates found.")
