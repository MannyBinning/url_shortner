# UX
URL Shortner is an application designed to shorten any long URLs. Design of this application has been kept very simple and straight forward to make it easier for the user to navigate through the site and to focus on the main purpose of the site.
<p align="center">
  <img src="static/img/UX.jpg" alt="responsive" width="600"/>
</p>

# User Stories 
- To be able to shorten URLs.
- To be able to view a list of the URLs already shortened. 
### To meet the requirements:
- Iput box has been added for the user to submit the link
- Once submitted the short URL is provided. 
- List has been created for the user to view the other URLs in the Database. 

# Data Structure 
For this Project, MongoDB has been used to store the Data. The Data stored in this scenario is the original URL so the user can be redirected to it when page is loaded. New URL is stored in order for the the user to access the webpage using the url. Also, the unique letters for each URL are store in order to the stop the system to create a same URL for different websites. 

# Deployment 

To deploy [Shorten URLS](http://short-li.herokuapp.com/index) please follow the following steps: 

1. Getting Started: You will have to go on GitHub [repository](https://github.com/MannyBinning/shorten_url) and click on the "code" button:

2. Installing modules: Once loaded, inside the terminal install the modules required for this application using pip, -m and requirements.txt.

3. Setting up Database: Using [MongoDB](https://www.mongodb.com/), create a collections named, urls. 

4. Store the data: Create a file called env.py containing the following code:

    ```
    import os

    os.environ.setdefault("IP", "0.0.0.0")
    os.environ.setdefault("PORT", "5000")
    os.environ.setdefault("SECRET_KEY", "your_secret_key_here")
    os.environ.setdefault("MONGO_URI", "your_own_uri")
    os.environ.setdefault("MONGO_DBNAME", "your_own_file_name")

    ```

    All the above information can be collected from the Overview tab within the MongoDB cluster dashboard. Once clicked on Connect and then in the modal, click the Connect your application button, where the driver needs to be 'Python' and application code will be given. 

5. Confidentiality: As env.py contains sensible information it will be stored in .gitignore to prevent it from getting pushed to git hub. 

6. Ready: After the above steps are completed, you can now use python3 run.py to get the application running in your local browser. 

### Deployment to Heroku

To deploy [Shorten URLS](http://short-li.herokuapp.com/index) please follow the following steps: 

1. Heroku needs to be aware of the dependencies the application has and to achieve that, the requirements.txt file needs to be created containing the list of the dependencies. For this, the command pip3 freeze –local > requirements.txt can be used.

2. Heroku needs to know all the files that run the app and to ensure that Procfile needs to be installed. 

3. Login at [Heroku](https://dashboard.heroku.com/apps), create a new app. 

4. On the deploy screen, select GitHub in the deployment section and select your app from the options of your GitHub repositories. 

5. Within settings sections create config vars, these are the same as environment variables in env.py file. These are used here as they cant be found on the GitHub page so will need to be set up on Heroku to get the application working.

6. Automatic Deployment will need to be enabled on the settings page so that Heroku runs the most recent update. 

7. Finally, the master branch will need to be deployed and the link will be received to run the application.

# Technologies Used
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Flask](https://en.wikipedia.org/wiki/Flask_(web_framework))
- [Bootstrap4](https://getbootstrap.com/) was used to organise the content in a grid format.
- [MongoDB](https://www.mongodb.com/) was used for data storage. 
- [Heroku](https://dashboard.heroku.com/apps) / [GitHub](https://github.com/) for deployment. 
- [RandomKeyGen](https://randomkeygen.com/) to generate random keys. 
