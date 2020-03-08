import cloudinary
import cloudinary.uploader
import shutil
import requests
from pprint import pprint

#
# 画像ファイルのダウンロード
#
def file_download(download_url, local_file):
    res = requests.get(download_url,stream=True)
    with open(local_file,"wb") as fp:
        shutil.copyfileobj(res.raw,fp)

# https://cloudinary.com/documentation/image_upload_api_reference
#
# 環境変数 CLOUDINARY_URL があれば自動設定のため設定不要
#cloudinary.config(
#  cloud_name = "xxxxxxxxxxx",
#  api_key = "999999999999999",
#  api_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXX"
#)

#
# テストファイル
#
test_target_file='test.png'
test_target_pubid='test'
effect_width=250
effect_height=250

#
# uploadする
#
res_upload = cloudinary.uploader.upload(file=test_target_file, public_id=test_target_pubid)
print("--- upload information ----------------------------------------")
pprint(res_upload)
print("---------------------------------------------------------------")

#
# uploadしたファイルをURLで確認
#
origin_url = res_upload['url']
origin_download_file = 'download_orign_' + test_target_file
file_download(origin_url, 'download_orign_test.png')

print("Origin image URL: {}".format(origin_url))
print("Origin download file: {}".format(origin_download_file))

#
# 画像サイズ変換用のURLを生成し確認
#
effect_url = cloudinary.utils.cloudinary_url(
    test_target_file,
    width=effect_width,
    height=effect_height,
    quality="auto",
    fetch_format="auto",
    secure=False, # HTTPS
)[0]

effect_download_file = 'download_effect_' + test_target_file
file_download(effect_url, effect_download_file)

print("Effect image URL: {}".format(effect_url))
print("Effect download file: {}".format(effect_download_file))

#
# uploadしたイメージの削除
#
res_destroy = cloudinary.uploader.destroy(public_id=test_target_pubid)
print("DESTROY: {}".format(res_destroy['result']))
