from plotly.subplots import make_subplots
import plotly.graph_objects as go

data = {
    "CAD": {
        "Solidworks": 11,
        "SW PDM": 7,
        "Inventor": 5,
        "AutoCAD": 5,
        "ProEngineer": 3,
    },
    "FEA/Simulation": {
        "ANSYS": 7,
        "SW Simulation": 2,
        "SKF Simpro": 2,
    },
    "Programming": {
        "Python": 10,
        "C/C++": 2,
        "VBA": 3,
        "Matlab": 4,
        # "Julia": 1,
        "Excel": 11,
        "Docker": 3,
    },
    "OS": {
        "Mac OS": 7,
        "Windows": 11,
        "Linux": 7,
    },
    "Project": {
        "Jira": 2,
        "MS Project": 2,
        "Hansoft": 2,
    },
}

sorted_data = [
    sorted(val.items(), key=lambda kv: kv[1], reverse=True) for val in data.values()
]

X = [[kv[0] for kv in data] for data in sorted_data]
Y = [[min(kv[1], 10) for kv in data] for data in sorted_data]

max_len = max((len(data) for data in sorted_data))
norm_width = lambda X: [x / max_len for x in X]

fig = make_subplots(
    rows=1,
    cols=5,
    shared_yaxes=True,
    shared_xaxes=True,
    column_widths=norm_width([len(x) for x in X]),
    horizontal_spacing=0.012,
    column_titles=list(data.keys()),
)

[
    fig.add_trace(
        go.Bar(
            x=x,
            y=y,
            marker=dict(
                color=y,
                # colorscale="gray",
                colorscale="viridis",
                cmin=-4,
                cmax=15,
                reversescale=True,
            ),
        ),
        row=1,
        col=col + 1,
    )
    for col, (x, y) in enumerate(zip(X, Y))
]

fig.update_layout(
    barmode="stack",
    #   xaxis=dict('categoryorder':'value descending'},
    width=1800,
    height=520,
    showlegend=False,
    yaxis=dict(
        range=[0, 10],
        tickmode="array",
        tickvals=[*range(11)],
        ticktext=[1, *[" "] * 4, 5, *[" "] * 3, 10, "+"],
        tickfont=dict(size=32),
        nticks=10,
    ),
    font=dict(family="Arial", size=32, color="black"),
    # font=dict(family="Red Hat Display", size=32, color="black"),
    plot_bgcolor="#F3F3F3",
)

fig.update_xaxes(tickfont=dict(size=30), tickangle=-45)
fig.update_yaxes(
    nticks=11,
    gridcolor="#D0D0D0",
)

fig["layout"]["yaxis"]["title"] = "Years Experience"
fig["layout"]["yaxis"]["title"].update(
    font=dict(size=32),
)

fig.update_annotations(font_size=34)
# fig.show()

# fig.write_image("fig1.png")
fig.write_html("fig1.html")
