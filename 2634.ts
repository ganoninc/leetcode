type Fn = (n: number, i: number) => any;

function filter(arr: number[], fn: Fn): number[] {
  let filteredArr: number[] = [];
  arr.forEach((num, i) => {
    fn(num, i) && filteredArr.push(num);
  });
  return filteredArr;
}
