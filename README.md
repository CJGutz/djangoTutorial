# djangoTutorial

This repository contains

- django website learned from "NetNinja tutorial"
- django website components made learned from other tutorials or myself


# From udemy but using Django

Given for tasks that the learner have been given
Self for tasks where the learner must figure it out themselves
Info for messages to learner about trying or learning stuff.

Dockerfile updated to python 
Use slim buster. alpine fails with Pillow
Create requirements.txt file

https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/

## Tasks:

### Section 6
- Self: Watch section 6 but with these changes instead of react.
- Given: Use Dockerfile.dev
- Self: Write a simple explanation comment over each command
- Self: Create requirements.txt file
- Given: Show "docker run -f Dockerfile.dev"
- Self: Use -f to create image from Dockerfile
- Self: Create container from image. Hint: -p maps ports
- Info: While the container is running, try to make changes to the article_list template and refresh the page. Did any changes occur? No. Because we have not use "volumes"
- Self: Follow docker-compose in video, but change ports and remove node-modules volume
- Given: Use test in tests.py that tests if snippet method works. Learner can follow docker-compose from video but needs to drop node-modules volume and change command to python manage.py test
- Info: 81 can't be used with django, but still nice to understand
- Given: npm run build equivalency would be "python3 manage.py collectstatic --no-input" (I DONT KNOW)
- Info: make sure static folder in settings the folder in the Dockerfile

### Section 7
