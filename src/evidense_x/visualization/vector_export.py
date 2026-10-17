def save_vector_figure(fig, out_path: str, dpi: int = 300):
    fig.savefig(out_path, dpi=dpi, bbox_inches='tight')
