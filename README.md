# Instagram Followers List

A Python script that extracts the Instagram followers and following lists from a given username.


## Warning

For security reasons, make sure that your Instagram account is already set up with the 2FA (two-factor authentication), otherwise, this script won't be useful.


## ChromeDriver

Make sure to download the correct webdriver for your Operating System and Google Chrome version. Select which one is appropriate for your environment from the Google official repository, download the ZIP file, extract it and save the ChromeDrive file into `tools` folder.
Then, run the commands listed in the `Preparing the Environment` section.

## Preparing the Environment

- ### GNU/LINUX (Terminal)

    - `$ virtualenv env -p python3`
    - `$ source env/bin/activate`
    - `(env) $ pip install -r requirements.txt`

- ### MS Windows (PowerShell)

    - `PS > py -m venv env`
    - `PS > .\env\Script\activate`
    - `(env) PS > py -m pip install --upgrade pip` (Optional)
    - `(env) PS > py -m pip install -r  requirements.txt`


## Running the Script

- ### GNU/LINUX (Terminal)
    - `(env) $ python3.7 main.py`

- ### MS Windows (PowerShell)
    - `(env) PS > py .\main`
