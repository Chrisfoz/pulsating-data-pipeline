# Pulsating Data Pipeline Diagrams

Create beautiful data pipeline flow diagrams with pulsating arrows using Python code.

This project extends the ["Diagram as Code"](https://diagrams.mingrammer.com/) concept to create animated data flow visualizations that show the movement of data through your systems.

## Features

- Define data pipelines using simple Python code
- Generate SVG diagrams with animated, pulsating arrows
- Export to HTML for interactive viewing with controls
- Customize animation speed and colors
- Switch between color themes
- Create GIF animations for presentations

## Installation

```bash
# Install the core requirements
pip install diagrams

# Clone this repository
git clone https://github.com/Chrisfoz/pulsating-data-pipeline.git
cd pulsating-data-pipeline

# Optional dependencies for GIF creation
pip install cairosvg imageio numpy pillow
```

## Quick Start

```python
from animated_diagram import AnimatedDiagram, PulsatingEdge
from diagrams.aws.database import RDS
from diagrams.aws.analytics import Kinesis, Athena
from diagrams.aws.storage import S3

# Create an animated diagram
with AnimatedDiagram("Simple Data Pipeline", filename="pipeline.svg"):
    source = RDS("Source DB")
    stream = Kinesis("Data Stream")
    storage = S3("Data Lake")
    analytics = Athena("Analytics")
    
    # Define flows with pulsating arrows
    source >> PulsatingEdge(color="blue") >> stream
    stream >> PulsatingEdge(color="green") >> storage
    storage >> PulsatingEdge(color="red") >> analytics

# Export to HTML with interactive controls
from html_exporter import HtmlExporter
exporter = HtmlExporter("pipeline.svg")
exporter.export("pipeline.html")
```

## Examples

See the [examples](./examples) directory for more detailed examples:

- `example_simple_pipeline.py`: A basic data pipeline with pulsating arrows
- `example_complex_pipeline.py`: A multi-stage pipeline with clusters and different arrow colors/speeds

## Output Formats

### SVG with Animations
The SVG output includes CSS animations that will show pulsating arrows when viewed in a modern web browser.

### HTML with Interactive Controls
The HTML exporter creates a page with your diagram and adds controls to:
- Pause/play animations
- Adjust animation speed
- Switch between color themes

### GIF/Video (Limited)
The `create_gif_from_svg` function can create GIF files, but these won't show the animations. For true animations, you'll need to:
1. Use the HTML output
2. Use a screen recorder to capture the animations
3. Convert to GIF or video as needed

## Extending and Customizing

### Adding New Color Themes

Edit the `html_exporter.py` file to add new color themes:

```python
# Add a new theme in the CSS section
.theme-dark .blue-pulse { stroke: #003366; }
.theme-dark .green-pulse { stroke: #006633; }
.theme-dark .red-pulse { stroke: #660033; }
```

### Creating Custom Animation Patterns

Modify the `@keyframes pulse` definition in `animated_diagram.py`:

```css
@keyframes pulse {
    0% { stroke-width: 1; stroke-opacity: 0.8; }
    25% { stroke-width: 3; stroke-opacity: 1; }
    50% { stroke-width: 1; stroke-opacity: 0.8; }
    75% { stroke-width: 3; stroke-opacity: 1; }
    100% { stroke-width: 1; stroke-opacity: 0.8; }
}
```

## License

MIT

## Acknowledgments

This project is built on top of the excellent [diagrams](https://github.com/mingrammer/diagrams) library by MinJae Kwon (mingrammer).