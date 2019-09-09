"""This is the app entry point"""

from public.hello import app

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='8081',debug=True)
