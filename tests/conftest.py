import sys
import os

# Ensure project root and src/ are on sys.path for test discovery
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
src_dir = os.path.join(project_root, 'src')

if project_root not in sys.path:
    sys.path.insert(0, project_root)
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)
