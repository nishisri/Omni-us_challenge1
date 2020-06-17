import json

class Response:
    def __init__(self, document_id, collection_id, status, file_name, created_date, revision_number):
        self.document_id = document_id
        self.collection_id = collection_id
        self.status = status
        self.file_name = file_name
        self.created_date = created_date
        self.revision_number = revision_number


def json_read_items():
    with open('api-response.json', 'r') as json_file:
        response_data = json.loads(json_file.read())
    return [Response(**k) for k in response_data['payload']['items']]