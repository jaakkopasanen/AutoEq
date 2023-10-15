# -*- coding: utf-8 -*-
import math
import os
import sys
from glob import glob
import numpy as np
import pandas as pd
import re
from rapidfuzz import fuzz


class NameItem:
    def __init__(self, source_name, name, form, url=None, rig=None):
        self.url = url
        self.source_name = source_name
        self.name = name
        self.form = form
        self.rig = rig

    def __str__(self):
        return '"' + '"\t"'.join([self.url or '', self.source_name or '', self.name or '', self.form or '', self.rig or '']) + '"'

    def copy(self):
        return NameItem(self.source_name, self.name, self.form, url=self.url, rig=self.rig)


class NameIndex:
    def __init__(self, rows=None, items=None):
        self.df = pd.DataFrame(rows if rows is not None else [], columns=['url', 'source_name', 'name', 'form', 'rig'])
        if items is not None:
            rows = [[item.url, item.source_name, item.name, item.form, item.rig] for item in items]
            self.df = pd.concat([self.df, pd.DataFrame(rows, columns=self.df.columns)])
            self.df = self.df.drop_duplicates()

    def __len__(self):
        return self.df.shape[0]

    def __bool__(self):
        return len(self) > 0

    @property
    def items(self):
        items = []
        for i, row in self.df.iterrows():
            items.append(NameItem(row['source_name'], row['name'], row['form'], url=row['url'],  rig=row['rig']))
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
        items = []
        for file in glob(glob_pattern, recursive=True):
            form = None
            path_components = cls.split_path(os.path.abspath(file))
            name = path_components[-1]
            for component in path_components:
                if component in ['over-ear', 'in-ear', 'earbud']:
                    form = component
            name = re.sub(r'\.[tc]sv$', '', name)
            items.append(NameItem(None, name, form, url=None, rig=None))
        return cls(items=items)

    @classmethod
    def read_tsv(cls, file_path):
        index = cls()
        if not os.path.isfile(file_path):
            return index
        df = pd.read_csv(file_path, sep='\t', header=0, encoding='utf-8')
        if list(df.columns) != ['url', 'source_name', 'name', 'form', 'rig']:
            raise TypeError(f'"{file_path}" columns {df.columns} are corrupted')
        df.replace([np.nan], [None], inplace=True)
        index.df = df
        return index

    def write_tsv(self, file_path):
        df = self.df.iloc[self.df['source_name'].str.lower().argsort()]
        df.to_csv(file_path, sep='\t', header=True, index=False, encoding='utf-8')

    def mask(self, url=None, source_name=None, name=None, form=None, rig=None):
        """Creates a filter mask for rows which match the given query parameters."""
        # TODO source_url and rig
        mask = None
        if url is not None:
            mask = (self.df.url == url)
        if source_name is not None:
            m = (self.df.source_name == source_name)
            mask = m if mask is None else mask & m
        if name is not None:
            m = (self.df.name == name)
            mask = m if mask is None else mask & m
        if form is not None:
            m = (self.df.form == form)
            mask = m if mask is None else mask & m
        if rig is not None:
            m = (self.df.rig == rig)
            mask = m if mask is None else mask & m
        return mask

    def concat(self, name_index):
        """Merges another NameIndex to this."""
        self.df = pd.concat([self.df, name_index.df])

    def add(self, item):
        """Adds an item to index."""
        self.df = pd.concat(
            [self.df, pd.DataFrame([[item.url, item.source_name, item.name, item.form, item.rig]], columns=self.df.columns)])
        self.df = self.df.drop_duplicates()

    def remove_duplicates(self):
        """Removes duplicate entries."""
        self.df = self.df.drop_duplicates()

    def update(self, new_item, source_name=None, name=None, form=None):
        """Updates all items which match the given query parameters to the given item.

        Args:
            new_item: New value as NameItem
            source_name: Name of the items in the source to update
            name: True name of the items to update
            form: Form of the items to update

        Returns:
            None
        """
        if self.find(source_name=new_item.source_name, name=name, form=form):
            mask = self.mask(source_name=source_name, name=name, form=form)
            try:
                self.df.loc[mask] = np.tile([new_item.source_name, new_item.name, new_item.form], (sum(mask), 1))
            except Exception as err:
                print(source_name, name, form)
                print(new_item)
                print(mask)
                raise err
        else:
            self.add(new_item)

    def find(self, url=None, source_name=None, name=None, form=None, rig=None):
        """Finds all items which match the given query parameters.

        Args:
            url: Measurement source URL
            source_name: Measurement name in the source
            name: Measurement name in AutoEq
            form: Measured item form (over-ear, in-ear or earbud)
            rig: Measurement rig used

        Returns:
            New NameIndex instance with the matching items
        """
        mask = self.mask(url=url, source_name=source_name, name=name, form=form, rig=rig)
        return NameIndex(rows=self.df.loc[mask].copy())

    def find_one(self, **kwargs):
        results = self.find(**kwargs)
        if results:
            return results.items[0]

    def search_by_source_name(self, name, threshold=80):
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
            ratio = fuzz.ratio(item.source_name, name)
            token_set_ratio = fuzz.token_set_ratio(item.source_name.lower(), name.lower())
            if ratio > threshold or token_set_ratio > threshold:
                matches.append((item, ratio, token_set_ratio))
        return sorted(matches, key=lambda x: x[1], reverse=True)

    def search_by_name(self, name, threshold=80):
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
            ratio = fuzz.ratio(item.name, name)
            token_set_ratio = fuzz.token_set_ratio(item.name.lower(), name.lower())
            if ratio > threshold or token_set_ratio > threshold:
                matches.append((item, ratio, token_set_ratio))
        return sorted(matches, key=lambda x: x[1], reverse=True)
