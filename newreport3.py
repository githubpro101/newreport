from fpdf import FPDF
from daily_counts import plot_daily_count_states,plot_daily_count_countries
from helper import get_state_names, get_country_names, Mode
from time_series_analysis import plot_states, plot_countries
from create_case_maps import plot_usa_case_map, plot_global_case_map
from datetime import timedelta,date

WIDTH=210
Height=297

def create_title(day,pdf):
    pdf.set_font('Arial', '', 24)  
    pdf.ln(60)
    pdf.write(5, f"Covid Analytics Report")
    pdf.ln(10)
    pdf.set_font('Arial', '', 16)
    pdf.write(4, f'{day}')
    pdf.ln(5)

def create_report(day, filename="tutorial.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.image("./resources/letterhead_cropped.png",0,0, WIDTH)
    create_title(day, pdf)

    plot_usa_case_map(filename="usa_cases.png", day=day)
    pdf.image("usa_cases.png", 5, 90, WIDTH-20)

    pdf.add_page()

    states = ["New Hampshire", "Massachusetts"]
    plot_daily_count_states(states, filename="test.png")
    pdf.image("test.png", 5, 30,WIDTH/2-5)

    plot_daily_count_states(states, mode=Mode.DEATHS, filename="test2.png")
    pdf.image("test2.png", WIDTH/2+5, 30,WIDTH/2-5)

    pdf.add_page()

    plot_states(states, days=7, filename="test3.png")
    pdf.image("test3.png", 5, 110,WIDTH/2-5)

    plot_states(states, days=7, mode=Mode.DEATHS, filename="test4.png")
    pdf.image("test4.png", WIDTH/2+5, 110,WIDTH/2-5)

    pdf.output(filename)

if __name__=='__main__':
    ini_time_for_now = date.today()
    past_date_before_1day = ini_time_for_now - timedelta(days = 1)
    day=past_date_before_1day.strftime("%m/%d/%y").replace("/0","/").lstrip("0")

    create_report(day)