import dropbox
import sys

TOKEN = sys.argv[1]
FOLDER_NAME = morpheus['customOptions']['dbfoldernewname']
NEW_FOLDER_NAME = morpheus['customOptions']['dbfoldernewname']

dbx = dropbox.Dropbox(TOKEN)
dbx.files_move_v2(from_path=f'/morpheus/{FOLDER_NAME}', to_path=f'/morpheus/{NEW_FOLDER_NAME}', autorename=False)
