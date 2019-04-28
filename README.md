# Collective Intelligence Final Project

## Project Description

This project was built by Mark Coretsopoulos, Andy Han, and Jeremy Krovitz as part of their Collective Intelligence (COMP 440) final course project at Macalester College during the spring 2019 semester.

Perform sentiment analysis on streamed tweets about movies before they are released in theater, and see whether if there is a correlation between sentiment and opening weekend performance. For example, does a strong prevalence of positive tweets indicate a financially successful performance in the opening theater? Or, does a more mixed reaction to a movie’s release indicate something else different entirely? Also, how does a movie’s reception on twitter match up to both critical and audience reviews on review aggregate sites such as Rotten Tomatoes and Metacritic?

The project will curate and collect an original dataset of tweets about movies that will be released between March 29, 2019 and April 19, 2019. We will also look at literature about sentiment analysis of tweets about films to serve as the research foundation for our project.

## Movies Analyzed
• Week 1 (3/29) - Dumbo

• Week 2 (4/5) - Shazam, Pet Sematary, The Haunting of Sharon Tate, Best of Enemies

• Week 3 ( 4/12) - Hellboy, Missing Link

• Week 4 (4/19) - The Curse of La Llorona, Breakthrough, Little Woods

##Before Installation:

1. Sign up for an Amazon AWS account: [aws.amazon.com](aws.amazon.com)
2. Once signed up, login and click on your username.
3. In the dropdown menu click on **My Security Credentials.**
4. Click on **Access keys (access key ID and secret access key)** to expand.
5. Click **Create Access Key**.
6. Click the **Download Key File** button in the popup that appears. Keep your key file in a safe place, and remmber where you store it, as you will need it later.

## Install
1. Download this repository to your computer and unzip the folder.

2. Download Anaconda 3 through this link: [https://www.anaconda.com/distribution/#download-section](https://www.anaconda.com/distribution/#download-section)

3. If you need assistance installing Anaconda:

    Directions for Mac OS X: [https://www.datacamp.com/community/tutorials/installing-anaconda-mac-os-x](https://www.datacamp.com/community/tutorials/installing-anaconda-mac-os-x)

    Directions for Windows: [https://www.datacamp.com/community/tutorials/installing-anaconda-windows](https://www.datacamp.com/community/tutorials/installing-anaconda-windows)

4. After Anaconda 3 is installed successfully, open your terminal if you are using a Mac or your Anaconda prompt if you are using a PC.

5. Type in **cd**, drag the repository folder into the terminal window / Anaconda Prompt window, and press [Enter].

6. Type **conda env create -f awsEnv.yml**.

7. Type **conda activate awsenv**.

8. An internet browser tab should open up with an iPython Notebook. If a browser tab does not popup, open an internet browser window and type [http://localhost:8888/](http://localhost:8888) into the address bar.

9. When the window loads, if the file 'readingInMovieTweets.ipynb' is not open, it should be displayed in the panel on the left. Click on it. If the file is already open, procede to step 11.

10. Fill in your 'access key ID' and 'secret access key' where specified.

11. Click **Run All Cells** to see the code output.

12. When you are done running code, click **File** and select **Quit**.

13. A quit confirmation message will popup. Click **Quit** to confirm.

14. You can then close the tab.

15. Back in the terminal window, type in **conda deactivate**, which will deactivate the conda environment.
