const decodeFloat16 = (binary) => {
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
  const columnSeparatorCounts = { ',': 0, ';': 0, '\t': 0, '|': 0 };
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

const parseCSV = (csv) => {
  csv = csv.trim();

  const [columnSeparator, decimalDelimiter] = findCsvSeparators(csv);
  if (columnSeparator === null) {
    throw new Error('Column separator couldn\'t be detected');
  }
  if (decimalDelimiter === ',') {
    csv = csv.replace(',', '.')
  }

  const rows = csv.split('\n');
  const frequency = [];
  const raw = [];
  for (const row of rows) {
    if (!/^\d/.test(row)) {
      // Skip rows which don't start with numbers
      continue;
    }
    const cells = row.trim().split(columnSeparator);
    if (cells.length < 2) {
      throw new Error('CSV data has row(s) with less than 2 values');
    }
    frequency.push(parseFloat(cells[0].trim()));
    raw.push(parseFloat(cells[1].trim()));
    if (isNaN(frequency[frequency.length - 1]) || isNaN(raw[raw.length - 1])) {
      throw new Error('Non-numbers detected in CSV data');
    }
  }
  const freqSet = new Set();
  for (const freq of frequency) {
    if ( freqSet.has(freq)) {
      throw new Error(`Duplicate frequency "${freq}" in CSV data`);
    }
    freqSet.add(freq);
  }

  const dataPoints = [];
  for (let i = 0; i < frequency.length; ++i) {
    dataPoints.push({ frequency: frequency[i], raw: raw[i] });
  }

  return dataPoints;
};

export { decodeFloat16, downloadAsFile, parseCSV };
