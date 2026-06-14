# Register
curl -X POST http://localhost:8000/auth/register \
`-H "Content-Type: application/json" \
-d '{"name":"Abhishek","email":"abhishek@gmail.com","password":"<password>"}'`

# Login
curl -X POST http://localhost:8000/auth/login \
-H "Content-Type: application/json" \
-d '{"email":"abhishek@gmail.com","password":"<password>"}'

# Use returned token
curl -X GET http://localhost:8000/auth/me \
-H "Authorization: Bearer <token>"