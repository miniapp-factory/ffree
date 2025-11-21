#!/usr/bin/env python3
"""
Word and character counter.
"""

def main():
    text = input("Enter text: ")
    words = len(text.split())
    chars = len(text)
    print(f"Words: {words}")
    print(f"Characters: {chars}")

if __name__ == "__main__":
    main()
