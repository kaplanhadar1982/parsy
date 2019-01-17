from . import routes

@routes.route('/',methods=['GET'])
def index():
    return "this is the Zerver speeking"