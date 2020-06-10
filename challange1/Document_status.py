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


def doc_status():
    responses = json_read_items()
    result = {}
    for res in responses:
        key = res.status
        if key not in result:
            temp = {"sum": 0, "docs": []}
            result[key] = temp

        result[key]["docs"].append(res)
        result[key]["sum"] = result[key]["sum"] + 1
    return result


def find_by_status(status):
    return doc_status()[status]["docs"]


def find_by_file_name(file_name):
    responses = json_read_items()
    result = []
    for res in responses:
        if res.file_name == file_name:
            result.append(res)
    return result
