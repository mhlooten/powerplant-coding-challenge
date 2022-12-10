## Build and launch the API
To run the backend, navigate inside the main folder.  
Install the requirements in requirements.txt and execute `python main.py`.    
The backend should now be available locally on port 8888.  
Payloads can be POSTed on the */productionplan* endpoint (http://localhost:8888/productionplan).  
A json body is returned with the result of the algorithm.

The python version used for development is Python 3.11.1

## Testing
There are several unit tests available, which mainly test the API (input) restrictions.  
To run the tests, first run the backend as explained above, then run the tests with `pytest .\tests\unittest.py`.

## Structure
main.py --> Creation of the Flask app  
Rest/productionplan.py --> Productionplan endpoint  
Algorithms/Solver.py --> Algorithm to find the power for each factory  
Objects/ --> Folder with the powerplant object/factory. The factories in the json document are converted into objects for easier use during the algorithm.  
tests/unittest.py --> Several unit tests to check the response of the API with different payloads

## Docker
For an implementation using docker, please refer to the 'docker' branch
