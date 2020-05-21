# Research

Install IPywidgets
```bash
jupyter nbextension enable --py widgetsnbextension
jupyter labextension install @jupyter-widgets/jupyterlab-manager
```

Create kernel
```bash
python -m ipykernel install --user --name="ai-lab" --display-name="AutoEq (Python 3)"
```

Run Jupyter Lab
```bash
jupyter lab
```