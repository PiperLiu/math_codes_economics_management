"""SVG-to-GIF entry point; see 03_pinv_scenes.py for geometry."""
from pathlib import Path
import runpy
svg_frame = runpy.run_path(str(Path(__file__).with_name('03_pinv_scenes.py')))['minimum']
