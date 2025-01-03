# ApiKey API

This documentation clearly specifies how to retrieve all API keys and the expected response.

* Parameters:
    - id: (number) Unique identifier for the record. [Primary Key, Auto-generated]
    - companyId: (number) The ID of the associated company. [Required]
    - apiKey: (string) The API key associated with the company. [Required]

## Add Api Key

* URL: /api/apiKey
* Method: POST
* Description: This endpoint creates a new API key for a specific company. The **companyId** parameter must be provided in the request body. If the API key is successfully created, it will be returned in the response. In case of missing fields or an error, an appropriate message will be returned.
* Request Body:
    * companyId (integer): The ID of the company for which the API key will be created. [Required]
* Example Request:
  ```bash
  POST /api/apiKey
  ```
  ```json
      {
      "companyId": 123
     }
  ```

* Response
    * 201 Created: API key added successfully.
        * Body: A JSON object containing the newly created API key.
        * Example Response:
          ```json
           {
           "status": "success",
           "message": "API key added successfully",
           "data": {
            "apiKey": "new-generated-api-key"
            }
           }
           ```
    * 400 Bad Request: ID not found.
        * Body:
          ```json
          {
          "status": "failed",
          "message": "Missing required fields. Required fields are: companyId."
          }

          ```
          OR
          ```json
          {
          "status": "failed",
          "message": "Could not create API key."
          }
          ```


## Regenerate Api Key 

* URL: /api/apiKey
* Method: PUT
* Description: This endpoint regenerates an API key for a specific company. The accessToken, userIdInToken, and password must be provided in the request. If the API key is successfully regenerated, it will return a success message. If the required fields are missing or the regeneration fails, an appropriate error message will be returned.
* Request Body:
  * companyId (integer): The ID of the company for which the API key is to be regenerated. [Required]
  * password (string): The password to validate the request. [Required]
    
* Query Parameters:
    * accessToken (string): The access token for authentication. [Required]
    * userIdInToken (string): The user ID in the access token. [Required]
      
* Example Request:
  ```bash
  POST /api/apiKey?accessToken=abc1&userIdInToken=1
  ```
  ```json
  {
  "companyId": 123,
  "password": "user-password"
  }
  ```

* Response
   * 200 OK: Api key regenareted successfully
   * Body: A JSON object containing the success message.
   * Example Response:
       ```json
       {
       "status": "success",
       "message": "API key regenerated successfully"
       }
       ```
   * 400 Bad Request: Missing required fields or unable to regenerate the API key.
       * Body
           ```json
           {
           "status": "Failed",
           "message": "Missing required fields. Required fields are: companyId, accessToken, password."
           }
           ```


## Get Api Key By User Id

* URL: /api/apiKey
* Method: GET
* Description:This endpoint retrieves the API key associated with a specific user ID. The userIdInToken parameter must be provided in the query string. If the API key is found, it will be returned in the response. In case of missing fields or an error, an appropriate message will be returned.
* Query Parameters:
      * userIdInToken (integer): The unique user ID used to fetch the API key. [Required]

* Example Request
  ```bash
  GET /api/apiKey?userIdInToken=12345
  ```

* Response
    * 200 OK: Successfully retrieved the Api Key
      * Body: A JSON object containing the api key data
      
      * Example Response
      ```json
      {
      "status": "success",
      "message": "Successfully.",
      "data": {
      "companyId": 1,
      "apiKey": "abcdef123456"
      }
      }
      ```
    * 400 Bad Request: userId not found.
        ```json
          {
          "status": "failed",
          "message": "userId not found.",
          "data": null
          }
        ```


## Get All Api Keys

* URL: /api/apiKeys
* Method: GET
* Description: This endpoint retrieves all API keys stored in the system. The response will include all available API keys. If no data is found, an appropriate message will be returned.
* Example Request
  ```bash
  GET /api/apiKeys
  ```

* Response
    * 200 OK: Successfully retrieved all API keys.
      * Body: A JSON object containing the API keys.
      * Example Response

      ```json
      {
      "status": "success",
      "message": "Successfully retrieved all API keys.",
      "data": [
          {
          "companyId": 1,
          "apiKey": "abcdef123456"
          },
          {
          "companyId": 2,
          "apiKey": "ghijk987654"
          }
      ]
      }
      ``` 

## Delete Api Key

* URL: /api/apiKey
* Method: DELETE
* Description: This endpoint deletes an API key associated with the provided id. The id parameter must be passed as a query parameter. If the API key is successfully deleted, a success message will be returned. In case of missing id or failure to delete, an appropriate error message will be returned.
* URL parameters
      * id (integer): The unique identifier for the API key to be deleted.
* Example Request:
  ```bash
  DELETE /api/apiKey?id=1
  ```

* Response
    * 200 OK: API Key deleted successfully.
      * Body:
        ```json
        {
          "message": "Successfully"
        }
        ```
    * 400 Bad Request: id not found or invalid
      ```json
      {
        "mesage": "id not found."
      }
  


