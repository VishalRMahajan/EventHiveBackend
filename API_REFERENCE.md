
# Auth

### Register

**Endpoint:** `POST /auth/register`

Registers a new user.

#### Request Body

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `usertype`| `str`    | Type of user (e.g., student, committee member) |
| `fname`   | `str`    | First name of the user     |
| `lname`   | `str`    | Last name of the user      |
| `email`   | `str`    | Email address of the user  |
| `password`| `str`    | Password of the user       |

#### Responses

- 201 CREATED: User registered successfully
- 400 BAD REQUEST: Student already exists

### Login

**Endpoint:** `POST /auth/login`

Logs in a user.

#### Request Body

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `usertype`| `str`    | Type of user (e.g., student, committee member) |
| `email`   | `str`    | Email address of the user  |
| `password`| `str`    | Password of the user       |

#### Responses

- 200 OK: Login successful
- 401 UNAUTHORIZED: Invalid credentials

### Protected Route

**Endpoint:** `GET /auth/protected`

Returns user information for authenticated users.

#### Responses

- 200 OK: User is authenticated
- 401 UNAUTHORIZED: User is not logged in





# Fest 

### Add Event

**Endpoint:** `POST /fest/add`

Adds a new event to the database.

#### Request Body

| Parameter        | Type     | Description                       |
| :--------------- | :------- | :-------------------------------- |
| `event_name`     | `str`    | Name of the event                 |
| `committee_name` | `str`    | Name of the organizing committee |
| `contact_person` | `str`    | Contact person for the event      |
| `description`    | `str`    | Description of the event          |
| `Date`           | `str`    | Date of the event                 |
| `Time`           | `str`    | Time of the event                 |
| `Ticket_price`   | `str`    | Ticket price for the event        |
| `venue`          | `str`    | Venue of the event                |
| `phone`          | `str`    | Contact number for the event      |

#### Responses

- 201 CREATED: Event added successfully
- 400 BAD REQUEST: Event already exists

### Get All Events

**Endpoint:** `GET /fest/all`

Retrieves all events from the database.

#### Responses

- List of all events with details.

### Fetch Event

**Endpoint:** `GET /fest/fetch`

Retrieves details of a specific event.

#### Query Parameter

- `event_name`: Name of the event to fetch.

#### Responses

- Event details if found, otherwise returns a 404 Not Found error.

### Get Ticket Price

**Endpoint:** `GET /fest/ticket_price`

Retrieves the ticket price of an event.

#### Query Parameter

- `event_name`: Name of the event to fetch ticket price for.

#### Responses

- Ticket price of the event if found, otherwise returns a 404 Not Found error.


# Profile

### Get User Profile

**Endpoint:** `GET /profile/me`

Returns the profile information of the logged-in user.

#### Responses

- 200 OK: Returns the user's email, role, first name, and last name.
- 401 UNAUTHORIZED: User is not logged in.

### Update User Profile

**Endpoint:** `POST /profile/update`

Updates the first name and last name of the logged-in user.

#### Request Body

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `fname`   | `str`    | Updated first name         |
| `lname`   | `str`    | Updated last name          |

#### Responses

- 200 OK: User profile updated successfully.

### Get All Users

**Endpoint:** `GET /profile/getall`

Returns a list of all user profiles.

#### Responses

- 200 OK: Returns a list of user profiles.


## Payment

### Payment by Email

**Endpoint:** `GET /pay`

Makes a payment using the Razorpay API.

#### Query Parameters

| Parameter   | Type   | Description                    |
|-------------|--------|--------------------------------|
| `amount`    | `int`  | Amount to be paid              |
| `email`     | `str`  | Email address of the user      |
| `event_name`| `str`  | Name of the event              |
| `committee` | `str`  | Name of the organizing committee |

#### Responses

- Renders a payment page with the Razorpay payment form.

### Payment by User

**Endpoint:** `GET /pay/{amount}`

Makes a payment using the Razorpay API for a logged-in user.

#### Query Parameters

| Parameter   | Type   | Description                    |
|-------------|--------|--------------------------------|
| `amount`    | `int`  | Amount to be paid              |

#### Responses

- Renders a payment page with the Razorpay payment form.

### Verify Payment

**Endpoint:** `GET /verify_payment`

Verifies a payment using the Razorpay API.

#### Query Parameters

| Parameter    | Type   | Description                    |
|--------------|--------|--------------------------------|
| `order_id`   | `str`  | ID of the order                |
| `payment_id` | `str`  | ID of the payment              |
| `payment_sign`| `str` | Payment signature              |

#### Responses

- 200 OK: Payment successful
- 400 BAD REQUEST: Payment failed

## Event Management

### Keep Ticket Record

**Endpoint:** `POST /addeventdb`

This Endpoint keeps record of user who have booked ticket by using following details

#### Request Body

| Parameter        | Type   | Description                                   |
|------------------|--------|-----------------------------------------------|
| `email`          | `str`  | Email address of the user                     |
| `event_name`     | `str`  | Name of the event                             |
| `committee`      | `str`  | Name of the organizing committee              |

#### Responses

- 200 OK: Event added successfully
- 400 BAD REQUEST: Event already exists

### Check if User is Registered for Event

**Endpoint:** `POST /checkifregistered`

Checks if a user is registered for a specific event.

#### Request Body

| Parameter        | Type   | Description                                   |
|------------------|--------|-----------------------------------------------|
| `email`          | `str`  | Email address of the user                     |
| `event_name`     | `str`  | Name of the event                             |
| `committee`      | `str`  | Name of the organizing committee              |

#### Responses

- 200 OK: User is registered for the event
- 400 BAD REQUEST: User is not registered for the event

### Verify Ticket

**Endpoint:** `POST /verify_ticket`

Verifies a ticket for a specific event.

#### Request Body

| Parameter        | Type   | Description                                   |
|------------------|--------|-----------------------------------------------|
| `event_name`     | `str`  | Name of the event                             |
| `email`          | `str`  | Email address of the user                     |
| `committee`      | `str`  | Name of the organizing committee              |

#### Responses

- 200 OK: Ticket is verified
- 400 BAD REQUEST: Ticket is not verified

### Get Booked Ticket Data

**Endpoint:** `POST /bookedticketdata`

Retrieves data for all booked tickets for a specific committee.

#### Request Body

| Parameter        | Type   | Description                                   |
|------------------|--------|-----------------------------------------------|
| `committee`      | `str`  | Name of the organizing committee              |

#### Responses

- List of all booked tickets with user details


