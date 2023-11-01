#barChart.py
from models.orderModal import OrderDetails
from flask import jsonify, request

def bar_chart(id):
    try:
        month = {
            'january': 0,
            'february': 0,
            'march': 0,
            'april': 0,
            'may': 0,
            'june': 0,
            'july': 0,
            'august': 0,
            'september': 0,
            'october': 0,
            'november': 0,
            'december': 0
        }

        value = OrderDetails.find()
        data = [item for item in value if item['customer']['orderDate'].split('.')[2] == id]

        for item in data:
            m = item['customer']['orderDate'].split('.')[1]
            total = float(item['payment']['Total'])

            if m == '01':
                month['january'] += total
            elif m == '02':
                month['february'] += total
            elif m == '03':
                month['march'] += total
            elif m == '04':
                month['april'] += total
            elif m == '05':
                month['may'] += total
            elif m == '06':
                month['june'] += total
            elif m == '07':
                month['july'] += total
            elif m == '08':
                month['august'] += total
            elif m == '09':
                month['september'] += total
            elif m == '10':
                month['october'] += total
            elif m == '11':
                month['november'] += total
            else:
                month['december'] += total

        return jsonify({
            'statusCode': 200,
            'month': month
        })
    except Exception as error:
        return jsonify({
            'error': str(error),
            'message': "Server Side Error",
            'statusCode': 500
        })
