// see https://www.codewars.com/kata/554e4a2f232cdd87d9000038

function DNAStrand(dna){
   let complements = [];
   let arr = dna.split("")
                .map(function (val) {
                        if (val === 'A') {
                            complements.push('T');
                        } else if (val === 'T') {
                            complements.push('A');
                        } else if (val === 'G') {
                            complements.push('C');
                        } else {
                            complements.push('G');
                     }
                 });
   return complements.join("")
}
