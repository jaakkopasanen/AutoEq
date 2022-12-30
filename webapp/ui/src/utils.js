function findObjectInArray(arr, key, val) {
  // Finds the first object in array of object which has the requested value in the requested key
  for (const obj of arr) {
    if (obj[key] === val) {
      return obj;
    }
  }
  return null;
}

export { findObjectInArray };
