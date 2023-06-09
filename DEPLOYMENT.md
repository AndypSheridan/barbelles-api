# Deployment

## Table of Contents

---

### Setting up a basic Django project and deploying to Heroku

-   [**Deployment**](#deployment)
    -   [**_Initial Deployment_**](#initial-deployment)
    -   [**_Create Repository_**](#create-repository)
    -   [**_Setting up the Workspace_**](#setting-up-the-workspace-to-be-done-locally-via-the-console-of-your-chosen-editor)
    -   [**_Using JWT Tokens_**](#using-jwt-tokens)
    -   [**_Adding feature to register users_**](#adding-feature-to-register-users)
    -   [**_Adding JWT Tokens functionality_**](#add-jwt-tokens-functionality)
    -   [**_Add profile id and profile image fields_**](#add-profile-id-and-profile-image-fields)
    -   [**_Add the root route_**](#add-the-root-route)
    -   [**_Adding JSON renderer_**](#adding-json-renderer)
    -   [**_Date and time formatting_**](#date-and-time-formatting)
    -   [**_Deploying an app to Heroku_**](#deploying-an-app-to-heroku)
        -   [**_Create a New External Database_**](#create-a-new-external-database)
        -   [**_Create Heroku App_**](#create-heroku-app)
        -   [**_Connect to the Database_**](#connect-to-the-database)
        -   [**_Preparing Environment and settings.py File_**](#preparing-environment-and-settings.py-file)
        -   [**_Store Static and Media Files on Cloudinary_**](#store-static-and-media-files-on-cloudinary)
        -   [**_Final Steps_**](#final-steps)
-   [**_Cloning on a Local Machine or Via Gitpod Terminal_**](#cloning-on-a-local-machine-or-via-gitpod-terminal)

## Initial Deployment

I took the following steps to deploy the site to Heroku and have listed any console commands required to initiate it. My aim was to ensure this process was completed as early as possible in the project, to avoid complications or issues as it progressed.


### Create repository:

-   Create a new repository in GitHub and clone it locally following [these instructions](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
    -   **Note** - If you are cloning my project, then you can skip all pip installs below and just run the following command in the terminal to install all the required libraries/packages at once:
        -   pip install -r requirements.txt
    -   **IMPORTANT** - If developing locally on your device, ensure you set up/activate the virtual environment ([see below](#setting-up-the-workspace-to-be-done-locally-via-the-console-of-your-chosen-editor)) before installing/generating the requirements.txt file; failure to do this will pollute your machine and put other projects at risk

### Setting up the Workspace (To be done locally via the console of your chosen editor):

1. Create a virtual environment on your machine (Can be skipped if using gitpod):
    - python -m venv .venv
1. To ensure the virtual environment is not tracked by version control, add .venv to the .gitignore file.
1. Install Django 3.2 alongside gunicorn:
    - `pip3 install 'django<4' gunicorn`
    - **Note:** Django 3.2 is the _LTS_ (Long term support) version which is preferable to use over the Django 4 beta.
1. Install supporting libraries:
    - `pip install dj_database_url==0.5.0 psycopg2`
    - `pip install dj3-cloudinary-storage`
1. Create requirements.txt:
    - `pip freeze --local > requirements.txt`
1. Create an empty folder for your project in chosen location.
1. Create a project in the above folder:
    - `django-admin startproject PROJECT_NAME .` (in the case of this project, the project name was "sfportal")
1. Create an app within the project:
    - `python3 manage.py startapp APP_NAME` (in the case of this project, the app name was "sfblog")
1. Add new app to bottom of the list of installed apps in settings.py and save file
1. Migrate changes:
    - `python3 manage.py migrate`
1. Test server works locally:
    - `python3 manage.py runserver` (This should display the default Django success page)

### Using JWT tokens

1. In the *terminal*: `pip install `pip install dj-rest-auth==2.1.9`
    - in *settings.py*: `INSTALLED_APPS = [ ...
                        'django_filters',
                        'rest_framework.authtoken', 'dj_rest_auth',
                        ‘profiles’,
                        ... ]`
    - in main *urls.py* file:
    `urlpatterns = [ ...,
        path('api-auth/', include('rest_framework.urls')),
        path('dj-rest-auth/', include('dj_rest_auth.urls')),
        path('', include('profiles.urls')), ....,]`
    - in the *terminal*, migrate the database: `python manage.py migrate`

### Adding feature to register users

1. In the *terminal*, install Django all-Auth: `pip install 'dj-rest-auth[with_social]'`
    - In *settings.py*, add relevant apps to installed apps:
    `INSTALLED_APPS = [ ...,
        'dj_rest_auth',
        'django.contrib.sites', 'allauth',
        'allauth.account', 'allauth.socialaccount', 'dj_rest_auth.registration',
        'profiles',
        ..., ]`
    - Add site id value under installed apps list: `SITE_ID = 1`
    - In *main urls.py file*, add registration urls to the url patterns list:
    `urlpatterns = [ ...,
        path('dj-rest-auth/', include('dj_rest_auth.urls')),
        path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
        path('', include('profiles.urls')), ...,
        ]`

### Adding JWT Tokens functionality

1. In the *terminal*: `pip install djangorestframework-simplejwt==4.7.2`
    - In *env.py*, differentiate between Dev and Prod mode: `os.environ['DEV'] = 1`
    - In *settings.py*:
    `REST_FRAMEWORK = { 'DEFAULT_AUTHENTICATION_CLASSES': [(
        'rest_framework.authentication.SessionAuthenticatio n'
        if 'DEV' in os.environ
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    )] }`
    - enable token authentication: `REST_USE_JWT = True`
    - `JWT_AUTH_COOKIE = 'my-app-auth'`
    Declare cookie names for access and refresh tokens: 
    `JWT_AUTH_SECURE = True JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'`


### Add profile id and profile image fields

1. Create a new *serializers.py file*: e.g. `barbelles_api / serializers.py`
    - in the new serializers.py file, import: 
    `from dj_rest_auth.serializers import UserDetailsSerializer from rest_framework import serializers`
    - create profile_id and profile_image fields: 
    `class CurrentUserSerializer(UserDetailsSerializer): 
        profile_id = serializers.ReadOnlyField(source='profile.id') 
        profile_image = serializers.ReadOnlyField(source='profile.image.url') 

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('profile_id', 'profile_image')`
    - overwrite the default serializer **place under JWT_AUTH_REFRESH_COOKIE**: 
    `REST_AUTH_SERIALIZERS = {'USER_DETAILS_SERIALIZER': 'drf_api.serializers.CurrentUserSerializer'}`

    - In the *terminal*:
    - `python manage.py migrate`
    - `pip freeze > requirements.txt`
    - Add, commit and push

### Add the root route

1. In the IDE / terminal, create a *views.py* file: e.g. `barbelles_api / views`
    - in the new *views.py* file, import: 
    `from rest_framework.decorators import api_view 
     from rest_framework.response import Response`
    - create root route and return custom message: 
    `@api_view()
    def root_route(request):
    return Response({"message": "Welcome to my django rest framework API!"})`
    - set imports: `...
                    from .views import root_route`
    - add *url patterns* to list: 
    `urlpatterns = [ ...,
    path('', root_route)
    ]`

### Adding JSON renderer

1. In *settings.py*, add pagination:
    ```
    REST_FRAMEWORK = { ...,
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    }
    ```
    - set JSON renderer if DEV environment not present:
    ```
    REST_FRAMEWORK = { ...
    }
    if 'DEV' not in os.environ:
    REST_FRAMEWORK['DEFAULT_RENDERER_CL ASSES'] = [
    'restframework.renderers.JSONRenderer' ]
    ```

### Date and time formatting

1. In *settings.py*: 
    ```
    REST_FRAMEWORK = { ...
    'DATETIME_FORMAT': '%d %b %Y'
    }
    ```
    - In *comments.serializers.py*, set imports:
    ```
    ...
    from django.contrib.humanize.templatetags.humanize
    import naturaltime
    ```
    - Set fields in *comment serializer class*:
    ```
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    ```
    - set methods underneath fields: 
    ```
    def get_created_at(self, obj):
        return naturaltime(obj.created_at)
    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)
    ```
    - Add, commit and push changes

## Deploying an App to heroku

### Create a New External Database:

For the purposes of this project I used ([ElephantSQL](https://www.elephantsql.com/)) and the following assumes you already have an account:

1. Log in to your account
    - Click "Create new instance"
1. Set up your plan:
    - Give your project a name (commonly the name of your project)
    - Select the Tiny Turtle (Free) plan
    - Tag fields can be left blank
1. Select the nearest location:
    - For me, this was Ireland.
    - Click review and then 'Create Instance'
1. Return to the ElephantSQL dashboard:
    - Click on the **database instance name** for this project:
    - Copy your **ElephantSQL** _database URL_ (It will start with postgres://)

### Create Heroku App:

The below works on the assumption that you already have an account with [Heroku](https://id.heroku.com/login) and are already signed in.

1. Create a new Heroku app:
    - Click "New" in the top right-hand corner of the landing page, then click "Create new app."
1. Give the app a unique name:
    - It will form part of the URL (in the case of this project, I called the Heroku app sci-fi-portal)
1. Select the nearest location:
    - For me, this was Europe.
1. Add Database to the Heroku app:
    - Open _settings_ tab and click **Reveal Config Vars**
    - Add a Config Var called **DATABASE_URL**
    - **NOTE:** The **value** should be the ElephantSQL database url copied in the previous step.
1. From your editor, go to your projects settings.py file and copy the SECRET_KEY variable. Add this to the same name variable under the Heroku App's config vars.
    - left box under config vars (variable KEY) = SECRET_KEY
    - right box under config vars (variable VALUE) = Value copied from settings.py in project.

### Connect to the Database

I used **gitpod** for this project:

1. In **gitpod**:
   ** In the terminal **
   _ Install dj_database_url: `pip install dj_database_url`
   _ in **settings.py**:
   _ Import library: `import dj_database_url`
   _ Separate the Dev and Prod environments: 
        ```
       DATABASES = {
            'default': ({
                'ENGINE': 'django.db.backends.sqlite3', 'NAME': BASE_DIR / 'db.sqlite3',
            } if 'DEV' in os.environ else dj_database_url.parse(
                os.environ.get('DATABASE_URL')
            ))
        }
        ```
    * In the **terminal**:
    Install gunicorn: `pip install gunicorn`    
    * Create **Procfile**
    * In Procfile:`release: python manage.py makemigrations && python manage.py migrate
   web: gunicorn drf_api.wsgi`
    - in **settings.py**: set the allowed hosts: `ALLOWED_HOSTS = ['<YOURAPPNAME>.herokuap p.com', 'localhost']`
    - in the **terminal**: `pip install django-cors-headers`
    - in **settings.py**, add cors headers: 
                            ```
                            INSTALLED_APPS = [ ...
                            'dj_rest_auth.registration',
                            'corsheaders',
                            'profiles',
                            ... ]
                            ```
    - add to middleware:    
                            ```
                            MIDDLEWARE = [
                            'corsheaders.middleware.Cors Middleware',
                            ... ]
                            ```
                        
    - set the ALLOWED_ORIGINS for network request made by the server:
    `if 'CLIENT_ORIGIN' in os.environ: CORS_ALLOWED_ORIGINS =[
        os.environ.get('CLIENT_ORIGIN') ]
    else:
        CORS_ALLOWED_ORIGIN_RE GEXES = [
        r"^https://.*\.gitpod\.io$", ]`

    - Allow *cookies*: `CORS_ALLOW_CREDENTIALS = True`

    - Allow front and backend sites to be deployed to different platforms: `JWT_AUTH_SAMESITE = 'None'`

1. Set the remaining **environment variables**:
    - in **env.py**: `os.environ['SECRET_KEY'] = 'CreateRandomValue'`
    - in **settings.py**, replace insecure key with the environment variable: 
    `SECRET_KEY = os.environ.get('SECRET_KEY')`
    - replace the DEBUG setting to be only true in Dev and False modes: `DEBUG = 'DEV' in os.environ`

1. In **Heroku**:
    - Add Secret Key to Config Vars: **SECRET_KEY (value:) "Made up secret key"**
    - Add `DISABLE_COLLECTSTATIC = 1` config var
    - For this project it was also necessary to add **PORT 8000**

1. In the **terminal**: `pip freeze > requirements.txt` and push changes to GitHub


### Connect the project's github repo to Heroku

1.  In **Heroku**:
    - Select the deployment method, e.g. *GitHub*
    - Select the project repo name from GitHub and then connect
    - In the deploy section choose *master branch*
    - Click *deploy branch*
    - Open app to view

1.  In the **terminal**:

    -   **SAVE ALL FILES** Make an initial commit and push the code to the GitHub Repository.

    `git add .
    git commit -m "Initial deployment"
    git push`

1. **FINAL DEPLOYMENT**
    In *settings.py*
    - Set `DEBUG = False`

    In *Heroku*
    - Remove 'disable_collectstatic' variable
    - Select *Deploy branch*


### Cloning on a Local machine or Via Gitpod Terminal

1. Navigate to the GitHub repository, and follow these steps to clone the project into your IDE of choice.

    - **Gitpod** only requires you to have the web extension installed and click the green Gitpod button from the repositories main page. If you are using Gitpod, please skip step 2 below as you do not require a virtual environment to protect your machine.

1. Create the virtual environment with the terminal command **`python3 -m venv venv`.** Once complete add the "venv" file to your ".gitignore" file and use the terminal command **`venv\Scripts\activate.bat`** to activate it.

    - **_IMPORTANT_** If developing locally on your device, ensure you _set up/activate the virtual environment before installing/generating the requirements.txt file_; failure to do this will pollute your machine and put other projects at risk.

1. **Install the requirements** listed in _requirements.txt_ using the terminal command **`pip3 install -r requirements.txt`**

Please note that since the project has been developed from scratch, I have installed required libraries as the project progressed. I have already included a requirements.txt for this app by using the **terminal command** `pip3 freeze > requirements.txt` to generate it.

1. **[Create your own Heroku app](create-heroku-app)** and update allowed hosts in settings.py.

1. **[Create your .env file](#attach-the-database)**

1. **Run server locally with `python3 mange.py runserver`**

**[Back to Readme](README.md)**
