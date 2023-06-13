# **BarBelles**
## **API Overview**

The BarBelles API has been developed using the Django Rest Framework in order to serve as the back-end component to Barbelles, an online fitness community for women. The front-end, developed using React, provides women with a safe and inclusive space to share their own personal fitness journeys as well as the opportunity to learn and interact with other in the community. Users can read posts by others, create, update and delete their own posts as well as follow other users. There is also the facility to add, edit or delete comments. Users can learn from video Tutorials added by the site owner, Kate Ross. The BarBelles API provides the functionality for all of these interactions, connecting to an external Postgresql database to store images, profile data, videos, comments and followers.

The entire basis of this project is to facilitate a smooth, seamless user experience on the front-end.

<hr>

![Screenshot of BarBelles API](docs/images/api-home.png)

The deployed API can be found [here](https://barbelles-api.herokuapp.com/).

<hr>

## Table of contents:
1. [**Site Overview**](#site-overview)
1. [**Planning stage**](#planning-stage)
    * [**Strategy**](#strategy)
      * [***Site Aims***](#site-aims)
      * [***Target Audiences***](#target-audiences)
      * [***User Stories***](#user-stories)
    * [***Wireframes***](#wireframes)
    * [***Database Schema***](#database-schema)
    * [***Colour Scheme***](#color-scheme)
    * [***Typography***](#typography)
1. [**Agile Development**](#agile-development)
1. [**Features**](#features)
    * [***Admin Page***](#admin-page)
    * [***Posts***](#posts)
    * [***Tutorials***](#tutorials)
    * [***Comments and tutorial comments***](#comments-and-tutorial-comments)
    * [***Likes and favourites***](#likes-and-favourites)
    * [***Followers***](#followers)
    * [***Defensive Design***](#defensive-design)
    * [***User Authentication***](#user-authentication)
    * [***404 Page***](#404-page)
1. [**Future-Enhancements**](#future-enhancements)
1. [**Testing Phase**](#testing-phase)
1. [**Deployment**](#deployment)
1. [**Software and Tech**](#software-and-tech)
1. [**Media**](#media)
1. [**Credits**](#credits)
1. [**Honourable mentions**](#honorable-mentions)

<hr>

## **Planning Stage**

### **API Aims:**

* Provide the back-end component to a front-end site developed with React.js.
* To assist the user in registering, logging in and logging out on the front-end.
* To provide front-end users with CRUD (create, read, update and delete) functionality for posts found on the site.
* To allow users on the front-end to create, edit and delete their own comments and delete their own.
* To facilitate the functionality for front-end users to follow or un-follow other users in the community.
* To give regular users the opportunity to view tutorials added to the site.
* To allow only the site owner to add, edit or remove tutorials from the front-end.
* To allow for greater community interaction by giving users the opportunity to like or un-like posts.
* Provide filtered content for the front-end user based on whether they follow a user or have liked or favourited tutorials.
* Enhance the user experience integrated search function for those trying to find a specific user or post.
* Offer users the opportunity to provide more information about themselves by adding to their user profile. 

<hr>


### **User Stories:**

#### **Site User**
As a **Registered** user I can: 
* *sign in* in order to *view site content and interact with the community*.
* *navigate the site* easily in order to *view its content and interact with others*.
* *view posts by other users* in order to *take inspiration from the community*.
* *create a post* in order to *share my fitness journey with the community*.
* *update or delete a post* in order to *make changes to my own content or keep my contributions relevant*.
* *comment on other users' posts* in order to *share my opinions and interact with the community*.
* *update comments I make on posts or tutorials* in order to *contribute to, and interact with the community*.
* *upload a profile picture or bio* in order to *tell people a little more about myself*.
* *edit or update my profile* in order to *keep my account up to date*.
* *like or unlike a post* in order to *show my appreciation for other users' contributions*.
* *easily logout* in order to *end my session on the site*.
* *view tutorials* in order to *learn from content added by the site owner*.
* *follow or un-follow other users* so their *posts are added to my feed*.


As an **Unregistered** User I can:
* *sign up* in order to *view site content and interact with the community*.


#### **Site Admin**
As a **Site Admin** I can: 
* *add tutorials in the form of youTube videos* in order to *motivate and educate those in the community*.
* *edit or delete tutorials* in order to *correct mistakes or keep content relevant*.
* *view popular profiles within the community* in order to *see who is the most popular*.
* *respond to questions posted in comments* in order to *interact with and educate the community*.

<hr>

### **Wireframes**

No wireframes were required for the API. Wireframes for the front-end site can be found in the Readme.md file for that project.


<hr>

### **Database Schema**

I used [DrawSQL](https://drawsql.app)​ to help visualise my database tables. See the image below:

![Database Schema](docs/schema/barbelles-api-erd.png)

<hr>

### **Colour Scheme:**
​
No color scheme was required for this project. The color scheme for the front-end can be found in the Readme file for that project.

<hr>​

#### **Typography**
​
Typography was not required for this project. The typography for the front-end can be found in the Readme file for that project.

​<hr>

## Agile Development

I used Github projects to create and track issues and User Stories. The Agile processes and methodologies can be viewed [here](/AGILE.md)

<br>
<hr>
<br>

# **Features**

## **API Navigation**

Navigation of the API is chiefly through typed urls. The available pages are listed below.

### **Admin Page**

The Admin page was setup almost immediately after creating a superuser in the terminal. This was crucial as it provided an initial means of adding test data and users to the project. Due to the fact I had to wipe my database, I was advised to remove the SQLite3 DB and connect solely to my Postgres database. The screenshot below shows the admin page populated with the most current data at the time of writing.

![Screenshot of admin page](docs/images/api-admin.png)


<hr>

### **Posts**
​
The post list page shows a list of all posts added either in the admin panel or from the front end:

![Screenshot of posts list](docs/images/api-posts.png)

It is also possible to view the detail of each individual post:

![Screenshot of post detail](docs/images/api-post-detail.png)

Posts can be edited, updated or deleted on the front-end or via the admin panel.


<hr>

### **Tutorials**

The tutorial list page shows tutorials uploaded by the site owner or users designated as staff on the backend. The field 'is_staff' in the Profile model can be accessed on the front end, so users for whom 'is_staff' is true, are able to access the 'Share tutorial' link in the front-end navbar.

![Tutorials list](docs/images/api-tutorials.png)

The tutorial detail page shows the details of each individual tutorial uploaded:

![Tutorial detail page](docs/images/api-tutorial-detail.png)

Tutorials can be edited, updated or deleted on the front-end or via the admin panel only by specific users.


<hr>

### **Comments and tutorial comments**

Users can add comments to both posts and tutorials. Comments are added to posts and tutorial comments are added to tutorials. On the front-end, these are added on the post or tutorial detail page. Lists of each can be seen in the screenshots below:

![Screenshot of comments list](docs/images/api-comments.png)
![Screenshot of tutorial comments list](docs/images/api-tutorial-comments.png)

Details of both individual comments and tutorial comments can be viewed. See below:

![Screenshot of comment detail page](docs/images/api-comment-detail.png)
![Screenshot of tutorial comment detail page](docs/images/api-tutorial-comment-detail.png)

Users can create, edit or delete their own comments on the front-end.


### **Likes and favourites**

Likes and favourites are similar in terms of functionality; likes can be added to posts so a user can like or unlike a post on the front end. A filter allows for liked posts to be accessed through a link in the NavBar. Tutorials can be 'favourited' or 'unfavourited' and can also be accessed on the front-end through the favourites link in the navbar. On the back-end, lists of both are rendered as below:

![Screenshot of likes list](docs/images/api-likes.png)
![Screenshot of favourites list](docs/images/api-favourites.png)

Details of each individual like or favourite can be seen in the screenshots below:

![Screenshot of likes detail](docs/images/api-like-detail.png)
![Screenshot of favourites detail](docs/images/api-favourites-detail.png)


<hr>

### **Followers**

The API provides the functionality for users on the front-end to follow or un-follow each other. Effectively a follow is created for a 'follow' and destroyed for an 'un-follow'. Each follow can be viewed on the back-end as below:

![Screenshot of followers list](docs/images/api-followers.png)

The detail of each follow can be viewed in more detail by adding its id to the URL and is rendered as below:

![Screenshot of follow detail](docs/images/api-follower-detail.png)


<hr>

## **Defensive Design**
### **Permissions**

Permission checks are run through the use of the IsAuthenticated class which will grant or deny access to different parts of the API. In the case of this API, it essentially means users cannot edit or delete posts, comments, tutorials, likes or followers that are not their own. This adds a fairly robust level of security and will return a '401 Unauthorized' or '403 Forbidden' response.

The impact on the front-end is such that users with malicious intent will not be able to access content which they shouldn't.

![Screenshot of delete page](docs/images/delete-book.png)


<hr>

### User Authentication

All pages feature User Authentication meaning that a User must be logged in to view all site content. This encourages Users to signup as well as preventing malicious attempts to edit or delete content. If a user knows or guesses a correct URL without being logged in they will encounter this screen:

![Screenshot of authentication](docs/images/user-authentication.png)


<hr>

### **404 Page**

A custom 404 page was added to catch instances when the User may have mis-typed a URL, or if content has been removed from the site. The 404 page features text displaying the content is not available and features a back button:

![Screenshot of 404 page](docs/images/404.png)


<hr>

### **500 Page**

A custom 500 page was added to catch instances when a potentially malicious User might try to subvert the site, for example to access personal data or delete content. In this case the page below displays and features a back button to redirect them to the previous page:

![Screenshot of 500 page](docs/images/500-page.png)


<hr>

## **Future-Enhancements**
​
There are a number of areas with scope for future improvement. This project has been very challenging and ultimately the project deadline was looming. There is potential to add the following:
​
* Adding movies and games to fit into a 'Categories' drop-down menu.
* The option for Users to add to the Authors section.
* User images to be added to comments and book reviews.
* A community page for User who opt in to have their profiles displayed publicly.
* The search function to be updated to display results in the new categories.
* Using the Google Books API to retrieve book information. I did explore this option before the inception of the project but decided against including it due to time constraints.

<hr>

## User Authentication

All pages feature User Authentication meaning that a User must be logged in to view all site content. This encourages Users to signup as well as preventing malicious attempts to edit or delete content. If a user knows or guesses a correct URL without being logged in they will encounter this screen:

[Screenshot of authentication](docs/images/user-authentication.png)

<hr>

## **Testing Phase**

The testing process, along with bugs, can be viewed [here](/TESTING.md)​

<hr>

## **Deployment**

The Deployment was a fairly lengthy process so I have detailed it in a separate file. It can be found [here](/DEPLOYMENT.md)

The final deployment can be viewed [here](https://sci-fi-portal.herokuapp.com/)

<hr>

## **Software and Tech**

The following software and tech was used:

- [BootStrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/) to provide key components such as the navbar and cards.
- [Cloudinary](https://cloudinary.com) to handle static images and files as well as to offer the User a front end method of uploading images.
- CSS to provide custom styling in addition to Bootstrap.
- [Django](https://www.djangoproject.com/) as a Python framework to develop the project.
- [Django all auth](https://django-allauth.readthedocs.io/en/latest/) used to handle user authentication.
- [DrawSQL](https://drawsql.app/) to develop the logic for the project.
- [ElephantSQL](https://www.elephantsql.com/) to handle the PostgreSQL database.
- [Figma](https://www.figma.com/) to assist with the planning phase of the project.
- [Font Awesome](https://fontawesome.com/) to provide search, heart, profile, social media icons etc.
- Git (Gitpod and Github) as my version control for the site.
- [Gitpod](https://gitpod.io/) and VS Code to create, load and push my code to Github.
- [Heroku](https://www.heroku.com/) to deploy the project.
- HTML - The base language to create templates for the site
- JavaScript - only used twice: for the back or cancel buttons and to populate the hidden created_by field in the add_book form.
- [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) used to implement logic from views.py and models.py.
- Microsoft Excel to develop the logic for the project.
- [Optimizilla](https://imagecompressor.com/) to compress background images for the site.
- Python - Installed packages can be found in the requirements.txt file.
- [Shutterstock](https://www.shutterstock.com/) to source the background images for the site.
- [Summernote](https://summernote.org/) to provide a WYSIWYG text editor in the admin area.

<hr>

## **Media**

* All book images are from [Amazon UK](https://www.amazon.co.uk/)
* All background images came from a free trial subscription to [Shutterstock](https://www.shutterstock.com/)
* All author images and bios are from [Wikipedia](https://www.wikipedia.org/) other than:
  * N.K. Jemisin: bio and image from [author website](https://nkjemisin.com/)
  * Adrian Tchaikovsky: bio taken from [author website](https://adriantchaikovsky.com/)
​
<hr>

## **Credits**

* The colour palette for the project is from [Pinterest](https://www.pinterest.co.uk/pin/204491639320145500/).

* The idea to use Cloudinary to handle static and media files came from the [Code Institute](https://codeinstitute.net/) walkthrough project: 'I Think, Therefore I Blog.

* The [Django Documentation](https://docs.djangoproject.com/en/4.1/) was immensely helpful in helping me gain a greater understanding of the project.

* The JavaScript code used to populate the hidden created-by field in the 'add book' form came from [this](https://www.youtube.com/playlist?list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi) series of videos by John Elder on YouTube.

* [This Post](https://www.section.io/engineering-education/uploading-images-to-cloudinary-from-django-application/) from Shuaib Oseni was helpful when it came to creating the front end method to upload an image to CLoudinary.

* The idea to automatically create the User Profile came from [this article](https://groups.google.com/g/django-users/c/cvbuURVHN0w) on Google Groups.

* General References:
  * Stack Overflow
  * Code Institute LMS
  * Bootstrap Documentation
  * Jinja Documentation
  * Cloudinary Documentation
  * Geeks for Geeks
  * W3C School
  * Course material on the CodeCademy website which helped reinforce my understanding of Python.

<hr>

## **Honourable mentions**

* The biggest thank you goes to my mentor, Richard Wells, who gave a significant amount of his time to provide me with help, feedback and ideas on the project; he has been invaluable in so many ways and a genuine source of motivation for me.
* Thanks to the Code Institute team for providing me with some basic knowledge of Python and Django.
* Thanks to the Code Institute who helped me overcome a major bug in the final deployment of the project
* Thanks to the Code Institute community on Slack who helped remind me that everyone has difficult days.
* A huge thank you to my family who support my coding journey on a daily basis.

<hr>

Links to additional related files: [AGILE.md](/AGILE.md) | [DEPLOYMENT.md](/DEPLOYMENT.md) | [TESTING.md](/TESTING.md)