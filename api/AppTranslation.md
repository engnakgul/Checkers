---
layout: default

---


# App Translation API 


* Parameters
    * id (integer): The unique identifier for the translation. [Primary Key, Auto-generated]
    * resource (JSON): A JSON object containing the translation data. [Required]


## Get Translation By Id

* URL:         /api/get-translation-by-id/:id
* Method: GET
* Description: This endpoint retrieves a translation by its **unique id**. The **id** must be provided as a URL parameter. If the translation is successfully retrieved, it will be returned in the response. If the **id** is not found or is invalid, an appropriate error message will be returned.

* URL Parameters:
  * id (integer): The unique identifier for the translation.

* Example Request
  
    ```bash
    GET /api/get-translation-by-id/1
    ```

* Response
  * 200 OK: Translation retrieved successfully.
    * Body
      
      ```json
      {
      "status":  "Successfully retrieved translation"
      "data": {
        "id": 1,
        "text": "Translation text",
        "language": "en"
      }
      }

  * 400 Bad Request: ID not found.
    * Body:
      
      ```json
      {
      "message":"ID not found."
      }


## Get All Translations
* URL: /api/get-translation-by-id/:id
* Method: GET
* Description: This endpoint retrieves all available translations. If translations exist, they will be returned in the response. If no translations are found, an appropriate message will be returned.
* URL parameters: None

* Example Request:
  
  ```bash
  GET /api/apiKeys
  ```

* Response

  * 200 OK: Successfully retrieved translations.

    * Body: A JSON object containing all translations.
    * Example Response:
      
      ```json
      {
      {
      "status": "success",
      "message": "Successfully retrieved translations",
      "data": [
          {
            "id": 1,
            "resource": {
              "en": {
                "greeting": "Hello"
              },
              "tr": {
                "greeting": "Merhaba"
              }
            }
          }
        ]
      }
      }
      ```

    * 400 Bad Request: No translations found.

      * Body:No data found.
        
        ```json
        {
        "message": "No data found."
        }

        ```

## Create Translation API

* URL: /api/create-translation
* Method: POST
* Description:This endpoint allows users to create a new translation entry. The translation data should be provided in the request body as a JSON object. Upon successful creation, the new translation entry is returned in the response.
*  Example Request:
  
   ```bash
   POST /api/translations
   Content-Type: application/json
   
   {
     "resource": {
       "en": "Hello",
       "es": "Hola",
       "fr": "Bonjour"
     }
   }
   ```

* Response

  * 200 OK: Successfully retrieved translations.

    * Body: A JSON object containing all translations.
    * Example Response:
      
      ```json
      {
      "message": "Translation created successfully",
      "data": {
        "id": 1,
        "resource": {
          "en": "Hello",
          "es": "Hola",
          "fr": "Bonjour"
        }
      }
      }
      ```
      
  


## Update Translation API

* URL: /api/create-translation
* Method: POST
* Description:This endpoint allows users to update an existing translation entry by providing the translation ID in the URL and the updated translation data in the request body. If the update is successful, the updated translation is returned in the response.
*  Example Request:
  
   ```bash
   PUT /api/translations/1
   Content-Type: application/json
   
   {
     "resource": {
       "en": "Hi",
       "es": "Hola",
       "fr": "Salut"
     }
   }
   ```

* Response

  * 200 OK: Successfully updated translations.

    * Example Response:
      
      ```json
      {
        "message": "Translation updated successfully",
        "data": {
          "id": 1,
          "resource": {
            "en": "Hi",
            "es": "Hola",
            "fr": "Salut"
          }
        }
      }
      ```
   * 404 Not Found: Translation not found.

     * Body:If no translation is found with the given ID.
        
       ```json
       {
       "message": "Translation not found."
       }
       ```
       
   * 400 Bad Request: Invalid ID parameter.
     
      * Body: If the ID parameter is invalid or missing required fields in the body.
          
        ```json
        {
        "message": "Invalid ID parameter."
        }
        ```


# Delete Translation API

* URL: /api/delete-translation/:id
* Method: DELETE
* Description: This endpoint deletes a specific translation entry identified by its ID. If the deletion is successful, a success message is returned. If the ID is invalid or the translation is not found, an appropriate error message is returned.
* URL Parameters:
     * id (integer): The ID of the translation to delete. [Required]
* Example Request:
  ```bash
  DELETE /api/delete-translation/1
  ```

* Response

  * 200 OK: Successfully deleted translations.

    * Example Response:
      ```json
      {
        "message": "Translation deleted successfully"
      }
      ```
 * 400 Bad Request: If the ID parameter is invalid or not provided.
   ```json
   {
     "message": "Invalid ID parameter."
   }
   ```
* 404 Not Found: If no translation is found with the given ID.
  ```json
  {
     "message": "Translation not found."
   }

   

   
