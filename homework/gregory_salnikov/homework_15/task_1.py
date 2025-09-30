import mysql.connector
from mysql.connector import Error


def create_connection():
    """Создание подключения к базе данных"""
    try:
        connection = mysql.connector.connect(
            user='st-onl',
            passwd='AVNS_tegPDkI5BlB2lW5eASC',
            host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
            port=25060,
            database='st-onl'
        )
        if connection.is_connected():
            print("Успешное подключение к базе данных")
            return connection
    except Error as e:
        print(f"Ошибка подключения: {e}")
        return None


def execute_query(connection, query, params=None, fetch=False):
    """Выполнение SQL запроса"""
    try:
        cursor = connection.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        if fetch:
            result = cursor.fetchall()
            cursor.close()
            return result
        else:
            connection.commit()
            last_id = cursor.lastrowid
            cursor.close()
            return last_id
    except Error as e:
        print(f"Ошибка выполнения запроса: {e}")
        return None


def main():
    # Подключаемся к базе данных
    connection = create_connection()
    if not connection:
        return

    try:
        # 1. Добавляем студента
        print("\n1. Добавляем студента...")
        student_query = "INSERT INTO students (name, second_name) VALUES (%s, %s)"
        student_id = execute_query(connection, student_query, ('Gregory', 'Salnikov'))
        print(f"Добавлен студент с ID: {student_id}")

        # 2. Добавляем книги для студента
        print("\n2. Добавляем книги...")
        book1_query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
        book1_id = execute_query(connection, book1_query, ('First Book for Gregory', student_id))
        book2_id = execute_query(connection, book1_query, ('Second Book for Gregory', student_id))
        print(f"Добавлены книги с ID: {book1_id}, {book2_id}")

        # 3. Добавляем группу
        print("\n3. Добавляем группу...")
        group_query = "INSERT INTO `groups` (title, start_date) VALUES (%s, %s)"
        group_id = execute_query(connection, group_query, ('Group of Gregory', 'Март'))
        print(f"Добавлена группа с ID: {group_id}")

        # 4. Определяем студента в группу
        print("\n4. Определяем студента в группу...")
        update_student_query = "UPDATE students SET group_id = %s WHERE id = %s"
        execute_query(connection, update_student_query, (group_id, student_id))
        print("Студент добавлен в группу")

        # 5. Добавляем предметы
        print("\n5. Добавляем предметы...")
        subjects = ['SQUAT', 'BENCH', 'DEADLIFT']
        subject_ids = []

        for subject in subjects:
            subject_query = "INSERT INTO subjects (title) VALUES (%s)"
            subject_id = execute_query(connection, subject_query, (subject,))
            subject_ids.append(subject_id)
            print(f"Добавлен предмет '{subject}' с ID: {subject_id}")

        # 6. Добавляем уроки для каждого предмета
        print("\n6. Добавляем уроки...")
        lesson_ids = []

        for i, subject_id in enumerate(subject_ids):
            lesson1_query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
            lesson2_query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"

            lesson1_id = execute_query(connection, lesson1_query, (f'{subjects[i]} Lesson 1', subject_id))
            lesson2_id = execute_query(connection, lesson2_query, (f'{subjects[i]} Lesson 2', subject_id))

            lesson_ids.extend([lesson1_id, lesson2_id])
            print(f"Добавлены уроки для предмета {subjects[i]}: {lesson1_id}, {lesson2_id}")

        # 7. Добавляем оценки студенту за все уроки
        print("\n7. Добавляем оценки...")
        for lesson_id in lesson_ids:
            mark_query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
            execute_query(connection, mark_query, ('five', lesson_id, student_id))
        print("Добавлены оценки за все уроки")

        # 8. Получаем и выводим все данные студента
        print("\n8. Получаем данные студента...")

        # Оценки студента
        marks_query = "SELECT * FROM marks WHERE student_id = %s"
        marks = execute_query(connection, marks_query, (student_id,), fetch=True)
        print("\nОценки студента:")
        for mark in marks:
            print(mark)

        # Книги студента
        books_query = "SELECT * FROM books WHERE taken_by_student_id = %s"
        books = execute_query(connection, books_query, (student_id,), fetch=True)
        print("\nКниги студента:")
        for book in books:
            print(book)

        # Полная информация о студенте
        full_info_query = """
        SELECT * FROM `groups` g
        JOIN students st ON g.id = st.group_id
        JOIN books b ON st.id = b.taken_by_student_id
        JOIN marks m ON b.taken_by_student_id = m.student_id
        JOIN lessons l ON m.lesson_id = l.id
        JOIN subjects s ON l.subject_id = s.id
        WHERE st.id = %s
        """
        full_info = execute_query(connection, full_info_query, (student_id,), fetch=True)
        print("\nПолная информация о студенте:")
        for info in full_info:
            print(info)

    except Error as e:
        print(f"Произошла ошибка: {e}")
    finally:
        if connection.is_connected():
            connection.close()
            print("\nСоединение с базой данных закрыто")


if __name__ == "__main__":
    main()
