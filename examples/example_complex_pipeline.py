"""
A more complex data pipeline example showing clusters and multiple data flows.
"""

from diagrams import Cluster
from diagrams.aws.database import RDS, DynamoDB
from diagrams.aws.analytics import Kinesis, EMR, Athena, Glue
from diagrams.aws.storage import S3
from diagrams.aws.compute import Lambda

# Import our custom classes
from animated_diagram import AnimatedDiagram, PulsatingEdge
from html_exporter import HtmlExporter

# Create an animated diagram with top-to-bottom direction
with AnimatedDiagram("Complex Data Pipeline", filename="complex_pipeline.svg", direction="TB"):
    # Data sources
    with Cluster("Data Sources"):
        db = RDS("Transactional DB")
        events = DynamoDB("Events Store")
    
    # Ingestion layer
    with Cluster("Ingestion"):
        stream = Kinesis("Data Stream")
        ingest_fn = Lambda("Ingest Function")
    
    # Storage layer
    with Cluster("Storage"):
        raw = S3("Raw Data")
        processed = S3("Processed Data")
        
    # Processing layer
    with Cluster("Processing"):
        etl = Glue("ETL Jobs")
        spark = EMR("Spark Cluster")
    
    # Analytics layer
    with Cluster("Analytics"):
        warehouse = Athena("Data Warehouse")
        reporting_fn = Lambda("Reporting")
    
    # Define the flows with different speeds and colors
    db >> PulsatingEdge(color="blue", pulse_speed="4s") >> stream
    events >> PulsatingEdge(color="blue", pulse_speed="2s") >> stream
    
    stream >> PulsatingEdge(color="green") >> ingest_fn
    ingest_fn >> PulsatingEdge(color="green") >> raw
    
    raw >> PulsatingEdge(color="red") >> etl
    raw >> PulsatingEdge(color="red") >> spark
    
    etl >> PulsatingEdge(color="orange") >> processed
    spark >> PulsatingEdge(color="orange") >> processed
    
    processed >> PulsatingEdge(color="purple") >> warehouse
    warehouse >> PulsatingEdge(color="purple") >> reporting_fn

# Export to HTML for interactive viewing
exporter = HtmlExporter("complex_pipeline.svg")
html_path = exporter.export("complex_pipeline.html")
print(f"HTML exported to: {html_path}")

print("Open the HTML file in a browser to see the animation")