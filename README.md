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


# Readme

## Styling

## Features

## Deployment?

## Credits

