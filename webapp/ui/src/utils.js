import * as Papa from 'papaparse';

const decodeFloat16 = (binary) => {
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
};

const downloadAsFile = (data, fileType, fileName) => {
  const anchor = document.createElement('a');
  const file = new Blob([data], {type: fileType});
  anchor.href = URL.createObjectURL(file);
  anchor.download = fileName;
  document.body.appendChild(anchor); // Required for this to work in FireFox
  anchor.click();
  anchor.remove();
};

const findCsvSeparators = (csv) => {
  const rows = csv.trim().split('\n')
  const columnSeparatorCounts = { ',': 0, ';': 0, '\t': 0, '|': 0, ' ': 0 };
  let nNumericRows = 0;
  for (const row of rows) {
    if (!/^\d/.test(row)) {
      // Skip rows which don't start with numbers
      continue;
    }
    nNumericRows++;
    for (const columnSeparator of Object.keys(columnSeparatorCounts)) {
      if (row.includes(columnSeparator)) {
        columnSeparatorCounts[columnSeparator] += 1;
      }
    }
  }
  const columnSeparatorCandidates = [];
  for (const [sep, count] of Object.entries(columnSeparatorCounts)) {
    if (count === nNumericRows) {
      columnSeparatorCandidates.push(sep)
    }
  }
  let columnSeparator = '';
  if (columnSeparatorCandidates.includes('\t')) {
    columnSeparator = '\t';
  } else if (columnSeparatorCandidates.includes(';')) {
    columnSeparator = ';';
  } else if (columnSeparatorCandidates.includes('|')) {
    columnSeparator = '|';
  } else if (columnSeparatorCandidates.includes(' ')) {
    columnSeparator = ' ';
  } else if (columnSeparatorCandidates.includes(',')) {
    return [',', '.'];
  } else {
    return [null, null];
  }
  if (columnSeparatorCandidates.includes(',')) {
    return [columnSeparator, ','];
  }
  return [columnSeparator, '.'];
};

const parseCSV = (csvString) => {
  // Remove lines which don't start with a digit to get rid of comments
  csvString = csvString.trim().split('\n').filter(row => /^\d/.test(row)).join('\n');
  const [columnSeparator, decimalDelimiter] = findCsvSeparators(csvString);
  if (columnSeparator === null) {
    throw new Error('Column separator couldn\'t be detected');
  }
  if (decimalDelimiter === ',') {
    csvString = csvString.replaceAll(',', '.');
  }
  const parseResult = Papa.parse(csvString, { delimiter: columnSeparator, header: false});
  if (parseResult.errors.length > 0) {
    throw new Error(parseResult.errors[0].message);
  }
  return parseResult.data.map(row => {
    if (isNaN(parseFloat(row[0])) || isNaN(parseFloat(row[1]))) {
      throw new Error('Non-numeric values present');
    }
    return { frequency: parseFloat(row[0]), raw: parseFloat(row[1]) };
  });
};

const bandwidth = (q) => {
  return Math.log2((2*q**2+1) / (2*q**2) + Math.sqrt((((2*q**2 + 1) / q**2)**2)/4-1));
};

const initParametricEqNodes = (parametricEq, audioContext) => {
  const biquadNodes = [];
  const typeMap = { 'LOW_SHELF': 'lowshelf', 'HIGH_SHELF': 'highshelf', 'PEAKING': 'peaking' }
  for (const filter of parametricEq.filters) {
    const node = audioContext.createBiquadFilter();
    node.type = typeMap[filter.type];
    node.frequency.value = filter.fc;
    node.Q.value = filter.q;
    node.gain.value = filter.gain;
    if (biquadNodes.length > 0) {
      // Connect subsequent node to this one
      biquadNodes[biquadNodes.length - 1].connect(node);
    }
    biquadNodes.push(node);
  }
  return biquadNodes;
};

const initConvolutionNode = (audioBuffer, audioContext) => {
  const node = audioContext.createConvolver();
  node.normalize = false;
  node.buffer = audioBuffer;
  return node;
};

const transposeArrayToObject = (arr, keys) => {
  if (arr === null) {
    return null;
  }
  const obj = {};
  for (const key of keys) {
    obj[key] = [];
  }
  for (const el of arr) {
    for (const key of keys) {
      obj[key].push(el[key]);
    }
  }
  return obj;
};

const transposeObjectToArray = (obj, keys) => {
  const arr = [];
  for (let i = 0; i < obj[keys[0]].length; ++i) {
    const val = {};
    for (const key of keys) {
      val[key] = obj[key][i];
    }
    arr.push(val);
  }
  return arr;
};

export {
  decodeFloat16, downloadAsFile, parseCSV, bandwidth, initParametricEqNodes, initConvolutionNode,
  transposeArrayToObject, transposeObjectToArray
};
