---
layout: default
title: "Analysis API"
---


# Analysis API

### Get Analysis By Id

**URL**: /api/get-analysis-by-id/:id
**Method**: Get
**Description**: Retrieves an analysis by its Id
**URL Parameters**:
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
    * 400 Bad REquest: ID not found.
        * Body:
          ```json
          {"message": "ID not found."}

