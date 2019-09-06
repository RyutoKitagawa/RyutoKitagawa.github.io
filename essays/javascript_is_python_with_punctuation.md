---
layout: essay
type: essay
title: Javascript is Python With Punctuation
# All dates must be YYYY-MM-DD format!
date: 2019-09-05
labels:
  - Javascript
  - Python
---

<img src = "../images/javascript_logo.png" alt = "Javascript">

## Javascript vs Python

One of the first things I noticed when using the Javascript language is how similar it was to Python.  Unlike Java, Javascript didn't require the creation of a Main class to run the program.  Unlike C/C++, creating function declarations isn't necessary.  Python shares these properties along with many others such as: not requiring type declarations for variables, allowing arrays to contain values of different data types, and automatically passing objects and arrays into functions by reference.  

However, one of the major differences between Python and Javascript is their syntax.  Javascript, like Java and C/C++, requires a semicolon be placed at the end of a line of code, as well as curly braces surrounding the body of flow control statements such as "if" and "while" statements.  These two languages also differ in how they treat classes.  Javascript essentially treats classes like a function, and only adding the "class" as a keyword to make programming easier.  This means that you can create a function in Javascript that acts identical to a class in javascript:

```javascript
function Obj(x, y) {
    this.x = x;
    this.y = y;
}

Obj.prototype.z = function() {
    console.log("Function");
}

class ObjClass {
    constructor (x, y) {
        this.x = x;
        this.y = y;
    }
    
    z() {
        console.log("Function");
    }
}
```

However, in Python, the only way to create a class is by using the "class" keyword.  There are several other minor differences between Python and Javascript, such as for loop syntax, but these are the more intricat differences between the languages.

## Javascript as It Stands

Javascript, when looking at it on its own, is a fairly powerful language.  One of the main advantages that it has compared to other languages is the support it has on webpage browsers and HTML.  This makes it easier to integrate javascript code into websites, and allows a larger audience to access the code that you had written.  Javascript also simplifies the experience for end users, as there isn't any need to "compile" code like in C languages, and Java.  

One interesting aspect of Javascript is the emphasis of the language seems to be away from Object Oriented Programming.  The reason I believe this is because of the way they allow functions to act similarly to classes, and thus makes classes feel more like an afterthought than an integral part of the programming language.  Compare this to Java, where the developer needs to create a Main class before they can even run code, and it becomes clear that the focus was heavily on Object Oriented Programming.  This doesn't necessarily mean that Javascript doesn't do Object Oriented Programming well, this just means that this wasn't the intended purpose for the language.  I believe that the intended use of javascript was to work well with HTML, and allow devlopers to create websites and make them more dynamic than they would have otherwise been able to with just the tools they have in HTML and CSS.

## Programming Under Pressure

Deviating from the Javascript language, programming under pressure is an important part of being a softwrae developer.  Due to the large amount of stress that software engineers often face during their job, it's important for them to be able to work efficiently and produce a quality product.  This is why I believe that programming under a time pressure is important for helping students devlop the ability to handle pressure well.  This can also help students develop in other ways as well, such as building stronger connections in their brains as they try to find an optimal solution quickly.  They may also find more creative solutions since they are forced to think more critically about the problem given that they only have a limited amount of time to solve it.

However, there may be downfalls as well.  Students may become more preoccupied with getting an algorithm to run at all, rather than focusing on whether what they built is efficent or good practice for software engineering.  This may also cause students to develop a habit of being impatient and believing that problems should be solved much faster than they really are solved.  This can encourage people to cut corners, get sloppy, and develop habits that solves problems now, but doesn't take into consideration the future.

However, it's also the responsibility of the student to practice programming in environments outside of just time sensitive cases.  We should be practicing in all manners of situations and formats in order to ensure that we are well rounded, and capable of handling many difficult situations.  Software engineering is a lot like an art form, and there are many different styles and approaches one may take.  It's important for a developer to find a style that they are comfortable with, but it's just as important to practice a wide variety of styles to ensure that they are the most versitile and capable developer they can be.
