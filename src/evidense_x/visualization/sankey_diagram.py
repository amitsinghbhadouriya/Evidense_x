"""Flow diagram visualizer tracking record migration between clean and defective states."""
import matplotlib.pyplot as plt

def plot_defect_migration_flow(clean_count: int, leaked_count: int, missing_count: int, output_path: str) -> None:
    """Renders a structured flow representation of dataset record defect partitioning."""
    fig, ax = plt.subplots(figsize=(6, 4))
    categories = ["Clean", "Contaminated/Leaked", "Missing/Imputed"]
    counts = [clean_count, leaked_count, missing_count]
    colors = ["#2ecc71", "#e74c3c", "#f39c12"]
    
    ax.bar(categories, counts, color=colors, edgecolor="black", width=0.5)
    ax.set_ylabel("Record Count")
    ax.set_title("Dataset Record Defect State Allocation")
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
