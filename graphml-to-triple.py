import networkx as nx
import csv
import re

# Load GraphML
# replace with your file path
G = nx.read_graphml("kwg-lite-schema-diagram.graphml")


def clean_label(label):
    """Convert GraphML node labels to readable format."""
    if not label:
        return None
    if isinstance(label, str):
        label = label.strip()
        # Skip 'n1', 'n5', etc.
        if re.fullmatch(r"n\d+", label):
            return None
    return label

# Try to get labels or use node id fallback


def get_node_label(node_id):
    node_data = G.nodes[node_id]
    return clean_label(node_data.get('label') or node_id)

# Get edge label or default to relationship if missing


def get_edge_label(u, v, edge_data):
    label = edge_data.get('label') or edge_data.get('type') or 'relatedTo'
    return label.strip()


triples = []

# Extract triples
for u, v, edge_data in G.edges(data=True):
    subj = get_node_label(u)
    obj = get_node_label(v)
    pred = get_edge_label(u, v, edge_data)

    if subj and obj:
        triples.append((subj, pred, obj))

# Deduplicate
triples = list(set(triples))

# Write to CSV
with open('cleaned_triples_lite.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['subject', 'predicate', 'object'])
    for triple in triples:
        writer.writerow(triple)
