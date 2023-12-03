# -*- coding: utf-8 -*-

import ipywidgets as widgets
import webbrowser
import urllib.parse


class NamePrompt:
    def __init__(
            self, item, callback, guessed_name=None, name_proposals=None, similar_names=None):
        """IPyWidgets UI element for setting name for a crawled headphone"""
        self._item = item
        self.callback = callback
        self._guessed_name = guessed_name or item.source_name or ''
        self._guessed_name = self._guessed_name.strip()
        self._name_proposals = name_proposals if name_proposals is not None else []
        self._similar_names = similar_names if similar_names is not None else []
        # UI elements
        self.search_button = widgets.Button(description='🔎', layout=widgets.Layout(width='48px', height='44px'))
        self.search_button.on_click(self.handle_search)
        self._name_proposal_buttons = []
        self.text_field = widgets.Text(value=self.guessed_name, layout=widgets.Layout(width='400px'))
        self.form_buttons = []
        for form in ['over-ear', 'in-ear', 'earbud', 'ignore']:
            btn = widgets.Button(description=form, layout=widgets.Layout(width='80px'))
            btn.on_click(self.handle_form_click)
            self.form_buttons.append(btn)
        self.widget = None
        self.reload_ui()

    def reload_ui(self):
        for button in self.form_buttons:
            button.button_style = 'success' if button.description == self.item.form else (
                'danger' if button.description == 'ignore' else 'warning')
        self.widget = widgets.VBox([
            widgets.HBox([
                widgets.VBox([
                    widgets.HTML(
                        value=f'<h4 style="margin: 0;text-align: center; line-height: 1.7">{self.name}</h4>'
                              f'<i style="text-align: center; display: inline-block; width: 100%; line-height: 1">'
                              f'{urllib.parse.unquote(self.item.url) or self.item.source_name}</i>'),
                ], layout=widgets.Layout(text_align='center', min_width='400px')),
                self.search_button
            ], layout=widgets.Layout(width='600px')),
            widgets.HBox([
                widgets.VBox([
                    *self._name_proposal_buttons,  # Name suggestions
                    widgets.HBox([*self.form_buttons]),
                    self.text_field,
                    widgets.Label(f'Measured on: {self.item.rig}'),
                ]),
                widgets.HTML(
                    '<div style="margin-left: 12px"><b>Naming convention</b><br />' +
                    '<br>'.join(self.similar_names) + '</div>'
                ),
            ]),
        ])

    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, item):
        self._item = item
        self.reload_ui()

    @property
    def guessed_name(self):
        return self._guessed_name

    @guessed_name.setter
    def guessed_name(self, value):
        if self.guessed_name == self.text_field.value:
            # User hasn't updated text field value manually, safe to update to new guessed name
            self._guessed_name = value.strip()
            self.text_field.value = self._guessed_name
            self.reload_ui()

    @property
    def name_proposals(self):
        return self._name_proposals

    @name_proposals.setter
    def name_proposals(self, name_proposals):
        self._name_proposals = name_proposals if name_proposals is not None else []
        # Add button for each name proposal
        self._name_proposal_buttons = []
        if self._name_proposals is not None:
            for item in name_proposals.items:
                btn = widgets.Button(
                    description=f'{item.name}',
                    button_style='success' if self.guessed_name and item.name.lower() == self.guessed_name.lower() else 'primary',
                    layout=widgets.Layout(width='400px'))
                btn.on_click(self.handle_name_proposal_click)
                self._name_proposal_buttons.append(btn)
            self.reload_ui()

    @property
    def similar_names(self):
        return self._similar_names

    @similar_names.setter
    def similar_names(self, similar_names):
        self._similar_names = similar_names if similar_names is not None else []
        if self._similar_names:
            self.reload_ui()

    @property
    def name(self):
        return self.guessed_name or urllib.parse.unquote(self.item.url.split('/')[-1])

    def handle_search(self, btn):
        quoted = urllib.parse.quote_plus(self.name)
        url = f'https://google.com/search?q={quoted}&tbm=isch'
        webbrowser.open(url)

    def handle_name_proposal_click(self, btn):
        btn.button_style = 'success'
        item = self.item.copy()
        proposal_item = self.name_proposals.find_one(name=btn.description).copy()
        item.name = proposal_item.name
        item.form = proposal_item.form
        self.callback(item)

    def handle_form_click(self, btn):
        item = self.item.copy()
        item.name = self.text_field.value.strip()
        item.form = btn.description
        self.callback(item)
