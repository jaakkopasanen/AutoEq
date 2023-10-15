# -*- coding: utf-8 -*-

import ipywidgets as widgets


class NamePrompt:
    def __init__(
            self, item, callback, manufacturer=None, search_callback=None, name_proposals=None, similar_names=None):
        """IPyWidgets UI element for setting name for a crawled headphone"""
        self.item = item
        self.manufacturer = manufacturer
        self.callback = callback
        self.name_proposals = name_proposals
        self.search_callback = search_callback

        # Add button for each name proposal
        buttons = []
        if name_proposals is not None:
            for item in name_proposals.items:
                btn = widgets.Button(
                    description=f'{item.name}', button_style='primary', layout=widgets.Layout(width='400px'))
                btn.on_click(self.on_name_proposal_click)
                buttons.append(btn)

        # Create HTML title
        title = f'<h4 style="margin: 0">{self.item.source_name}</h4>'
        input_text = self.item.source_name

        self.text_field = widgets.Text(value=input_text, layout=widgets.Layout(width='400px'))
        search_button = widgets.Button(description='🔎', layout=widgets.Layout(width='48px'))
        search_button.on_click(self.on_search)

        # Form buttons
        form_buttons = []
        forms = ['over-ear', 'in-ear', 'earbud'] if self.item.form is None else [self.item.form]
        forms.append('ignore')
        for form in forms:
            btn = widgets.Button(
                description=form,
                button_style='danger' if form == 'ignore' else 'success',
                layout=widgets.Layout(width='80px'))
            btn.on_click(self.on_form_click)
            form_buttons.append(btn)

        # Similar names for establishing naming convention
        if similar_names is None:
            similar_names = []

        self.widget = widgets.VBox([
            widgets.HBox([
                widgets.VBox([
                    widgets.HBox([widgets.HTML(value=title), search_button]),  # Title and search
                    *buttons,  # Name suggestions
                ]),
                widgets.HTML(
                    '<div style="margin-left: 12px"><b>Naming convention</b><br />' +
                    '<br>'.join(similar_names) + '</div>'
                ),
            ]),
            widgets.HBox([self.text_field, *form_buttons]),
        ])

    @property
    def name(self):
        return self.item.source_name

    def on_search(self, btn):
        self.search_callback(self.item.source_name)

    def on_name_proposal_click(self, btn):
        btn.button_style = 'success'
        self.callback(self.name_proposals.find_one(name=btn.description).copy())

    def on_form_click(self, btn):
        item = self.item.copy()
        item.name = self.text_field.value.strip()
        item.form = btn.description
        self.callback(item)
