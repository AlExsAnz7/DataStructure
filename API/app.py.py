#create 
#stores

POST /store {"name": "alex_store", "items": []}

#items
POST /store/alex_store/item {"name": "cellphone", "price": 189.67}

#GET
GET /store
GET /store/alex_store

{

        "stores": [
        {
                
                "name": "alex_store", 
                "items": [
                {

                        "name": "cellphone", 
                        "price": 189.67
                }     
            ]
         }
    ]
}