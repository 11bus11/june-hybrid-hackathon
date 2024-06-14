# june-hybrid-hackathon

1. Clone the repository:
  - Run the following command in a terminal
  - `git clone https://github.com/11bus11/june-hybrid-hackathon.git`

2. Change the branch
    - In the terminal, in the root folder, write `git checkout -b <Your branch name>`

3. Create a virtual environment by writing `virtualenv venv` (You need to have installed virtualenv).
    - Activate the virtual environment by writing `source venv/bin/activate`

4. Install the necessary packages by running `pip install -r requirements.txt`

5. To run the project locally with `DEBUG` enabled, make sure to include `os.environ['DEV'] = '1'` in your `env.py` file. Then run the project with the command `python manage.py runserver`

6. Go to `localhost:3000` to check that the server is running.

## Structure

Paths:

- __/__ = homepage = index.html (template in users/templates)
  - The template gets passed the user object of the current user

- __/book-appointment__ = book-appointment.html (template in scheduling/templates/)
/patient = patient.html (template in users/templates)
  - user object of the current user: user
  - a list of time slot objects: object_list
  - has a crispy form: form (to create an appointment)
  - unauthorized users get redirected to homepage

- __/patient__ = patient.html (template in users/templates)

- __/accounts/signup__ = signup.html (template in .templates/account/)

- __/accounts/login__ = login.html (template in .templates/account/)

- __/accounts/logout__ = logout.html (template in .templates/account/)

## Github steps

Merging your code into main:
1. Make sure you are on the main branch: check by running command `git branch`
  - If not on main branch, switch to main branch with `git checkout main`

2. Update your local main branch to mirror the live main branch, command: `git pull origin main`

3. Create a new branch: `git checkout -b <your branchname>`

4. Add your work

5. git add, commit, and push, using `git push origin <your branchname>`

6. Go to your repository on GitHub, and click to open a PR
  - If everything is green, share PR link with team

7. If PR is then merged to main, change from your local branch to your local main branch (following step 1).
  - Repeat process

If PR leads to conflicts:
1. In your local environment, switch to the main branch, `git checkout main`

2. Pull the latest version of main, with `git pull origin main`

3. Switch back to the branch you were working on, `git checkout <your branchname>`

4. Merge the new main into your local branch: `git merge main`

5. Now you should see a list of files that contain conflicts (if any). Time to fix the conflicts:
  - Review the files and manually edit the code.

6. Once all conflicts are resolved, add, commit and push changes to your branch, `git push origin <your branchname>`

7. Go to GitHub. You should now see a green tick on the PR.


# june-hybrid-hackathon(team_1):

## Sjukstugan

![sjukstugan_introduction_picture]()

## Features:

### The header:

The header is included on all pages with four navbar links to seperate pages which are the following:

* Sjukstugan(link to homepage)

* About

* Book

* Profile

![header]()

### The landing page image: 

Below the header the user can see a green welcome text with a simple and clean dark grey description text underneath it to give the user an easy and fast experience. To the right side of the welcome text and description text the user can see a green circular shaped image which is intended to look like a cartoon inspired bacteria molecule.

![landing_page_image]()

### Footer:

The footer is included on all four pages and contains all our social media platform links which are the following:

*Instagram

*Facebook

*Twitter

*Youtube

The footer also includes an email address to our support.

![footer]()

### The About page:

The about page gives the user a view of a green about us text with a smaller dark grey description text underneath it. The description text tells the user about our story and when our company was founded. On the right side of the about us text and description text the user can see a red circular shaped image which is intended to look like a cartoon inspired blood molecule.

![about_page]()

### The book an appointment form:

This section can be found on the booking page gives the user an alternative to book an appointment with us. Our team has designed the form to be easily understandable and readable for all people no matter what the age is.

The book an appointment form includes the following input fields:

*

*

*

![booking_form]()

### The log in form:

This section can be found on the profile page gives the user an option to log in to their account.

The log in form includes the following input fields:

*

*

*

![log_in_page]()

### Overall info:

The website has colors and a design that our team feels matches or inspires the user experience of a swedish based healthcare business culture. The yellow colour is inspired from the swedish flag and the overall colours are inspired from healthcare related experiences:

The total colours are:

* Green

* Red

* Light yellow

* Dark yellow

* White

* Light grey

* Dark grey(Used on the small texts)

* Blue(Can be found on the profile page for a couple of links)

### Validator testing:

*The HTML and CSS code has been validated through:

*W3C Validator(HTML): https://validator.w3.org/nu/

*Jigsaw Validator(CSS): https://www.w3.org/

### Overall tests:

* Lighthouse results:

![lighthouse]()

* Amiresponsive results:

Here is a link to the results:

![amiresponsive]()

### Unfixed bugs:

*There was no bugs discovered on this project.

### Deployment:

The deployment was made through github. The step by step process where the following: Settings --> Pages --> Source --> Deploy from a branch --> Main --> /(root) --> Save.

![github_screenshot]()

### Credit:

* The majority of the total code was taken from or inspired by

### Media:

* All the icons used in the code was taken from font awsome. Here is a url adress to their homepage: https://fontawesome.com/




