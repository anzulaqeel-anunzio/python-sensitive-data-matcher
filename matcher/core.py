# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import re
import os

class SensitiveDataMatcher:
    # Patterns
    PATTERNS = {
        'Email': re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'),
        'Credit Card': re.compile(r'\b(?:\d[ -]*?){13,16}\b'), # Rough match
        'SSN': re.compile(r'\b\d{3}-\d{2}-\d{4}\b'),
        'AWS Access Key': re.compile(r'\bAKIA[0-9A-Z]{16}\b'),
        'Generic API Key': re.compile(r'(?i)(?:key|token|secret).{0,20}[:=].{0,1}["\']([a-zA-Z0-9_\-]{20,})["\']')
    }

    @staticmethod
    def is_likely_false_positive(match, line):
        # Ignore comments or example values
        if 'example' in line.lower() or 'placeholder' in line.lower():
            return True
        if line.strip().startswith('#') or line.strip().startswith('//'):
            return True
        return False

    @staticmethod
    def scan_file(filepath):
        issues = []
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                for line_num, line in enumerate(f, 1):
                    for name, pattern in SensitiveDataMatcher.PATTERNS.items():
                        matches = pattern.findall(line)
                        for match in matches:
                            if SensitiveDataMatcher.is_likely_false_positive(match, line):
                                continue
                                
                            # For CC, verify Luhn algorithm? Overkill for linter, but ok.
                            # Just report potential match
                            
                            issues.append({
                                'line': line_num,
                                'file': filepath,
                                'type': name,
                                'msg': f"Potential {name} detected"
                            })
        except Exception:
            pass
        return issues

    @staticmethod
    def scan_directory(directory):
        all_issues = []
        for root, dirs, files in os.walk(directory):
            if 'node_modules' in dirs: dirs.remove('node_modules')
            if '.git' in dirs: dirs.remove('.git')
            
            for file in files:
                # Skip binaries
                if file.endswith(('.py', '.js', '.txt', '.md', '.json', '.xml', '.yml', '.env')):
                    path = os.path.join(root, file)
                    issues = SensitiveDataMatcher.scan_file(path)
                    all_issues.extend(issues)
        return all_issues

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
