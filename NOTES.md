# Register
curl -X POST http://localhost:8000/auth/register \
`-H "Content-Type: application/json" \
-d '{"name":"Abhishek","email":"abhishek@gmail.com","password":"secret123"}'`

# Login
curl -X POST http://localhost:8000/auth/login \
-H "Content-Type: application/json" \
-d '{"email":"abhishek@gmail.com","password":"secret123"}'

# Use returned token
curl -X GET http://localhost:8000/auth/me \
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJlNzQwYWZmYi0zMDVlLTRmZDQtYmNhMS1mZWY0ZTJkZTZiZmIiLCJleHAiOjE3ODE1NTMwNjR9.-JR8K4FeIPLzYyyrW88DgBjk1PZxovSID5dlCO5jqVE"