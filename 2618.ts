function checkIfInstanceOf(obj: any, classFunction: any): boolean {
  if (!classFunction) return false;
  if (!obj) return false;

  let objPrototype = Object.getPrototypeOf(obj);
  let classPrototype = classFunction.prototype;
  while (objPrototype) {
    if (objPrototype === classPrototype) return true;
    objPrototype = Object.getPrototypeOf(objPrototype);
  }
  return false;
}

console.log(checkIfInstanceOf(new Date(), Date)); // true
console.log(checkIfInstanceOf(new Date(), undefined)); // true
