#@title <-- Install ngrok
TOKEN = "Your ngrok token here"

def install_ngrok():
    import os
    from zipfile import ZipFile
    from urllib.request import urlretrieve
    
    url = 'https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip'
    urlretrieve(url, 'ngrok-amd64.zip')
    
    with ZipFile('ngrok-amd64.zip', 'r') as zip_ref:
        zip_ref.extractall('/usr/local/bin/')
    os.chmod('/usr/local/bin/ngrok', 0o755)
    os.unlink('ngrok-amd64.zip')

install_ngrok()
if TOKEN != "":
    !ngrok authtoken $TOKEN
