import json
import requests


def delete_customer():
    headers = {
       'Authorization': 'token 91736f269c3111b:c8198224c1bfcde'
   }
    url_customer= "https://venturitech.erpnext.com/api/resource/Customer?limit_page_length=500"
    resp = requests.get(url=url_customer, headers=headers)
    
    for r in resp.json()["data"]:
        requests.delete(url=f"https://venturitech.erpnext.com/api/resource/Customer/{r['name']}", headers=headers)

def uploading_items():
   local_url = f"http://test7:8001/files/BOMs_RX1000 Differential Machine(2) - BOMs_RX1000 Differential Machine(2).csv.csv"
   local_headers=  {
        'Authorization': 'token a8674cc266d8ff7:06dd260f1406e35'
   }
   headers = {
       'Authorization': 'token 91736f269c3111b:c469c17f7deb14e'
   }
   url_uom = "https://venturitech.erpnext.com/api/resource/UOM"
   response = requests.get(local_url, headers=local_headers)
   content = response.content.decode('utf-8')
   reader = csv.reader(content.splitlines(), delimiter=',')
   for row in reader:
       try:
           uom = {}
           uom["uom_name"] = row[5]
           requests.post(url=url_uom, headers=headers, data=json.dumps(uom))
           url_item = f"https://venturitech.erpnext.com/api/resource/Item"
           item= {}
           item["quickbooks_id"] = row[0]
           item["item_name"] = row[2]
           item["item_code"] = row[1]
           item["description"] = row[3]
           item["stock_uom"] = row[5].strip()
           item["is_stock_item"] = 1
           item["item_group"]  = "Component"
           item["min_order_qty"] = row[4]
           item["last_purchase_rate"] = row[6].replace("$", "").strip()
           requests.post(url=url_item, headers=headers, data=json.dumps(item))
       except Exception as e:
           print(f"{e}")

def delete_items():
    local_url = "http://test7:8001/files/BOMs - RX3N1 Coolant Machinec524d6.csv"
    local_headers=  {
        'Authorization': 'token a8674cc266d8ff7:06dd260f1406e35'
   }
    headers = {
       'Authorization': 'token 91736f269c3111b:c469c17f7deb14e'
   }
    item_url = "https://venturitech.erpnext.com/api/resource/Item"
    response = requests.get(local_url, headers=local_headers)
    content = response.content.decode('utf-8')
    reader = csv.reader(content.splitlines(), delimiter=',')
    for row in reader:
        resp = requests.delete(url=f"https://venturitech.erpnext.com/api/resource/Item/{row[1]}", headers=headers)
        print(f"{resp.json()}")




def uploading_customers():
   local_url = f"http://test7:8001/files/customer.CSV - customer.csv"
   local_headers=  {
       'Authorization': 'token 22e108996b738c9:29ffae749384efc'
   }
   headers = {
       'Authorization': 'token 91736f269c3111b:c469c17f7deb14e'
   }
  
   url_customer= "https://venturitech.erpnext.com/api/resource/Customer"
   response = requests.get(local_url, headers=local_headers)
   content = response.content.decode('utf-8')
   reader = csv.reader(content.splitlines(), delimiter=',')
   for row in reader:
       try:
           customer= {}
           customer["customer_name"] = row[0]
           customer["territory"] = "All Territories"
           customer["customer_group"] = "Commercial"
           customer["customer_type"] = "Individual"
           requests.post(url=url_customer, headers=headers, data=json.dumps(customer))
       except Exception as e:
           print(f"{e}")


def uploading_supplier():
   local_url = f"http://test7:8001/files/vendors.CSV"
   local_headers=  {
       'Authorization': 'token a8674cc266d8ff7:06dd260f1406e35'
   }
   headers = {
       'Authorization':'token 91736f269c3111b:c469c17f7deb14e'
   }
  
   url_customer= "https://venturitech.erpnext.com/api/resource/Supplier"
   local_url_customer = "http://test7:8001/api/resource/Supplier"
   response = requests.get(local_url, headers=local_headers)
   content = response.content.decode('utf-8')
   reader = csv.reader(content.splitlines(), delimiter=',')
   for row in reader:
       try:
           customer= {}
           customer["supplier_name"] = row[2]
           customer["supplier_group"] = "All Supplier Groups"
           customer["supplier_type"] = "Company"
           requests.post(url=local_url_customer, headers=local_headers, data=json.dumps(customer))
       except Exception as e:
           print(f"{e}")

def create_address_billing():
   local_url = f"http://test7:8001/files/customer.CSV - customer.csv"
   local_headers=  {
        'Authorization': 'token a8674cc266d8ff7:06dd260f1406e35'
   }
   headers = {
       'Authorization': 'token 91736f269c3111b:c469c17f7deb14e'
   }
  
   response = requests.get(local_url, headers=local_headers)
   content = response.content.decode('utf-8')
   reader = csv.reader(content.splitlines(), delimiter=',')
   for row in reader:
        try:
           
            url_item = f"https://venturitech.erpnext.com/api/resource/Address"
            local_url_item = f"http://test7:8001/api/resource/Address"
            address= {}
            address["address_title"]= row[0]
            address["address_type"] = "Billing"
            address["address_line1"] = row[1]
            address["address_line2"] = row[1]
            address["city"] = row[15]
            # address["custom_secondary_contact"] = row[14]
            # address["custom_alt_phone"] = row[13]
            # address["custom_first_name"] = row[7]
            # address["custom_last_name"] = row[9]
            address["custom_primary_contact"] = row[4]
            address["email_id"] = row[2]
            address["phone"] = row[5]
            address["state"] = row[16]
            address["pin_code"] = row[17]
            address["country"] = row[18]
            # address["fax"] = row[12]
            address["is_primary_address"] = 1
            address["links"] = [{"link_doctype":"Customer", "link_name":row[0]}]
            requests.post(url=url_item, headers=headers, data=json.dumps(address))
            requests.put(url=f"https://venturitech.erpnext.com/api/resource/Customer/{row[0]}", headers=headers, data=json.dumps({"customer_primary_address":f"{row[0]}-Billing"}))
        except Exception as e:
           print(f"{e}")

def create_address_customer_shipping():
   local_url = f"http://test7:8001/files/customer.CSV - customer.csv"
   local_headers=  {
        'Authorization': 'token a8674cc266d8ff7:06dd260f1406e35'
   }
   headers = {
      'Authorization': 'token 91736f269c3111b:c469c17f7deb14e'
   }
  
   response = requests.get(local_url, headers=local_headers)
   content = response.content.decode('utf-8')
   reader = csv.reader(content.splitlines(), delimiter=',')
   for row in reader:
        try:
           
            url_item = f"https://venturitech.erpnext.com/api/resource/Address"
            local_url_item = f"http://test7:8001/api/resource/Address"
            address= {}
            address["address_title"]= row[0]
            address["address_type"] = "Shipping"
            address["address_line1"] = "{0}\n{1}".format(row[7], row[8])
            address["address_line2"] = "{0}\n{1}\n{2}".format(row[9], row[10], row[11])
            address["city"] = row[15]
            # address["custom_secondary_contact"] = row[14]
            # address["custom_alt_phone"] = row[13]
            # address["custom_first_name"] = row[7]
            # address["custom_last_name"] = row[9]
            address["custom_primary_contact"] = row[4]
            address["email_id"] = row[2]
            address["phone"] = row[5]
            # address["fax"] = row[12]
            address["state"] = row[16]
            address["pin_code"] = row[17]
            address["country"] = row[18]
            address["is_shipping_address"] = 1
            address["links"] = [{"link_doctype":"Customer", "link_name":row[0]}]
            requests.post(url=url_item, headers=headers, data=json.dumps(address))
            #requests.put(url=f"https://venturitech.erpnext.com/api/resource/Customer/{row[0]}", headers=headers, data=json.dumps({"customer_primary_address":f"{row[0]}-Billing"}))
        except Exception as e:
           print(f"{e}")

def create_contact_customer():
   local_url = f"http://test7:8001/files/customer.CSV - customere33cac.csv"
   local_headers=  {
       'Authorization': 'token a8674cc266d8ff7:06dd260f1406e35'
   }
   headers = {
       'Authorization': 'token 91736f269c3111b:c469c17f7deb14e'
   }
  
   response = requests.get(local_url, headers=local_headers)
   content = response.content.decode('utf-8')
   reader = csv.reader(content.splitlines(), delimiter=',')
   for row in reader:
       try:
            requests.put(url=f"https://venturitech.erpnext.com/api/resource/Customer/{row[0]}", headers=headers, data=json.dumps({"customer_primary_contact":f"{row[0]}-{row[0]}"}))

        #    url_item = f"https://venturitech.erpnext.com/api/resource/Contact"
        #    customer= {}
        #    if row[2] != '':
        #         customer["first_name"] = row[0]
        #         customer["company_name"] = row[0]
        #         customer["links"] = [{"link_doctype":"Customer", "link_name":row[0]}]
        #         if row[2] != '':
        #             customer["email_ids"] = [{"email_id": row[2], "is_primary":1}]
        #         if row[3] != '':
        #             customer["email_ids"] = [{"email_id": row[3]}]
        #         resp = requests.post(url=url_item, headers=headers, data=json.dumps(customer))
        #         #print(f"{resp.json()}")
       except Exception as e:
           print(f"{e}")

def create_supplier_billing():
   local_url = f"http://test7:8001/files/vendors.CSV"
   local_headers=  {
        'Authorization': 'token a8674cc266d8ff7:06dd260f1406e35'
   }
   headers = {
       'Authorization': 'token 91736f269c3111b:c8198224c1bfcde'
   }
  
   response = requests.get(local_url, headers=local_headers)
   content = response.content.decode('utf-8')
   reader = csv.reader(content.splitlines(), delimiter=',')
   for row in reader:
        try:
           
            url_item = f"https://venturitech.erpnext.com/api/resource/Address"
            local_url_item = f"http://test7:8001/api/resource/Address"
            address= {}
            address["address_title"]= row[2]
            address["address_type"] = "Billing"
            address["address_line1"] = "{0}\n{1}".format(row[10], row[11])
            address["address_line2"] = "{0}\n{1}".format(row[12], row[13])
            address["city"] = row[10]
            address["custom_secondary_contact"] = row[25]
            address["custom_alt_phone"] = row[24]
            address["custom_first_name"] = row[7]
            address["custom_last_name"] = row[9]
            address["custom_primary_contact"] = row[20]
        #    address["email_id"] = row[3]
            address["phone"] = row[22]
            address["fax"] = row[23]
            address["is_primary_address"] = 1
            address["links"] = [{"link_doctype":"Supplier", "link_name":row[2]}]
            requests.post(url=url_item, headers=headers, data=json.dumps(address))
            requests.put(url=f"https://venturitech.erpnext.com/api/resource/Supplier/{row[2]}", headers=headers, data=json.dumps({"supplier_primary_address":f"{row[2]} - Billing"}))
        except Exception as e:
           print(f"{e}")

def create_address_shipping():
   local_url = f"http://test7:8001/files/vendors.CSV"
   local_headers=  {
        'Authorization': 'token a8674cc266d8ff7:06dd260f1406e35'
   }
   headers = {
       'Authorization': 'token 91736f269c3111b:c8198224c1bfcde'
   }
  
   response = requests.get(local_url, headers=local_headers)
   content = response.content.decode('utf-8')
   reader = csv.reader(content.splitlines(), delimiter=',')
   for row in reader:
       try:
            if row[15] != '':
                url_item = f"https://venturitech.erpnext.com/api/resource/Address"
                local_url_item = f"http://test7:8001/api/resource/Address"
                address= {}
                address["address_title"]= row[2]
                address["address_type"] = "Shipping"
                address["address_line1"] = "{0}\n{1}".format(row[15], row[16])
                address["address_line2"] = "{0}\n{1}".format(row[17], row[18])
                address["city"] = row[10]
                address["custom_secondary_contact"] = row[25]
                address["custom_alt_phone"] = row[24]
                address["custom_first_name"] = row[7]
                address["custom_last_name"] = row[9]
                address["custom_primary_contact"] = row[20]
                #    address["email_id"] = row[3]
                address["phone"] = row[22]
                address["fax"] = row[23]
                address["is_shipping_address"] = 1
                address["links"] = [{"link_doctype":"Supplier", "link_name":row[2]}]
                requests.post(url=url_item, headers=headers, data=json.dumps(address))
        #requests.put(url=f"https://venturitech.erpnext.com/api/resource/Supplier/{row[2]}", headers=headers, data=json.dumps({"supplier_primary_address":f"{row[2]} - Billing"}))
       except Exception as e:
           print(f"{e}")


def create_contact():
   local_url = f"http://test7:8001/files/vendors.CSV"
   local_headers=  {
       'Authorization': 'token a8674cc266d8ff7:06dd260f1406e35'
   }
   headers = {
       'Authorization': 'token 91736f269c3111b:c8198224c1bfcde'
   }
  
   response = requests.get(local_url, headers=local_headers)
   content = response.content.decode('utf-8')
   reader = csv.reader(content.splitlines(), delimiter=',')
   for row in reader:
       try:


           url_item = f"https://venturitech.erpnext.com/api/resource/Contact"
           customer= {}
           if row[7] != '':
                customer["first_name"] = row[7]
                customer["last_name"] = row[9]
                customer["salutation"] = row[6]
                customer["designation"] = row[21]
                customer["company_name"] = row[5]
                customer["links"] = [{"link_doctype":"Supplier", "link_name":row[2]}]
                requests.post(url=url_item, headers=headers, data=json.dumps(customer))
       except Exception as e:
           print(f"{e}")

def update_supplier_details():
   local_url = f"http://test7:8001/files/vendors.CSV"
   local_headers=  {
        'Authorization': 'token a8674cc266d8ff7:06dd260f1406e35'
   }
   headers = {
       'Authorization': 'token 91736f269c3111b:c8198224c1bfcde'
   }
  
   response = requests.get(local_url, headers=local_headers)
   content = response.content.decode('utf-8')
   reader = csv.reader(content.splitlines(), delimiter=',')
   for row in reader:
       try:
         requests.put(url=f"https://venturitech.erpnext.com/api/resource/Supplier/{row[2]}", headers=headers, data=json.dumps({"supplier_primary_address":f"{row[2]}-Billing"}))
         if row[7] != '' and row[9] == '':
             requests.put(url=f"https://venturitech.erpnext.com/api/resource/Supplier/{row[2]}", headers=headers, data=json.dumps({"supplier_primary_contact":f"{row[7]}-{row[2]}"}))    
         if row[7] != '' and row[9] != '':
             requests.put(url=f"https://venturitech.erpnext.com/api/resource/Supplier/{row[2]}", headers=headers, data=json.dumps({"supplier_primary_contact":f"{row[7]} {row[9]}-{row[2]}"}))   
       except Exception as e:
           print(f"{e}")      
           


def create_bom():
   local_url = "http://test7:8001/files/BOMs_RX1000 Differential Machine(2) - BOMs_RX1000 Differential Machine(2).csv (1).csv"
   local_headers=  {
        'Authorization': 'token a8674cc266d8ff7:06dd260f1406e35'
   }
   headers = {
       'Authorization': 'token 91736f269c3111b:c469c17f7deb14e'
   }
  
   url_bom = "https://venturitech.erpnext.com/api/resource/BOM"
   response = requests.get(local_url, headers=local_headers)
   content = response.content.decode('utf-8')
   reader = csv.reader(content.splitlines(), delimiter=',')
   items = []
   for row in reader:
        requests.put(url=f"https://venturitech.erpnext.com/api/resource/Item/{row[1]}", headers=headers, data=json.dumps({"last_purchase_rate":row[6].replace("$", "").strip()}))
        items.append({
            "item_code": row[1],
           "item_name": row[2],
           "qty": row[4],
           "rate":row[6],
           "description": row[3]
        })
   try:
       bom = {}
       bom["item"] = "10505"
       bom["uom"] = "Unit"
       bom["quantity"] = 1
       bom["rm_cost_as_per"] = "Last Purchase Rate"
       bom["items"] = items
       bom["docstatus"] = 0
       res = requests.post(url=url_bom, headers=headers, data=json.dumps(bom))
       print(f"{res.text}")
   except Exception as e:
       print(f"{e} ")

def create_stock_entry():
   local_url = "http://test7:8001/files/BOMs_RX555 Brake Machine - BOMs_RX555 Brake Machine.csv.csv"
   local_headers=  {
        'Authorization': 'token a8674cc266d8ff7:06dd260f1406e35'
   }
   headers = {
       'Authorization': 'token 91736f269c3111b:c469c17f7deb14e'
   }
  
   url_bom = "https://venturitech.erpnext.com/api/resource/Stock Entry"
   response = requests.get(local_url, headers=local_headers)
   content = response.content.decode('utf-8')
   reader = csv.reader(content.splitlines(), delimiter=',')
   items = []
   for row in reader:
        if row[8] != '' or row[8] != '0' or row[8] != 0:
            items.append({
            "item_code": row[1],
            "item_name": row[2],
            "qty": row[8],
            "basic_rate":row[6].replace("$", "").strip(),
            "t_warehouse": "5112 Heintz - VT",
            "description": row[3]
            })
   try:
       bom = {}
       bom["stock_entry_type"] = "Material Receipt"
       bom["items"] = items
       bom["docstatus"] = 0
       res = requests.post(url=url_bom, headers=headers, data=json.dumps(bom))
       print(f"{items}")
       print(f"{res.json()}")
   except Exception as e:
       print(f"{e} ")