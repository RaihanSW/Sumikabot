Sumika Bot

Merupakan sebuah bot yang dapat membalas input dari user. Domain dari bot ini berupa sapaan, perkenalan, dan ekspresi. 

Cara menjalankan program

1. Clone program dari github
2. modifikasi intent yang akan digunakan pada intent.json
3. Install dependencies "pip install -r requirements.txt"
4. jalankan "python train.py" untuk melakukan training agar program dapat mendeteksi intent dari user
5. setelah itu, jalankan "python app.py"
6. chatbot dapat dijalankan pada "localhost:3000"

Dockerfile

Digunakan untuk membuat image pada Docker, dapat jalankan:

1. Docker build -t Sumikabot
2. Docker run Sumikabot

Websocket yang digunakan

1. Heroku, Namun upload terkendala karena ukuran size (maks upload file 500 MB, namun library PYTorch berukuran besar sehingga menutup kemungkinan penggunaan websocket)
2. Firebase, Flask digunakan sebagai servernya dan HTML, CSS, JS digunakan untuk Front-Endnya, kendala dari penggunaan Firebase adalah terkendalanya penggunaan Flask server dikarenakan terhalang untuk menggunakan Google Cloud untuk integrasinya



## Credits:
This repo was used for the frontend code:
https://github.com/hitchcliff/front-end-chatjs
