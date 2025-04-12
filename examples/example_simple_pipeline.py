"""
A simple data pipeline example showing data flow with pulsating arrows.
"""

from diagrams import Node
from diagrams.aws.database import RDS
from diagrams.aws.analytics import Kinesis, Athena
from diagrams.aws.storage import S3

# Import our custom classes
from animated_diagram import AnimatedDiagram, PulsatingEdge
from html_exporter import HtmlExporter

# Create an animated diagram
with AnimatedDiagram("Simple Data Pipeline", filename="simple_pipeline.svg"):
    source = RDS("Source DB")
    stream = Kinesis("Data Stream")
    storage = S3("Raw Storage")
    analytics = Athena("Analytics")
    
    # Define flows with pulsating arrows
    source >> PulsatingEdge(color="blue") >> stream
    stream >> PulsatingEdge(color="green") >> storage
    storage >> PulsatingEdge(color="red") >> analytics

# Export to HTML for interactive viewing
exporter = HtmlExporter("simple_pipeline.svg")
html_path = exporter.export("simple_pipeline.html")
print(f"HTML exported to: {html_path}")

print("Open the HTML file in a browser to see the animation")