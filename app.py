from shiny import App, ui, reactive, render
from palmerpenguins import load_penguins
import seaborn as sns
import matplotlib.pyplot as plt

# 🔗 GitHub Repo: https://github.com/sabrouch36/cintel-03-reactive

penguins_df = load_penguins()

app_ui = ui.page_fluid(
    ui.layout_sidebar(
        ui.sidebar(
            ui.h2("Penguin Filters"),
            ui.input_checkbox_group(
                id="selected_species",
                label="Select species:",
                choices=["Adelie", "Chinstrap", "Gentoo"],
                selected=["Adelie", "Chinstrap", "Gentoo"]
            ),
            ui.input_slider(
                id="min_flipper_length",
                label="Minimum Flipper Length (mm):",
                min=170,
                max=235,
                value=180
            )
        ),
        ui.div(
            ui.h2("CC3.1 - Penguin Dashboard"),
            ui.output_text_verbatim("filtered_count"),
            ui.output_data_frame("filtered_table"),
            ui.output_plot("mass_histogram"),
            ui.output_plot("pie_chart")
        )
    )
)

def server(input, output, session):

    @reactive.calc
    def filtered_data():
        return penguins_df[
            (penguins_df["species"].isin(input.selected_species())) &
            (penguins_df["flipper_length_mm"] >= input.min_flipper_length())
        ]

    @output
    @render.text
    def filtered_count():
        return f"Filtered rows: {len(filtered_data())}"

    @output
    @render.data_frame
    def filtered_table():
        return filtered_data()

    @output
    @render.plot
    def mass_histogram():
        df = filtered_data()
        fig, ax = plt.subplots()
        sns.histplot(data=df, x="body_mass_g", hue="species", multiple="stack", ax=ax)
        ax.set_title("Body Mass Distribution")
        ax.set_xlabel("Body Mass (g)")
        ax.set_ylabel("Count")
        return fig

    @output
    @render.plot
    def pie_chart():
        df = filtered_data()
        fig, ax = plt.subplots()
        df["species"].value_counts().plot.pie(autopct='%1.1f%%', ax=ax)
        ax.set_title("Species Distribution")
        ax.set_ylabel("")
        return fig

app = App(app_ui, server)
