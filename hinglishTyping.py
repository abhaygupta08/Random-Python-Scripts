textinput = input('TEXT: ')


'''
single single go to this operation try with string split then send the get request and sotre those res which are on top priority according to resp of result object
'''

url = 'https://inputtools.google.com/request?text='+texturl+'&itc=hi-t-i0-und&num=4&cp=0&cs=1&ie=utf-8&oe=utf-8&app=demopage'

reuslt = request.get('url').text