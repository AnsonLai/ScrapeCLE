var links = document.querySelectorAll('a[href="#"]');
links.forEach(el => { el.click()});

var endpoints = document.querySelectorAll('a[href]');
var output = [];
endpoints.forEach(el => { output.push(el.href)});
console.log(output.toString());

var output = [];


console.log(document.querySelectorAll('#ops-document-formats a'));


var links = document.querySelectorAll('#books a');
var output = [];
links.forEach(el => { output.push(el.href)});
console.log(output.toString());

console.log(document.querySelectorAll('#treeWrapper>div>ul>li>a'));