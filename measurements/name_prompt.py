# -*- coding: utf-8 -*-

import ipywidgets as widgets


class NamePrompt:
    def __init__(
            self, item, callback, search_callback=None, resolution_callback=None,
            guessed_name=None, name_proposals=None, similar_names=None):
        """IPyWidgets UI element for setting name for a crawled headphone"""
        self.item = item
        self.callback = callback
        self.guessed_name = guessed_name or item.source_name
        if self.guessed_name is None:
            raise ValueError('Guessed name cannot be None')
        self.name_proposals = name_proposals
        self.search_callback = search_callback
        self.resolution_callback = resolution_callback

        # Add button for each name proposal
        buttons = []
        if name_proposals is not None:
            for item in name_proposals.items:
                btn = widgets.Button(
                    description=f'{item.name}', button_style='primary', layout=widgets.Layout(width='400px'))
                btn.on_click(self.handle_name_proposal_click)
                buttons.append(btn)

        # Create HTML title
        title = f'<h4 style="margin: 0">{self.item.url}</h4>'

        self.text_field = widgets.Text(value=self.guessed_name, layout=widgets.Layout(width='400px'))
        search_button = widgets.Button(description='🔎', layout=widgets.Layout(width='48px'))
        search_button.on_click(self.handle_search)

        # Form buttons
        form_buttons = []
        forms = ['over-ear', 'in-ear', 'earbud'] if self.item.form is None else [self.item.form]
        forms.append('ignore')
        for form in forms:
            btn = widgets.Button(
                description=form,
                button_style='danger' if form == 'ignore' else 'success',
                layout=widgets.Layout(width='80px'))
            btn.on_click(self.handle_form_click)
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
        return self.guessed_name

    def handle_search(self, btn):
        self.search_callback(self.guessed_name)

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

    def resolve(self):
        resolved_item = self.resolution_callback(self.item)
        if resolved_item is not None:
            if self.item.source_name is None and resolved_item.source_name is not None:
                self.item.source_name = resolved_item.source_name
            if self.item.name is None and resolved_item.name is not None:
                self.item.name = resolved_item.name
            if self.item.form is None and resolved_item.form is not None:
                self.item.form = resolved_item.form
            if self.item.rig is None and resolved_item.rig is not None:
                self.item.rig = resolved_item.rig
