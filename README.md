## A simple program to convert json type object in programming language to a json type

#### An object in Angular is defied as below

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
