function* fibGenerator(): Generator<number, any, number> {
  let valN2 = -1;
  let valN1 = 1;
  while (true) {
    let nextVal = valN2 + valN1;
    yield nextVal;
    valN2 = valN1;
    valN1 = nextVal;
  }
}

const gen = fibGenerator();
gen.next().value; // 0
gen.next().value; // 1
gen.next().value; // 1
gen.next().value; // 2
gen.next().value; // 3
