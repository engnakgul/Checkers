# Endpoints

## Activation API

### Get Activation By ID
* URL:/api/get-activation-by-id/:id
* Method: GET
* Description: Retrieves an activation by its ID
* URL Parameters:
    * id (integer): The ID of the activation to retrieve
* Query Parameters: None
* Request Body: None
* Response:
    * 200 OK: Activation retrieved successfully
        * Body: A JSON object containing the activation details.
        * Example Response:
            ```json
            {
            "id":1,
            "mt5ID": "testmt5id",
            "mt5Value":"testmt5value",
            "mt5Description": "test activation description"
            }

        * 400 Bad Request: ID not found
            * Body:
              ```json 
              {"message": "ID not found."}

