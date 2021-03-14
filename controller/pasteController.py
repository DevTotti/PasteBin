from flask_restful import Resource
from flask import Response, request, jsonify
from models.pasteModel import Paste, DeleteExpired
import string, random
from urllib.parse import urlparse
import os, json
from middleware.errors import invalid_request



class PasteAPI(Resource):

    def __init__(self):

        self.database = Paste
        
        self.host = request.host_url


    def post(self) -> Response:

        pasteMetadata = request.get_json()['pasteMetadata']
        
        paste_code = self.get_paste_code()
        
        pasteMetadata['paste_code'] = paste_code
        
        db = self.database

        try:

            post_data = db(**pasteMetadata).save()
            
            result = {'obj_id': str(post_data.id), 'date': str(post_data.created), 'expiry': str(post_data.expiration)}

            save_expiry = DeleteExpired(**result).save()

            new_url = self.host + post_data.paste_code

            new_result_ = {'id': str(post_data.id), 'code': post_data.paste_code, 'url': new_url}
            
            response = jsonify({"result": new_result_})
            
            response.status_code = 200
            
            return response
        
        except Exception as error:

            print(error)

            if error.__class__.__name__ == 'ValidationError':

                return invalid_request()

            else:

                return Response(status=500)
            


    def generate_encode(self):

        text = [''.join([random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for n in range(6)])]

        random.shuffle(text)

        short_code = ''.join(text)

        return short_code



    def get_paste_code(self):

        code_db = Paste

        paste_code = ''

        exist = True

        while exist:

            short_code = self.generate_encode()

            try:
                response = code_db.objects.get(paste_code=short_code)
                
                exist = True

            except:

                paste_code = short_code

                exist = False

        return paste_code



class PasteOtherAPI(Resource):

    def __init__(self):
        self.database = Paste
        self.host = request.host_url

    def get(self, shortCode: str) -> Response:

        db = self.database
        
        if shortCode:
            try:
                data = db.objects.get(paste_code=shortCode)
                pass_wrd = data['password']
                
                if pass_wrd != '':
                    try:

                        password = request.get_json()['password']

                        if pass_wrd == password:
                            content = {"text": data['text']}
                            response = jsonify(content)

                            return response

                        else:
                            return invalid_request


                    except:
                        return invalid_request

                else:
                    content = {"text": data['text']}
                    response = jsonify(content)

                    return response

            except:
                return invalid_request

        else:

            return invalid_request


            