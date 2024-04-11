### List dependencies
`pip freeze > requirements.txt`

### Prepare setup.py

### Create deployment branch

### Ignore unnecessary files
`git rm -r --cached .`

### Test the deployment
+ `git clone --no-hardlinks --branch <branch_name> --single-branch /path/to/chatbot_webapp`
+ e.g., `git clone --no-hardlinks --branch deployment_v1.0_2404 --single-branch /home/alan/Documents/chatbot_webapp`
