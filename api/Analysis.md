---
layout: default
title: "Analysis API"
subtitle: [{"Get Analysis By Id"}, {"Get All Analysis "}]
---


# Analysis API

## Get Analysis By Id

* URL: /api/get-analysis-by-id/:id
* Method: GET
* Description: Retrieves an analysis by its Id
* URL Parameters:
    * id (integer): The unique ID of the activation to retrieve
* Example Request:
   ```bash
   GET /api/get-analysis-by-id/1
   ```
* Response
    * 200 Ok: Analysis Retrieved successfully
        * Body: A JSON object containing the activation details
        * Example Response:
          ```json
          {
          "id": 1,
          "title": "Title Analysis",
          "description": "test description",
          "content": "test content",
          "analysisType":"basic",
          "coverImage":"xx.jpg",
          "contentImage": "test content"
          }
          ```
    * 400 Bad Request: ID not found.
        * Body:
          ```json
          {"message": "ID not found."}
          ```
----------------------------------

## Get All Analysis 

* URL: /api/get-all-analysis
* Method: GET
* Description: Retrieves a list of all analyses.
* Example Request:
   ```bash
   GET /api/get-all-analysis
   ```
* Response
    * 200 Ok: Successfully retrieved the list of analyses.
        * Body: An array of JSON objects, each representing an analysis.
        * Example Response:
          ```json
          [
           {
          "id": 1,
          "title": "Analysis 1",
          "description": "Description for analysis 1",
          "content": "Content for analysis 1",
          "analysisType": "basic",
          "coverImage": "image1.jpg",
          "contentImage": "content1.jpg"
          },
          {
             "id": 2,
             "title": "Analysis 2",
             "description": "Description for analysis 2",
             "content": "Content for analysis 2",
             "analysisType": "advanced",
             "coverImage": "image2.jpg",
             "contentImage": "content2.jpg"
           }
          ]
          ```
         
    * 400 Bad Request: No data found.
        * Body:
          ```json
          {"message": "No data found."}
          ```
----------------------------------
## Create Analysis

* URL: /api/create-analysis
* Method: POST
* Description: Create a new Analysis
*  Example Request:
   ```bash
   POST  /api/create-analysis
   ```

* Response
    * 201 OK: Analysis created successfully
        * Example Response:
             ```json
             {
             "id":1,
             "title":"Test tittle",
             "description": "Test decription",
             "content": "Test content",
             "analysisType":"Basic",
             "coverImage": "cover.jpg",
             "contentImage":"contentImage.jpg"
             }
             ```
        * Another Example Response:
          ```json
          {
            "id":1,
             "title":"",
             "description": "",
             "content": "Test content",
             "analysisType":"",
             "coverImage": "cover.jpg",
             "contentImage":"contentImage.jpg"
          }

    * 400 Bad Request: Failed to create analysis.
         * Body:
             ```json
             {"message": "Failed to create analysis."}
             ```


-----------------------

## Update Analysis

* URL: /api/update-analysis/:id
* Method: PUT
* Description: Update an Analysis
*  Example Request:
   ```bash
   POST  /api/update-analysis/1
   ```
* Response
    * 200 OK: Analysis updated successfully
        * Example Response:
             ```json
             {
             "id":1,
             "title":"Test tittle updated",
             "description": "Test decription updated",
             "content": "Test content updated",
             "analysisType":"Basic",
             "coverImage": "cover.jpg",
             "contentImage":"contentImage.jpg"
             }
             ```
   * 404 Not Found: Analysis not found.
      * Body:
             ```json
             {"message": "Analysis not found."}
             ```
-------------------------------------
## Delete Analysis

* URL: /api/delete-analysis/:id
* Method: PUT
* Description: Update an Analysis
*  Example Request:
   ```bash
   POST  /api/delete-analysis/1
   ```
* Response
    * 200 OK: Analysis updated successfully
    * 404 Not Found: Analysis not found.
      * Body:
        ```json
        {"message": "Analysis not found."}
        ```


        


