# face_recog_in_py
## how to run the code
make sure u r installed c++, cmake

### Run
pip or pip3 install -r requirements.txt

then run python3 index.py

open postman and send post requst to =>
http://localhost:5000/addimg with body like this ===|>  

{
 
	"img" : "https://www.deccanherald.com/sites/dh/files/articleimages/2020/07/25/trump%20musk-1595659161.jpg",
	
	"faces" : {
		"elon muskss" : "https://upload.wikimedia.org/wikipedia/commons/3/34/Elon_Musk_Royal_Society_%28crop2%29.jpg",
		"jeff bezos" : "https://cdn.britannica.com/56/199056-050-CCC44482/Jeff-Bezos-2017.jpg",
		"donald trumpo" : "https://static.dw.com/image/55598269_303.jpg"
		
	}
}

