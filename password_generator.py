import secrets
import string
import argparse
import sys
from typing import List, Dict
import re

class PasswordGenerator:
    """
    A comprehensive password generator with customizable options and security features.
    """
    
    def __init__(self):
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        self.ambiguous = "il1Lo0O"
    
    def generate_password(self, 
                         length: int = 12,
                         include_uppercase: bool = True,
                         include_lowercase: bool = True,
                         include_digits: bool = True,
                         include_symbols: bool = True,
                         exclude_ambiguous: bool = False,
                         min_uppercase: int = 1,
                         min_lowercase: int = 1,
                         min_digits: int = 1,
                         min_symbols: int = 1) -> str:
        """
        Generate a secure password with specified criteria.
        
        Args:
            length: Length of the password
            include_uppercase: Include uppercase letters
            include_lowercase: Include lowercase letters
            include_digits: Include numbers
            include_symbols: Include special characters
            exclude_ambiguous: Exclude ambiguous characters (il1Lo0O)
            min_uppercase: Minimum uppercase letters required
            min_lowercase: Minimum lowercase letters required
            min_digits: Minimum digits required
            min_symbols: Minimum symbols required
        
        Returns:
            Generated password string
        """
        if length < 4:
            raise ValueError("Password length must be at least 4 characters")
        
        # Build character pool
        char_pool = ""
        required_chars = []
        
        if include_lowercase:
            chars = self.lowercase
            if exclude_ambiguous:
                chars = ''.join(c for c in chars if c not in self.ambiguous)
            char_pool += chars
            required_chars.extend([secrets.choice(chars) for _ in range(min_lowercase)])
        
        if include_uppercase:
            chars = self.uppercase
            if exclude_ambiguous:
                chars = ''.join(c for c in chars if c not in self.ambiguous)
            char_pool += chars
            required_chars.extend([secrets.choice(chars) for _ in range(min_uppercase)])
        
        if include_digits:
            chars = self.digits
            if exclude_ambiguous:
                chars = ''.join(c for c in chars if c not in self.ambiguous)
            char_pool += chars
            required_chars.extend([secrets.choice(chars) for _ in range(min_digits)])
        
        if include_symbols:
            char_pool += self.symbols
            required_chars.extend([secrets.choice(self.symbols) for _ in range(min_symbols)])
        
        if not char_pool:
            raise ValueError("At least one character type must be selected")
        
        if len(required_chars) > length:
            raise ValueError("Required minimum characters exceed password length")
        
        # Generate remaining characters
        remaining_length = length - len(required_chars)
        password_chars = required_chars + [secrets.choice(char_pool) for _ in range(remaining_length)]
        
        # Shuffle the password characters
        secrets.SystemRandom().shuffle(password_chars)
        
        return ''.join(password_chars)
    
    def generate_passphrase(self, num_words: int = 4, separator: str = "-", capitalize: bool = True) -> str:
        """
        Generate a memorable passphrase using common words.
        
        Args:
            num_words: Number of words in the passphrase
            separator: Character to separate words
            capitalize: Capitalize first letter of each word
        
        Returns:
            Generated passphrase
        """
        # Common word list (you can expand this or load from a file)
        word_list = [
            "apple", "brave", "cloud", "dance", "eagle", "flame", "grace", "happy",
            "imagine", "jungle", "knight", "light", "magic", "nature", "ocean", "peace",
            "quiet", "river", "storm", "tiger", "unity", "village", "wisdom", "xenial",
            "yellow", "zebra", "anchor", "bridge", "castle", "dragon", "earth", "forest",
            "galaxy", "harbor", "island", "journey", "kingdom", "legend", "mountain", "noble"
        ]
        
        words = [secrets.choice(word_list) for _ in range(num_words)]
        
        if capitalize:
            words = [word.capitalize() for word in words]
        
        # Add a random number at the end for extra security
        passphrase = separator.join(words) + separator + str(secrets.randbelow(1000))
        
        return passphrase
    
    def analyze_strength(self, password: str) -> Dict[str, any]:
        """
        Analyze password strength and provide feedback.
        
        Args:
            password: Password to analyze
        
        Returns:
            Dictionary with strength analysis
        """
        score = 0
        feedback = []
        
        # Length check
        length = len(password)
        if length >= 12:
            score += 25
        elif length >= 8:
            score += 15
            feedback.append("Consider using at least 12 characters")
        else:
            score += 5
            feedback.append("Password is too short - use at least 8 characters")
        
        # Character variety checks
        has_lower = bool(re.search(r'[a-z]', password))
        has_upper = bool(re.search(r'[A-Z]', password))
        has_digit = bool(re.search(r'\d', password))
        has_symbol = bool(re.search(r'[!@#$%^&*()_+\-=\[\]{}|;:,.<>?]', password))
        
        char_variety = sum([has_lower, has_upper, has_digit, has_symbol])
        score += char_variety * 15
        
        if not has_lower:
            feedback.append("Add lowercase letters")
        if not has_upper:
            feedback.append("Add uppercase letters")
        if not has_digit:
            feedback.append("Add numbers")
        if not has_symbol:
            feedback.append("Add special characters")
        
        # Pattern checks
        if not re.search(r'(.)\1{2,}', password):  # No 3+ repeated characters
            score += 10
        else:
            feedback.append("Avoid repeating characters")
        
        if not re.search(r'(012|123|234|345|456|567|678|789|890)', password):
            score += 10
        else:
            feedback.append("Avoid sequential numbers")
        
        # Determine strength level
        if score >= 85:
            strength = "Very Strong"
        elif score >= 70:
            strength = "Strong"
        elif score >= 50:
            strength = "Moderate"
        elif score >= 30:
            strength = "Weak"
        else:
            strength = "Very Weak"
        
        return {
            "score": score,
            "strength": strength,
            "feedback": feedback,
            "length": length,
            "has_lowercase": has_lower,
            "has_uppercase": has_upper,
            "has_digits": has_digit,
            "has_symbols": has_symbol
        }
    
    def generate_multiple(self, count: int = 5, **kwargs) -> List[str]:
        """
        Generate multiple passwords with the same criteria.
        
        Args:
            count: Number of passwords to generate
            **kwargs: Arguments to pass to generate_password()
        
        Returns:
            List of generated passwords
        """
        return [self.generate_password(**kwargs) for _ in range(count)]

def main():
    """Main function to handle command-line interface."""
    parser = argparse.ArgumentParser(description="Advanced Password Generator")
    parser.add_argument("-l", "--length", type=int, default=12, help="Password length (default: 12)")
    parser.add_argument("-c", "--count", type=int, default=1, help="Number of passwords to generate")
    parser.add_argument("--no-uppercase", action="store_true", help="Exclude uppercase letters")
    parser.add_argument("--no-lowercase", action="store_true", help="Exclude lowercase letters")
    parser.add_argument("--no-digits", action="store_true", help="Exclude digits")
    parser.add_argument("--no-symbols", action="store_true", help="Exclude symbols")
    parser.add_argument("--exclude-ambiguous", action="store_true", help="Exclude ambiguous characters")
    parser.add_argument("-p", "--passphrase", action="store_true", help="Generate passphrase instead")
    parser.add_argument("-w", "--words", type=int, default=4, help="Number of words in passphrase")
    parser.add_argument("-a", "--analyze", type=str, help="Analyze strength of provided password")
    
    args = parser.parse_args()
    
    generator = PasswordGenerator()
    
    try:
        if args.analyze:
            # Analyze provided password
            analysis = generator.analyze_strength(args.analyze)
            print(f"\nPassword Analysis for: {'*' * len(args.analyze)}")
            print(f"Length: {analysis['length']}")
            print(f"Strength: {analysis['strength']}")
            print(f"Score: {analysis['score']}/100")
            
            if analysis['feedback']:
                print("\nSuggestions for improvement:")
                for suggestion in analysis['feedback']:
                    print(f"  • {suggestion}")
            
            print(f"\nCharacter types present:")
            print(f"  • Lowercase: {'✓' if analysis['has_lowercase'] else '✗'}")
            print(f"  • Uppercase: {'✓' if analysis['has_uppercase'] else '✗'}")
            print(f"  • Digits: {'✓' if analysis['has_digits'] else '✗'}")
            print(f"  • Symbols: {'✓' if analysis['has_symbols'] else '✗'}")
            
        elif args.passphrase:
            # Generate passphrase
            for i in range(args.count):
                passphrase = generator.generate_passphrase(num_words=args.words)
                print(f"Passphrase {i+1}: {passphrase}")
        
        else:
            # Generate regular passwords
            passwords = generator.generate_multiple(
                count=args.count,
                length=args.length,
                include_uppercase=not args.no_uppercase,
                include_lowercase=not args.no_lowercase,
                include_digits=not args.no_digits,
                include_symbols=not args.no_symbols,
                exclude_ambiguous=args.exclude_ambiguous
            )
            
            for i, password in enumerate(passwords, 1):
                print(f"Password {i}: {password}")
                
                # Show strength analysis for single password
                if args.count == 1:
                    analysis = generator.analyze_strength(password)
                    print(f"Strength: {analysis['strength']} ({analysis['score']}/100)")
    
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()