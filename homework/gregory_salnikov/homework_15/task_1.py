import mysql.connector
from mysql.connector import Error


def create_connection():
    """Создание подключения к базе данных"""
    try:
        db = mysql.connector.connect(
            user='st-onl',
            passwd='AVNS_tegPDkI5BlB2lW5eASC',
            host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
            port=25060,
            database='st-onl'
        )
        print("Успешное подключение к базе данных")
        return db
    except Error as e:
        print(f"Ошибка подключения: {e}")
        return None


def execute_query(db, query, params=None, fetch=False):
    """Выполнение SQL запроса"""
    cursor = db.cursor()
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        if fetch:
            result = cursor.fetchall()
            return result, cursor.lastrowid
        else:
            db.commit()
            return None, cursor.lastrowid
    except Error as e:
        print(f"Ошибка выполнения запроса: {e}")
        db.rollback()
        return None, None
    finally:
        cursor.close()


def main():
    db = create_connection()
    if not db:
        return

    try:
        print("\n1. Добавление студента...")
        student_query = "INSERT INTO students (name, second_name) VALUES (%s, %s)"
        student_params = ('Gregory', 'Salnikov')
        _, student_id = execute_query(db, student_query, student_params)
        print(f"Добавлен студент с ID: {student_id}")

        print("\n2. Добавление книг для студента...")
        books = [
            ('First Book for Gregory', student_id),
            ('Second Book for Gregory', student_id)
        ]

        book_ids = []
        for book_title, taken_by in books:
            book_query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
            book_params = (book_title, taken_by)
            _, book_id = execute_query(db, book_query, book_params)
            book_ids.append(book_id)
            print(f"Добавлена книга '{book_title}' с ID: {book_id}")

        print("\n3. Добавление группы...")
        group_query = "INSERT INTO `groups` (title, start_date) VALUES (%s, %s)"
        group_params = ('Group of Gregory', 'Март')
        _, group_id = execute_query(db, group_query, group_params)
        print(f"Добавлена группа с ID: {group_id}")

        print("\n4. Привязка студента к группе...")
        update_student_query = "UPDATE students SET group_id = %s WHERE id = %s"
        update_student_params = (group_id, student_id)
        execute_query(db, update_student_query, update_student_params)
        print(f"Студент {student_id} привязан к группе {group_id}")

        print("\n5. Добавление предметов...")
        subjects = ['SQUAT', 'BENCH', 'DEADLIFT']
        subject_ids = {}

        for subject in subjects:
            subject_query = "INSERT INTO subjects (title) VALUES (%s)"
            subject_params = (subject,)
            _, subject_id = execute_query(db, subject_query, subject_params)
            subject_ids[subject] = subject_id
            print(f"Добавлен предмет '{subject}' с ID: {subject_id}")

        print("\n6. Добавление уроков...")
        lessons_data = [
            ('SQUAT Lesson 1', subject_ids['SQUAT']),
            ('SQUAT Lesson 2', subject_ids['SQUAT']),
            ('BENCH Lesson 1', subject_ids['BENCH']),
            ('BENCH Lesson 2', subject_ids['BENCH']),
            ('DEADLIFT Lesson 1', subject_ids['DEADLIFT']),
            ('DEADLIFT Lesson 2', subject_ids['DEADLIFT'])
        ]

        lesson_ids = []
        for lesson_title, subject_id in lessons_data:
            lesson_query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
            lesson_params = (lesson_title, subject_id)
            _, lesson_id = execute_query(db, lesson_query, lesson_params)
            lesson_ids.append(lesson_id)
            print(f"Добавлен урок '{lesson_title}' с ID: {lesson_id}")

        print("\n7. Добавление оценок...")
        for lesson_id in lesson_ids:
            mark_query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
            mark_params = ('five', lesson_id, student_id)
            execute_query(db, mark_query, mark_params)
            print(f"Добавлена оценка 'five' за урок {lesson_id}")

        print("\n" + "=" * 50)
        print("ВЫВОД ДАННЫХ СТУДЕНТА:")
        print("=" * 50)

        print("\n8.1 Все оценки студента:")
        marks_query = "SELECT * FROM marks WHERE student_id = %s"
        marks_params = (student_id,)
        marks, _ = execute_query(db, marks_query, marks_params, fetch=True)

        for mark in marks:
            print(f"Оценка: {mark}")

        print("\n8.2 Все книги студента:")
        books_query = "SELECT * FROM books WHERE taken_by_student_id = %s"
        books_params = (student_id,)
        books, _ = execute_query(db, books_query, books_params, fetch=True)

        for book in books:
            print(f"Книга: {book}")

        print("\n8.3 Полная информация о студенте:")
        full_info_query = """
        SELECT 
            st.id as student_id,
            st.name as student_name,
            st.second_name as student_second_name,
            g.title as group_title,
            b.title as book_title,
            m.value as mark_value,
            l.title as lesson_title,
            s.title as subject_title
        FROM `groups` g
        JOIN students st ON g.id = st.group_id
        JOIN books b ON st.id = b.taken_by_student_id
        JOIN marks m ON st.id = m.student_id
        JOIN lessons l ON m.lesson_id = l.id
        JOIN subjects s ON l.subject_id = s.id
        WHERE st.id = %s
        """
        full_info_params = (student_id,)
        full_info, _ = execute_query(db, full_info_query, full_info_params, fetch=True)

        print("\nПолная информация:")
        for row in full_info:
            print(f"Студент: {row[1]} {row[2]}, Группа: {row[3]}, "
                  f"Книга: {row[4]}, Оценка: {row[5]}, "
                  f"Урок: {row[6]}, Предмет: {row[7]}")

    except Error as e:
        print(f"Произошла ошибка: {e}")
    finally:
        if db.is_connected():
            db.close()
            print("\nПодключение к базе данных закрыто")


if __name__ == "__main__":
    main()
