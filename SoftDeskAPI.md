# Project: SoftDesk API

## End-point: Login User
### Method: POST
>```
>http://127.0.01:8000/api/token/
>```
### Body (**raw**)

```json
{
    "email": "{{userMail}}",
    "password": "{{userPassword}}"
}
```

### Response: 200
```json
{
    "refresh": "{{refreshToken}}",
    "access": "{{accessToken}}"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Refresh Token
### Method: POST
>```
>http://127.0.01:8000/api/token/refresh/
>```
### Body (**raw**)

```json
{
    "refresh": "{{refreshToken}}"
}
```

### Response: 200
```json
{
    "access": "{{accessToken}}"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Get Projects List
### Method: GET
>```
>http://127.0.0.1:8000/api/projects/
>```
### Body (**raw**)

```json

```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|{{accessToken}}|string|


### Response: 200
```json
{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "New Project",
            "description": "A description",
            "type": "BE",
            "author": 1,
            "contributors": [
                1
            ]
        },
        {
            "id": 2,
            "title": "SoftDesk API",
            "description": "A description",
            "type": "BE",
            "author": 1,
            "contributors": []
        },
        {
            "id": 3,
            "title": "SoftDesk Webapp",
            "description": "A description",
            "type": "FE",
            "author": 1,
            "contributors": []
        }
    ]
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Create Project
### Method: POST
>```
>http://127.0.0.1:8000/api/projects/
>```
### Body (**raw**)

```json
{
    "title": "New Project",
    "description": "A description",
    "type": "BE"
}
```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|{{accessToken}}|string|


### Response: 201
```json
{
    "id": 1,
    "title": "New Project",
    "description": "A description",
    "type": "BE",
    "author": 1,
    "contributors": []
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Get Project
### Method: GET
>```
>http://127.0.0.1:8000/api/projects/{{projectID}}
>```
### Body (**raw**)

```json

```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|{{accessToken}}|string|


### Response: 200
```json
{
    "id": 1,
    "title": "New Project",
    "description": "A description",
    "type": "BE",
    "author": 1,
    "contributors": [
        1
    ]
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Edit Project
### Method: PUT
>```
>http://127.0.0.1:8000/api/projects/{{projectID}}/
>```
### Body (**raw**)

```json
{
    "title": "Edit Project",
    "description": "A description",
    "type": "ANDROID"
}
```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|{{accessToken}}|string|


### Response: 200
```json
{
    "id": 1,
    "title": "Edit Project",
    "description": "A description",
    "type": "ANDROID",
    "author": 1,
    "contributors": [
        1
    ]
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Delete Project
### Method: DELETE
>```
>http://127.0.0.1:8000/api/projects/{{projectID}}/
>```
### Body (**raw**)

```json

```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|{{accessToken}}|string|


### Response: 204
```json
null
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Get Issues List
### Method: GET
>```
>http://127.0.0.1:8000/api/projects/{{projectID}}/issues/
>```
### Body (**raw**)

```json

```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|{{accessToken}}|string|


### Response: 200
```json
{
    "count": 4,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "Important issue",
            "description": "A description",
            "tag": "BUG",
            "priority": "HIGH",
            "project": 1,
            "status": "TO_DO",
            "author": 1,
            "assignee_user": 1,
            "created_time": "2022-05-31T16:10:18.774866Z"
        },
        {
            "id": 2,
            "title": "Write doc",
            "description": "A description",
            "tag": "ENHANCEMENT",
            "priority": "LOW",
            "project": 1,
            "status": "DONE",
            "author": 1,
            "assignee_user": 1,
            "created_time": "2022-05-31T16:14:27.788526Z"
        },
        {
            "id": 3,
            "title": "A task",
            "description": "A description",
            "tag": "TASK",
            "priority": "LOW",
            "project": 1,
            "status": "DONE",
            "author": 1,
            "assignee_user": 1,
            "created_time": "2022-05-31T16:16:09.226151Z"
        },
        {
            "id": 4,
            "title": "Issue",
            "description": "A description",
            "tag": "BUG",
            "priority": "NORMAL",
            "project": 1,
            "status": "TO_DO",
            "author": 1,
            "assignee_user": 1,
            "created_time": "2022-05-31T16:16:53.101865Z"
        }
    ]
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Create Issue
### Method: POST
>```
>http://127.0.0.1:8000/api/projects/{{projectID}}/issues/
>```
### Body (**raw**)

```json
{
    "title": "Important issue",
    "description": "A description",
    "tag": "BUG",
    "priority": "HIGH",
    "status": "TO_DO"
}
```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|{{accessToken}}|string|


### Response: 201
```json
{
    "id": 1,
    "title": "Important issue",
    "description": "A description",
    "tag": "BUG",
    "priority": "HIGH",
    "project": 1,
    "status": "TO_DO",
    "author": 1,
    "assignee_user": 1,
    "created_time": "2022-05-31T16:10:18.774866Z"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Get Issue
### Method: GET
>```
>http://127.0.0.1:8000/api/projects/{{projectID}}/issues/{{issueID}}
>```
### Body (**raw**)

```json

```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|{{accessToken}}|string|


### Response: 200
```json
{
    "id": 4,
    "title": "Issue",
    "description": "A description",
    "tag": "BUG",
    "priority": "NORMAL",
    "project": 1,
    "status": "TO_DO",
    "author": 1,
    "assignee_user": 1,
    "created_time": "2022-05-31T16:16:53.101865Z"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Edit Issue
### Method: PUT
>```
>http://127.0.0.1:8000/api/projects/{{projectID}}/issues/{{issueID}}/
>```
### Body (**raw**)

```json
{
    "title": "Edit issue",
    "description": "A description",
    "tag": "BUG",
    "priority": "HIGH",
    "status": "TO_DO"
}
```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|{{accessToken}}|string|


### Response: 200
```json
{
    "id": 4,
    "title": "Edit issue",
    "description": "A description",
    "tag": "BUG",
    "priority": "HIGH",
    "project": 1,
    "status": "TO_DO",
    "author": 1,
    "assignee_user": 1,
    "created_time": "2022-05-31T16:16:53.101865Z"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Delete Issue
### Method: DELETE
>```
>http://127.0.0.1:8000/api/projects/{{projectID}}/issues/{{issueID}}/
>```
### Body (**raw**)

```json

```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|{{accessToken}}|string|


### Response: 204
```json
null
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Get Comments List
### Method: GET
>```
>http://127.0.0.1:8000/api/projects/{{projectID}}/issues/{{issueID}}/comments
>```
### Body (**raw**)

```json

```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|{{accessToken}}|string|


### Response: 200
```json
{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "description": "New comment",
            "author": 1,
            "issue": 1,
            "created_time": "2022-06-01T15:34:41.595524Z"
        },
        {
            "id": 2,
            "description": "A comment",
            "author": 1,
            "issue": 1,
            "created_time": "2022-06-01T15:35:40.726890Z"
        },
        {
            "id": 3,
            "description": "About issue",
            "author": 1,
            "issue": 1,
            "created_time": "2022-06-01T15:36:15.079688Z"
        }
    ]
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Create Comment
### Method: POST
>```
>http://127.0.0.1:8000/api/projects/{{projectID}}/issues/{{issueID}}/comments/
>```
### Body (**raw**)

```json
{
    "description": "A comment"
}
```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|{{accessToken}}|string|


### Response: 201
```json
{
    "id": 1,
    "description": "New comment",
    "author": 1,
    "issue": 1,
    "created_time": "2022-06-01T15:34:41.595524Z"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Get Comment
### Method: GET
>```
>http://127.0.0.1:8000/api/projects/{{projectID}}/issues/{{issueID}}/comments/{{commentID}}
>```
### Body (**raw**)

```json

```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|{{accessToken}}|string|


### Response: 200
```json
{
    "id": 1,
    "description": "New comment",
    "author": 1,
    "issue": 1,
    "created_time": "2022-06-01T15:34:41.595524Z"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Edit Comment
### Method: PUT
>```
>http://127.0.0.1:8000/api/projects/{{projectID}}/issues/{{issueID}}/comments/{{commentID}}/
>```
### Body (**raw**)

```json
{
    "description": "Edited comment"
}
```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|{{accessToken}}|string|


### Response: 200
```json
{
    "id": 3,
    "description": "Edited comment",
    "author": 1,
    "issue": 1,
    "created_time": "2022-06-01T15:36:15.079688Z"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Delete Comment
### Method: DELETE
>```
>http://127.0.0.1:8000/api/projects/{{projectID}}/issues/{{issueID}}/comments/{{commentID}}/
>```
### Body formdata

|Param|value|Type|
|---|---|---|


### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|{{accessToken}}|string|


### Response: 204
```json
null
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
_________________________________________________
Powered By: [postman-to-markdown](https://github.com/bautistaj/postman-to-markdown/)
