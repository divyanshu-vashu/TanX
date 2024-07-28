# TanX Assignment
## Create a price alert application that triggers an email when the user’s target price is Achieved.


<img width="1280" alt="image" src="https://github.com/user-attachments/assets/6eb6ce5a-5c72-46d4-a87d-d4fbfb7fa5ab">


# HOME PAGE : 
`http://127.0.0.1:8000/`

# Now 3 Api 
## 1.Fetch all Alert 

`curl -X GET "http://localhost:8000/api/alerts/"`

<p> Or `http://localhost:8000/api/alerts/` search on browser</p>

//change line --make space

## 2. Create a New Alert:

  `curl -X POST "http://localhost:8000/api/alerts/" -H "Content-Type: application/json" -d '{"email": "vdkalife@gmail.com", "target_price": 70000.00}' `
## 3. Delete an Alert : 

`curl -X DELETE "http://localhost:8000/api/alerts/delete/1/"`




