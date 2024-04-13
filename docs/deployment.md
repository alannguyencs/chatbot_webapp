### List dependencies
+ prepare `requirements.txt`

### Prepare setup.py

### Create deployment branch

### Ignore unnecessary files
`git rm -r --cached .`

### Test the deployment
+ `git clone --no-hardlinks --branch <branch_name> --single-branch /path/to/chatbot_webapp`
+ e.g., `git clone --no-hardlinks --branch deployment_v1.0_2404 --single-branch /home/alan/Documents/chatbot_webapp`
+ Remark: to pull the updated changes, we go to `/path/to/chatbot_webapp` and run `git pull origin <branch_name>`
+ Environment:
```
conda deactivate
conda remove --name test_env --all
conda create -n test_env python=3.10
conda activate test_env
```
+ Iteratively install dependencies and test the code with `streamlit run scripts/app.py`
+ Generate dependencies: `pip freeze > requirements.txt` just to get the format. Unfortunately, requirements contains multiple unnecessary packages. Then should manually select the appropriate packages.
+ Generate the wheel: `python setup.py sdist bdist_wheel`
+ Test the wheel:
```
conda deactivate
conda remove --name test_env --all
conda create -n test_env python=3.10 --yes
conda activate test_env
pip install dist/chatbot_webapp-1.0-py3-none-any.whl
streamlit run scripts/app.py
```
+ Copy the package `dist/chatbot_webapp-1.0-py3-none-any.whl` to this working directory

### Deploying your Dockerized web application
+ Build the Docker Image: `sudo docker build --no-cache -t chatbot_webapp_image -f Dockerfile.web_app .`
+ Verify the Image Was Created: `sudo docker images`
+ Run the Docker Container: `sudo docker run -d -p 8501:8501 chatbot_webapp_image`
+ Access the Web Application: `http://localhost:8501`
+ Managing the Container (to see all running containers): `sudo docker ps`
+ To stop the container: `sudo docker stop container_id`
+ To get the list of existing containers: `sudo docker container ls -a`
+ To start the container again, use: `docker start container_id`