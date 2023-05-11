# family-tree-backend
The Tree of Family: backend part with an API Gateway

To install the dependencies, run this command:  
`pip3 install -r requiremenets.txt`

Then, you can run the project for

Development mode:  
`python3 -m uvicorn app:app --reload --port 8000`

Production mode:  
`python3 -m gunicorn app:app -k uvicorn.workers.UvicornWorker`