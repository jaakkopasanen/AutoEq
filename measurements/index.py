# -*- coding: utf-8 -*-

import pandas as pd


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

    @property
    def items(self):
        items = []
        for i, row in self.df.iterrows():
            items.append(Item(row['false_name'], row['true_name'], row['form']))
        return items

    @classmethod
    def read(cls, file_path):
        index = cls()
        df = pd.read_csv(file_path, sep='\t', header=0, encoding='utf-8')
        if not df.columns.all(['false_name', 'true_name', 'form']):
            raise TypeError(f'"{file_path}" columns {df.columns} are corrupted')
        df.fillna('', inplace=True)
        for i, row in df.iterrows():
            index.add(Item(row['false_name'], row['true_name'], row['form']))
        return index

    def write(self, file_path):
        df = self.df.sort_values(by=['false_name'])
        df.to_csv(file_path, sep='\t', header=True, index=False)

    def add(self, item):
        """Add an item to index

        Args:
            item: Item instance

        Returns:
            None
        """
        self.df = self.df.append(pd.DataFrame([[item.false_name, item.true_name, item.form]], columns=self.df.columns))

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
