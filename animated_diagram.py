from diagrams import Diagram, Edge
import os
import tempfile
import shutil

class PulsatingEdge(Edge):
    """An edge that shows a pulsating animation effect"""
    
    def __init__(self, color="blue", pulse_speed="3s", **kwargs):
        super().__init__(**kwargs)
        self.attributes["class"] = f"pulsating-arrow {color}-pulse"
        self.attributes["data-pulse-speed"] = pulse_speed
        self.attributes["stroke"] = color

class AnimatedDiagram(Diagram):
    """A diagram that outputs SVG with animated edges"""
    
    def __init__(self, name, filename=None, direction="LR", **kwargs):
        if filename and not filename.endswith(".svg"):
            filename = f"{filename}.svg"
        
        kwargs["outformat"] = "svg"
        super().__init__(name, filename=filename, direction=direction, **kwargs)
    
    def render(self):
        """Render the diagram and add animation definitions"""
        original_svg_path = super().render()
        
        # Read the original SVG
        with open(original_svg_path, 'r') as f:
            svg_content = f.read()
        
        # Add animation styles
        animation_styles = """
        <style>
            @keyframes pulse {
                0% { stroke-width: 1; stroke-opacity: 0.8; }
                50% { stroke-width: 3; stroke-opacity: 1; }
                100% { stroke-width: 1; stroke-opacity: 0.8; }
            }
            
            .pulsating-arrow {
                animation: pulse var(--pulse-speed, 3s) infinite;
            }
            
            .blue-pulse {
                stroke: #0066cc;
                --pulse-speed: 3s;
            }
            
            .green-pulse {
                stroke: #00cc66;
                --pulse-speed: 2.5s;
            }
            
            .red-pulse {
                stroke: #cc3300;
                --pulse-speed: 2s;
            }
            
            .orange-pulse {
                stroke: #ff9900;
                --pulse-speed: 4s;
            }
            
            .purple-pulse {
                stroke: #9900cc;
                --pulse-speed: 5s;
            }
        </style>
        """
        
        # Insert the animation styles after the opening SVG tag
        enhanced_svg = svg_content.replace("<svg ", f"<svg \n{animation_styles}")
        
        # Write the enhanced SVG back
        with open(original_svg_path, 'w') as f:
            f.write(enhanced_svg)
        
        return original_svg_path

def create_gif_from_svg(svg_path, output_gif=None, duration=10, fps=15):
    """Convert SVG to GIF animation using cairosvg and imageio
    
    This function requires the following packages:
    - cairosvg
    - imageio
    - numpy
    - pillow
    """
    try:
        import cairosvg
        import imageio
        import numpy as np
        from PIL import Image
    except ImportError:
        print("Error: Required packages not found. Please install: cairosvg, imageio, numpy, pillow")
        return None
    
    if output_gif is None:
        output_gif = os.path.splitext(svg_path)[0] + ".gif"
    
    # Create a temp directory for frames
    temp_dir = tempfile.mkdtemp()
    
    try:
        # Generate frames
        frame_count = duration * fps
        frames = []
        
        # Convert SVG to PNG
        png_path = os.path.join(temp_dir, "base.png")
        cairosvg.svg2png(url=svg_path, write_to=png_path, scale=2.0)
        
        # Use the PNG for all frames (animation is handled by browser)
        base_img = np.array(Image.open(png_path))
        
        # Create the GIF (static image since we can't capture CSS animations)
        # Note: The actual animation needs a browser or SVG viewer that supports animations
        with imageio.get_writer(output_gif, mode='I', duration=1/fps) as writer:
            for _ in range(frame_count):
                writer.append_data(base_img)
        
        print(f"GIF created at {output_gif}, but note that it won't show the animation.")
        print("For animated arrows, view the SVG file in a web browser.")
        
        return output_gif
        
    finally:
        # Clean up temporary files
        shutil.rmtree(temp_dir)