# Low-Code/No-Code Platform Comparison Tool

A comprehensive Streamlit-based comparison tool for analyzing low-code/no-code platforms, providing dynamic performance metrics and interactive visualizations.

## Features

- Interactive platform comparison matrix
- Performance metrics visualization
- Cost calculator
- User reviews and ratings
- Feature comparison checklist
- Dynamic data visualization using Plotly
- PostgreSQL database integration

## Technical Stack

- Python 3.11
- Streamlit for web interface
- PostgreSQL for data storage
- Plotly for data visualization
- SQLAlchemy for database ORM

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
- DATABASE_URL
- PGHOST
- PGPORT
- PGUSER
- PGPASSWORD
- PGDATABASE

4. Initialize the database:
```bash
python init_db.py
```

5. Run the application:
```bash
streamlit run main.py
```

## Project Structure

- `main.py`: Main application entry point
- `components/`: UI components and widgets
- `utils/`: Utility functions and database operations
- `.streamlit/`: Streamlit configuration
- `init_db.py`: Database initialization script

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
