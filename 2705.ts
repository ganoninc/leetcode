type JSONValue =
  | null
  | boolean
  | number
  | string
  | JSONValue[]
  | { [key: string]: JSONValue };
type Obj = Record<string, JSONValue> | Array<JSONValue>;

function compactObject(obj: Obj): Obj {
  let compactObject = structuredClone(obj);
  return browseAndDeleteFalsyValues(compactObject);
}

function browseAndDeleteFalsyValues(obj: Obj): Obj {
  if (Array.isArray(obj)) {
    let filteredArray: Array<JSONValue> = [];
    obj.forEach((elt) => {
      if (
        Object.prototype.toString.call(elt) === "[object Object]" ||
        Array.isArray(elt)
      ) {
        filteredArray.push(browseAndDeleteFalsyValues(elt as Obj));
      } else {
        if (Boolean(elt)) filteredArray.push(elt);
      }
    });
    return filteredArray;
  } else if (Object.prototype.toString.call(obj) === "[object Object]") {
    for (const [property, value] of Object.entries(obj)) {
      if (
        Object.prototype.toString.call(value) === "[object Object]" ||
        Array.isArray(value)
      ) {
        obj[property] = browseAndDeleteFalsyValues(value as Obj);
      }
      if (!Boolean(value)) delete obj[property];
    }
  }
  return obj;
}

const testObj = { a: null, b: [false, 1] };
console.log(compactObject(testObj));
