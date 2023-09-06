let alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']




//replace the letter by its index in alphabet Array 
function myNameIs(name){
  let result = ""
  for (let i = 0; i < name.length; i++) {
    result += alphabet.indexOf(name[i].toLowerCase())
  }
  return result
}


// myNameIs("Ahmed") should return  '071243'
// myNameIs("Dorlean") return 31417114013
// myNameIs("a") return  0
// myNameIs("Sandrine") return 180133178134


algoTest()
function algoTest(fun) {
    if (myNameIs("Ahmed") == '071243') {
        console.log('\x1b[42m', 'Success', '\x1b[0m');
    }
    else {
        console.log('\x1b[41m', 'Fail', '\x1b[0m');
    }

    if (myNameIs("Dorlean") == 31417114013) {
        console.log('\x1b[42m', 'Success', '\x1b[0m');
    }
    else {
        console.log('\x1b[41m', 'Fail', '\x1b[0m');
    }

    if (myNameIs("a") == 0) {
        console.log('\x1b[42m', 'Success', '\x1b[0m');
    }
    else {
        console.log('\x1b[41m', 'Fail', '\x1b[0m');
    }

    if (myNameIs("Sandrine") == 180133178134) {
        console.log('\x1b[42m', 'Success', '\x1b[0m');
    }
    else {
        console.log('\x1b[41m', 'Fail', '\x1b[0m');
    }
}