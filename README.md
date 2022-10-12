#### Set Up
Ensure you have docker and docker-compose installed

Clone the repository `````
Switch to repository ```sudo cd weatherAPI```
Startup the project with ```sudo docker-compose up --build```
If all goes well the project should be up and running on ```0.0.0.0:8000```

#### Making requests
Note: API limits days to a maximum of 14 days in the tier currently consumed by this API
You can make requests using CURL on the terminal using the command below replacing location and day with your preference:
```
curl --request GET \
  --url http://0.0.0.0:8000/api/locations/<location>/<days>=1

```
You can also use an API client(Postman, Insomnia etc) by sending a GET request to ```http://0.0.0.0:8000/api/locations/<location>/days=<days>```

This also works in a browser. Just type
 ```http://0.0.0.0:8000/api/locations/<location>/days=<days>``` of course replacing location and day with the appropriate values; hit enter and you are good to go!
#### Checking coverage
```
sudo docker-compose run web coverage run --source='.' manage.py test api
sudo docker-compose run web coverage report
```
Some of those fancy coverage badges coming soon!