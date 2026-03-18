# Ekantipur Web Scraper

This is a robust Python web scraper built as a submission for the **Web Scraping Intern** role at Audio Bee. It leverages the [Playwright](https://playwright.dev/python/) framework to extract dynamic content efficiently from [Ekantipur.com](https://ekantipur.com).

## Overview
The script automates a Chromium browser to navigate dynamic layouts, ensuring the DOM is fully loaded before scraping. 
It performs two distinct tasks:
1. **Entertainment News (`/entertainment`)**: Extracts the top 5 articles, retrieving the title, article image URL, author name, and assigning the category "मनोरञ्जन".
2. **Cartoon of the Day (Homepage)**: Locates the `cartoon-slider` section to extract the daily cartoon, capturing the title/alt text, the image URL, and the cartoonist's name.

The output is processed into a neat `output.json` file using UTF-8 encoding to preserve all Nepali characters perfectly.

## Requirements
- Python 3.8+
- [uv](https://docs.astral.sh/uv/) (Modern Python package manager)

## Installation
1. Clone this repository.
2. Initialize and sync the environment:
   ```bash
   uv sync
   ```
3. Install the Playwright Chromium binaries:
   ```bash
   uv run playwright install chromium
   ```

## Usage
Run the script using `uv`:
```bash
uv run python scraper.py
```

The script will launch a visible browser window (for demonstration purposes), navigate the pages, and automatically generate `output.json` in the root directory upon successful execution.

## File Structure
- `scraper.py` - Core scraping logic and Playwright navigation.
- `output.json` - The generated data output in the required JSON format.
- `prompts.txt` - Documented AI prompts used during the development of this project.
- `recording.mp4` - A screencast demonstrating the scraping process and tool usage.
- `pyproject.toml` - Environment dependencies managed by `uv`.
