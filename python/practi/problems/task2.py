elements={
    "name":"'udayasree",
    "age":17,
    "citizen":"Indian"
},{
    "name":"radha",
    "age":35,
    "citizen":"Indian"
}
for i in range(len(elements)):
    if elements[i]["age"]>18 and elements[i]["citizen"]=="Indian":
        print(elements[i]["name"],"is eligible to vote")
    else:
        print(elements[i]["name"],"is not eligible to vote")

