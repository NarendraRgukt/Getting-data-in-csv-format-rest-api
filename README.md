# Getting-data-in-csv-format-rest-api
It is the Django REST API which allows user to get the data from the server in the format of CSV file<br>
when the user requests the data the it will return the file which contains the information according to the request of user<br><br>
This rest api returns the users that are available in the server<br>
Here we user custom User Model in Django which uses email as username instead of Default User Model<br>

<h2>API Endpoints</h2><br>

<h1>POST-localhost:8000/import/csv/convertion/</h1><br>
This API End point is used to when the user send the data in the list of dictionaries it will convert that data into csv file without saving it in the database<br>

Request Body:<br>
[<br>
{<br>
  "field1": "string",<br>
  "field2": "string"<br>
},<br>

{<br>
  "field1": "string",<br>
  "field2": "string"<br>
}<br>
]<br>

Responses:<br>
STATUS:200<br>

Response Body:<br>
It is the csv file which contains the Json Data as follows<br>
Name of the document:Data.csv<br>
field1,field2<br>
string,string<br>
string,string<br>

<h1>GET-localhost:8000/import-csv/</h1><br>

This API Endpoint is used to get the data from the server in the CSV file format.The headers of the csv file is the fields of the model.<br>
Each row in the csv file represents an object in the model.<br>
Here I used User model for retrieving the data<br>

Responses:
STATUS:200<br>

Response Body:<br>
It is the csv file which contains the data of the user model<br>
Name of the document:Data.csv<br>
field1,field2<br>
string,string<br>
string,string<br>


Here fields are the various fields in the user model like name,email,last_login,is_active,is_staff,is_superuser,permissions,<br>
and each row represents its corresponding values of an object in the model.

