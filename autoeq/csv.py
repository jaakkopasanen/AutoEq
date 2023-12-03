# -*- coding: utf-8 -*-
import re

numeric_start = re.compile(r'^\d')
autoeq_columns = {
    'raw', 'smoothed', 'error', 'error_smoothed', 'equalization', 'parametric_eq', 'fixed_band_eq', 'equalized_raw',
    'equalized_smoothed', 'target'
}

# Regex for AutoEq style CSV
header_pattern = r'frequency(?:,(?:raw|smoothed|error|error_smoothed|equalization|parametric_eq|fixed_band_eq|equalized_raw|equalized_smoothed|target))+'
float_pattern = r'-?\d+(?:\.\d+)?'
autoeq_pattern = re.compile(rf'{header_pattern}(?:\n{float_pattern}(?:,{float_pattern})+)+')
rew_float_pattern = rf'(?:{float_pattern}|\?)'
rew_separator = rf'(?:, |; | |\t)'
rew_pattern = re.compile(rf'^(?:\*.*\n)*\* Freq\(Hz\){rew_separator}SPL\(dB\){rew_separator}Phase\(degrees\)\n(?:{rew_float_pattern}{rew_separator}{rew_float_pattern}{rew_separator}{rew_float_pattern})+\n*')
crinacle_pattern = re.compile(rf'[\s\n]?Frequency\tdB\tUnweighted(?:\n{float_pattern}\t{float_pattern})+[.\n]?')


class CsvParseError(Exception):
    pass


def find_csv_separators(csv):
    """Finds column and decimal separators in a CSV string

    Args:
        csv: CSV text data

    Returns:
        (column_separator, decimal separator)
    """
    lines = csv.strip().split('\n')
    # First find all potential column separators by checking which characters appear on each line that starts with digit
    column_separator_candidates = {',', ';', '\t', '|'}
    for line in lines:
        if not numeric_start.match(line):  # Skip rows which don't start with numbers
            continue
        remove_candidates = []
        for column_separator in column_separator_candidates:
            if column_separator not in line:
                # Numeric line doesn't contain the column separator candidate, eliminate the candidate
                remove_candidates.append(column_separator)
        for remove_candidate in remove_candidates:
            column_separator_candidates.remove(remove_candidate)

    if len(column_separator_candidates) == 0:
        raise CsvParseError('Could not find column and decimal separators')

    if column_separator_candidates == {','}:
        # Only comma found, it must be the column separator and decimal point must be dot
        return [',', '.']

    if ',' in column_separator_candidates:
        # Comma is included in the candidates (along with something else), it must be the decimal separator
        decimal_separator = ','
        column_separator_candidates.remove(',')
    else:
        decimal_separator = '.'

    if len(column_separator_candidates) > 1:
        raise CsvParseError(f'Found multiple potential column separators: {column_separator_candidates}')

    return list(column_separator_candidates)[0], decimal_separator


def find_csv_columns(csv, column_separator):
    lines = csv.strip().split('\n')
    numeric_lines = [line for line in lines if column_separator in line and numeric_start.search(line)]
    n_columns = list(set([len(line.split(column_separator)) for line in numeric_lines]))
    if len(n_columns) != 1:
        raise CsvParseError('Numeric lines have different number of columns')
    n_columns = n_columns[0]
    for line in lines:
        if not numeric_start.search(line) and len(line.split(column_separator)) == n_columns:
            return [cell.strip() for cell in line.split(column_separator)]


def parse_csv(csv):
    lines = csv.strip().split('\n')
    lines = [line for line in lines if line.strip()]
    csv = '\n'.join(lines)
    if autoeq_pattern.match(csv):  # Matches AutoEq produced CSV files
        columns = lines[0].split(',')
        return {column: [float(line.split(',')[i]) for line in lines[1:]] for i, column in enumerate(columns)}

    if rew_pattern.match(csv) or crinacle_pattern.match(csv):
        # These two have all sort of junk in them but the first column is frequency and the second SPL, so all good
        csv = '\n'.join([re.sub(r'(?:, ?| |\t)', '\t', line) for line in lines if numeric_start.match(line) and '?' not in line])
        lines = csv.split('\n')

    column_separator, decimal_separator = find_csv_separators(csv)
    columns = find_csv_columns(csv, column_separator)

    # Find indexes of frequency and raw columns
    if columns is None:
        # No header, assume first column is frequency and the second is SPL
        ixs = {'frequency': 0, 'raw': 1}
    else:
        ixs = {'frequency': None, 'raw': None}
        for i, column in enumerate(columns):
            if re.match(r'^freq', column, flags=re.IGNORECASE):
                ixs['frequency'] = i
            if re.match(r'^(?:spl|gain|ampl|raw)', column, flags=re.IGNORECASE):
                ixs['raw'] = i
        if ixs['frequency'] is None:
            if len(columns) == 2:  # Can't find proper columns but there's only two, assuming freq + raw
                ixs = {'frequency': 0, 'raw': 1}
            else:
                raise CsvParseError('Failed to find frequency column')
        if ixs['raw'] is None:
            raise CsvParseError('Failed to find SPL column')

    # Read and parse data lines
    data_line_pattern = re.compile(rf'^-?\d+(?:{column_separator}\d+)?')
    data = {'frequency': [], 'raw': []}
    for line in lines:
        if not data_line_pattern.match(line):
            continue
        cells = line.split(column_separator)
        if decimal_separator == ',':
            cells = [float(cell.replace(',', '.')) for cell in cells]
        else:
            cells = [float(cell) for cell in cells]
        for column, ix in ixs.items():
            data[column].append(cells[ix])
    return data


def create_csv(columns_dict):
    lines = [','.join(columns_dict.keys())]
    for i, f in enumerate(columns_dict['frequency']):
        lines.append(','.join([f'{arr[i]:.2f}' for arr in columns_dict.values()]))
    return '\n'.join(lines)
