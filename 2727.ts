type JSONValue =
  | null
  | boolean
  | number
  | string
  | JSONValue[]
  | { [key: string]: JSONValue };
type Obj = Record<string, JSONValue> | JSONValue[];

function isEmpty(obj: Obj): boolean {
  if (Object.prototype.toString.call(obj) === "[object Object]") {
    return Object.keys(obj).length === 0;
  } else {
    return (obj as JSONValue[]).length === 0;
  }
}
