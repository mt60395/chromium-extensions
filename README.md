# chromium-extensions
## Description

Downloads the following Chrome Web Store extensions for Chromium:

- [uBlock Origin](https://clients2.google.com/service/update2/crx?response=redirect&prodversion=49.0&acceptformat=crx3&x=id%3Dcjpalhdlnbpafiamejdnhcphjbkeiagm%26installsource%3Dondemand%26uc)

- [HTTPS Everywhere](https://clients2.google.com/service/update2/crx?response=redirect&prodversion=49.0&acceptformat=crx3&x=id%3Dgcbommkclmclpchllfjekcdonpmejbdp%26installsource%3Dondemand%26uc)

- [Cookie Auto Delete](https://clients2.google.com/service/update2/crx?response=redirect&prodversion=49.0&acceptformat=crx3&x=id%3Dfhcgjolkccmbidfldomjliifgaodjagh%26installsource%3Dondemand%26uc)

- [History Auto Delete](https://clients2.google.com/service/update2/crx?response=redirect&prodversion=49.0&acceptformat=crx3&x=id%3Dbhfakmaiadhflpjloimlagikhodjiefj%26installsource%3Dondemand%26uc)

- [DuckDuckGo Privacy Essentials](https://clients2.google.com/service/update2/crx?response=redirect&prodversion=49.0&acceptformat=crx3&x=id%3Dbkdgflcldnnnapblkhphbgpggdiikppg%26installsource%3Dondemand%26uc)

- [Decentraleyes](https://clients2.google.com/service/update2/crx?response=redirect&prodversion=49.0&acceptformat=crx3&x=id%3Dldpochfccmkkmhdbclfhpagapcfdljkj%26installsource%3Dondemand%26uc)

## Notice
You can also access the links for each extension through the README.

## Installation
- Go to ```chrome://flags/#extension-mime-request-handling``` and enable "Always prompt for install" under "Handling of extension MIME type requests".
- This is to allow everything to install automatically; Chrome doesn't seem to have this flag. This script is still viable but you must install the extensions manually after everything is downloaded.
- Make sure you have Python installed. 
- Run chromium-extensions.py with Python.

## Cookie Auto Delete
Note that Cookie Auto Delete may be inconvenient for users that like to stay logged in to websites on their web browser, if you choose to enable the auto cleaning option.
