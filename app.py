from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Cab Booking System Backend'

@app.route('/book', methods=['POST'])
def book_cab():
    data = request.json
    pickup = data.get('pickup')
    destination = data.get('destination')

    # Perform booking logic (store in database or any other action)
    response = {'message': 'Booking successful!', 'pickup': pickup, 'destination': destination}

    # Check if the request is from Google Assistant
    if request.headers.get('User-Agent') == 'google-assistant':
        return jsonify({'fulfillmentText': 'Your cab from {} to {} has been booked.'.format(pickup, destination)})
    else:
        return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
