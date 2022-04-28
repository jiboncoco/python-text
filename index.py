import json

data = '{ "name":"Fauzi", "promo":"First Buy Promo", "link":"https://google.com" }'
data_object = json.loads(data)
pairs = data_object.items()

message = 'Halo '+data_object['name']+', ini ada promo '+data_object['promo']+', bisa di klik di link '+ data_object['link']

print(message)

    