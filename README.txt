Instructions to install:
1. (optional) Activate your virtual environment if you wish to use one
2. Install dependencies with: pip install -r requirements.txt
3. python rolepointsite/manage.py runserver
4. Visit http://127.0.0.1:8000/social in your browser

About the application:
This simple Django application fulfills requirements outlined in README_SPEC.txt
as part of the rolepoint coding test. The .json file being represented is
excercise-data.json. Since we are looking at algorithm optimization for searching
through the data given in the excercise-data.json file at a reasonable speed, 
that will be the focus of the social view, even though in practice this
information would be stored in a indexed database table for fast retrieval
