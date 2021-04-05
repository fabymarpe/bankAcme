# Bank ACME

# How to install
1. Create project folder on local pc
2. From the project folder to clone the project 'git clone https://github.com/fabymarpe/bankAcme.git'

# How to run
1. From the project folder run _docker-compose up_
2. From your browser go to http://localhost:5000/ to make sure the service is running
3. Make a POST call from postman using the following collection:

    ```
   {
	"info": {
		"_postman_id": "7afc833e-8a94-4a37-b6c7-abbedc40b3f2",
		"name": "bankAcme",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
	},
	"item": [
		{
			"name": "http://localhost:5000/workflow",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "formdata",
					"formdata": [
						{
							"key": "file",
							"type": "file",
							"src": "path_to_file"
						}
					]
				},
				"url": {
					"raw": "http://localhost:5000/workflow",
					"protocol": "http",
					"host": [
						"localhost"
					],
					"port": "5000",
					"path": [
						"workflow"
					]
				}
			},
			"response": []
        }]
   }
    
