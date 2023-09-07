# Instagram Followers List

A Python script that extracts the Instagram followers and following lists from a given username.


## Warning: Project Out-of-Date

This code hasn't been working since Meta updated the Instagram interface for desktop systems (last quarter of 2022). You can find further information by [clicking here](https://github.com/marcelnishihara/instagram-followers-list/issues/1#issue-1573126008).  
Please check the [repository Issue page](https://github.com/marcelnishihara/instagram-followers-list/issues) before forking this project.


## Warning: 2FA (Two-factor Authentication)

For security reasons, ensure that your Instagram account is already set up with the 2FA (two-factor authentication), otherwise, this script won't be useful.


## ChromeDriver

Make sure to download the correct webdriver for your Operating System and Google Chrome version. Select the one that is appropriate for your environment from the [official Google repository](https://chromedriver.chromium.org/downloads), download the ZIP file, extract it, and save the ChromeDriver file into the `tools` folder. Afterward, run the commands listed in the `Preparing the Environment` section.


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
