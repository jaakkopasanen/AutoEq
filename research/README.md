# Research

Install Jupyter Lab
```bash
python -m pip install -U jupyter jupyterlab ipywidgets
```

Install IPywidgets
```bash
jupyter nbextension enable --py widgetsnbextension
jupyter labextension install @jupyter-widgets/jupyterlab-manager
```

Create kernel
```bash
python -m ipykernel install --user --name="autoeq" --display-name="AutoEq (Python 3)"
```

Run Jupyter Lab
```bash
jupyter lab
```
