# Activation Endpoints

### Get Activation By Id

* URL: /api/get-activation-by-id/:id
* Method: Get
* Description: Retrieves an activation by its Id
* URL Parameters:
    * id (integer): The unique ID of the activation to retrieve

* Query parameters: None
* Request Body: None
* Response
    * 200 Ok: Activation Retrieved successfully
        * Body: A JSON object containing the activation details
        * Example Response:
          ```json
          {
          "id": 123,
          "name": "Sample Activation",
          "status": "active",
          "createdAt": "2025-01-01T00:00:00Z"
          }
          ```
    * 400 Bad REquest: ID not found.
        * Body:
          ```json
          {"message": "ID not found."}
