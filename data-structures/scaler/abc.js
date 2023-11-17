function computeMultiplesSum(n) {
  // Write your code here
  // To debug: console.error('Debug messages...');
  sum = 0;
  for (let i = 1; i < n; i++) {
    if (i%3 == 0 || i%5==0||i%7==0) {
      sum += i
    }
  }

  return sum;
}

console.log(computeMultiplesSum(15))