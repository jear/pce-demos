# Creating XaaS Instance Types with Morpheus

- This is the code to replicate this [example](https://docs.morpheusdata.com/en/latest/getting_started/guides/xaas_instance.html)

## About Dropbox API
- Personnaly I have created my dropbox account with my gmail.com e-mail and SSO.
- Then created an "App folder" access type, with permissions like in this [example](https://patternica.com/blog/how-to-get-dropbox-api-access-token).
- Then generated the token to be saved in Morpheus Cipher

## About Python script execution
- To execute Python script within Morpheus Appliance or elsewhere, be sure you have install virtualenv

## Using  [Dropbox API Explorer](https://dropbox.github.io/dropbox-api-v2-explorer/#files_create_folder_v2)
```
<%= cypher.read('secret/dropboxtoken') %>
```

## Using Python requests
```
<%= cypher.read('secret/morphapitoken') %>
```

## In the Catalog Item creation, the only thing I have updated is :
```
   "dbfoldername": "<%= customOptions.dbfoldername %>",
```


## At the end of the form, don't forget to add :
![Edit_Catalog_Item](https://github.com/user-attachments/assets/784d6ba5-3892-4fca-8e3a-0114ed8e5acc)
