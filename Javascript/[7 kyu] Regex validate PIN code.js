// see https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/solutions/javascript

function validatePIN (pin) {
  if (pin.length === 4 || pin.length ===6) {
    return /^\d+$/.test(pin);
  }
  return false
}