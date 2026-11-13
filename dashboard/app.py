import pandas as pd
import plotly.express as px
import streamlit as st
from sqlalchemy import create_engine
import os
from pathlib import Path
from dotenv import load_dotenv

# =====================================================
# 1. PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="Hotel Booking Analytics",
    page_icon="🏨",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =====================================================
# 2. DESIGN TOKENS
# =====================================================

# Tinggi tiap chart (px). Naikkan kalau layar besar, turunkan kalau layar kecil.
CHART_HEIGHT = 270

BG = "#0A0F1E"
TEXT = "#E6EDF7"
MUTED = "#8A9BB8"
GRID = "rgba(148, 163, 184, 0.10)"
CYAN = "#22D3EE"
PINK = "#F472B6"

# Gradasi bar: nilai kecil -> violet, nilai besar -> cyan
BAR_SCALE = [
    [0.0, "#7C3AED"],
    [0.5, "#3B82F6"],
    [1.0, "#22D3EE"],
]


# =====================================================
# 3. THEME (CSS)
# =====================================================

st.markdown("""
<style>
    :root {
        --border: rgba(148, 163, 184, 0.16);
        --text: #E6EDF7;
        --muted: #8A9BB8;
    }

    /* Buang elemen bawaan Streamlit yang memakan ruang vertikal.
       Hapus baris ini kalau menu titik tiga di kanan atas masih dibutuhkan. */
    [data-testid="stHeader"],
    [data-testid="stToolbar"],
    [data-testid="stDecoration"],
    #MainMenu,
    footer {
        display: none !important;
    }

    /* Blok <style> ini sendiri tidak boleh ikut menambah jarak */
    [data-testid="stElementContainer"]:has([data-testid="stMarkdownContainer"] > style),
    .element-container:has([data-testid="stMarkdownContainer"] > style) {
        display: none !important;
    }

    /* Background: dasar navy gelap + dua cahaya lembut (indigo & cyan) */
    .stApp {
        background:
            radial-gradient(900px 480px at 8% -8%, rgba(99, 102, 241, 0.22), transparent 60%),
            radial-gradient(800px 420px at 100% 0%, rgba(34, 211, 238, 0.14), transparent 55%),
            #0A0F1E;
        background-attachment: fixed;
        color: var(--text);
    }

    /* Margin & jarak antar elemen dirapatkan */
    [data-testid="stMainBlockContainer"],
    .main .block-container {
        max-width: 1680px;
        padding: 0.9rem 1.75rem 0.5rem !important;
    }

    [data-testid="stVerticalBlock"] {
        gap: 0.7rem !important;
    }

    [data-testid="stHorizontalBlock"] {
        gap: 0.75rem !important;
    }

    [data-testid="stMarkdownContainer"] p {
        margin: 0;
    }

    /* Header */
    .top-header {
        padding-top: 2px;
    }

    .top-title-row {
        display: flex;
        align-items: center;
        gap: 10px;
        flex-wrap: wrap;
    }

    .top-emoji {
        font-size: 1.5rem;
        line-height: 1;
    }

    .top-title {
        font-size: 1.55rem;
        font-weight: 750;
        letter-spacing: -0.03em;
        line-height: 1.15;
        background: linear-gradient(90deg, #F1F7FF 0%, #A5B4FC 60%, #67E8F9 100%);
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .top-sub {
        color: var(--muted);
        font-size: 0.85rem;
        margin-top: 5px;
    }

    .status-pill {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 3px 10px;
        border-radius: 999px;
        background: rgba(45, 212, 191, 0.10);
        border: 1px solid rgba(45, 212, 191, 0.35);
        color: #5EEAD4;
        font-size: 10.5px;
        font-weight: 600;
        letter-spacing: 0.06em;
    }

    .status-dot {
        width: 6px;
        height: 6px;
        border-radius: 50%;
        background: #2DD4BF;
        box-shadow: 0 0 8px #2DD4BF;
    }

    /* Filter */
    [data-testid="stWidgetLabel"] {
        min-height: 0;
        margin-bottom: 2px;
    }

    [data-testid="stWidgetLabel"] p {
        color: var(--muted) !important;
        font-size: 12px !important;
        font-weight: 500;
        margin: 0;
    }

    [data-baseweb="select"] > div {
        background: rgba(22, 33, 58, 0.9) !important;
        border: 1px solid rgba(148, 163, 184, 0.22) !important;
        border-radius: 10px !important;
        min-height: 38px;
        color: var(--text);
    }

    [data-baseweb="select"] > div:hover,
    [data-baseweb="select"] > div:focus-within {
        border-color: rgba(34, 211, 238, 0.6) !important;
    }

    span[data-baseweb="tag"] {
        background: linear-gradient(135deg, #4F46E5, #0891B2) !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 7px !important;
        font-weight: 600;
    }

    span[data-baseweb="tag"] svg {
        fill: #FFFFFF !important;
    }

    [data-baseweb="popover"] [data-baseweb="menu"],
    [data-baseweb="popover"] ul {
        background: #131C33 !important;
    }

    [data-baseweb="popover"] li[role="option"]:hover {
        background: rgba(99, 102, 241, 0.25) !important;
    }

    /* KPI cards */
    [data-testid="stMetric"] {
        position: relative;
        overflow: hidden;
        background: linear-gradient(150deg, rgba(34, 46, 80, 0.85) 0%, rgba(15, 23, 42, 0.92) 100%);
        border: 1px solid var(--border);
        border-radius: 14px;
        padding: 12px 16px 10px;
        min-height: 0;
        box-shadow:
            0 8px 24px -12px rgba(0, 0, 0, 0.6),
            inset 0 1px 0 rgba(255, 255, 255, 0.05);
    }

    [data-testid="stMetric"]::before {
        content: "";
        position: absolute;
        inset: 0 0 auto 0;
        height: 2px;
        background: linear-gradient(90deg, #22D3EE, #6366F1 55%, #A855F7);
    }

    [data-testid="stMetricLabel"],
    [data-testid="stMetricLabel"] p {
        color: var(--muted) !important;
        font-size: 12px !important;
    }

    [data-testid="stMetricValue"] {
        width: fit-content;
        font-size: 1.55rem;
        font-weight: 750;
        letter-spacing: -0.02em;
        line-height: 1.25;
        background: linear-gradient(90deg, #67E8F9, #A5B4FC);
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* Chart cards */
    [data-testid="stPlotlyChart"] {
        background: linear-gradient(160deg, rgba(24, 35, 64, 0.80) 0%, rgba(13, 20, 38, 0.92) 100%);
        border: 1px solid var(--border);
        border-radius: 14px;
        padding: 4px 6px 2px;
        box-shadow: 0 10px 30px -16px rgba(0, 0, 0, 0.7);
        overflow: hidden;
        transition: border-color 0.2s ease;
    }

    [data-testid="stPlotlyChart"]:hover {
        border-color: rgba(34, 211, 238, 0.30);
    }

    [data-testid="stCaptionContainer"] {
        text-align: center;
        opacity: 0.7;
    }

    [data-testid="stCaptionContainer"] p {
        color: var(--muted);
        font-size: 11px;
    }

    @media (max-width: 768px) {
        [data-testid="stMainBlockContainer"],
        .main .block-container {
            padding: 0.75rem 0.9rem !important;
        }

        .top-title {
            font-size: 1.25rem;
        }
    }
</style>
""", unsafe_allow_html=True)



# =====================================================
# 4. DATA SOURCE
# =====================================================

# Load environment variables dari file .env jika tersedia
project_dir = Path(__file__).resolve().parent.parent
env_path = project_dir / ".env"
load_dotenv(env_path)

DATABASE_URL = os.getenv("DATABASE_URL")
CSV_PATH = project_dir / "data" / "processed" / "hotel_bookings_clean.csv"


@st.cache_data
def load_data():
    # Mode lokal: gunakan PostgreSQL
    if DATABASE_URL:
        engine = create_engine(DATABASE_URL)

        try:
            df = pd.read_sql(
                "SELECT * FROM hotel_bookings",
                engine
            )
        finally:
            engine.dispose()

        return df

    # Mode publik: gunakan CSV dari repository
    if CSV_PATH.exists():
        return pd.read_csv(CSV_PATH)

    raise FileNotFoundError(
        f"Dataset tidak ditemukan: {CSV_PATH}"
    )


DATA_SOURCE = "DATABASE CONNECTED" if DATABASE_URL else "CSV DATA SOURCE"



# =====================================================
# 5. CHART HELPERS
# =====================================================

BASE_LAYOUT = dict(
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(
        family="Inter, Segoe UI, Arial, sans-serif",
        color="#C9D6EA",
        size=11
    ),
    margin=dict(l=12, r=12, t=42, b=12),
    title=dict(
        font=dict(size=14, color=TEXT),
        x=0.03,
        xanchor="left",
        y=0.965,
        yanchor="top"
    ),
    hoverlabel=dict(
        bgcolor="#1B2742",
        bordercolor="#334766",
        font=dict(color="#FFFFFF", size=12)
    ),
    showlegend=False,
    height=CHART_HEIGHT,
    bargap=0.35
)

PLOT_CONFIG = {"displayModeBar": False}


def style_fig(fig, **overrides):
    """Terapkan tema yang sama ke semua chart."""
    fig.update_layout(**{**BASE_LAYOUT, **overrides})

    fig.update_xaxes(
        showgrid=False,
        zeroline=False,
        showline=False,
        title_text=None,
        tickfont=dict(color=MUTED, size=11),
        automargin=True
    )

    fig.update_yaxes(
        showgrid=True,
        gridcolor=GRID,
        zeroline=False,
        showline=False,
        title_text=None,
        tickfont=dict(color=MUTED, size=11),
        automargin=True
    )

    return fig


def make_bar(data, category, value, title, horizontal=False, bargap=0.35):
    """Bar chart dengan gradasi warna berdasarkan nilai."""
    lo, hi = data[value].min(), data[value].max()

    fig = px.bar(
        data,
        x=value if horizontal else category,
        y=category if horizontal else value,
        orientation="h" if horizontal else "v",
        color=value,
        color_continuous_scale=BAR_SCALE,
        range_color=[lo, hi] if hi > lo else [0, hi],
        text=value,
        title=title
    )

    fig.update_traces(
        texttemplate="%{text:,}",
        textposition="outside",
        textfont=dict(color=TEXT, size=11),
        cliponaxis=False,
        marker_line_width=0,
        hovertemplate=(
            "%{y}<br>%{x:,} bookings<extra></extra>"
            if horizontal
            else "%{x}<br>%{y:,} bookings<extra></extra>"
        )
    )

    fig.update_coloraxes(showscale=False)

    style_fig(fig, bargap=bargap)

    # Sudut bar membulat (butuh Plotly versi baru; dilewati kalau belum ada)
    try:
        fig.update_traces(marker_cornerradius=6)
    except ValueError:
        pass

    # Sumbu nilai disembunyikan karena angka sudah tampil di atas bar
    if horizontal:
        fig.update_xaxes(visible=False, range=[0, hi * 1.18])
        fig.update_yaxes(showgrid=False)
    else:
        fig.update_yaxes(visible=False, range=[0, hi * 1.18])

    return fig


# =====================================================
# 6. LOAD DATA, HEADER & FILTERS
# =====================================================

try:
    original_df = load_data()

    if original_df.empty:
        st.warning("Database belum memiliki data booking.")
        st.stop()

    # Header dan filter dalam satu baris supaya hemat ruang vertikal
    head_col, filter1, filter2, filter3 = st.columns([1.7, 1.2, 1.2, 0.9])

    with head_col:
        st.markdown("""
<div class="top-header">
    <div class="top-title-row">
        <span class="top-emoji">🏨</span>
        <span class="top-title">Hotel Booking Analytics</span>
        <span class="status-pill"><span class="status-dot"></span>{DATA_SOURCE}</span>
    </div>
    <div class="top-sub">Hotel performance, customer behavior &amp; booking insights</div>
</div>
""", unsafe_allow_html=True)

    with filter1:
        selected_year = st.multiselect(
            "Arrival Year",
            options=sorted(
                original_df["arrival_date_year"].unique()
            ),
            default=sorted(
                original_df["arrival_date_year"].unique()
            )
        )

    with filter2:
        selected_hotel = st.multiselect(
            "Hotel Type",
            options=sorted(original_df["hotel"].unique()),
            default=sorted(original_df["hotel"].unique())
        )

    with filter3:
        selected_status = st.selectbox(
            "Booking Status",
            options=[
                "All Bookings",
                "Not Canceled",
                "Canceled"
            ]
        )

    # Filter tahun dan hotel
    base_df = original_df[
        (original_df["arrival_date_year"].isin(selected_year)) &
        (original_df["hotel"].isin(selected_hotel))
    ].copy()

    # Cancellation rate dihitung sebelum filter status
    cancellation_rate = (
        base_df["is_canceled"].mean() * 100
        if not base_df.empty else 0
    )

    # Filter status untuk analisis lainnya
    df = base_df.copy()

    if selected_status == "Not Canceled":
        df = df[df["is_canceled"] == 0].copy()

    elif selected_status == "Canceled":
        df = df[df["is_canceled"] == 1].copy()

    # =================================================
    # 7. EMPTY DATA CHECK
    # =================================================

    if df.empty:
        st.warning(
            "Tidak ada data untuk kombinasi filter yang dipilih."
        )
        st.stop()

    # =================================================
    # 8. KPI SECTION
    # =================================================

    total_bookings = len(df)

    estimated_revenue = df["estimated_revenue"].sum()

    average_adr = df["adr"].mean()

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    kpi1.metric(
        "Total Bookings",
        f"{total_bookings:,}"
    )

    kpi2.metric(
        "Cancellation Rate",
        f"{cancellation_rate:.2f}%",
        help="Dihitung dari seluruh status booking setelah filter tahun dan hotel."
    )

    kpi3.metric(
        "Estimated Revenue",
        f"${estimated_revenue:,.2f}"
    )

    kpi4.metric(
        "Average ADR",
        f"${average_adr:,.2f}"
    )

    # =================================================
    # 9. PREPARE DATA
    # =================================================

    df["month_number"] = pd.to_datetime(
        df["arrival_date_month"],
        format="%B"
    ).dt.month

    df["booking_month"] = pd.to_datetime(
        df["arrival_date_year"].astype(str)
        + "-"
        + df["month_number"].astype(str)
        + "-01"
    )

    monthly_bookings = (
        df.groupby("booking_month")
        .size()
        .reset_index(name="total_bookings")
        .sort_values("booking_month")
    )

    hotel_bookings = (
        df.groupby("hotel")
        .size()
        .reset_index(name="total_bookings")
    )

    status_order = ["Not Canceled", "Canceled"]

    cancellation_data = (
        df["is_canceled"]
        .map({0: "Not Canceled", 1: "Canceled"})
        .value_counts()
        .reindex(status_order, fill_value=0)
        .rename_axis("booking_status")
        .reset_index(name="total_bookings")
    )

    cancellation_data["label"] = (
        cancellation_data["booking_status"]
        + "  ·  "
        + (
            cancellation_data["total_bookings"]
            / cancellation_data["total_bookings"].sum()
            * 100
        ).round(1).astype(str)
        + "%"
    )

    customer_data = (
        df["customer_type"]
        .value_counts()
        .reset_index()
    )

    customer_data.columns = ["customer_type", "total_bookings"]

    country_data = (
        df["country"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    country_data.columns = ["country", "total_bookings"]

    country_data = country_data.sort_values("total_bookings")

    channel_data = (
        df["distribution_channel"]
        .value_counts()
        .reset_index()
    )

    channel_data.columns = ["distribution_channel", "total_bookings"]

    # =================================================
    # 10. CHARTS - BARIS 1
    # =================================================

    chart1, chart2, chart3 = st.columns([1.5, 1, 1.15])

    with chart1:
        fig_monthly = px.line(
            monthly_bookings,
            x="booking_month",
            y="total_bookings",
            markers=True,
            title="Monthly Booking Trends"
        )

        fig_monthly.update_traces(
            line=dict(color=CYAN, width=2.5, shape="spline", smoothing=0.7),
            marker=dict(
                size=5,
                color=CYAN,
                line=dict(color=BG, width=1.5)
            ),
            fill="tozeroy",
            fillcolor="rgba(34, 211, 238, 0.10)",
            hovertemplate="%{x|%b %Y}<br>%{y:,} bookings<extra></extra>"
        )

        style_fig(fig_monthly)
        fig_monthly.update_xaxes(tickformat="%b %y")

        st.plotly_chart(
            fig_monthly,
            use_container_width=True,
            theme=None,
            config=PLOT_CONFIG
        )

    with chart2:
        fig_hotel = make_bar(
            hotel_bookings,
            category="hotel",
            value="total_bookings",
            title="Bookings by Hotel Type",
            bargap=0.55
        )

        st.plotly_chart(
            fig_hotel,
            use_container_width=True,
            theme=None,
            config=PLOT_CONFIG
        )

    with chart3:
        fig_cancellation = px.pie(
            cancellation_data,
            names="label",
            values="total_bookings",
            hole=0.68,
            title="Booking Cancellation Distribution"
        )

        fig_cancellation.update_traces(
            marker=dict(
                colors=[CYAN, PINK],
                line=dict(color=BG, width=3)
            ),
            sort=False,
            textinfo="none",
            hovertemplate="%{label}<br>%{value:,} bookings<extra></extra>"
        )

        style_fig(
            fig_cancellation,
            showlegend=True,
            legend=dict(
                orientation="v",
                yanchor="middle",
                y=0.5,
                xanchor="left",
                x=1.02,
                bgcolor="rgba(0,0,0,0)",
                font=dict(color="#C9D6EA", size=11)
            )
        )

        fig_cancellation.add_annotation(
            text=(
                f"<b>{total_bookings:,}</b><br>"
                f"<span style='font-size:11px;color:{MUTED}'>bookings</span>"
            ),
            x=0.5,
            y=0.5,
            showarrow=False,
            font=dict(size=20, color=TEXT)
        )

        st.plotly_chart(
            fig_cancellation,
            use_container_width=True,
            theme=None,
            config=PLOT_CONFIG
        )

    # =================================================
    # 11. CHARTS - BARIS 2
    # =================================================

    chart4, chart5, chart6 = st.columns([1, 1.15, 1])

    with chart4:
        fig_customer = make_bar(
            customer_data,
            category="customer_type",
            value="total_bookings",
            title="Bookings by Customer Type"
        )

        st.plotly_chart(
            fig_customer,
            use_container_width=True,
            theme=None,
            config=PLOT_CONFIG
        )

    with chart5:
        fig_country = make_bar(
            country_data,
            category="country",
            value="total_bookings",
            title="Top 10 Customer Countries",
            horizontal=True,
            bargap=0.3
        )

        st.plotly_chart(
            fig_country,
            use_container_width=True,
            theme=None,
            config=PLOT_CONFIG
        )

    with chart6:
        fig_channel = make_bar(
            channel_data,
            category="distribution_channel",
            value="total_bookings",
            title="Bookings by Distribution Channel"
        )

        st.plotly_chart(
            fig_channel,
            use_container_width=True,
            theme=None,
            config=PLOT_CONFIG
        )
        

    # =================================================
    # 12. FOOTER
    # =================================================

    st.caption(
        "Hotel Booking Analytics | Data Engineering & Analytics Project"
    )

except Exception as e:
    st.error(f"Dashboard error: {e}")