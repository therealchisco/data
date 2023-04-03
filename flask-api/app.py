from flask import Flask, jsonify
from csv_reader import CsvProcessor

app = Flask(__name__)
csv_file_path = 'data/telecom.csv'

@app.route('/', methods=['GET'])
def get_json():
    """
    Returns Data in JSON format using an Object
    of the class CsvProcessor we created and the json_chunk method 
    as the response to a GET request.
    """
    print("Aha")
    try:
        processor = CsvProcessor(csv_file_path,1000)
        json_chunk = processor.json_chunk()
        return json_chunk, 200
    except Exception as e:
        error_message = {'error': str(e)}
        return jsonify(error_message), 500

if __name__ == '__main__':
    app.run()