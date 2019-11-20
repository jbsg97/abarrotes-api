from server import app

#Ejecutar Servicio/Servidor
#if __name__ == '__main__':
    #app.run(debug=True, port=4000)
#    app.run(debug=True, host='172.16.1.108', port=80)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)