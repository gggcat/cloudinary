# cloudinary

## .env file

``` .env
CLOUDINARY_URL=cloudinary://XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

## Run example

``` PowerShell
PS > docker-compose run cloudinary  
cloud_name:     xxxxxxxxx
api_key:        999999999999999
api_secret:     ***************XXXX
private_cdn:    False
(2020/03/08 13:14:32) root@d2f1a7b31fc3 /cloudinary-work/example $python -B cloudinary_example.py
--- upload information ----------------------------------------
{'access_mode': 'public',
 'bytes': 3079,
 'created_at': '2020-03-08T04:14:45Z',
 'etag': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
 'format': 'png',
 'height': 295,
 'original_filename': 'test',
 'placeholder': False,
 'public_id': 'test',
 'resource_type': 'image',
 'secure_url': 'https://res.cloudinary.com/xxxxxxxxx/image/upload/v1000000000/test.png',
 'signature': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
 'tags': [],
 'type': 'upload',
 'url': 'http://res.cloudinary.com/xxxxxxxxx/image/upload/v1000000000/test.png',
 'version': 1000000000,
 'width': 631}
---------------------------------------------------------------
Origin image URL: http://res.cloudinary.com/xxxxxxxxx/image/upload/v1000000000/test.png
Origin download file: download_orign_test.png
Effect image URL: http://res.cloudinary.com/xxxxxxxxx/image/upload/f_auto,h_250,q_auto,w_250/test.png
Effect download file: download_effect_test.png
DESTROY: ok
(2020/03/08 13:14:46) root@d2f1a7b31fc3 /cloudinary-work/example $
```

