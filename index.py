import json

# set json sesuai soal
data = '{ "name":"Fauzi", "promo":"First Buy Promo", "link":"https://google.com" }'

# load menjadi object
data_object = json.loads(data)

# tapi pada case ini tanpa looping pun berhasil
message = 'Halo '+data_object['name']+', ini ada promo '+data_object['promo']+', bisa di klik di link '+ data_object['link']

print(message)

    