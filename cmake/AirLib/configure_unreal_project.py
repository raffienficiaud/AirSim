import sys
import json
import datetime
from pathlib import Path


def run():
    destination = Path(sys.argv[1])
    if not destination.exists():
        raise RuntimeError(f"Unreal project folder {destination.absolute()} does not exist")

    projects_in_folder = list(destination.glob("*.uproject"))
    if len(projects_in_folder) != 1:
        raise RuntimeError(f"Unreal project folder {destination.absolute()} contains no Unreal project (or too many) " + str(projects_in_folder))

    with projects_in_folder[0].open() as f:
        content = json.load(f)

    print(content)
    content_original = content.copy()

    if "AdditionalDependencies" not in content:
        content["AdditionalDependencies"] = []

    if "AirSim" not in content["AdditionalDependencies"]:
        content["AdditionalDependencies"] = ["AirSim"]

    if "Plugins" not in content:
        content["Plugins"] = []

    for plugin in content["Plugins"]:
        if plugin["Name"] == "AirSim":
            plugin["Enabled"] = "true"
            break
    else:
        content["Plugins"] += [{"Name": "AirSim", "Enabled": True}]

    if content != content_original:
        projects_in_folder[0].rename(
            projects_in_folder[0].with_name(
                projects_in_folder[0].name + f".bck{datetime.datetime.now().isoformat()}"))

        with projects_in_folder[0].open("w") as f:
            json.dump(content,  f, indent=4)

        print("New project saved")


if __name__ == "__main__":
    run()
