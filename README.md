# Instagram Followers List

A Python script that extracts the Instagram followers and following lists from a given username.


## Warning: Project Out-of-Date

This project doesn't work anymore since Meta updated the Instagram interface for desktop systems (last quarter of 2022).  
You can reach further information [clicking here](https://github.com/marcelnishihara/instagram-followers-list/issues/1#issue-1573126008).  
I'm going to work on this as soon as possible.


## Setting the Username and Password

Insert into the `tools/credentials.py` file the username and password of the Instagram account you want to extract the list of following and followers, just like the example below:

```py
credentials = {
    'username' : 'brucewayne',
    'password' : 'selinakyle1940'
}
```

## ChromeDriver

Make sure to download the correct webdriver for your Operating System and Google Chrome version. Select which one is appropriate for your environment from the Google official repository, download the ZIP file, extract it and save the ChromeDrive file into `tools` folder.

Then, run the commands listed in the `Preparing the Environment` section.

## Preparing the Environment

- `$ virtualenv env -p python3`
- `$ source env/bin/activate`
- `(env) $ pip install -r requirements.txt`

## Running the Script

- `(env) $ time python3.7 main.py`

## Result File

After successfully ran the script, you're going to see a JSON file in the root folder of this project containing an object with your following and followers list.

The name of this JSON file will look like `brucewayne_1991_8_5_19h30min00s.json`, which is the Instagram username, date and time of the script execution.

Its content will be something like the following example:

```js
{
    "following" : [
        "oswaldcobblepot",
        "introduce_me_as_joker",
        "selinakyle",
        "ras_al_ghul",
        "eddy.nigma"
    ],
    "followers" : [
        "selinakyle",
        "alfred.pennyworth",
        "dick.grayson"
        "commr_james_gordon"
    ]
}
```
