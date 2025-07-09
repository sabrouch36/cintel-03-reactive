# 🐧 Cintel-03 Reactive Penguin Dashboard

This interactive web application was built using **Shiny for Python (PyShiny)**. It allows users to explore the **Palmer Penguins dataset** with reactive filters and dynamic visualizations.

## 🔍 Features

- **Reactive Filtering** based on:
  - Species (Adelie, Chinstrap, Gentoo)
  - Island (Torgersen, Biscoe, Dream)
  - Minimum flipper length (slider)
- **Data Table**: View filtered penguin data
- **Visualizations**:
  - Stacked Histogram of body mass
  - Pie chart showing species distribution
  - Histogram of flipper length with KDE
  - New: Scatter plot comparing bill length vs flipper length
- **Modern layout** using `ui.card`, `ui.layout_columns`, and visual polish

## 🚀 How to Run

1. Visit the Shiny Playground: [https://shinylive.io/py/](https://shinylive.io/py/)
2. Paste the contents of `app.py` and `requirements.txt`
3. Run the app and interact with the sidebar filters

## 📂 Repository Contents

- `app.py` – Main application logic
- `requirements.txt` – Extra packages used (only `plotly`)
- `screenshot1.png` – App before filter change
- `screenshot2.png` – App after applying filters
- `README.md` – Project description

## 🔗 Links

- [GitHub Repo](https://github.com/sabrouch36/cintel-03-reactive)

## 🏆 Bonus (Exploration)

- Added extra filtering by island
- Added scatterplot visualization
- Enhanced UI with icons and layout

## 📚 Dataset

Palmer Penguins dataset via `palmerpenguins` package  
Source: [https://allisonhorst.github.io/palmerpenguins/](https://allisonhorst.github.io/palmerpenguins/)
