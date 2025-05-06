contact_info={
    "Alice":{
        "Phone":"044111222",
        "email":"alice@gmail.com",
        "address":"rruga B",
        "birthday":"20/08/1997"
    },
"Bob":{
        "Phone":"0446473647",
        "email":"bob@gmail.com",
        "address":"rruga B",
        "birthday":"20/08/1997"
    },
"Eve":{
        "Phone":"0441143434",
        "email":"eve@gmail.com",
        "address":"rruga B",
        "birthday":"20/08/1997"
    }
}
print(contact_info)

#1. print out Bob;s info
print(contact_info["Bob"])
#2.Create two new personas Jane and John
contact_info["Jane"]={
        "Phone":"0441143434",
        "email":"jane@gmail.com",
        "address":"rruga B",
        "birthday":"20/08/1997"
    }
contact_info["John"]={
        "Phone":"0441143434",
        "email":"john@gmail.com",
        "address":"rruga B",
        "birthday":"20/08/1997"
    }
#3.print Jane's infocc
print(contact_info["Jane"])
#4.update Jane's phone number and print
contact_info["Jane"]["Phone"]="044111222"
print(contact_info["Jane"]["Phone"])
print(contact_info)