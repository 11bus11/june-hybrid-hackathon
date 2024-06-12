# june-hybrid-hackathon

1. Clone the repository:
  - Run the following command in a terminal
  - `git clone https://github.com/11bus11/june-hybrid-hackathon.git`

2. Change the branch
    - In the terminal, in the root folder, write `git checkout -b <Your brand name>`

3. Create a virtual environment by writing `virtualenv venv` (You need to have installed virtualenv).
    - Activate the virtual environment by writing `source venv/bin/activate`

4. Install the necessary packages by running `pip install -r requirements.txt`

5. To run the project locally with `DEBUG` enabled, make sure to include `os.environ['DEV'] = '1'` in your `env.py` file. Then run the project with the command `python manage.py runserver`

6. Go to `localhost:3000` to check that the server is running.
