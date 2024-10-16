
# GRAPHIQUEZ

### A terminal-based data visualization application.

---

## How to Run

```bash
pip install -r requirements.txt
python3 main/main.py
```

### Database Usage

This project uses a cloud database (MongoDB Atlas) to store log records. Your IP address and computer name will be saved. Additionally, your username and password (encrypted with SHA256) will be stored to manage your account.

---

## Application Features

After logging in, you will have four options:

1. **Settings**: Modify application settings.
2. **Graphiquez for Datasets**: Select datasets and create visualizations as you wish.
3. **Graphiquez for Mathematical Functions**: Choose 2D or 3D, input a function, and let it plot.
4. **Account**: View and manage your account information.

---

## Graphiquez for Datasets (PRO Mode)

You can select datasets for the x and y axes using one of the following methods:

1. Use files located in the default folder.
2. Provide the complete path to a file.
3. Provide a link containing an HTML table.

### Terminal Commands and Parameters

After selecting your dataset, you'll see a terminal interface with the following functions:

1. **draw**: Draws graphs.
   - Example: `draw=scatter color=blue xlabel=xaxis ylabel=yaxis title=mygraph`
2. **show**: Displays the graph.
   - Example: Just type `show`
3. **savefigure**: Saves the figure as a project file to continue working on it later.
4. **save**: Saves the figure as an image.
5. **changedata**: Updates the dataset or column you are working on.
   - Example: `changedata=x file=example.xlsx column=0`
6. **reset**: Resets the figure, clearing all settings and data.

---

### Usage and Parameters

Note: Not all parameters are required; defaults will be used for any omitted.

#### Draw Commands

```plaintext
draw=line color=<red,blue,green...> label=<name> xlabel=<name> ylabel=<name> title=<name> linestyle=<solid,dashed...> marker=<o,-...>
draw=scatter color=<red,...> label=<name> xlabel=<name> ylabel=<name> title=<name> marker=<o,-...>
draw=bar color=<color> xlabel=<name> ylabel=<name> title=<name> width=<value>
draw=pie title=<name>
```

#### Non-Parameter Commands

- **show**: Displays the graph.
- **savefigure**: Saves the figure as a project file.
- **reset**: Resets the figure and clears all settings.

#### Save Command

- Use the `name` parameter to save in the default folder.
- Use the `path` parameter to save to a specified location.
  - Example: `save=chart extension=.png name=example` or `save=chart path=/users/yourname/desktop/extension=.jpeg`

---

### Changing Data

- The `file` parameter searches in the default folder (changeable in settings).
- Example: `changedata=x file=example.csv column=0`
- Example with path: `changedata=x path=/path/to/file.csv column=0`
- Example with link: `changedata=x link=http://example.com/table column=0`

---

## Graphiquez for Amateurs

Similar to PRO mode, but parameters are given as ordinary inputs. Type `default` for any input you want to use default values.

---

## Graphiquez for Mathematical Functions

1. **2D**
2. **3D**

Input the function with only `x` and `y` variables. No trigonometric functions like `sin`, `cos`, etc. are allowed.

**Important Notes:**
- Write `2*x` instead of `2x`.
- Write `x**2` instead of `x^2`.

Define the limits for the x-axis when prompted.
