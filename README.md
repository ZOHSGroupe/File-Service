## Description

File-Service is an Application Programming Interface (API) to upload files to google-drive of ZOHS assurance company.
## Installation :
```bash
# install requirements
$ pip install -r requirements.txt 
```
## Running the app : 
```bash
# Run application
$ uvicorn main:app --workers 4 --host 127.0.0.1 --port 5000 --reload --log-level info
```
## Build Docker image : 
```bash
# build a docker image
$ docker build -t file-service .
```
## Running the app in the Docker : 
```bash
# Run docker image
$ docker run -p 5000:5000 file-service
```
## Stay in touch :
- Author - [Ouail Laamiri](https://www.linkedin.com/in/ouaillaamiri/)
- Test - [Postman](https://www.postman.com/avionics-meteorologist-32935362/workspace/postman-api-fundamentals-student-expert/collection/29141176-282aba17-b309-429b-94ff-a7d13f6f4e1a?action=share&creator=29141176)
- Documentation - [Postman](https://documenter.getpostman.com/view/29141176/2s9Ykt4eMm)

## License

Email-Service is [MIT licensed](LICENSE).