import os

class PathResolver:
    @staticmethod
    def get_results_dir(base: str = ".") -> str:
        d = os.path.join(base, "results")
        os.makedirs(d, exist_ok=True)
        return d

    @staticmethod
    def get_figures_dir(base: str = ".") -> str:
        d = os.path.join(base, "figures")
        os.makedirs(d, exist_ok=True)
        return d
