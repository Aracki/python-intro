from intro.app import app


# only for debugging within a docker container
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4446, threaded=True, debug=True)

