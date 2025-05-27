# eBird recent hotspot observations

### Introduction

This script uses your eBird API key and the location code for a specific hotspot to display a list of recent observations.

The output is nicely formatted to include total species count, total count for today, total count prior to today, and checklist timestamps.

To make the app work for your hotspot of choice, you'll need to edit the constants `EBIRD_LOCATION` and `EBIRD_LOCATION_NAME` in the file `main.py`. See comments in that file for help finding the location code for your favorite hotspot.

### macOS menu bar

The script's output can easily be turned into a macOS menu bar icon using [Platypus](https://sveinbjorn.org/platypus). This allows you to quickly check live, recent observations for your favorite hotspot straight from the menu bar. See detailed instructions for creating the macOS app underneath the screenshot below.

### Screenshot

<img width="1000" alt="desktop-screenshot-smaller" src="https://github.com/user-attachments/assets/bc7223ab-afce-403a-99ed-0b6955a484b0" />

### Creating the macOS menu bar app

Follow these instructions to create the menu bar app. Feel free to reach out if you need help.

#### 1. Create a virtual environment with the required Python packages

1. Make sure you have cloned or downloaded the repo on your machine
2. Open the Terminal application, then navigate to the repo folder
3. Execute these commands in the repo folder to create a virtual environment with the required Python packages
```
python -m venv .venv
source .venv/bin/activate
pip install requests keyring
```
4. (Optional) Check to make sure the packages have been installed
```
pip list
```

#### 2. Download and install Platypus

5. Download and install [Platypus](https://sveinbjorn.org/platypus), developed by Sveinbjorn Thordarson
6. Open Platypus

#### 3. Create the macOS menu bar app using Platypus

7. Choose an `App Name` (for instance, "eBird BYT")
8. Under Script Path, click button `Select Script`
9. Navigate to and select the file "main.py" in the repo folder on your machine
10. Copy the information you now see for `Script Path` and paste it into the empty box next to `Script Type`
11. At the end of the string, remove "main.py" and replace it with ".venv/bin/python"
12. In the dropdown menu for `Interface`, select "Stats Menu"
13. Click on `Status Item Settings` (also in the `Interface` section)
14. Set `Status Item` to "Icon"
15. Next to the icon, click `Select`
16. Select the file "feather.svg" in the repo folder
17. Click `Apply`
18. Click `Create App`

Below is just an example of what the relevant information looks like on my machine. You will need to fill out different information, specific to your machine.

![image](https://github.com/user-attachments/assets/705062e4-295a-4d38-84be-2f9043835a9d)

You can now open the app and should see the feather icon appear in your menu bar.

Make sure to add your eBird API Key as a password item in your macOS Keychain (using the Keychain Access app).
