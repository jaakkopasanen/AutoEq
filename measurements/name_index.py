# -*- coding: utf-8 -*-

import os
import sys
from glob import glob
import numpy as np
import pandas as pd
import re
from rapidfuzz import fuzz


class NameItem:
    def __init__(self, false_name, true_name, form):
        self.false_name = false_name
        self.true_name = true_name
        self.form = form

    def __str__(self):
        return '\t'.join([self.false_name or '', self.true_name or '', self.form or ''])

    def copy(self):
        return NameItem(self.false_name, self.true_name, self.form)


class NameIndex:
    def __init__(self, rows=None, items=None):
        self.df = pd.DataFrame(rows if rows is not None else [], columns=['false_name', 'true_name', 'form'])
        if items is not None:
            for item in items:
                self.add(item)

    def __len__(self):
        return self.df.shape[0]

    def __bool__(self):
        return len(self) > 0

    @property
    def items(self):
        items = []
        for i, row in self.df.iterrows():
            items.append(NameItem(row['false_name'], row['true_name'], row['form']))
        return items

    @staticmethod
    def split_path(path):
        components = []
        while True:
            path, file = os.path.split(path)
            if file:
                components.append(file)
            elif path:
                components.append(path)
                break
            else:
                break
        return components[::-1]

    @classmethod
    def read_files(cls, glob_pattern):
        rows = []
        for file in glob(glob_pattern, recursive=True):
            form = None
            path_components = cls.split_path(os.path.abspath(file))
            name = path_components[-1]
            for component in path_components:
                if component in ['onear', 'inear', 'earbud']:
                    form = component
            name = re.sub(r'\.[tc]sv$', '', name)
            rows.append([name, name, form])
        return cls(rows=rows)

    @classmethod
    def read_tsv(cls, file_path):
        index = cls()
        if not os.path.isfile(file_path):
            return index
        df = pd.read_csv(file_path, sep='\t', header=0, encoding='utf-8')
        if list(df.columns) != ['false_name', 'true_name', 'form']:
            raise TypeError(f'"{file_path}" columns {df.columns} are corrupted')
        df.fillna('', inplace=True)
        index.df = df
        return index

    def write_tsv(self, file_path):
        df = self.df.iloc[self.df['false_name'].str.lower().argsort()]
        df.to_csv(file_path, sep='\t', header=True, index=False, encoding='utf-8')

    def mask(self, false_name=None, true_name=None, form=None):
        """Creates a filter mask for rows which match the given query parameters."""
        mask = None
        if false_name is not None:
            mask = (self.df.false_name == false_name)
        if true_name is not None:
            m = (self.df.true_name == true_name)
            mask = m if mask is None else mask & m
        if form is not None:
            m = (self.df.form == form)
            mask = m if mask is None else mask & m
        return mask

    def concat(self, name_index):
        """Merges another NameIndex to this."""
        self.df = pd.concat([self.df, name_index.df])

    def add(self, item):
        """Adds an item to index."""
        false_name = item.false_name if item.false_name is not None else ''
        true_name = item.true_name if item.true_name is not None else ''
        form = item.form if item.form is not None else ''
        self.df = pd.concat([self.df, pd.DataFrame([[false_name, true_name, form]], columns=self.df.columns)])
        self.df = self.df.drop_duplicates()

    def remove_duplicates(self):
        """Removes duplicate entries."""
        self.df = self.df.drop_duplicates()

    def update(self, item, false_name=None, true_name=None, form=None):
        """Updates all items which match the given query parameters to the given item.

        Args:
            item: New value as NameItem
            false_name: False name of the items to update
            true_name: True name of the items to update
            form: Form of the items to update

        Returns:
            None
        """
        if self.find(false_name=item.false_name, true_name=true_name, form=form):
            mask = self.mask(false_name=false_name, true_name=true_name, form=form)
            try:
                self.df.loc[mask] = np.tile([item.false_name, item.true_name, item.form], (sum(mask), 1))
            except Exception as err:
                print(false_name, true_name, form)
                print(item)
                print(mask)
                raise err
        else:
            self.add(item)

    def find(self, false_name=None, true_name=None, form=None):
        """Finds all items which match the given query parameters.

        Args:
            false_name: False name of the items to find
            true_name: True name of the items to find
            form: Form of the items to find

        Returns:
            New NameIndex instance with the matching items
        """
        mask = self.mask(false_name=false_name, true_name=true_name, form=form)
        return NameIndex(rows=self.df.loc[mask].copy())

    def find_one(self, **kwargs):
        results = self.find(**kwargs)
        if results:
            return results.items[0]

    def search_by_false_name(self, name, threshold=80):
        """Finds all items which match closely to all given query parameters.

        Args:
            name: Name to search by. Ignored if None.
            threshold: Threshold for matching with RapidFuzz.

        Returns:
            List of matching triplets with NameItem, RapidFuzz ratio and RapidFuzz token_set_ratio
        """
        matches = []
        for item in self.items:
            # Search with false name
            ratio = fuzz.ratio(item.false_name, name)
            token_set_ratio = fuzz.token_set_ratio(item.false_name.lower(), name.lower())
            if ratio > threshold or token_set_ratio > threshold:
                matches.append((item, ratio, token_set_ratio))
        return sorted(matches, key=lambda x: x[1], reverse=True)

    def search_by_true_name(self, name, threshold=80):
        """Finds all items which match closely to all given query parameters.

        Args:
            name: Name to search by. Ignored if None.
            threshold: Threshold for matching with RapidFuzz.

        Returns:
            List of matching triplets with NameItem, RapidFuzz ratio and RapidFuzz token_set_ratio
        """
        matches = []
        for item in self.items:
            # Search with false name
            ratio = fuzz.ratio(item.true_name, name)
            token_set_ratio = fuzz.token_set_ratio(item.true_name.lower(), name.lower())
            if ratio > threshold or token_set_ratio > threshold:
                matches.append((item, ratio, token_set_ratio))
        return sorted(matches, key=lambda x: x[1], reverse=True)
