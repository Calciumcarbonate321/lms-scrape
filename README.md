This repository is a proof of concept of selenium on the cloud behind an API. Currently this is used to get screenshot of lms home page after logging in.

`/lms_ss?username=[username]&password=[password]`

To run it

`pip install -r requirements.txt`

and

`python run.py`

or 

`uvicorn main:app --reload`
