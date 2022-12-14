from flask import Flask, request, abort
import pandas as pd

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        #webhook_data = pd.read_csv('/home/grigory/Local/Work/bank131/webhook_data.csv')
        print(request.json)
        data = request.json
        df = pd.json_normalize(data)
        #webhook_data = pd.concate([webhook_data, df], ignore_index=True)
        print(df)
        
        df.to_csv('/home/grigory/Local/Work/bank131/webhook_data.csv')
        return 'success', 200
    else:
        abort(400)

if __name__ == '__main__':
    app.run()