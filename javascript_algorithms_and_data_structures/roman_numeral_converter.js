const roman_num = {"M": 1000, "CM": 900, "D": 500, "CD":400, "C":100, "XC":90, "L":50, "XL":40, "X":10, "IX":9, "V":5, "IV":4, "I":1}
  
var roman_num_text = "";

function convertToRoman(num) {
  if (num > 0) {
      for (const [key, value] of Object.entries(roman_num)) {
          if (num > value) {
              num = num - value;
              roman_num_text = roman_num_text + key;
              break;
          } else if (num == value) {
              num = num - value;
              roman_num_text = roman_num_text + key;
              break;
          } 
      } // end for loop
      convertToRoman(num);
    }  // end if loop
    return roman_num_text;
} // end of function

// test function
//convertToRoman(891);
