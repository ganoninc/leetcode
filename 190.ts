// function reverseBits(n: number): number {
//   let result = 0;
//   //   console.log(n.toString(2));

//   for (let i = 0; i < 32; i++) {
//     result = result << 1;
//     result = result | (n & 1);
//     n = n >> 1;
//   }

//   //   console.log(result.toString(2));
//   return result >>> 0;
// }

// With a lookup table to have o(4) access time (32 bits = 4 * 8 bytes)
class Solution {
  private lookup: Record<number, number>;

  constructor() {
    this.lookup = {};
    for (let i = 0; i < 256; i++) {
      this.lookup[i] = this.reverseByte(i);
    }

    // for (const key of Object.keys(this.lookup)) {
    //   console.log(
    //     `Value: ${Number.parseInt(key).toString(2)}, reversed: ${this.lookup[key].toString(2)}`
    //   );
    // }
  }

  private reverseByte(n: number): number {
    let reversedByte = 0;

    for (let i = 0; i < 8; i++) {
      reversedByte = reversedByte << 1;
      reversedByte = reversedByte | (n & 1);
      n = n >> 1;
    }

    return reversedByte;
  }

  reverseBits(n: number): number {
    let reversedBits: number = 0;

    console.log(n.toString(2));

    reversedBits = this.lookup[n & 0xff] << 24; //The first byte, aka the highest in the result, pushed to the very right
    reversedBits = reversedBits | (this.lookup[(n >> 8) & 0xff] << 16); // Then the second becomes the third
    reversedBits = reversedBits | (this.lookup[(n >> 16) & 0xff] << 8); // Then the third becomes second
    reversedBits = reversedBits | this.lookup[(n >> 24) & 0xff]; // Lastly, the first becomes last (at the very left)

    return reversedBits >>> 0;
  }
}

const solution = new Solution();
solution.reverseBits(483);
