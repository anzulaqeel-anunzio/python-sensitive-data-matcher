# Sensitive Data Pattern Matcher

A regex-based scanner that sweeps your codebase for potentially exposed sensitive information such as emails, credit card numbers, Social Security Numbers (SSN), and AWS keys.

<!-- Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742 -->

## Features

*   **Multi-Check**: Scans for:
    *   Emails (PII)
    *   Credit Card Numbers
    *   SSNs
    *   AWS Access Keys
    *   Generic API Tokens
*   **False Positive Reduction**: Ignores lines identified as comments or containing "example" keywords.

## Usage

```bash
python run_matcher.py [path]
```

### Examples

**1. Scan Project**
```bash
python run_matcher.py src/
```

**2. Check Config**
```bash
python run_matcher.py config.yaml
```

## Requirements

*   Python 3.x

## Contributing

Developed for Anunzio International by Anzul Aqeel.
Contact: +971545822608 or +971585515742

## License

MIT License. See [LICENSE](LICENSE) for details.


---
### 🔗 Part of the "Ultimate Utility Toolkit"
This tool is part of the **[Anunzio International Utility Toolkit](https://github.com/anzulaqeel-anunzio/ultimate-utility-toolkit)**.
Check out the full collection of **180+ developer tools, scripts, and templates** in the master repository.

Developed for Anunzio International by Anzul Aqeel.
