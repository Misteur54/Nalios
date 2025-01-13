function helloNalios() {
    // For this use the ascii code for not use string
    const asciiHelloNalios = [
        72, 101, 108, 108, 111,
        44, 32,
        78, 97, 108, 105, 111, 115,
        32, 33,
    ]
    let messageHelloNalios = asciiHelloNalios.map(ascii => String.fromCharCode(ascii)).join('')
    console.log(messageHelloNalios)
}
helloNalios();