# -*- coding: utf-8 -*-

import os
import sys
from glob import glob
import pandas as pd
import re
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir)))
from measurements.utils import split_path


class Item:
    def __init__(self, false_name, true_name, form):
        self.false_name = false_name
        self.true_name = true_name if true_name else false_name
        self.form = form

    def __str__(self):
        return '\t'.join([self.false_name, self.true_name, self.form])


class Index:
    def __init__(self, items=None):
        self.df = pd.DataFrame([], columns=['false_name', 'true_name', 'form'])
        if items is not None:
            for item in items:
                self.add(item)

    def add(self, item):
        """Add an item to index

        Args:
            item: Item instance

        Returns:
            None
        """
        form = item.form
        if form is None:
            form = ''
        self.df = self.df.append(pd.DataFrame([[item.false_name, item.true_name, form]], columns=self.df.columns))

    @property
    def items(self):
        items = []
        for i, row in self.df.iterrows():
            items.append(Item(row['false_name'], row['true_name'], row['form']))
        return items

    @classmethod
    def read_files(cls, glob_pattern):
        index = cls()
        for file in glob(glob_pattern):
            form = None
            path_components = split_path(os.path.abspath(file))
            name = path_components[-1]
            for component in path_components:
                if component in ['onear', 'inear', 'earbud']:
                    form = component
            name = re.sub(r'\.[tc]sv$', '', name)
            item = Item(name, name, form)
            index.add(item)
        return index

    @classmethod
    def read_tsv(cls, file_path):
        index = cls()
        df = pd.read_csv(file_path, sep='\t', header=0, encoding='utf-8')
        if not df.columns.all(['false_name', 'true_name', 'form']):
            raise TypeError(f'"{file_path}" columns {df.columns} are corrupted')
        df.fillna('', inplace=True)
        for i, row in df.iterrows():
            index.add(Item(row['false_name'], row['true_name'], row['form']))
        return index

    def write_tsv(self, file_path):
        df = self.df.iloc[self.df['false_name'].str.lower().argsort()]
        df.to_csv(file_path, sep='\t', header=True, index=False, encoding='utf-8')

    def find_by_false_name(self, name):
        """Find a single Item by false name

        Args:
            name: False name

        Returns:
            Matching Item or None
        """
        try:
            row = self.df.loc[self.df['false_name'] == name].to_numpy()[0]
            return Item(*row)
        except IndexError:
            return None

    def find_by_true_name(self, name):
        """Find all items by their true name.

        Args:
            name: True name

        Returns:
            List of matching Items
        """
        arr = self.df.loc[self.df['true_name'] == name].to_numpy()
        return [Item(*row) for row in arr]

    def find_by_form(self, form):
        """Find all Items by form name

        Args:
            form: Form name

        Returns:
            List of matching Items
        """
        arr = self.df.loc[self.df['form'] == form].to_numpy()
        return [Item(*row) for row in arr]
