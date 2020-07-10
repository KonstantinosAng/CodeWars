// see https://www.codewars.com/kata/54da5a58ea159efa38000836/solutions/javascript

function findOdd(A) {
   if (A.map((number) => {
      let times = 0
      for (let i=0; i <= A.length; i++) {
          if (A[i] === number) {
                times++;
          }
      }
      if (times%2 !== 0) {
          index = number
          return true
      }
      }))  {
      return index
    }
}
