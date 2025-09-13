# password-generator
# 🔐 Advanced Password Generator

A secure, feature-rich password generator written in Python that creates strong passwords and memorable passphrases with comprehensive strength analysis.

## ✨ Features

- **Secure Password Generation**: Uses Python's `secrets` module for cryptographically secure randomness
- **Customizable Options**: Control length, character types, and complexity requirements
- **Password Strength Analysis**: Comprehensive analysis with scoring and improvement suggestions
- **Passphrase Generation**: Create memorable multi-word passphrases
- **Batch Generation**: Generate multiple passwords at once
- **Command-Line Interface**: Easy-to-use CLI with extensive options
- **Ambiguous Character Exclusion**: Option to exclude easily confused characters (il1Lo0O)
- **Minimum Requirements**: Enforce minimum counts for different character types

## 🚀 Quick Start

### Installation

```bash
git clone https://github.com/yourusername/password-generator.git
cd password-generator
python password_generator.py
```

### Basic Usage

```bash
# Generate a default 12-character password
python password_generator.py

# Generate a 16-character password
python password_generator.py -l 16

# Generate 5 passwords at once
python password_generator.py -c 5

# Generate a memorable passphrase
python password_generator.py -p

# Analyze password strength
python password_generator.py -a "YourPasswordHere"
```

## 📖 Detailed Usage

### Command-Line Arguments

| Argument | Description | Default |
|----------|-------------|---------|
| `-l, --length` | Password length | 12 |
| `-c, --count` | Number of passwords to generate | 1 |
| `--no-uppercase` | Exclude uppercase letters | False |
| `--no-lowercase` | Exclude lowercase letters | False |
| `--no-digits` | Exclude digits | False |
| `--no-symbols` | Exclude special characters | False |
| `--exclude-ambiguous` | Exclude ambiguous characters | False |
| `-p, --passphrase` | Generate passphrase instead | False |
| `-w, --words` | Number of words in passphrase | 4 |
| `-a, --analyze` | Analyze strength of provided password | None |

### Examples

#### Generate Custom Passwords
```bash
# 20-character password without symbols
python password_generator.py -l 20 --no-symbols

# Password without ambiguous characters
python password_generator.py --exclude-ambiguous

# Generate 10 simple passwords (letters and numbers only)
python password_generator.py -c 10 --no-symbols
```

#### Generate Passphrases
```bash
# Default 4-word passphrase
python password_generator.py -p

# 6-word passphrase
python password_generator.py -p -w 6

# Generate 3 passphrases
python password_generator.py -p -c 3
```

#### Password Analysis
```bash
# Analyze password strength
python password_generator.py -a "MyPassword123!"

# Example output:
# Password Analysis for: *************
# Length: 13
# Strength: Strong
# Score: 78/100
# 
# Character types present:
#   • Lowercase: ✓
#   • Uppercase: ✓
#   • Digits: ✓
#   • Symbols: ✓
```

## 🏗️ Code Structure

### `PasswordGenerator` Class

The main class providing all password generation functionality:

- `generate_password()`: Creates secure passwords with customizable criteria
- `generate_passphrase()`: Generates memorable word-based passwords
- `analyze_strength()`: Analyzes password strength and provides feedback
- `generate_multiple()`: Creates multiple passwords with the same criteria

### Security Features

- **Cryptographically Secure**: Uses `secrets.SystemRandom()` for true randomness
- **No Predictable Patterns**: Avoids sequential or repeated characters
- **Configurable Complexity**: Enforce minimum character type requirements
- **Strength Scoring**: Comprehensive analysis based on security best practices

## 🛡️ Security Considerations

This tool generates passwords using Python's `secrets` module, which is designed for cryptographic purposes and provides better security than the standard `random` module. The generated passwords are suitable for production use.

### Best Practices
- Use passwords of at least 12 characters
- Include multiple character types (uppercase, lowercase, digits, symbols)
- Avoid using the same password for multiple accounts
- Consider using a password manager to store generated passwords

## 🧪 Testing

### Manual Testing
```bash
# Test basic functionality
python password_generator.py -c 5 -l 8

# Test passphrase generation
python password_generator.py -p -c 3

# Test strength analysis
python password_generator.py -a "TestPassword123!"
```

### Integration with Password Managers
The generated passwords work seamlessly with popular password managers like:
- 1Password
- Bitwarden
- LastPass
- Dashlane

## 📊 Password Strength Scoring

The strength analysis uses a comprehensive scoring system:

- **Length**: 25 points for 12+ chars, 15 for 8-11 chars, 5 for less
- **Character Variety**: 15 points each for lowercase, uppercase, digits, symbols
- **Pattern Avoidance**: 10 points each for avoiding repetition and sequences
- **Total**: Maximum 100 points

### Strength Categories
- **90-100**: Very Strong 🔥
- **70-89**: Strong 💪
- **50-69**: Moderate ⚡
- **30-49**: Weak ⚠️
- **0-29**: Very Weak ❌

## 🔧 Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup
```bash
git clone https://github.com/yourusername/password-generator.git
cd password-generator
# Make your changes
# Test thoroughly
# Submit pull request
```

## 📈 Future Enhancements

- [ ] Web interface using Flask/FastAPI
- [ ] Password history and duplicate detection
- [ ] Export to various formats (CSV, JSON)
- [ ] Custom word lists for passphrases
- [ ] Integration with popular APIs
- [ ] GUI version using tkinter or PyQt

## 🆘 Troubleshooting

### Common Issues

**Issue**: "Password length must be at least 4 characters"
**Solution**: Increase the length parameter: `python password_generator.py -l 8`

**Issue**: "At least one character type must be selected"
**Solution**: Don't exclude all character types. Keep at least one enabled.

**Issue**: "Required minimum characters exceed password length"
**Solution**: Increase password length or reduce minimum requirements.

## 📞 Support

If you encounter any issues or have questions:
1. Check the troubleshooting section above
2. Search existing [GitHub Issues](https://github.com/yourusername/password-generator/issues)
3. Create a new issue with detailed information

## 🙏 Acknowledgments

- Python's `secrets` module for secure random generation
- The cybersecurity community for password security best practices
- Contributors and users who help improve this tool

---

⭐ **Star this repository if you find it useful!** ⭐
