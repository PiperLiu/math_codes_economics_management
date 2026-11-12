from pathlib import Path
from runpy import run_path
svg_frame = run_path(str(Path(__file__).with_name('06_visuals.py')))['slice_scene']
