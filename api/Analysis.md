---
layout: default
title: "Analysis API"
subtitle: [{"Get Analysis By Id"}, {"Get All Analysis "},{"Create Analysis"}, {"Update Analysis"}, {"Delete Analysis"}]
---


# Analysis API

* Parameters:
   - id:               (number) Unique identifier for the analysis. [Primary Key, Auto-generated]
   - title:            (string) Title of the analysis. [Required]
   - description:      (string) Description of the analysis. [Required]
   - content:          (string) Content or body of the analysis. [Required]
   - analysisType:     (string) Type of the analysis. Defaults to 'basic', other option 'technical'. [Required]
   - coverImage:       (string) URL or path to the cover image. [Required]
   - contentImage:     (string) URL or path to the content image. [Required]


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
   ```json
   {
   "id": 1,
   "title": "Title Analysis",
   "description": "test description",
   "content": "test content",
   "analysisType":"basic",
   "coverImage":"coverImage.png",
   "contentImage": "content.png"
   }
   ```
* Response
    * 200 Ok: Analysis Retrieved successfully
        * Body: A JSON object containing the activation details
        * Example Response:
             ```json
             {
             "statusCode": 200,
             "status": "success",
             "message": "Analysis Retrieved successfully"
             }
             ```
          
    * 400 Bad Request: ID not found.
        * Body:
          ```json
          {
          "statusCode": 400,
          "status": "Failed",
          "message": "ID not found."
          }
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
* Response
    * 200 Ok: Successfully retrieved the list of analyses.
        * Body: An array of JSON objects, each representing an analysis.
        * Example Response:
             ```json
             {
             "statusCode": 200,
             "status": "success",
             "message": "Analysis Retrieved successfully"
             }
             ```
          
         
    * 400 Bad Request: No data found.
        * Body:
          ```json
          {
          "statusCode": 400,
          "status": "Failed",
          "message": "No data found."
          }
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

   * Or:
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
     ```
   
* Response
    * 201 OK: Analysis created successfully
        * Example Response:
             ```json
             {
             "statusCode": 200,
             "status": "success",
             "message": "Analysis created successfully"
             }
             ```

    * 400 Bad Request: Failed to create analysis.
         * Body:
             ```json
             {
             "statusCode": 400,
             "status": "Failed",
             "message": "Failed to create analysis."
             }
             ```


------------------------

## Update Analysis

* URL: /api/update-analysis/:id
* Method: PUT
* Description: Update an Analysis
*  Example Request:
   ```bash
   POST  /api/update-analysis/1
   ```
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
* Response
    * 200 OK: Analysis updated successfully
        * Example Response:
             ```json
             {
             "statusCode": 200,
             "status": "success",
             "message": "Analysis updated successfully"
             }
             ```
   * 404 Not Found: Analysis not found.
      * Body:
         ```json
         {
         "statusCode": 404,
         "status": "Failed",
         "message": "Analysis not found."
         }
         ```
-------------------------------------
## Delete Analysis

* URL: /api/delete-analysis/:id
* Method: DELETE
* Description: Delete an Analysis
*  Example Request:
   ```bash
   POST  /api/delete-analysis/1
   ```
* Response
    * 200 OK: Analysis deleted successfully
         ```json
             {
             "statusCode": 200,
             "status": "success",
             "message": "Analysis deleted successfully"
             }
             ```
    * 404 Not Found: Analysis not found.
      * Body:
        ```json
         {
         "statusCode": 404,
         "status": "Failed",
         "message": "Analysis not found."
         }
         ```

