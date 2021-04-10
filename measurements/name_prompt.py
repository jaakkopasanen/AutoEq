# -*- coding: utf-8 -*-

import sys
from pathlib import Path
if str(Path(__file__).resolve().parent) not in sys.path:
    sys.path.insert(1, str(Path(__file__).resolve().parent))
import ipywidgets as widgets


class NamePrompt:
    def __init__(self, model, callback, manufacturer=None, name_proposals=None, search_callback=None, false_name=None):
        self.model = model
        self.callback = callback
        self.manufacturer = manufacturer
        self.name_proposals = name_proposals
        self.search_callback = search_callback

        buttons = []
        if name_proposals is not None:
            for item in name_proposals.items:
                btn = widgets.Button(
                    description=f'{item.true_name}', button_style='primary', layout=widgets.Layout(width='596px'))
                btn.on_click(self.on_click)
                buttons.append(btn)

        title = '<h4 style="margin: 0">'
        if false_name:
            title += f'{false_name} → '
        if manufacturer:
            title += f'<span style="color: blue">{manufacturer}&nbsp;</span>'
            text = f'{manufacturer} {model}'
        else:
            text = model
        title += f'{model}</h4>'
        search_button = widgets.Button(description='🔎', layout=widgets.Layout(width='48px'))
        search_button.on_click(self.on_search)
        self.text_field = widgets.Text(
            value=text,
            layout=widgets.Layout(width='404px'))
        form_buttons = []
        for form in 'onear inear earbud'.split():
            btn = widgets.Button(description=form, button_style='success', layout=widgets.Layout(width='64px'))
            btn.on_click(self.on_submit)
            form_buttons.append(btn)
        self.widget = widgets.VBox([
            widgets.HBox([
                widgets.HTML(value=title),
                search_button
            ]),
            *buttons,
            widgets.HBox([self.text_field, *form_buttons]),
            widgets.HTML('<hr/>')
        ], layout=widgets.Layout(width='600px'))

    def on_search(self, btn):
        if self.manufacturer:
            self.search_callback(f'{self.manufacturer} {self.model}')
        else:
            self.search_callback(self.model)

    def on_click(self, btn):
        item = self.name_proposals.find_one(true_name=btn.description)
        self.callback(btn.description.strip(), item.form)

    def on_submit(self, btn):
        self.callback(self.text_field.value.strip(), btn.description)
