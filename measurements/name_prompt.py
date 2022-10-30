# -*- coding: utf-8 -*-

import ipywidgets as widgets


class NamePrompt:
    def __init__(self, model, callback, manufacturer=None, name_proposals=None, search_callback=None, false_name=None,
                 form=None, similar_names=None):
        self.model = model
        self.callback = callback
        self.manufacturer = manufacturer
        self.name_proposals = name_proposals
        self.search_callback = search_callback

        # Add button for each name proposal
        buttons = []
        if name_proposals is not None:
            for item in name_proposals.items:
                btn = widgets.Button(
                    description=f'{item.true_name}', button_style='primary', layout=widgets.Layout(width='596px'))
                btn.on_click(self.on_click)
                buttons.append(btn)

        # Create HTML title
        title = '<h4 style="margin: 0">'
        if false_name:
            title += f'{false_name} → '
        if manufacturer:
            title += f'<span style="color: blue">{manufacturer}&nbsp;</span>'
            text = f'{manufacturer} {model}'
        else:
            text = model
        title += f'{model}</h4>'

        # Name input field
        self.text_field = widgets.Text(
            value=text,
            layout=widgets.Layout(width='404px'))

        # Search button
        search_button = widgets.Button(description='🔎', layout=widgets.Layout(width='48px'))
        search_button.on_click(self.on_search)

        # Form buttons
        form_buttons = []
        forms = ['onear', 'inear', 'earbud'] if form is None else [form]
        forms.append('ignore')
        for form in forms:
            btn = widgets.Button(
                description=form,
                button_style='danger' if form == 'ignore' else 'success',
                layout=widgets.Layout(width='64px'))
            btn.on_click(self.on_submit)
            form_buttons.append(btn)

        # Similar names for establishing naming convention
        if similar_names is None:
            similar_names = []

        self.widget = widgets.VBox([
            widgets.HBox([
                widgets.VBox([
                    widgets.HBox([
                        widgets.HTML(value=title),
                        search_button
                    ]),
                    *buttons,
                    widgets.HBox([self.text_field, *form_buttons]),
                ]),
                widgets.HTML('<div style="margin-left: 12px">' + '<br>'.join(similar_names) + '</div>')
            ]),
            widgets.HTML('<hr/>')
        ], layout=widgets.Layout(width='1200px'))

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
