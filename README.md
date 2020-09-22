# chromium-extensions
## Description

Downloads the following Chrome Web Store extensions for Chromium:

- uBlock Origin

- HTTPS Everywhere

- Cookie Auto Delete

- History Auto Delete

- DuckDuckGo Privacy Essentials

- Decentraleyes

## Notice
Windows may require you to register browsers for the webbrowser module. You may modify the Python script to remove 'chromium' from webbrowser.get() to use the default web browser; this means you must set Chromium as your default web browser.

## Installation
- Go to ```chrome://flags/#extension-mime-request-handling``` and enable "Always prompt for install" under "Handling of extension MIME type requests".
- This is to allow everything to install automatically; Chrome doesn't seem to have this flag. This script is still viable but you must install the extensions manually after everything is downloaded.
- Make sure you have Python installed. 
- Run chromium-extensions.py with Python.

## Cookie Auto Delete
Note that Cookie Auto Delete may be inconvenient for users that like to stay logged in to websites on their web browser, if you choose to enable the auto cleaning option.
