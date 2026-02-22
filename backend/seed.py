from app.database import SessionLocal, engine, Base
from app.models.category import Category

def seed_data():
    # Создаем сессию
    db = SessionLocal()
    try:
        # Проверяем, есть ли уже категории, чтобы не дублировать
        if db.query(Category).count() == 0:
            print("Добавление категорий...")
            categories = [
                Category(name="Электроника", slug="electronics"),
                Category(name="Одежда", slug="clothing"),
                Category(name="Дом и сад", slug="home-garden")
            ]
            db.add_all(categories)
            db.commit()
            print("Категории успешно добавлены!")
        else:
            print("Категории уже есть в базе.")
    except Exception as e:        print(f"Ошибка: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_data()