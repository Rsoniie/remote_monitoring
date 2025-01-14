# from app import app

# if __name__ == "__main__":
#     app.run(debug=True)


import os
from app import app
# from flask_cors import CORS



if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000)) 
    app.run(host='0.0.0.0', port=port, debug=True)  
