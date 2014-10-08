/**
 * Created by renzo on 10/1/14.
 */

//var hello= function hello(name){
//    return 'Hello World'+name;
//}
function hello(name) {
    var str = 'Hello World' + name;
    return  str;
}
var hello2 = hello;

console.log(hello2());

var hello = 1

//hello();

function geradorDeContadora() {
    var i = 1;

    function a() {
        i += 1;
        return i;
    }

    return a;
}

variavel = "Elenildo";

console.log(variavel);

function f() {
    if (0 !== []) {
        console.log('Verdadeiro');
    }
    else {
        console.log([] + undefined)

        console.log('Falso');
    }
    var escopo = 3.999;
}
f()

//console.log(escopo);

var fcn = geradorDeContadora();

console.log(fcn())
console.log(fcn())
var fcn2 = geradorDeContadora();


console.log(fcn2())

function mostrarEventoDeMouse(evento) {
    console.log(evento)
}


var a = [1, 2, 'Renzo'];
a.push('Nuccitelli');
a.unshift(0);
a.splice(3, 2);

for (var i = 0; i < a.length; i += 1) {
    console.log(a[i]);
}

var obj = {nome: "Renzo", 'sobrenome': "Nuccitelli", 1: 'Blah',
    ola: function (){
        return 'Olá'+this.nome;
    },
    vetor:a,
    obj:{att:'t'}
};
console.log(obj.nome);
console.log(obj.sobrenome);
console.log(obj['sobrenome']);
console.log(obj[1]);
console.log(obj.ola());

console.log(obj);






















