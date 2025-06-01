import dropbox
import sys

TOKEN = sys.argv[1]
FOLDER_NAME = morpheus['customOptions']['dbfoldername']

dbx = dropbox.Dropbox(TOKEN)
dbx.files_create_folder_v2(path=f'/morpheus/{FOLDER_NAME}', autorename=False)
