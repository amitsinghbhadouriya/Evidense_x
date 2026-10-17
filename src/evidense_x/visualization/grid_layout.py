import matplotlib.pyplot as plt

def create_multi_panel_grid(nrows: int = 1, ncols: int = 3, figsize=(15, 4)):
    return plt.subplots(nrows, ncols, figsize=figsize)
