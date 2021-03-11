from flask_restful import Api
from controller.pasteController import PasteAPI

def api_routes(api: Api):
    api.add_resource(PasteAPI, '/')

    return api