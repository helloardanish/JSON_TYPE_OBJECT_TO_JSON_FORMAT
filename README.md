## A simple program to convert json type object in programming language to a json type

#### An object in Angular/Tyepescript is defied as below

```
data = {
    name: '',
    address: {
      city: '',
      country: ''
    }
  }


// with values

data = {
    name: 'A R Danish',
    address: {
      city: 'New Delhi',
      country: 'India'
    }
  }

```

#### We need to store the same data as a json structure but it will give error because key should be formatted so we have to create like below

```
{
  "name": "",
  "address": {
    "city": "",
    "country": ""
  }
}

```

The program will do the same so you don't have to format it mannually. 

Later it can be stored in .json file/JSON format or put the data in postgres database as an insert in jsonb type. It can be store in any other JSON type ORM(key value pair) databases.


#### For developer
 **Step 1 : Download the depency which are required:**
 <p>Python must be install in system. Dowload libraries PyQt6, pandas using command</p>
  <p>It is recommended to use virtual environment</p>

```
  pip install pandas
  pip install pyqt6
```

**Step 2 : Run using terminal:**

```
python3 Main.py
```
Window will appear
![image](https://github.com/helloardanish/JSON_TYPE_OBJECT_TO_JSON_FORMAT/assets/24757027/88b24a07-b0a5-4fdf-9d24-42ef792ca5b0)

**Step 3 : Write JSON object or copy paste from your code:**

![image](https://github.com/helloardanish/JSON_TYPE_OBJECT_TO_JSON_FORMAT/assets/24757027/596a30f6-a8df-4a86-8faf-097c3e802b22)

**Step 3 : Click format button:**

![image](https://github.com/helloardanish/JSON_TYPE_OBJECT_TO_JSON_FORMAT/assets/24757027/f48c0764-da40-4c9e-8f49-d23ffaba94e7)

It is formatted, copy it and use it.

## Download option added to download the formatted json file

![image](https://github.com/helloardanish/JSON_TYPE_OBJECT_TO_JSON_FORMAT/assets/24757027/522f9c33-b563-486b-ab45-b7398df455b9)


## A R
