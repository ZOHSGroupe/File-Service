### To install requirements :
pip install -r requirements.txt 
### To run app : 
uvicorn main:app --workers 4 --host 0.0.0.0 --port 5000 --reload --log-level info
### Build Docker image : 
docker build -t file-service .
### Run the Docker container : 
docker run -p 5000:5000 file-service
### Documentation of api in postman :
https://documenter.getpostman.com/view/29141176/2s9Ykt4eMm
