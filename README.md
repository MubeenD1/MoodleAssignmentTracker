# Assignment Tracker

This project is a web application that tracks and displays upcoming assignments from Moodle. The data is fetched using the Moodle API and displayed on a website built with the Flask web framework.

## Features

- ~**Fetch Assignments**: Automatically pulls assignment data from Moodle using your personal account user ID.~ (coming soon)
- **Display Assignments**: Shows upcoming assignments on a simple HTML page.
- **Future Updates**: Plans to enhance the website's appearance and functionality with additional features.

## Installation (For running locally)

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/assignment-tracker.git
    cd assignment-tracker
    ```

2. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    - Create a `.env` file in the root directory.
    - Add your Moodle API token:
      ```
      API_TOKEN=your_api_token
      ```

5. **Run the application**:
    ```bash
    python3 app.py
    ```

## Usage

- Open your browser and go to `localhost:5000/` to see the list of upcoming assignments.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
