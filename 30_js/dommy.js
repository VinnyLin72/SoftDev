let fib = (n) => {
    if(n < 3){
	return 1;
    }
    return fib(n - 2) + fib(n - 1);
}

itemList = document.getElementById("thelist");

document.getElementById("b").addEventListener("click", function(e){
    let newLi = document.createElement("li");
    newLi.innerHTML = "New list element";
    itemList.appendChild(newLi);
    addListListeners(newLi);
});

let addListListeners = (li) => {
    li.addEventListener("mouseenter", function(e){
        document.getElementById("h").innerHTML = this.innerHTML;
    });
    li.addEventListener("mouseout", function(e){
        document.getElementById("h").innerHTML = "Hello world";
    });
    li.addEventListener("click", function(e){
        this.remove();
    });
}

var lis = document.getElementsByTagName("li");
for(var i = 0; i < lis.length; i++){
    addListListeners(lis[i]);
}

var fib_num = 0;

document.getElementById("fb").addEventListener("click", function(e){
    let new_li = document.createElement("li");
    new_li.innerHTML = fib(++fib_num);
    document.getElementById("fiblist").appendChild(new_li);
})
