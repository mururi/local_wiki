# Awwwards Clone
#### A Django Neighborhood Watch/Local Wiki, Apr 18, 2022 
#### By **Dennis Kiboi** 

## Description 
This is a neighborhood watch or local wiki app built using Django. It allows a registered user to get up to date information about their neighborhood.

![Local Wiki](static/images/localwiki.png)

## How to Use
### Requirements
* A computer, tablet or phone
* Access to the internet

### View Live Site 
Ensure that your device of choice has a browser installed.
Click the link provided below to view the site.

https://local-wiki-mururi.herokuapp.com/

### Using the App
The user can navigate the web app easily and be able to:
* Sign in with the application to start using
* Set up a profile with their general location and neighborhood name
* Find a lsit of different businesses in their neighborhood
* Find contact information for the health department and police authorities near their neighborhood
* Create posts that will be visible to everyone in their neighborhood
* Change their neighborhood when they decide to move out
* Only view details of a single neighborhood

## Run Locally
### Setup/Installation Requirements
To run this app locally, you need a PC with the following installed:
* Python 3.+
* pip

### Installation Process
1. Clone this repository using

    ```bash
      git clone https://github.com/mururi/local_wiki.git
    ```

    or by downloading a ZIP file of the code.
  
2. The repository, if downloaded as a .zip file will need to be extracted to your preferred location and opened
3. Go to the project root directory and install the virtualenv library using pip an afterwards create a virtual environment. Run the following commands to do so:

    ```bash
      python3 -m venv --without-pip virtual 
    ```

    ```bash
      source virtual/bin/activate
    ```

    ```bash
      curl https://bootstrap.pypa.io/get-pip.py | python
    ```
 
4. Download the all dependencies in the requirements.txt using

    ```bash
      pip install -r requirements.txt
    ```
5. Open the terminal and navigate to the project directory and run the following commands to launch the program.

    ```bash
    python manage.py runserver
    ```

## Technologies Used
* Django
* Python
* HTML
* CSS/Bootstrap
* Heroku

## Support and Contact Details
Incase of any query, need for collaboration or issues with this code, feel free to reach me at
dennis.kiboi@student.moringaschool.com

## License 
MIT License

Copyright &copy; 2022 Dennis Kiboi

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.