from flask import Flask,request

app=Flask(__name__)

@app.route("/",methods=["POST","GET"])
def main():
    try:
        if request.method=='POST':
         
            audio=request.files['audio']
            audio_name=audio.filename
            if '.mp3' in audio_name:
            
                
                audio.save(audio_name)

                return {"response":"MP3 file upload successfully"}
            else:
                return {"error":"select you mp3 file"}
    except Exception as e:
        return {"error":str(e)}

if __name__=="__main__":
    app.run("0.0.0.0",debug=True)
    app.run(debug=True,port=8180)