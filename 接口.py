from flask import Flask,request,jsonify
#jsonify作用转换json字符串
app = Flask(__name__)
@app.route('/get')
def get():
    number = request.args.get('number')
    word = request.args.get('word')
    return jsonify({'number':number,'word':word})
#http://127.0.0.1:9000/get?number=123&word=hello


@app.route('/post')
def post():
    json_data = request.get_json()
    number = json_data['number']
    word = json_data['word']
    list = json_data['list']
    dict = json_data['dict']
    max_number=max(list)
    return jsonify({'number':number,'word':word,'list':list,'dict':dict})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)