---
layout: default

---


# App Translation API 


* Parameters
    * id (integer): The unique identifier for the translation. [Primary Key, Auto-generated]
    * resource (JSON): A JSON object containing the translation data. [Required]


## Get Translation By Id

* URL: /api/get-translation-by-id/:id
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






  


      
