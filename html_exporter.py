import os

class HtmlExporter:
    """Exports an SVG diagram to an HTML file with interactive controls"""
    
    def __init__(self, svg_path):
        self.svg_path = svg_path
        
    def export(self, output_path=None):
        """Export the SVG to an HTML file with controls"""
        if not output_path:
            output_path = os.path.splitext(self.svg_path)[0] + '.html'
        
        # Read the SVG content
        with open(self.svg_path, 'r') as f:
            svg_content = f.read()
        
        # HTML template with controls
        html_template = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Animated Data Pipeline</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 20px;
                    background-color: #f5f5f5;
                }
                
                h1 {
                    color: #333;
                    margin-bottom: 20px;
                }
                
                .controls {
                    margin-bottom: 20px;
                    padding: 15px;
                    background-color: #fff;
                    border-radius: 8px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                }
                
                .diagram-container {
                    border: 1px solid #ddd;
                    padding: 20px;
                    border-radius: 8px;
                    background-color: white;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                    overflow: auto;
                }
                
                button {
                    padding: 8px 15px;
                    margin-right: 10px;
                    cursor: pointer;
                    background-color: #4a86e8;
                    color: white;
                    border: none;
                    border-radius: 4px;
                    font-weight: bold;
                }
                
                button:hover {
                    background-color: #3a76d8;
                }
                
                /* Animation speeds */
                .speed-normal .pulsating-arrow {
                    animation-duration: var(--pulse-speed, 3s);
                }
                
                .speed-fast .pulsating-arrow {
                    animation-duration: calc(var(--pulse-speed, 3s) / 2);
                }
                
                .speed-slow .pulsating-arrow {
                    animation-duration: calc(var(--pulse-speed, 3s) * 2);
                }
                
                .paused .pulsating-arrow {
                    animation-play-state: paused;
                }
                
                /* Color themes */
                .theme-default .blue-pulse { stroke: #0066cc; }
                .theme-default .green-pulse { stroke: #00cc66; }
                .theme-default .red-pulse { stroke: #cc3300; }
                .theme-default .orange-pulse { stroke: #ff9900; }
                .theme-default .purple-pulse { stroke: #9900cc; }
                
                .theme-neon .blue-pulse { stroke: #00ffff; }
                .theme-neon .green-pulse { stroke: #00ff00; }
                .theme-neon .red-pulse { stroke: #ff00ff; }
                .theme-neon .orange-pulse { stroke: #ffff00; }
                .theme-neon .purple-pulse { stroke: #9d00ff; }
                
                .theme-pastel .blue-pulse { stroke: #aaccff; }
                .theme-pastel .green-pulse { stroke: #aaffcc; }
                .theme-pastel .red-pulse { stroke: #ffaacc; }
                .theme-pastel .orange-pulse { stroke: #ffddaa; }
                .theme-pastel .purple-pulse { stroke: #ddaaff; }
            </style>
        </head>
        <body>
            <h1>Animated Data Pipeline</h1>
            
            <div class="controls">
                <h3>Animation Controls</h3>
                <button id="pause-btn">Pause</button>
                <button id="play-btn">Play</button>
                <button id="speed-normal">Normal Speed</button>
                <button id="speed-slow">Slow</button>
                <button id="speed-fast">Fast</button>
                
                <h3>Color Themes</h3>
                <button id="theme-default">Default</button>
                <button id="theme-neon">Neon</button>
                <button id="theme-pastel">Pastel</button>
            </div>
            
            <div class="diagram-container theme-default" id="diagram">
                %s
            </div>
            
            <script>
                // Animation controls
                document.getElementById('pause-btn').addEventListener('click', function() {
                    document.getElementById('diagram').classList.add('paused');
                });
                
                document.getElementById('play-btn').addEventListener('click', function() {
                    document.getElementById('diagram').classList.remove('paused');
                });
                
                document.getElementById('speed-normal').addEventListener('click', function() {
                    const diagram = document.getElementById('diagram');
                    diagram.classList.remove('speed-slow', 'speed-fast');
                    diagram.classList.add('speed-normal');
                });
                
                document.getElementById('speed-slow').addEventListener('click', function() {
                    const diagram = document.getElementById('diagram');
                    diagram.classList.remove('speed-normal', 'speed-fast');
                    diagram.classList.add('speed-slow');
                });
                
                document.getElementById('speed-fast').addEventListener('click', function() {
                    const diagram = document.getElementById('diagram');
                    diagram.classList.remove('speed-normal', 'speed-slow');
                    diagram.classList.add('speed-fast');
                });
                
                // Theme controls
                document.getElementById('theme-default').addEventListener('click', function() {
                    const diagram = document.getElementById('diagram');
                    diagram.classList.remove('theme-neon', 'theme-pastel');
                    diagram.classList.add('theme-default');
                });
                
                document.getElementById('theme-neon').addEventListener('click', function() {
                    const diagram = document.getElementById('diagram');
                    diagram.classList.remove('theme-default', 'theme-pastel');
                    diagram.classList.add('theme-neon');
                });
                
                document.getElementById('theme-pastel').addEventListener('click', function() {
                    const diagram = document.getElementById('diagram');
                    diagram.classList.remove('theme-default', 'theme-neon');
                    diagram.classList.add('theme-pastel');
                });
            </script>
        </body>
        </html>
        """ % svg_content
        
        # Write the HTML file
        with open(output_path, 'w') as f:
            f.write(html_template)
            
        return output_path