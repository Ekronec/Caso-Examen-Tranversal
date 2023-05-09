let itemNumber = 0
const emails =[]

function addItemNumber() {
    itemNumber = itemNumber + 1;
    console.log(itemNumber)
    document.getElementById("itemNumber").innerHTML = itemNumber
    document.getElementById("cartItem").style.visibility="visible";
}

function showNumber(itemNumber){
    return itemNumber
}

function confPass(){
    if (document.getElementById("password").innerHTML === document.getElementById("confPassword").innerHTML)
    console.log("funciona");
    else 
    console.log("No son iguales")
}

function addingEmail(nameEmail){
    emails.push(nameEmail);
    console.log(emails);
}
