# Conway's Game of Life in Pygame

This project implements Conway's Game of Life, a cellular automaton simulation, using the Pygame library.

![Recording2025-03-31073227-ezgif com-optimize](https://github.com/user-attachments/assets/5196356a-ac69-419e-b13a-ea3bea73b0a6)

## Description

Conway's Game of Life is a zero-player game where cells on a grid evolve based on a set of rules. This project visually simulates these rules, allowing you to observe the dynamic patterns that emerge.

## Features

* **Visual Simulation:** Displays the evolving cells on a Pygame window.
* **Adjustable Grid Size:** The grid dimensions are determined by `SCREEN_WIDTH`, `SCREEN_HEIGHT`, and `CELL_SIZE` in `constants.py`.
* **Random Initialization:** The grid is initialized with random live and dead cells.
* **Game of Life Rules:** Implements the classic rules for cell survival, death, and birth.
* **Color Variety:** Live cells are displayed in randomly chosen colors from the `COLORS` list.
* **Exit on Escape:** The simulation can be exited by pressing the Escape key.

## Getting Started

### Prerequisites

* Python 3.x
* Pygame (`pip install pygame`)

### Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/joshGilstrap/Game_Of_Life
    ```

2.  Navigate to the project directory:

    ```bash
    cd <your_project_directory>
    ```

3.  Run the game:

    ```bash
    python main.py
    ```

## Usage

* The simulation will start automatically.
* Observe the evolving patterns of live and dead cells.
* Press the Escape key to exit the simulation.
* Close the Pygame window to exit the simulation.

## Code Explanation

* `constants.py`:
    * Defines constants for screen dimensions (`SCREEN_WIDTH`, `SCREEN_HEIGHT`), cell size (`CELL_SIZE`), grid dimensions (`GRID_WIDTH`, `GRID_HEIGHT`), and colors (`BLACK`, `WHITE`, `RED`, `GREEN`, `BLUE`, `CYAN`, `MAGENTA`, `YELLOW`, `COLORS`).
* `main.py`:
    * `create_grid()`: Initializes the grid with random live (1) or dead (0) cells.
    * `draw_grid()`: Draws the cells onto the Pygame screen, using random colors for live cells and a black outline.
    * `update_grid()`: Implements the core game logic, applying the rules of Conway's Game of Life to create the next generation.
    * `count_neighbors()`: Counts the live neighbors of a cell.
    * The main loop handles events (QUIT, K\_ESCAPE), updates the screen, and controls the simulation speed.

## Constants

* `SCREEN_WIDTH`, `SCREEN_HEIGHT`: Dimensions of the Pygame window (defined in `constants.py`).
* `CELL_SIZE`: Size of each cell in pixels (defined in `constants.py`).
* `GRID_WIDTH`, `GRID_HEIGHT`: Number of cells in the grid (calculated in `constants.py`).
* `COLORS`: List of colors used for live cells (defined in `constants.py`).

## Contributing

Contributions are welcome! If you have any ideas for improvements or new features, feel free to submit a pull request.

## License

This project is licensed under the MIT License.
