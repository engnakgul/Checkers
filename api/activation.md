# Activation Endpoints

* Parameters:
   - **id**:                (number) Unique identifier for the resource. [Primary Key, Auto-generated]
   - **mt5ID**:             (string) MetaTrader 5 account identifier. [Required, Unique]
   - **mt5Value**:          (number) Value associated with the MT5 account. [Required, Unique]
   - **mt5Description**:    (string) Description or details for the MT5 account. [Required]


### Get Activation By Id

* URL: /api/get-activation-by-id/:id
* Method: GET
* Description: Retrieves an activation by its Id
* URL Parameters:
    * id (integer): The unique ID of the activation to retrieve
* Example Request:
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
           "mt5ID": "12345678",
           "mt5Value": 1500,
           "mt5Description": "test description"
           }
           ```
    * 400 Bad Request: ID not found.
        * Body:
          ```json
          {
          "status": "Failed",
          "message": "ID not found."
          }
          ```



## Get All Activation 

* URL: /api/get-all-activations
* Method: GET
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
               "mt5ID": "123456",
               "mt5Value": 1400,
               "mt5Description": "test description"
               },
               {
               "id": 2,
               "mt5ID": "12345678",
               "mt5Value": 1500,
               "mt5Description": "test description 2"
               }
               ]
           ```
         
    * 400 Bad Request: No data found.
        * Body:
          ```json
          {
          "status": "Failed",
          "message": "No data found."
          }
          ```


## Create Activation 

* URL: /api/create-activation
* Method: POST
* Description: Create a new Activation
* Example Request:
   ```bash
   GET /api/create-activation
   ```
   ```json
   {
   "mt5ID": "12345678",
   "mt5Value": 1500,
   "mt5Description": "test description"
   }
   ```
   
* Response
    * 200 Ok: Activation created successfully.
         * Example Response:
             ```json
             {
             "status": "success",
             "message": "Activation created successfully.",
             "data":{
                "id":1,
                "mt5ID": "12345678",
                "mt5Value": 1500,
                "mt5Description": "test description"
             }
             }
             ```
    * 400 Bad Request: Failed to create activation.
        * Body:
          ```json
          {
          "status": "Failed",
          "message": "Failed to create activation."
          }
          ```
   


## Update Activation 

* URL: /api/update-activation/:id
* Method: PUT
* Description: Retrieves a list of all activations.
* Example Request:
   ```bash
   PUT /api/update-activation/1
   ```
   ```json
   {
   "mt5ID": "12345678",
   "mt5Value": 1500,
   "mt5Description": "test description updated"
   }
   ```
* Response
    * 200 Ok: Activation updated successfully.
        * Example Response:
          ```json
          {
          "status": "success",
          "message": "Activation updated successfully.",
          "data": {
          "mt5ID": "12345678",
          "mt5Value": 1500,
          "mt5Description": "test description updated"
           }
          }
          ```
         
    * 400 Bad Request: Activation not found.
        * Body:
          ```json
          {
          "status": "Failed.",
          "message": "Activation not found.",
          }
          ```


## Delete Activation 

* URL: /api/delete-activation/:id
* Method: DELETE
* Description: Retrieves a list of all activations.
* Example Request:
   ```bash
   DELETE /api/delete-activation/1
   ```
   
* Response
    * 200 Ok: Activation deleted successfully.
        * Body: An array of JSON objects, each representing an activations.
        * Example Response:
          ```json
          {
          "status": "success",
          "message": "Activation deleted successfully"
          }
          ```
         
    * 400 Bad Request: Activation not found.
        * Body:
          ```json
          {
          "status": "Failed",
          "message": "Failed to create activation."
          }
          ```
