'use strict'

console.log("Hello World");


//////   SECTION 1: WELCOME. WELCOME. WELCOME 
//01.
//02.
//03.
//04.
//05.

//////   SECTION 2: JavaScript Fundamentals - PART 1
//05.
//06.
//07.
//08.
//09.
//10.


//11. Data Type : JavaScript Data Types and Dynamic Typing

//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
//++++++++++++++++++++++++++++++++++++++++++++Objects and Primitive Data Types++++++++++++++++++++++++++++++++++++++++++++++++

/*
                 Objects and Primitive Data Types
In JavaScript, every value is either an object or a primitive value. A value is only a primitive when it is not an object.
let us focus on primitive data types.

There are seven primitive data types in JavaScript:

1. number
2. string
3. boolean
4. undefined
5. null
6. symbol
7. BigInt

*/
//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

//12.
//13.
//14.
//15.
//16.

//17. Strings and Template Literals().  ____ STRINGS AND TEMPLATE LITERALS ____ 
        const firstname_1 = 'Jonas';
        const job_n = 'teacher';
        const birthYear = 1991;
        const year = 2037;   

        const jones = " I'm " + firstname_1 + ', a' + (year - birthYear) + 'years old' + job + ' ! ';
        console.log(jones);

        // Templete Literal. ES6 Feature
        const jones_name = `I'm ${firstname_1}, a ${year - birthYear} year old ${job}`; 
        console.log(jones_names);

        //
        console.log(`Just a simple String . . .. `);

        // 
        console.log('String with \n\ 
            multiple \n\
            lines');

        // 
        console.log(`String 
            with multiple 
            lines`);


//33. Functions 
//34. Function Declaration VS Expression  
//35. Arrow Functions 
//36. Function calling another Function 
//37. Reviewing Function  

// < < < < < < 34. FUNCTION DECLARATION AND EXPRESSION > > > > >  




//#####################################################################################
// function declaration 
function calcage1(birthYear) {
    return 2034 - birthYear
}

const age1 = calcage1(1994);   // <---- This can be mention before declaration of the function 

//### Function declaration can be called before declaration - the reason being *HOISTING* . . . . .   (*THIS IS NOT A GOOD PRATICE*) 

//#####################################################################################

//#####################################################################################
// function expression 
const calcage2 = function (birthYear) {
    return 2034 - birthYear
} 

const age2 = calcage2(1994);

console.log(" XX - - Below is the result of the function declaration and expression examples - - XX ")

console.log(age1, age2);

// < < < < < < FUNCTION DECLARATION AND EXPRESSION > > > > >  

//#####################################################################################



//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
function cutfruitpieces(fruit) {
    return fruit * 4;
    }
    
//  FUNCTIONS // SECTION 3 - - # 33

    function fruitprocessor(apples, oranges) {
    
    const applespieces = cutfruitpieces (apples);
    const orangepieces = cutfruitpieces (oranges); 
    // the above stored variable are calling the "cutfruitpieces" i.e., an another function outside this function when in turn is cutting the fruits in to pieces. 
    
        console.log(apples, oranges);
        console.log("The above is the number of apples and oranges"); 
        console.log(applespieces, orangepieces);
        console.log("The above is the no of pieces the apple and oranges are cut in to");
        
        const juice = `Juice of ${apples} apples are cut in to total of ${applespieces} apple pieces, and 
        juice of ${oranges} oranges are cut into total of ${orangepieces} orange pieces`;
        
        return juice;
    }
    

    // the below is the way to // invoke // calling // running the fuction . . . . 
    fruitprocessor (3, 4);
    // the return value of juice that is the statement is stored in the the "fruitprocessor" but we need to store it to a variable in order to see what it is. 
    
    const applejuice = fruitprocessor (3, 4);
    console.log (applejuice);
    const orangejuice = fruitprocessor (2, 23);
    console.log(orangejuice);
    

    //@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@