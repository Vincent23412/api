from flask import Flask, request
import json
import random

app = Flask(__name__)

@app.route('/get_suggestion', methods=['GET'])
def get_suggestion():
    keyword = request.args.get('keyword')
    results = []
    # 根据关键字查询相关的建议词
    # 这里的查询逻辑可以自己实现，这里只是简单示例
    for i in range(random.randint(3, 6)):
        results.append(keyword + str(i))
    return json.dumps(results)

if __name__ == '__main__':
    app.run()
