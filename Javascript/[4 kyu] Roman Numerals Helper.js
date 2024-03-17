class RomanNumerals {
  static getLookupMap = () => ({
    M: 1000,
    CM: 900,
    D: 500,
    CD: 400,
    C: 100,
    XC: 90,
    L: 50,
    XL: 40,
    X: 10,
    IX: 9,
    V: 5,
    IV: 4,
    I: 1,
  })
  static toRoman(num) {
    if (isNaN(num)) return NaN
    let roman = ''

    const lookup = this.getLookupMap()

    for (let i in lookup) {
      while (num >= lookup[i]) {
        roman += i
        num -= lookup[i]
      }
    }

    return roman
  }

  static fromRoman(str) {
    const lookup = this.getLookupMap()

    let number = 0

    for (let i = 0; i < str.length; i++) {
      if (str[i] === 'I' && str[i + 1] === 'V') {
        number += lookup['IV']
        i++
      } else if (str[i] === 'I' && str[i + 1] === 'X') {
        number += lookup['IX']
        i++
      } else if (str[i] === 'X' && str[i + 1] === 'L') {
        number += lookup['XL']
        i++
      } else if (str[i] === 'X' && str[i + 1] === 'C') {
        number += lookup['XC']
        i++
      } else if (str[i] === 'C' && str[i + 1] === 'D') {
        number += lookup['CD']
        i++
      } else if (str[i] === 'C' && str[i + 1] === 'M') {
        number += lookup['CM']
        i++
      } else {
        number += lookup[str[i]]
      }
    }
    return number
  }
}

assert.strictEqual(RomanNumerals.toRoman(1000), 'M')
assert.strictEqual(RomanNumerals.toRoman(4), 'IV')
assert.strictEqual(RomanNumerals.toRoman(1), 'I')
assert.strictEqual(RomanNumerals.toRoman(1990), 'MCMXC')
assert.strictEqual(RomanNumerals.toRoman(2008), 'MMVIII')

assert.strictEqual(RomanNumerals.fromRoman('XXI'), 21)
assert.strictEqual(RomanNumerals.fromRoman('I'), 1)
assert.strictEqual(RomanNumerals.fromRoman('IV'), 4)
assert.strictEqual(RomanNumerals.fromRoman('MMVIII'), 2008)
assert.strictEqual(RomanNumerals.fromRoman('MDCLXVI'), 1666)
