const { RSAKeyPair, encryptedString } = require('./rsa/RSA')
const { setMaxDigits } = require('./rsa/BigInt')

setMaxDigits(19)

const e = process.argv[2]
const n = process.argv[3]
const key = new RSAKeyPair(e, '', n)

console.log(encryptedString(key, process.argv[4]))
