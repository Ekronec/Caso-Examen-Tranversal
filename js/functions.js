let itemNumber = 0

function addItemNumber() {
    itemNumber = itemNumber + 1;
    console.log(itemNumber)
    document.getElementById("itnumber").innerHTML = itemNumber
}

function showNumber(itemNumber){
    return itemNumber
}
