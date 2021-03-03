# Rocket League Garage Trade Bumper
Rocket League Garage trade bumper using Python and Selenium <br>
I had a lot of trade posts on RL Garage so I wanted to bump my trades automatically instead of clicking bump in each post. This is the first time I am using Selenium.
For now you have to run the code every 15-20 minutes because I did not add a timer.  

## Usage
1. Make sure you have Python 3 installed.
2. Clone repository ```git clone https://github.com/beruz/rl_garage_autobumper``` <br>
If you want to download Chrome Driver on your own use this link: https://chromedriver.chromium.org/downloads
4. Using a text editor go to ```data(CHANGE THIS).json``` and change the email and password with your own information.
5. Rename the file ```data(CHANGE THIS).json``` to ```data.json```
6. Install dependencies 
```
cd to_repository_location
pip install -r requirements.txt
```
or if you are using Anaconda Navigator then from Anaconda Prompt  

```
cd to_repository_location
conda install --file requirements.txt 
```
## Future Work 
Add cooldown timer so code can run in the background and bumps the trades every 15 or any desired minute.

## Contribution
The code can be used for personal usage and comments/feedbacks are welcome!