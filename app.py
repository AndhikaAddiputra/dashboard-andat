import json
import dash
from dash import dcc, html, dash_table, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

RISK_COLORS = {
    "Risiko Tinggi": "#d9534f",
    "Risiko Sedang": "#f0ad4e",
    "Risiko Rendah": "#5cb85c",
}

MAIN_DATA = "data/dataset_bersih.csv"
GEOJSON_PATH = "data/jabar_27.geojson"
RANKING_PATH = "data/ranking_risiko_kabkota.csv"
CLUSTER_SUMMARY_PATH = "data/cluster_summary.csv"
CORRELATION_PATH = "data/correlation_matrix.csv"

df = pd.read_csv(MAIN_DATA)
with open(GEOJSON_PATH) as f:
    geojson_data = json.load(f)

ranking = pd.read_csv(RANKING_PATH)
cluster_summary = pd.read_csv(CLUSTER_SUMMARY_PATH)
corr = pd.read_csv(CORRELATION_PATH, index_col=0)

df["Kab_Kota"] = df["Kab_Kota"].str.strip()

# Merge ranking data into main df for easy lookup
df = df.merge(
    ranking[["nama_wilayah_display", "ranking_risiko", "risk_index"]],
    left_on="Kab_Kota",
    right_on="nama_wilayah_display",
    how="left",
)
df.drop(columns=["nama_wilayah_display"], inplace=True)

kabkotas = sorted(df["Kab_Kota"].unique())

# Mapping Tingkat_Kerentanan -> prioritas_risiko in cluster_summary
RISK_TO_PRIORITY = {
    "Risiko Tinggi": "Prioritas Tinggi",
    "Risiko Sedang": "Prioritas Sedang",
    "Risiko Rendah": "Prioritas Rendah",
}

TERMINAL_COLORS = {
    "background": "#F8F9FA",
    "card_bg": "#FFFFFF",
    "text": "#212529",
    "accent": "#0D6EFD",
    "border": "#DEE2E6",
}

color_discrete_map = {
    "Risiko Tinggi": RISK_COLORS["Risiko Tinggi"],
    "Risiko Sedang": RISK_COLORS["Risiko Sedang"],
    "Risiko Rendah": RISK_COLORS["Risiko Rendah"],
}

app = dash.Dash(
    __name__,
    title="Dashboard Risiko Putus Sekolah Jawa Barat 2024",
    suppress_callback_exceptions=True,
)

app.layout = html.Div(
    style={"backgroundColor": TERMINAL_COLORS["background"], "fontFamily": "Inter, system-ui, sans-serif", "padding": "0", "margin": "0"},
    children=[
        html.Div(
            style={
                "backgroundColor": "#1a1a2e",
                "padding": "24px 32px",
                "color": "white",
                "display": "flex",
                "justifyContent": "space-between",
                "alignItems": "center",
                "flexWrap": "wrap",
                "gap": "12px",
            },
            children=[
                html.Div([
                    html.H1("Analisis Spasial & Klastering Risiko Putus Sekolah", style={"margin": "0", "fontSize": "22px", "fontWeight": "600"}),
                    html.P("Jawa Barat 2024 — 27 Kabupaten/Kota", style={"margin": "4px 0 0", "fontSize": "14px", "opacity": "0.8"}),
                ]),
                html.Div([
                    dcc.Dropdown(
                        id="kabkota-filter",
                        options=[{"label": "Semua Wilayah", "value": "ALL"}] + [{"label": k, "value": k} for k in kabkotas],
                        value="ALL",
                        clearable=False,
                        style={"width": "260px", "color": "#212529"},
                    ),
                ]),
            ],
        ),
        html.Div(
            style={
                "maxWidth": "1440px",
                "margin": "0 auto",
                "padding": "24px",
                "display": "flex",
                "flexDirection": "column",
                "gap": "20px",
            },
            children=[
                html.Div(
                    style={
                        "backgroundColor": TERMINAL_COLORS["card_bg"],
                        "borderRadius": "12px",
                        "boxShadow": "0 1px 3px rgba(0,0,0,0.08)",
                        "padding": "20px",
                        "border": f"1px solid {TERMINAL_COLORS['border']}",
                    },
                    children=[
                        html.H2("Peta Sebaran Risiko Putus Sekolah", style={"fontSize": "18px", "margin": "0 0 12px", "color": TERMINAL_COLORS["text"]}),
                        dcc.Graph(id="choropleth-map", style={"height": "520px"}),
                        html.Div(id="region-detail-card", style={"marginTop": "16px"}),
                    ],
                ),
                html.Div(
                    style={
                        "display": "grid",
                        "gridTemplateColumns": "1fr 1fr",
                        "gap": "20px",
                    },
                    children=[
                        html.Div(
                            style={
                                "backgroundColor": TERMINAL_COLORS["card_bg"],
                                "borderRadius": "12px",
                                "boxShadow": "0 1px 3px rgba(0,0,0,0.08)",
                                "padding": "20px",
                                "border": f"1px solid {TERMINAL_COLORS['border']}",
                            },
                            children=[
                                html.H2("Korelasi Kemiskinan vs Putus Sekolah", style={"fontSize": "18px", "margin": "0 0 12px", "color": TERMINAL_COLORS["text"]}),
                                dcc.Graph(id="scatter-plot", style={"height": "400px"}),
                            ],
                        ),
                        html.Div(
                            style={
                                "backgroundColor": TERMINAL_COLORS["card_bg"],
                                "borderRadius": "12px",
                                "boxShadow": "0 1px 3px rgba(0,0,0,0.08)",
                                "padding": "20px",
                                "border": f"1px solid {TERMINAL_COLORS['border']}",
                            },
                            children=[
                                html.H2("Breakdown Putus Sekolah per Jenjang", style={"fontSize": "18px", "margin": "0 0 12px", "color": TERMINAL_COLORS["text"]}),
                                dcc.Graph(id="bar-chart", style={"height": "400px"}),
                            ],
                        ),
                    ],
                ),
                html.Div(
                    style={
                        "display": "grid",
                        "gridTemplateColumns": "1fr 1fr",
                        "gap": "20px",
                    },
                    children=[
                        html.Div(
                            style={
                                "backgroundColor": TERMINAL_COLORS["card_bg"],
                                "borderRadius": "12px",
                                "boxShadow": "0 1px 3px rgba(0,0,0,0.08)",
                                "padding": "20px",
                                "border": f"1px solid {TERMINAL_COLORS['border']}",
                            },
                            children=[
                                html.H2("Peringkat Risiko Kabupaten/Kota", style={"fontSize": "18px", "margin": "0 0 12px", "color": TERMINAL_COLORS["text"]}),
                                html.Div(id="ranking-table-container"),
                            ],
                        ),
                        html.Div(
                            style={
                                "backgroundColor": TERMINAL_COLORS["card_bg"],
                                "borderRadius": "12px",
                                "boxShadow": "0 1px 3px rgba(0,0,0,0.08)",
                                "padding": "20px",
                                "border": f"1px solid {TERMINAL_COLORS['border']}",
                            },
                            children=[
                                html.H2("Karakteristik Klaster Risiko", style={"fontSize": "18px", "margin": "0 0 12px", "color": TERMINAL_COLORS["text"]}),
                                html.Div(id="cluster-summary-container"),
                            ],
                        ),
                    ],
                ),
            ],
        ),
    ],
)


def _risk_color(value):
    if value == "Risiko Tinggi":
        return RISK_COLORS["Risiko Tinggi"]
    elif value == "Risiko Sedang":
        return RISK_COLORS["Risiko Sedang"]
    elif value == "Risiko Rendah":
        return RISK_COLORS["Risiko Rendah"]
    return "#999"


def _build_choropleth(selected_kabkota):
    df_map = df.copy()
    hover_data = {
        "Kab_Kota": True,
        "Tingkat_Kerentanan": True,
        "Persentase_Miskin_Maret": ":.2f",
        "Putus_Sekolah_per_10k_Penduduk": ":.2f",
        "Total_Putus_Sekolah": True,
        "IPM_2024": ":.2f",
    }
    fig = px.choropleth_map(
        df_map,
        geojson=geojson_data,
        locations="Kab_Kota",
        featureidkey="properties.Kab_Kota",
        color="Tingkat_Kerentanan",
        color_discrete_map=color_discrete_map,
        map_style="carto-positron",
        zoom=7.5,
        center={"lat": -6.9, "lon": 107.6},
        opacity=0.85,
        labels={"Tingkat_Kerentanan": "Tingkat Risiko"},
        hover_name="Kab_Kota",
        hover_data=hover_data,
    )
    fig.update_traces(marker_line_width=1, marker_line_color="white")
    if selected_kabkota != "ALL":
        highlight_colors = []
        for kab in df_map["Kab_Kota"]:
            if kab == selected_kabkota:
                highlight_colors.append("rgba(255, 215, 0, 0.9)")
            else:
                risco = df_map[df_map["Kab_Kota"] == kab]["Tingkat_Kerentanan"].values[0]
                base = _risk_color(risco)
                highlight_colors.append(base.replace("1.0)", "0.4)"))
        fig.update_traces(marker_line_width=[3 if k == selected_kabkota else 1 for k in df_map["Kab_Kota"]])
    fig.update_layout(
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        paper_bgcolor=TERMINAL_COLORS["card_bg"],
        font_color=TERMINAL_COLORS["text"],
        legend=dict(orientation="h", yanchor="bottom", y=1.01, xanchor="right", x=1),
    )
    return fig


def _build_scatter(selected_kabkota):
    df_scatter = df.copy()
    fig = px.scatter(
        df_scatter,
        x="Persentase_Miskin_Maret",
        y="Putus_Sekolah_per_10k_Penduduk",
        color="Tingkat_Kerentanan",
        color_discrete_map=color_discrete_map,
        size=[30] * len(df_scatter),
        size_max=18,
        hover_name="Kab_Kota",
        hover_data={
            "Persentase_Miskin_Maret": ":.2f",
            "Putus_Sekolah_per_10k_Penduduk": ":.2f",
            "Tingkat_Kerentanan": True,
            "Total_Putus_Sekolah": True,
            "IPM_2024": ":.2f",
        },
        labels={
            "Persentase_Miskin_Maret": "Persentase Penduduk Miskin (%)",
            "Putus_Sekolah_per_10k_Penduduk": "Putus Sekolah per 10k Penduduk",
            "Tingkat_Kerentanan": "Tingkat Risiko",
        },
    )
    if selected_kabkota != "ALL":
        fig.update_traces(
            marker=dict(
                line=dict(
                    width=[3 if k == selected_kabkota else 1 for k in df_scatter["Kab_Kota"]],
                    color=["gold" if k == selected_kabkota else "rgba(0,0,0,0.3)" for k in df_scatter["Kab_Kota"]],
                ),
                opacity=[1.0 if k == selected_kabkota else 0.5 for k in df_scatter["Kab_Kota"]],
            )
        )
    fig.update_layout(
        margin={"r": 20, "t": 10, "l": 10, "b": 40},
        paper_bgcolor=TERMINAL_COLORS["card_bg"],
        plot_bgcolor=TERMINAL_COLORS["card_bg"],
        font_color=TERMINAL_COLORS["text"],
        xaxis=dict(gridcolor="#E9ECEF", zeroline=False),
        yaxis=dict(gridcolor="#E9ECEF", zeroline=False),
        legend=dict(orientation="h", yanchor="bottom", y=1.01, xanchor="right", x=1),
    )
    return fig


def _build_bar(selected_kabkota):
    jenjang_cols = ["Putus_SD", "Putus_SMP", "Putus_SMA", "Putus_SMK", "Putus_SLB"]
    if selected_kabkota != "ALL":
        row = df[df["Kab_Kota"] == selected_kabkota]
        if row.empty:
            return go.Figure()
        values = [int(row[c].values[0]) for c in jenjang_cols]
        title_text = f"Breakdown Jenjang — {selected_kabkota}"
    else:
        values = [int(df[c].sum()) for c in jenjang_cols]
        title_text = "Total Putus Sekolah per Jenjang (Semua Wilayah)"

    colors_bar = ["#4C72B0", "#55A868", "#DD8452", "#C44E52", "#937860"]
    fig = go.Figure(
        data=[
            go.Bar(
                x=jenjang_cols,
                y=values,
                marker_color=colors_bar,
                text=values,
                textposition="outside",
                hovertemplate="%{x}: %{y} siswa<extra></extra>",
            )
        ]
    )
    fig.update_layout(
        title={"text": title_text, "font": {"size": 14}},
        margin={"r": 20, "t": 40, "l": 10, "b": 40},
        paper_bgcolor=TERMINAL_COLORS["card_bg"],
        plot_bgcolor=TERMINAL_COLORS["card_bg"],
        font_color=TERMINAL_COLORS["text"],
        xaxis=dict(gridcolor="#E9ECEF", zeroline=False),
        yaxis=dict(gridcolor="#E9ECEF", zeroline=False, title="Jumlah Siswa"),
    )
    return fig


def _build_ranking_table():
    display_cols = ["ranking_risiko", "nama_wilayah_display", "risk_index", "putus_total", "persentase_penduduk_miskin_2024", "ipm_2024"]
    display_names = ["Peringkat", "Wilayah", "Indeks Risiko", "Total Putus", "Kemiskinan (%)", "IPM"]
    df_rank = ranking[display_cols].copy()
    df_rank.columns = display_names
    df_rank["Indeks Risiko"] = df_rank["Indeks Risiko"].round(2)
    df_rank["Kemiskinan (%)"] = df_rank["Kemiskinan (%)"].round(2)
    df_rank["IPM"] = df_rank["IPM"].round(2)

    style_cell = {
        "textAlign": "left",
        "fontSize": "13px",
        "padding": "6px 10px",
        "fontFamily": "Inter, system-ui, sans-serif",
    }
    style_header = {
        **style_cell,
        "fontWeight": "600",
        "backgroundColor": TERMINAL_COLORS["background"],
        "color": TERMINAL_COLORS["text"],
    }
    style_data_conditional = [
        {"if": {"column_id": "Peringkat"}, "fontWeight": "600"},
        {
            "if": {"filter_query": "{Peringkat} <= 5", "column_id": "Peringkat"},
            "backgroundColor": "rgba(217, 83, 79, 0.1)",
            "color": RISK_COLORS["Risiko Tinggi"],
            "fontWeight": "700",
        },
        {
            "if": {"filter_query": "{Peringkat} >= 25", "column_id": "Peringkat"},
            "backgroundColor": "rgba(92, 184, 92, 0.1)",
            "color": RISK_COLORS["Risiko Rendah"],
            "fontWeight": "700",
        },
    ]
    return dash_table.DataTable(
        columns=[{"name": c, "id": c} for c in display_names],
        data=df_rank.to_dict("records"),
        page_size=10,
        sort_action="native",
        style_cell=style_cell,
        style_header=style_header,
        style_data_conditional=style_data_conditional,
        style_table={"overflowX": "auto"},
    )


def _build_cluster_summary():
    cs = cluster_summary.copy()
    cs = cs.rename(columns={
        "prioritas_risiko": "Klaster",
        "jumlah_wilayah": "Jumlah Wilayah",
        "rata_rata_putus_total": "Rata-rata Putus Total",
        "rata_rata_kemiskinan_pct": "Rata-rata Kemiskinan (%)",
        "rata_rata_rls": "Rata-rata RLS (thn)",
        "rata_rata_hls": "Rata-rata HLS (thn)",
    })
    display_cols = ["Klaster", "Jumlah Wilayah", "Rata-rata Putus Total", "Rata-rata Kemiskinan (%)", "Rata-rata RLS (thn)", "Rata-rata HLS (thn)"]
    cs_display = cs[display_cols].copy()
    numeric_cols = ["Rata-rata Putus Total", "Rata-rata Kemiskinan (%)", "Rata-rata RLS (thn)", "Rata-rata HLS (thn)"]
    for c in numeric_cols:
        cs_display[c] = cs_display[c].round(2)

    risk_colors = {
        "Prioritas Rendah": RISK_COLORS["Risiko Rendah"],
        "Prioritas Sedang": RISK_COLORS["Risiko Sedang"],
        "Prioritas Tinggi": RISK_COLORS["Risiko Tinggi"],
    }

    style_cell = {
        "textAlign": "left",
        "fontSize": "13px",
        "padding": "8px 10px",
        "fontFamily": "Inter, system-ui, sans-serif",
    }
    style_header = {
        **style_cell,
        "fontWeight": "600",
        "backgroundColor": TERMINAL_COLORS["background"],
        "color": TERMINAL_COLORS["text"],
    }
    style_data_conditional = []
    for level, color in risk_colors.items():
        style_data_conditional.append({
            "if": {"filter_query": f"{{Klaster}} = '{level}'", "column_id": "Klaster"},
            "color": color,
            "fontWeight": "600",
        })
    return dash_table.DataTable(
        columns=[{"name": c, "id": c} for c in display_cols],
        data=cs_display.to_dict("records"),
        style_cell=style_cell,
        style_header=style_header,
        style_data_conditional=style_data_conditional,
        style_table={"overflowX": "auto"},
    )


def _default_detail_card():
    return html.Div(
        style={"textAlign": "center", "padding": "20px", "color": "#6c757d"},
        children=[html.Span("Klik salah satu wilayah di peta untuk melihat detail", style={"fontSize": "15px"})],
    )


def _build_detail_card(kabkota):
    row = df[df["Kab_Kota"] == kabkota]
    if row.empty:
        return _default_detail_card()
    r = row.iloc[0]

    risiko = r["Tingkat_Kerentanan"]
    color = _risk_color(risiko)
    peringkat = int(r["ranking_risiko"])
    total_putus = int(r["Total_Putus_Sekolah"])

    # Jenjang values
    jenjang = {
        "SD": int(r["Putus_SD"]),
        "SMP": int(r["Putus_SMP"]),
        "SMA": int(r["Putus_SMA"]),
        "SMK": int(r["Putus_SMK"]),
        "SLB": int(r["Putus_SLB"]),
    }

    # Cluster description from cluster_summary
    prioritas_key = RISK_TO_PRIORITY.get(risiko, "Prioritas Sedang")
    cs_row = cluster_summary[cluster_summary["prioritas_risiko"] == prioritas_key]
    if not cs_row.empty:
        cs = cs_row.iloc[0]
        jml_wilayah = int(cs["jumlah_wilayah"])
        rta_putus = cs["rata_rata_putus_total"]
        rta_kemiskinan = cs["rata_rata_kemiskinan_pct"]
        rta_ipm = None
        if "rata_rata_ipm" in cluster_summary.columns:
            rta_ipm = cs["rata_rata_ipm"]
        else:
            # Approximate from mean of wilayah's IPM
            rta_ipm = df[df["Tingkat_Kerentanan"] == risiko]["IPM_2024"].mean()
        cluster_wilayah = cs["wilayah"]
    else:
        jml_wilayah = 0
        rta_putus = 0
        rta_kemiskinan = 0
        rta_ipm = 0
        cluster_wilayah = ""

    insight_specific = (
        f"{kabkota} mencatat {total_putus} siswa putus sekolah "
        f"({r['Putus_Sekolah_per_10k_Penduduk']:.2f} per 10k penduduk) "
        f"dengan IPM {r['IPM_2024']:.2f} dan tingkat kemiskinan {r['Persentase_Miskin_Maret']:.2f}%."
    )
    insight_cluster = (
        f"Wilayah ini termasuk klaster {risiko} bersama {jml_wilayah - 1} kab/kota lain. "
        f"Klaster ini memiliki rata-rata IPM {rta_ipm:.2f}, "
        f"kemiskinan {rta_kemiskinan:.2f}%, "
        f"dan rata-rata total putus sekolah {rta_putus:.0f} siswa."
    )

    # Metrics for the grid
    metrics = [
        ("Total Putus", f"{total_putus}", "siswa"),
        ("Kemiskinan", f"{r['Persentase_Miskin_Maret']:.2f}", "%"),
        ("IPM", f"{r['IPM_2024']:.2f}", ""),
        ("Putus/10k", f"{r['Putus_Sekolah_per_10k_Penduduk']:.2f}", ""),
    ]

    card_style = {
        "borderRadius": "10px",
        "border": f"1px solid {TERMINAL_COLORS['border']}",
        "overflow": "hidden",
    }

    return html.Div(
        style=card_style,
        children=[
            # Header bar
            html.Div(
                style={
                    "backgroundColor": color,
                    "padding": "12px 20px",
                    "color": "white",
                    "display": "flex",
                    "justifyContent": "space-between",
                    "alignItems": "center",
                },
                children=[
                    html.Span(risiko, style={"fontWeight": "600", "fontSize": "14px", "letterSpacing": "0.5px"}),
                    html.Span(f"Peringkat #{peringkat}/27", style={"fontWeight": "600", "fontSize": "14px", "opacity": "0.9"}),
                ],
            ),
            # Body
            html.Div(
                style={"padding": "16px 20px"},
                children=[
                    # Title
                    html.H3(kabkota, style={"margin": "0 0 14px", "fontSize": "18px", "fontWeight": "600"}),
                    # Metrics grid
                    html.Div(
                        style={"display": "grid", "gridTemplateColumns": "repeat(4, 1fr)", "gap": "10px", "marginBottom": "14px"},
                        children=[
                            html.Div(
                                style={
                                    "backgroundColor": TERMINAL_COLORS["background"],
                                    "borderRadius": "8px",
                                    "padding": "10px",
                                    "textAlign": "center",
                                },
                                children=[
                                    html.Div(label, style={"fontSize": "11px", "color": "#6c757d", "marginBottom": "4px"}),
                                    html.Div(
                                        value,
                                        style={"fontSize": "20px", "fontWeight": "700", "color": TERMINAL_COLORS["text"]},
                                    ),
                                    html.Div(unit, style={"fontSize": "11px", "color": "#6c757d"}) if unit else "",
                                ],
                            )
                            for label, value, unit in metrics
                        ],
                    ),
                    # Jenjang breakdown bar
                    html.Div(
                        style={"display": "flex", "gap": "6px", "marginBottom": "14px", "alignItems": "center", "flexWrap": "wrap"},
                        children=[
                            html.Span("Jenjang:", style={"fontSize": "12px", "fontWeight": "600", "color": "#6c757d", "marginRight": "4px"}),
                            *[
                                html.Span(
                                    f"{jen}: {val}",
                                    style={
                                        "backgroundColor": TERMINAL_COLORS["background"],
                                        "borderRadius": "6px",
                                        "padding": "4px 10px",
                                        "fontSize": "12px",
                                        "fontWeight": "500",
                                        "color": TERMINAL_COLORS["text"],
                                    },
                                )
                                for jen, val in jenjang.items()
                            ],
                        ],
                    ),
                    # Insight text
                    html.Div(
                        style={
                            "backgroundColor": TERMINAL_COLORS["background"],
                            "borderRadius": "8px",
                            "padding": "12px 14px",
                            "fontSize": "13px",
                            "lineHeight": "1.6",
                            "color": TERMINAL_COLORS["text"],
                        },
                        children=[
                            html.P(insight_specific, style={"margin": "0 0 6px"}),
                            html.P(insight_cluster, style={"margin": "0"}),
                        ],
                    ),
                ],
            ),
        ],
    )


@app.callback(
    Output("kabkota-filter", "value"),
    Input("choropleth-map", "clickData"),
    prevent_initial_call=True,
)
def sync_click_to_filter(clickData):
    if clickData is None or "points" not in clickData:
        return dash.no_update
    kabkota = clickData["points"][0].get("location")
    return kabkota if kabkota in df["Kab_Kota"].values else dash.no_update


@app.callback(
    Output("region-detail-card", "children"),
    Input("choropleth-map", "clickData"),
    Input("kabkota-filter", "value"),
)
def show_region_detail(clickData, filter_value):
    ctx = dash.callback_context
    if not ctx.triggered:
        return _default_detail_card()
    trigger_id = ctx.triggered[0]["prop_id"]

    if trigger_id == "kabkota-filter.value":
        if filter_value == "ALL":
            return _default_detail_card()
        return _build_detail_card(filter_value)

    if trigger_id == "choropleth-map.clickData":
        if clickData is None or "points" not in clickData:
            return _default_detail_card()
        point = clickData["points"][0]
        kabkota = point.get("location")
        if not kabkota or kabkota not in df["Kab_Kota"].values:
            return _default_detail_card()
        return _build_detail_card(kabkota)

    return _default_detail_card()


@app.callback(
    Output("choropleth-map", "figure"),
    Input("kabkota-filter", "value"),
)
def update_choropleth(selected):
    return _build_choropleth(selected)


@app.callback(
    Output("scatter-plot", "figure"),
    Input("kabkota-filter", "value"),
)
def update_scatter(selected):
    return _build_scatter(selected)


@app.callback(
    Output("bar-chart", "figure"),
    Input("kabkota-filter", "value"),
)
def update_bar(selected):
    return _build_bar(selected)


@app.callback(
    Output("ranking-table-container", "children"),
    Input("kabkota-filter", "value"),
)
def update_ranking(_):
    return _build_ranking_table()


@app.callback(
    Output("cluster-summary-container", "children"),
    Input("kabkota-filter", "value"),
)
def update_cluster_summary(_):
    return _build_cluster_summary()


server = app.server
if __name__ == "__main__":
    app.run(debug=True, port=8050)
