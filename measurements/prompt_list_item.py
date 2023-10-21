# -*- coding: utf-8 -*-

import ipywidgets as widgets


class PromptListItem:
    def __init__(self, name_prompt, click_callback):
        self.click_callback = click_callback
        self.name_prompt = name_prompt
        self.widget = widgets.Button(
            description=name_prompt.name,
            button_style='warning',
            layout=widgets.Layout(width='300px', height='32px', min_height='32px')
        )
        self.widget.on_click(self.handle_click)
        self.resolution = None

    def handle_click(self, btn):
        self.click_callback(self)

    def active_style(self):
        self.widget.button_style = 'primary'

    def inactive_style(self):
        if self.resolution == 'success':
            self.widget.button_style = 'success'
        elif self.resolution == 'ignore':
            self.widget.button_style = 'danger'
        else:
            self.widget.button_style = 'warning'
