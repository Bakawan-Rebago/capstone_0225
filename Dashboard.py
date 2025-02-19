import streamlit as stl
import pandas as pd

stl.title("DASHBOARD")
stl.subheader("It is always fun to be here!")
stl.write("Join us and earn great salary!")
stl.divider()

chartList = ['LINE CHART', 'SCATTER CHART','BAR CHART']
def getChart(option):
    if option == "LINE CHART":
        stl.line_chart(data, x=xh, y=yh)
    elif option == "SCATTER CHART":
        stl.scatter_chart(data, x=xh, y=yh)
    elif option == "BAR CHART":
        stl.bar_chart(data, x=xh, y=yh)

try:
    data = pd.read_csv(stl.file_uploader("Upload a CSV or Excel file", type=["csv"]))

    columns = data.columns.tolist()
    xAxis, yAxis = stl.columns(2)
    with xAxis:
        xh = stl.selectbox("x",columns)
    with yAxis:
        yh = stl.selectbox("y", columns)

    chart_type = stl.selectbox("Choose a chart type:", chartList, index=0)
    stl.divider()
    # Display selected chart
    stl.subheader(chart_type)
    getChart(chart_type)

    stl.divider()

    rows_per_page = 10
    total_rows = len(data)
    total_pages = (total_rows // rows_per_page) + (1 if total_rows % rows_per_page else 0)

    page_number = stl.number_input("Page Number", min_value=1, max_value=total_pages, value=1, step=1)

    start_idx = (page_number - 1) * rows_per_page
    end_idx = min(start_idx + rows_per_page, total_rows)

    paginated_data = data.iloc[start_idx:end_idx]

    stl.dataframe(data)

    stl.write(f"📄 Page {page_number} of {total_pages} | Showing rows {start_idx + 1} to {end_idx} out of {total_rows}")

except:
    stl.write("Please upload excel or csv file.")
