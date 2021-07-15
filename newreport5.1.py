from fpdf import FPDF
from daily_counts import plot_daily_count_states,plot_daily_count_countries
from helper import get_state_names, get_country_names, Mode
from time_series_analysis import plot_states, plot_countries
from create_case_maps import plot_usa_case_map, plot_global_case_map
from datetime import timedelta,date
from practice import Day_I_want

WIDTH=210
Height=297

def create_title(Day_I_want,pdf):
    pdf.set_font('Arial', '', 15)  
    pdf.ln(65)
    pdf.write(0, f"Covid Analytics Report")
    pdf.ln(8)
    pdf.set_font('Arial', '', 12)
    pdf.write(0, f'{Day_I_want}')
    pdf.ln(5)

def create_report(Day_I_want, filename="CovidReport.pdf"):
    pdf = FPDF()
    pdf.add_page()

    pdf.image("./resources/WEEKLY COVID-19 REPORT.png",0,0, WIDTH)
    create_title(Day_I_want, pdf)

    plot_usa_case_map(filename="./tmp/usa_cases.png", day=Day_I_want)
    pdf.image("./tmp/usa_cases.png", 5, 90, WIDTH-20)

    states = ["California", "Texas"]

    plot_states(states, days=250, filename="./tmp/test3.png", end_date=Day_I_want)
    pdf.image("./tmp/test3.png", 5, 200,WIDTH/2-10)

    plot_states(states, days=250, mode=Mode.DEATHS, filename="./tmp/test4.png", end_date=Day_I_want)
    pdf.image("./tmp/test4.png", WIDTH/2, 200,WIDTH/2-10)





    pdf.add_page()


    plot_daily_count_states(states, filename="./tmp/test.png", day=Day_I_want)
    pdf.image("./tmp/test.png", 5, 20,WIDTH/2-10)

    plot_daily_count_states(states, mode=Mode.DEATHS, filename="./tmp/test2.png", day=Day_I_want)
    pdf.image("./tmp/test2.png", WIDTH/2, 20,WIDTH/2-10)

    plot_states(states, days=7, filename="./tmp/test3a.png", end_date=Day_I_want)
    pdf.image("./tmp/test3a.png", 5, 110,WIDTH/2-10)
    plot_states(states, days=7, mode=Mode.DEATHS, filename="./tmp/test4a.png", end_date=Day_I_want)
    pdf.image("./tmp/test4a.png", WIDTH/2, 110,WIDTH/2-10)

    plot_states(states, days=30, filename="./tmp/test3b.png", end_date=Day_I_want)
    pdf.image("./tmp/test3b.png", 5, 200,WIDTH/2-10)
    plot_states(states, days=30, mode=Mode.DEATHS, filename="./tmp/test4b.png", end_date=Day_I_want)
    pdf.image("./tmp/test4b.png", WIDTH/2, 200,WIDTH/2-10)


    pdf.add_page()

    plot_global_case_map("./tmp/global_cases.png", day=Day_I_want)
    countries = ['US', 'India', 'Canada']
    plot_countries(countries, days=7, filename="./tmp/cases4.png", end_date=Day_I_want)
    plot_countries(countries, days=7, mode=Mode.DEATHS, filename="./tmp/deaths4.png", end_date=Day_I_want)

    pdf.image("./tmp/global_cases.png", 5, 20, WIDTH-20)
    pdf.image("./tmp/cases4.png", 5, 130, WIDTH/2-10)
    pdf.image("./tmp/deaths4.png", WIDTH/2, 130, WIDTH/2-10)


    pdf.output(filename)

if __name__=='__main__':

    create_report(Day_I_want)