# LizGalleria

## Author
**Elizabeth Adhiambo Onyango**
~Full stack developer



<img src="/static/photos/screenshot1.png">
<img src="/static/photos/screenshot2.png">

## Project Description

This is a personal gallery where users can view different Images ,click on them to have a modal view of the picture. Users can also view the images description and search photos based on the categories and location the images were taken.

## BDD

| Behavior            | Input                         | Output                        |
| ------------------- | ----------------------------- | ----------------------------- |
| View photos of interest | Scroll to see a gallery and click on picture | Displays a picture with name description and copy link for sharing |
| Search a picture by category | Enter the category in the search input| Displays Images in the searched category |
| View pictures by location | Click on location of interest from the Navbar | Displays Images of chosen location |
| Copy Link to clipboard | Click on copy link button in the modal class | Copies link to clipboard |
| View Single picture | Click on photo of interest then click on image | Displays a single page with details of the picture and related images . You can aslo view varying sizes of the same photo|

<img src="/static/photos/screenshot3.png">
<br>




## Getting Started

To clone the repository, run:

    git clone https://github.com/Liz2222/galleria.git
Then navigating to the cloned directory:

    cd galleria


### Prerequisite
The Galleria project requires a prerequisite understanding of the following:
- Django Framework
- Python3.8
- Postgres
- Python virtualenv

## Setup and installation

###  Activate virtual environment
Activate virtual environment using python3.9 as default handler
    `virtualenv -p /usr/bin/python3.9 genv && source genv/bin/activate`
####  Install dependancies
Install dependancies that will create an environment for the app to run `pip3 install -r requirements.txt`
####  Create the Database
    - psql
    - CREATE DATABASE gallery;
####  .env file
Create .env file and paste paste the following filling where appropriate:

    SECRET_KEY = '<Secret_key>'
    DBNAME = 'galleria'
    USER = '<Username>'
    PASSWORD = '<password>'
    DEBUG = True
#### Run initial Migration
    python3.8 manage.py makemigrations gallery
    python3.8 manage.py migrate
#### Run the app
    python3.8 manage.py runserver
    

## Deployment

The application is deployed on Heroku and is live on this link:

[https://galleria-liz.herokuapp.com/](https://galleria-liz.herokuapp.com/)

## Built With

  - [Django 4.0.4](https://docs.djangoproject.com/en/4.0/releases/4.0.4/) - Back end logic of the application.
  - [Bootstrap4](https://bootstrap.com/) - Used for overall design and responsive site
  - [Pillow 9.1.1](https://pillow.readthedocs.io/en/stable/) - Used for image uploads.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code
of conduct, and the process for submitting pull requests to us.


## License

MIT License

Copyright (c) 2022 Elizabeth Adhiambo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
