function decodeFloat16 (binary) {
  'use strict';
  const exponent = (binary & 0x7C00) >> 10;
  const fraction = binary & 0x03FF;
  return (binary >> 15 ? -1 : 1) * (
    exponent ?
      (
        exponent === 0x1F ?
          fraction ? NaN : Infinity :
          Math.pow(2, exponent - 15) * (1 + fraction / 0x400)
      ) :
      6.103515625e-5 * (fraction / 0x400)
  );
}

export { decodeFloat16 };
