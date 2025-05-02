from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, nullable=True)
    is_active = Column(Integer, default=1)  # 1 for active, 0 for inactive
    
    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "full_name": self.full_name,
            "is_active": self.is_active,
        }
    
    @staticmethod
    def get_event_list():
        return [
            {"id": 1, "name": "Tech Conference", "date": "2023-10-01", "location": "Auditorium"},
            {"id": 2, "name": "Career Fair", "date": "2023-11-15", "location": "Gymnasium"},
            {"id": 3, "name": "Hackathon", "date": "2023-12-05", "location": "Library"},
        ]


    @staticmethod
    def get_dummy_data():
        return [
            {
                "id": 1,
                "username": "john_doe",
                "email": "john.doe@example.com",
                "full_name": "John Doe",
                "is_active": 1,
            },
            {
                "id": 2,
                "username": "jane_smith",
                "email": "jane.smith@example.com",
                "full_name": "Jane Smith",
                "is_active": 1,
            },
        ]