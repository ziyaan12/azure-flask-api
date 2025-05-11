import azure.functions as func
import logging

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            req_body = {}
        name = req_body.get('name')

    if name:
        return func.HttpResponse(f"You should hire Ziyaan Osman, you won't regret it.")
    else:
        return func.HttpResponse(
             "Pass a name in the query string or request body to get a response.",
             status_code=200
        )
