import os
import json

EXCLUDE_FILES = {
    "version.json",
    "Update_version.py"
}
EXCLUDE_DIRS = {
    ".git", ".github", "__pycache__"
}

def list_files(base_path="."):
    file_list = []
    for root, dirs, files in os.walk(base_path):
        # Exclude dirs
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for file in files:
            if file in EXCLUDE_FILES:
                continue
            path = os.path.join(root, file).replace("\\", "/")
            file_list.append(path.lstrip("./"))
    return sorted(file_list)

def get_current_version():
    try:
        with open("version.json") as f:
            return int(json.load(f).get("version", 0))
    except:
        return 0

def save_version_json(version, files):
    with open("version.json", "w") as f:
        json.dump({"version": version, "files": files}, f, indent=2)

def main():
    current_version = get_current_version()
    files = list_files()
    save_version_json(current_version + 1, files)
    print(f"✅ version.json updated to v{current_version + 1} with {len(files)} files")

if __name__ == "__main__":
    main()
