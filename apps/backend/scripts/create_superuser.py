import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import SessionLocal
from app.models import User
from app.core.security import get_password_hash

def create_superuser(email: str, password: str, full_name: str) -> None:
    db = SessionLocal()
    try:
        # Check if superuser already exists
        user = db.query(User).filter(User.email == email).first()
        if user:
            print(f"User with email {email} already exists")
            return

        # Create superuser
        superuser = User(
            email=email,
            full_name=full_name,
            hashed_password=get_password_hash(password),
            is_active=True,
            is_superuser=True
        )
        db.add(superuser)
        db.commit()
        print(f"Superuser {email} created successfully")
    except Exception as e:
        print(f"Error creating superuser: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python create_superuser.py <email> <password> <full_name>")
        sys.exit(1)

    email = sys.argv[1]
    password = sys.argv[2]
    full_name = sys.argv[3]
    create_superuser(email, password, full_name) 