type JSONValue =
  | null
  | boolean
  | number
  | string
  | JSONValue[]
  | { [key: string]: JSONValue };
type Obj = Record<string, JSONValue> | Array<JSONValue>;

function chunk(arr: Obj[], size: number): Obj[][] {
  let res: Obj[][] = [];

  arr.forEach((elt, i) => {
    if (i % size == 0) {
      res.push([]);
    }
    res[res.length - 1].push(elt);
  });

  return res;
}
