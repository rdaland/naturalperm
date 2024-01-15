import matplotlib.pyplot as pyplot
from figure import Figure

# setup
fig1 = Figure(n_total_elements=24, n_least_elements=6)
fig1.setup_figure()
fig1.setup_nodes()
# 3 -> 6
fig1.register_strand(least_element=3, decreasing_order=True)
fig1.edge_registry.add((3, 6))
fig1.register_strand(least_element=6, decreasing_order=False)
# 2 -> 4
fig1.register_strand(least_element=5, decreasing_order=True)
fig1.edge_registry.add((5, 4))
fig1.register_strand(least_element=4, decreasing_order=False)
# 6 -> 4
fig1.register_strand(least_element=2, decreasing_order=True)
fig1.edge_registry.add((2, 1))
fig1.register_strand(least_element=1, decreasing_order=False)
# render and save
fig1.render()
fig1.savefig("fig1.png")
