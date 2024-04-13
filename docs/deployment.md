### List dependencies
`pip freeze > requirements.txt`

### Prepare setup.py

### Create deployment branch

### Ignore unnecessary files
`git rm -r --cached .`

### Test the deployment
+ `git clone --no-hardlinks --branch <branch_name> --single-branch /path/to/chatbot_webapp`
+ e.g., `git clone --no-hardlinks --branch deployment_v1.0_2404 --single-branch /home/alan/Documents/chatbot_webapp`
+ Remark: to pull the updated changes, we go to `/path/to/chatbot_webapp` and run `git pull origin <branch_name>`
+ `python setup.py sdist bdist_wheel`
+ `conda remove --name test_env --all`
+ `conda create -n test_env python=3.10`
+ `conda activate test_env`
+ `pip install dist/chatbot_webapp-1.0-py3-none-any.whl`
+ `streamlit run scripts/app.py`

### Deploying your Dockerized web application
+ Build the Docker Image: `sudo docker build -t chatbot_webapp_image -f Dockerfile.web_app .`
+ Verify the Image Was Created: `docker images`
+ Run the Docker Container: `docker run -d -p 8501:8501 chatbot_webapp_image`
+ Access the Web Application: `http://localhost:8501`
+ Managing the Container (to see all running containers): `docker ps`
+ To stop the container: `docker stop container_id_or_name`
+ To start the container again, use: `docker start container_id_or_name`
