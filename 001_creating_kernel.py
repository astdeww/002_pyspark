# Create a new environment named 'graph_analysis' with necessary packages
conda create --name graph_analysis python=3.8 networkx matplotlib pandas jupyter

# Activate the environment
conda activate graph_analysis

# Install additional graph analysis packages
conda install -c conda-forge python-igraph
conda install -c conda-forge pygraphviz

# Install ipykernel and add the environment as a Jupyter kernel
conda install ipykernel
python -m ipykernel install --user --name graph_analysis --display-name "Graph Analysis"

# Verify the kernel installation
jupyter kernelspec list
