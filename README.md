# SP_Dogbreeds

First clone this project to your local desktop.

After that use anaconda navigator and install all dependencies from the requirements.txt.

Then (very important) run the dog_breeds_analysis.ipynb to download the data from kaggle and save them in the sql database.

At last, run docker and the command "docker build -t spdogbreeds:0.0.1 ." in your terminal. 
If there was no problem run "docker run -p 5000:5000 spdogbreeds:0.0.1" to start the flask web application.