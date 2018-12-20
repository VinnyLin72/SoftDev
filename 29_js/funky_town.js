// Team Undecided - Vincent Lin, Mai Rachlevsky
// SoftDev1 pd07
// K29 -- Sequential Progression II: Electric Boogaloo
// 2018-12-19

var fibonacci = function(n){
    if(n < 2){
	return n;
    } else {
	return fibonacci(n - 2) + fibonacci(n - 1);
    }
}

/* greatest common demoniator, Euclidean algorithm??? */
var gcd = function(a,b){
    if (b!=0)
	return gcd(b, a%b);
    else{
	return a;
    }
};

/* define a list for convenience */
var students = ['ananke', 'boule', 'irene', 'metron', 'ho polemos', 'philos','pratto', 'pisteuo', 'erchomai'];

/* input list, returns a random element */
var randomStudent = function(list){
    index = parseInt(Math.random()*list.length);
    return list[index];
};

var fibbutton = document.getElementById("fib");

var getFib = function() {
	console.log(fibonacci(4));
	document.getElementById("fib")
}
fibbutton.addEventListener('click', getFib);

    
var gcdbutton = document.getElementById("gcd");

var getGcd = function() {
    console.log(gcd(20,50));
    document.getElementById("gcd")
}
gcdbutton.addEventListener('click', getGcd);


var randbutton = document.getElementById("student");

var getStudent = function() {
    console.log(randomStudent(students));
    document.getElementById("student")
}
randbutton.addEventListener('click', getStudent);
