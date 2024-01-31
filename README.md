# SMService

This web project is built using Django, allowing users to send SMS messages through the Twilio service. It includes HTML form endpoints for user input and a REST API endpoint for JSON requests.

## Get started

### ⚙️ _Installation_

1. **Clone the repository**:

   ```bash
   git clone https://github.com/YuliaHladyshkevych/SMService
   cd sms_service
   
2. If you are using PyCharm - it may propose you automatically create venv for your project and install requirements in it, but if not:
   ```bash
   python -m venv venv
   venv\Scripts\activate (on Windows)
   source venv/bin/activate (on macOS)
3. You can open the project in IDE and configure .env file using .env.sample file 
as an example.

   
4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
5. **Apply database migrations:**
   ```bash
   python manage.py migrate
6. **Start the development server:**
   ```bash
   python manage.py runserver

## Endpoints
 1. `/home/ GET`

Access the home page with an HTML form for phone number and message input.

 2. `/send-sms/ POST`

Handles the HTML form submission from `/home/` and sends an SMS using Twilio.

 3. `/api/v1/send-sms/ POST`

Accepts JSON requests with the following structure:

```json
{
   "phone": "<some phone>",
   "message": "<some message>"
}
```

Sends an SMS to the specified phone number with the provided message.

## Logging

All sent SMS messages are logged in the `logs` file.


Feel free to explore and modify the project according to your needs.
