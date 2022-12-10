## Build and launch the API
To run the backend, navigate inside the main folder.  
Install the requirements in requirements.txt and execute `python main.py`.    
The backend should now be available locally on port 8888.  
Payloads can be POSTed on the */productionplan* endpoint (http://localhost:8888/productionplan).

The python version used for development is Python 3.11.1

## Testing
There are several unit tests available, which mainly test the API (input) restrictions.  
To run the tests, first run the backend as explained above, then run the tests with `pytest .\tests\unittest.py`.

# Docker
This branch has two additional files: *Dockerfile* and *docker-compose.yaml*.  
These files allow you to build an image of the application and run it inside a container.  
To build an image, use `docker image build -t some_name_you_choose .`.  
To run an image, use docker run `docker run -p 8888:5000 -d the_name_you_chose_above`.  
Alternatively, run `docker-compose up` inside the main folder.
