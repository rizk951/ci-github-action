# CI/CD Pipeline with GitHub Actions

![GitHub Actions](https://github.com/rizk951/ci-github-action/actions/workflows/main.yml/badge.svg)
![Code Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)

## 🚀 Project Overview
This project demonstrates a professional CI/CD pipeline implementation using GitHub Actions. It showcases modern software development practices including:
- Automated testing
- Continuous Integration
- Code coverage reporting
- Professional project structure

## 🛠️ Technical Stack
- Python 3.x
- GitHub Actions
- pytest for testing
- pytest-cov for coverage reporting

## 📊 Project Structure
```
.
├── .github/workflows/    # GitHub Actions workflows
├── src/                 # Source code
├── tests/              # Test files
├── setup.py            # Project configuration
├── requirements.txt    # Dependencies
└── README.md          # Project documentation
```

## 🧪 Features
- **Automated Testing**: Comprehensive test suite with 100% code coverage
- **CI/CD Pipeline**: Automated build, test, and deployment process
- **Code Quality**: Professional project structure and best practices
- **Documentation**: Detailed setup and usage instructions

## 🚀 Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/rizk951/ci-github-action.git
   ```

2. Set up the environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -e .
   ```

3. Run tests:
   ```bash
   python -m pytest tests/ --cov=src
   ```

## 📈 CI/CD Pipeline
The GitHub Actions workflow:
1. Runs on every push to main branch
2. Sets up Python environment
3. Installs dependencies
4. Runs tests with coverage
5. Generates coverage report
6. Prepares for deployment

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author
- **Rizk** - [GitHub Profile](https://github.com/rizk951)

## 🔗 Links
- [GitHub Repository](https://github.com/rizk951/ci-github-action)
- [LinkedIn Profile](https://www.linkedin.com/in/your-profile)  <!-- Replace with your LinkedIn profile -->
