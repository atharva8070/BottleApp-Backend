from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process-image', methods=['POST'])
def process_image():
    try:
        # Retrieve the image file from the request
        image_file = request.files['image']
        
        # Process the image using your Python code
        bottle_count = process_image_function(image_file)
        
        # Return the bottle count as a response
        response = {'count': bottle_count}
        return jsonify(response), 200
    
    except KeyError:
        # Handle the case where the 'image' file is not found in the request
        return 'No image file found', 400

def process_image_function(image_file):
    # Add your image processing code here
    # ...
    # Return the bottle count after processing the image
    return 10  # Replace with your actual bottle count

if __name__ == '__main__':
    app.run(debug=True)
