import webbrowser
c = webbrowser.get('chromium')

def get(extension):
	c.open("https://clients2.google.com/service/update2/crx?response=redirect&prodversion=49.0&acceptformat=crx3&x=id%3D" + extension + "%26installsource%3Dondemand%26uc")

extensions = [
        'cjpalhdlnbpafiamejdnhcphjbkeiagm',  # uBlock Origin
        'gcbommkclmclpchllfjekcdonpmejbdp',  # HTTPS Everywhere
        'fhcgjolkccmbidfldomjliifgaodjagh',  # Cookie Auto Delete
        'bhfakmaiadhflpjloimlagikhodjiefj',  # History Auto Delete
        'bkdgflcldnnnapblkhphbgpggdiikppg',  # DDG Privacy Essentials
        'ldpochfccmkkmhdbclfhpagapcfdljkj'   # Decentraleyes
]

if __name__ == "__main__":
        for ext in extensions:
                get(ext)
