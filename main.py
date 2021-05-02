import streamlit as st
import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from sklearn.datasets import load_iris
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from pathlib import Path
from scipy.stats import expon
import plotly.figure_factory as ff

def main():
    # 타이틀
    st.title('김나맥의 데이터사이언스 블로그')

    # 메뉴
    menu = ["시각화"]
    choice = st.sidebar.selectbox("메뉴", menu)

    # 서브메뉴
    st.subheader(choice)
    st.write(Path('markdown/title.md').read_text(encoding='utf-8'), unsafe_allow_html=True)

    # 입력버튼
    col1, col2, col3 = st.beta_columns(3)
    start = col1.number_input('시작값', value=0)
    end = col2.number_input('종료값', value=10)
    n = col3.number_input('개수', value=100)
  
    # 시각화 (Line plot)
    x = np.linspace(start, end, n)
    y = np.sin(x)
    y2 = np.cos(x)

    low_c = '#dd4124'
    high_c = '#009473'
    background_color = '#fcfcfc'
    hovertemplate = """
    f(%{x:,.2f})=%{y:,.2f}
    """

    fig = make_subplots(rows=1, cols=1, shared_xaxes=False)
    fig.add_trace(go.Scatter(
        x=x, y=y,
        marker=dict(size=1e-5, symbol='square', color=low_c, line=dict(width=0, color='#323232')),
        line=dict(width=4, dash='longdash'),
        name='sin(x)', mode='lines+markers'
    ))
    fig.add_trace(go.Scatter(
        x=x, y=y2,
        marker=dict(size=10, symbol='cross', color=high_c, line=dict(width=1, color='#323232')),
        name='cos(x)', mode='markers',
    ))
    fig.update_traces(
        hovertemplate=hovertemplate,
    )
    fig.update_layout(
        title=dict(text='<b>삼각함수</b>', font_size=20, font_color='#323232', xanchor='center', yanchor='top', x=0.475, y=0.97),
        margin=dict(l=40, r=40, b=40, t=60),
        width=800,
        height=400,
        font_family='Malgun Gothic',
        font_color='black',
        plot_bgcolor=background_color,
        paper_bgcolor=background_color,
        legend_title='<b>함수</b>',
        legend_title_font_size=17,
        legend_font_size=15,
        # hovermode='x unified',
        showlegend=True,
        hoverlabel_align='left',
    )
    fig.update_xaxes(
        title=dict(text='<b>x</b>', font_color='#323232', font_size=18, standoff=0),
        tickfont=dict(size=15, family='Malgun Gothic', color='#323232'),
        tickformat='.0f',
        tickangle=0,
        dtick=1,
        showline=True, linecolor='#323232', linewidth=2,
        zeroline=False, #zerolinewidth=2, zerolinecolor='black',
        showgrid=False, #gridcolor='black', gridwidth=1,
    )
    fig.update_yaxes(
        title=dict(text=r'<b>f(x)</b>', font_color='#323232', font_size=18, standoff=0),
        tickfont=dict(size=15, family='Malgun Gothic', color='#323232'),
        tickformat='.1f',
        dtick=0.5,
        showline=False, #linecolor='#323232', linewidth=2,
        zeroline=False, #zerolinewidth=2, zerolinecolor='black',
        showgrid=False, #gridcolor='black', gridwidth=1,
    )
    st.plotly_chart(fig)

    # 시각화 (Histogram)
    col1, col2 = st.beta_columns(2)
    param1 = col1.number_input('모수(X1)', value=10)
    param2 = col2.number_input('모수(X2)', value=20)

    np.random.seed(0)
    X1 = expon(0, param1)
    X2 = expon(0, param2)
    sample1 = X1.rvs(10000)
    sample2 = X2.rvs(10000)
    x = np.linspace(0, 130, 200)
    y1 = X1.pdf(x)
    y2 = X2.pdf(x)

    low_c = '#dd4124'
    high_c = '#009473'
    background_color = '#fcfcfc'
    hovertemplate = """
    %{x:,.2f}
    """

    fig = make_subplots(rows=1, cols=1, shared_xaxes=False)
    fig.add_trace(go.Histogram(
        x=sample1,
        name='X1',
        histnorm='probability',
        marker_color=low_c,
        marker_line_color='#323232',
        marker_line_width=1,
        xbins=dict(start=0, end=120, size=1),
    ))
    fig.add_trace(go.Scatter(
        x=x, y=y1,
        marker=dict(size=10, color='#323232'),
        name='X1_pdf', mode='lines',
        showlegend=False,
    ))
    fig.add_trace(go.Histogram(
        x=sample2,
        name='X2',
        histnorm='probability',
        marker_color=high_c,
        marker_line_color='#323232',
        marker_line_width=1,
        xbins=dict(start=0, end=120, size=1),
    ))
    fig.add_trace(go.Scatter(
        x=x, y=y2,
        marker=dict(size=10, color='#323232'),
        name='X2_pdf', mode='lines',
        showlegend=False,
    ))
    fig.update_traces(
        hovertemplate=hovertemplate,
        opacity=0.75,
    )
    fig.update_layout(
        barmode='overlay',
        title=dict(text='<b>지수분포</b>', font_size=20, font_color='#323232', xanchor='center', yanchor='top', x=0.475, y=0.97),
        margin=dict(l=40, r=40, b=40, t=60),
        width=800,
        height=400,
        font_family='Malgun Gothic',
        font_color='black',
        plot_bgcolor=background_color,
        paper_bgcolor=background_color,
        legend_title='<b>확률변수</b>',
        legend_title_font_size=17,
        legend_font_size=15,
        # showlegend=False,
        legend=dict(yanchor='top', xanchor='left', y=1.1, x=0.85, bordercolor='#323232', borderwidth=0),
        hoverlabel_align='left',
        annotations=[
            dict(x=60, y=0.05, ax=120, ay=-30,
                showarrow=True, arrowcolor='#323232', arrowhead=4, arrowsize=1, arrowwidth=2,
                font_color=high_c, font_size=15, font_family='Malgun Gothic', text='<b>주석</b>',
                borderwidth=1, bordercolor='#ffffff', borderpad=10,
            ),
        ],
        # shapes=[
        #     dict(type='path', path='M 60,0.05 Q 40,0.04 20,0.05', line_color='#323232'),
        # ],
    )
    fig.update_xaxes(
        title=dict(text='<b>x</b>', font_color='#323232', font_size=18, standoff=5),
        tickfont=dict(size=15, family='Malgun Gothic', color='#323232'),
        tickformat='.0f',
        tickangle=0,
        # dtick=1,
        showline=False, #linecolor='#323232', linewidth=2,
        zeroline=False, #zerolinewidth=2, zerolinecolor='black',
        showgrid=False, #gridcolor='black', gridwidth=1,
    )
    fig.update_yaxes(
        title=dict(text=r'<b>p(x)</b>', font_color='#323232', font_size=18, standoff=10),
        tickfont=dict(size=15, family='Malgun Gothic', color='#323232'),
        tickformat='.2f',
        # dtick=0.5,
        showline=False, #linecolor='#323232', linewidth=2,
        zeroline=False, #zerolinewidth=2, zerolinecolor='black',
        showgrid=False, #gridcolor='black', gridwidth=1,
    )
    # fig = ff.create_distplot(
    #     [sample1],
    #     group_labels=['plot'],
    #     curve_type='kde',
    #     show_rug=False,
    # )
    st.plotly_chart(fig)


if __name__ == '__main__':
    main()