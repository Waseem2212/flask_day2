from flask import Flask,request

app=Flask(__name__)

@app.route("/",methods=["POST","GET"])
def main():
    try:
        if request.method=='POST':
     
            video=request.files['video']
            video_name=video.filename

            if '.mp4' in video_name:                
                video.save(video_name)

                return {"response":"file saved successfully in your current durectory"}
            else:
                return {"error":"select you mp4 file"}
    except Exception as e:
        return {"error":str(e)}

if __name__=="__main__":
    app.run("0.0.0.0",debug=True)