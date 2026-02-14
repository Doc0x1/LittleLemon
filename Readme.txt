API Endpoints for Testing
=========================

Authentication
--------------
/auth/users/                    - User registration (POST)
/auth/token/login/              - Obtain auth token (POST: username, password)
/auth/token/logout/             - Logout / destroy token (POST, requires token)

Menu API
--------
/restaurant/menu/               - List all menu items (GET) / Create item (POST)
/restaurant/menu/<id>/          - Retrieve (GET), Update (PUT/PATCH), Delete (DELETE) a menu item

Table Booking API
-----------------
/restaurant/booking/tables/     - List all bookings (GET) / Create booking (POST)
/restaurant/booking/tables/<id>/ - Retrieve (GET), Update (PUT/PATCH), Delete (DELETE) a booking

All Menu and Booking endpoints require authentication.
Include the token in request headers: Authorization: Token <your-token>
