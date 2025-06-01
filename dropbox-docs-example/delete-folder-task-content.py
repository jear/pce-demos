import dropbox
import sys

TOKEN = sys.argv[1]
FOLDER_NAME = morpheus['customOptions']['dbfoldernewname']

dbx = dropbox.Dropbox(TOKEN)
dbx.files_delete_v2(path=f'/morpheus/{FOLDER_NAME}')
