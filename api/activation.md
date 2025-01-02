# Activation Endpoints

### Get Activation By Id

* URL: /api/get-activation-by-id/:id
* Method: Get
* Description: Retrieves an activation by its Id
* URL Parameters:
    * id (integer): The unique ID of the activation to retrieve

  ```bash
  GET /api/get-activation-by-id/1
  ```
* Response
    * 200 Ok: Activation Retrieved successfully
        * Body: A JSON object containing the activation details
        * Example Response:
          ```json
          {
          "id": 1,
          "mt5ID": "test mt5 id",
          "mt5Value": "test mt5 value",
          "mt5Description": "test description"
          }
          ```
    * 400 Bad REquest: ID not found.
        * Body:
          ```json
          {"message": "ID not found."}



## Get All Activation 

* URL: /api/get-all-activations
* Method: Get
* Description: Retrieves a list of all activations.
* Example Request:
   ```bash
   GET /api/get-all-activations
   ```
* Response
    * 200 Ok: Successfully retrieved the list of activations.
        * Body: An array of JSON objects, each representing an activations.
        * Example Response:
          ```json
          [
          {
          "id": 1,
          "mt5ID": "test mt5 id",
          "mt5Value": "test mt5 value",
          "mt5Description": "test description"
          },
          {
          "id": 2,
          "mt5ID": "test mt5 id 2",
          "mt5Value": "test mt5 value 2",
          "mt5Description": "test description 2"
          }
          ]
          ```
         
    * 400 Bad Request: No data found.
        * Body:
          ```json
          {"message": "No data found."}
          ```
