"""Mini application Python (pédagogique) avec mauvaises pratiques.
Objectif : que SonarQube remonte des problèmes faciles à corriger.
"""

import hashlib

# ❌ Secret / mot de passe en dur (mauvaise pratique)
DEFAULT_PASSWORD = "admin123"


def weak_hash(password: str) -> str:
    """❌ SHA1 est considéré faible pour du mot de passe."""
    return hashlib.sha1(password.encode("utf-8")).hexdigest()


def authenticate(user: str, password: str) -> bool:
    """❌ Auth simpliste (pédagogique)."""
    if user == "admin" and weak_hash(password) == weak_hash(DEFAULT_PASSWORD):
        return True
    return False


def read_user_input():
    """❌ Input non validé (pédagogique)."""
    name = input("Votre nom: ")
    print("Bonjour " + name)
    return name


if __name__ == "__main__":
    read_user_input()
    print(authenticate("admin", "admin123"))
