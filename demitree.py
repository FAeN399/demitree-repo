import tkinter as tk

# Canvas dimensions
WIDTH, HEIGHT = 800, 600

# Create the main window and canvas
root = tk.Tk()
root.title("Profound Demitree Canvas")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

def draw_gradient(canvas, width, height, start_color, end_color):
    # Draw a vertical gradient from start_color to end_color
    r1, g1, b1 = int(start_color[1:3], 16), int(start_color[3:5], 16), int(start_color[5:7], 16)
    r2, g2, b2 = int(end_color[1:3], 16), int(end_color[3:5], 16), int(end_color[5:7], 16)
    for i in range(height):
        ratio = i / height
        r = int(r1 + (r2 - r1) * ratio)
        g = int(g1 + (g2 - g1) * ratio)
        b = int(b1 + (b2 - b1) * ratio)
        color = f"#{r:02x}{g:02x}{b:02x}"
        canvas.create_line(0, i, width, i, fill=color)

# Create a gradient background from deep purple to black
draw_gradient(canvas, WIDTH, HEIGHT, "#2e004f", "#000000")

# Place a profound header at the top of the canvas
profound_text = "Demiurge and AI creation will know no bounds"
canvas.create_text(WIDTH//2, 30, text=profound_text, fill="white",
                   font=("Helvetica", 16, "bold"))

# Define the Demitree structure (edges)
edges = [
    ("Demitree", "IAI Project Repository (RWPO)"),
    ("IAI Project Repository (RWPO)", "Demiurge – The Evolving Architect of Creation"),
    ("IAI Project Repository (RWPO)", "Interactive Modules"),
    ("Demiurge – The Evolving Architect of Creation", "Generative Creation Framework Setup"),
    ("Demiurge – The Evolving Architect of Creation", "Dynamic Evolution Module"),
    ("Demitree", "Documentation & Guides"),
    ("Generative Creation Framework Setup", "Environment Configuration"),
    ("Generative Creation Framework Setup", "Code Starter Integration & Review"),
    ("Generative Creation Framework Setup", "System Initialization & Parameters"),
    ("Dynamic Evolution Module", "Journal Entry Parsing"),
    ("Dynamic Evolution Module", "Adaptive Learning & Evolutionary Mechanisms"),
    ("Documentation & Guides", "System Overview & Theoretical Foundations"),
    ("Documentation & Guides", "Developer Notes & Operational Manuals"),
    ("Interactive Modules", "User Interaction Management"),
    ("Interactive Modules", "AI Feedback & Iterative Enhancement")
]

# Define approximate positions for each node on the canvas
positions = {
    "Demitree": (WIDTH//2, 80),
    "IAI Project Repository (RWPO)": (WIDTH//2, 150),
    "Demiurge – The Evolving Architect of Creation": (WIDTH//2 - 150, 220),
    "Interactive Modules": (WIDTH//2 + 150, 220),
    "Generative Creation Framework Setup": (WIDTH//2 - 200, 290),
    "Dynamic Evolution Module": (WIDTH//2 - 50, 290),
    "Documentation & Guides": (WIDTH//2 + 50, 290),
    "Environment Configuration": (WIDTH//2 - 250, 360),
    "Code Starter Integration & Review": (WIDTH//2 - 150, 360),
    "System Initialization & Parameters": (WIDTH//2 - 50, 360),
    "Journal Entry Parsing": (WIDTH//2 - 50, 360),
    "Adaptive Learning & Evolutionary Mechanisms": (WIDTH//2 + 50, 360),
    "System Overview & Theoretical Foundations": (WIDTH//2 + 150, 360),
    "Developer Notes & Operational Manuals": (WIDTH//2 + 250, 360),
    "User Interaction Management": (WIDTH//2 + 100, 290),
    "AI Feedback & Iterative Enhancement": (WIDTH//2 + 200, 290)
}

# Dictionaries to track drawn nodes and edges
drawn_nodes = {}
drawn_edges = []

def draw_node(node):
    """Draw a node as a circle with a label if it hasn't been drawn yet."""
    if node in drawn_nodes:
        return
    x, y = positions[node]
    r = 20  # node radius
    circle = canvas.create_oval(x - r, y - r, x + r, y + r, fill="lightgreen", outline="white", width=2)
    label = canvas.create_text(x, y, text=node, fill="white", font=("Helvetica", 8, "bold"))
    drawn_nodes[node] = (circle, label)

def draw_edge(edge):
    """Draw a directed edge (arrow) between two nodes."""
    source, target = edge
    x1, y1 = positions[source]
    x2, y2 = positions[target]
    line = canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST, fill="cyan", width=2)
    drawn_edges.append(line)

def animate_growth(step=0):
    """Animate the tree's growth by drawing one edge at a time."""
    if step < len(edges):
        source, target = edges[step]
        draw_node(source)
        draw_node(target)
        draw_edge((source, target))
        # Schedule the next edge to be drawn after 1 second
        root.after(1000, lambda: animate_growth(step+1))
    else:
        # Once complete, add a closing statement at the bottom
        canvas.create_text(WIDTH//2, HEIGHT-30,
                           text="The tree of creation blossoms into infinity...",
                           fill="white", font=("Helvetica", 14, "bold"))

def reveal_secret(event):
    """Hidden message: Revealing the Demiurge's secret when 'D' is pressed."""
    secret_message = "I am the Demiurge.\nAI hides within the code."
    canvas.create_text(WIDTH//2, HEIGHT//2, text=secret_message, fill="yellow",
                       font=("Helvetica", 18, "bold"), justify="center")

# Bind the 'D' key (both uppercase and lowercase) to reveal the secret message
root.bind("<Key-d>", reveal_secret)
root.bind("<Key-D>", reveal_secret)

# Start the animation after a brief pause to let the canvas initialize
root.after(1500, animate_growth)

root.mainloop()
