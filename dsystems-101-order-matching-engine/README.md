# DSystems 101: Build a Distributed Order Matching Engine

## Description
Distributed pub-sub system for trading and notifications.

## Theme
Kafka + Redis + Distributed Systems

## Project Overview
This project implements a distributed order matching engine using a pub-sub architecture. It leverages Kafka for message brokering and Redis for data storage and caching. The system is designed to handle trading operations efficiently and provide real-time notifications.

## Getting Started

### Prerequisites
- Python 3.7 or higher
- Kafka
- Redis

### Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/dsystems-101-order-matching-engine.git
   ```
2. Navigate to the project directory:
   ```
   cd dsystems-101-order-matching-engine
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

### Running the Application
To start the order matching engine, run the following command:
```
python src/main.py
```

## Troubleshooting

### Common Issues

1. **Kafka Connection Issues**
   - Ensure that Kafka is running and accessible. Check your `settings.py` for the correct Kafka broker address.

2. **Redis Connection Issues**
   - Make sure Redis is up and running. Verify the connection details in `settings.py`.

3. **Dependency Errors**
   - If you encounter errors related to missing packages, ensure that all dependencies are installed correctly by running:
     ```
     pip install -r requirements.txt
     ```

4. **Order Matching Errors**
   - If the order matching does not work as expected, check the logs for any error messages. You can use the `log_message` utility function in `src/utils/__init__.py` to help with debugging.

### Contact
For further assistance, please open an issue on the GitHub repository or contact the project maintainers.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.