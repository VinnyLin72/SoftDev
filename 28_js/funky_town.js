// Team WestVirginia - Jared Asch, Vincent Lin
// SoftDev1 pd07
// K28 -- Sequential Programming
// 2018-12-19

let fibonacci = (n) => {
    if(n < 2){
	return 1;
    } else {
	return fibonacci(n - 2) + fibonacci(n - 1);
    }
}

let gcd = (a, b) => {
    if(b == 0){
	return a;
    }
    return gcd(b, a % b);
}

let students = ["Vincent Lin", "Jared Asch", "Shin Bamba", "Timothy 'Timothy MC Gaming' Marder", "Teddy Peters"]

let random_student = (list) => {
    return list[ Math.floor(Math.random() * list.length) ];
}
