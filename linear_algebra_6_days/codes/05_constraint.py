from pathlib import Path
import runpy
svg_frame = runpy.run_path(str(Path(__file__).with_name('05_visuals.py')))['constraint']
