import pytest
from django.test import TestCase
from apps.notes.models import Note


class TestNoteModel(TestCase):
    """Простые тесты для модели Note"""
    
    def test_create_note(self):
        """Тест создания заметки"""
        note = Note.objects.create(
            title='Тестовая заметка',
            content='Содержание заметки'
        )
        
        self.assertEqual(note.title, 'Тестовая заметка')
        self.assertEqual(note.content, 'Содержание заметки')
        self.assertIsNotNone(note.created_at)
        self.assertIsNotNone(note.updated_at)
    
    def test_note_str_method(self):
        """Тест метода __str__"""
        note = Note.objects.create(
            title='Очень длинный заголовок заметки для тестирования обрезки',
            content='Содержание'
        )
        
        # Проверяем что __str__ возвращает первые 50 символов заголовка
        expected = 'Очень длинный заголовок заметки для тестирования о'
        self.assertEqual(str(note), expected)
    
    def test_note_ordering(self):
        """Тест сортировки заметок по дате создания"""
        # Создаем несколько заметок
        note1 = Note.objects.create(title='Первая', content='Содержание 1')
        note2 = Note.objects.create(title='Вторая', content='Содержание 2')
        note3 = Note.objects.create(title='Третья', content='Содержание 3')
        
        # Получаем все заметки (должны быть отсортированы по -created_at)
        notes = Note.objects.all()
        
        # Проверяем порядок (самая новая должна быть первой)
        self.assertEqual(notes[0], note3)
        self.assertEqual(notes[1], note2)
        self.assertEqual(notes[2], note1)
    
    def test_note_verbose_names(self):
        """Тест verbose_name модели"""
        self.assertEqual(Note._meta.verbose_name, 'Заметка')
        self.assertEqual(Note._meta.verbose_name_plural, 'Заметки')
    
    def test_note_fields(self):
        """Тест полей модели"""
        note = Note.objects.create(
            title='Тест',
            content='Содержание'
        )
        
        # Проверяем что поля существуют
        self.assertTrue(hasattr(note, 'title'))
        self.assertTrue(hasattr(note, 'content'))
        self.assertTrue(hasattr(note, 'created_at'))
        self.assertTrue(hasattr(note, 'updated_at'))
    
    def test_content_max_length_validator(self):
        """Тест валидатора максимальной длины контента"""
        # Создаем заметку с очень длинным содержанием (больше 10000 символов)
        long_content = 'a' * 10001
        
        note = Note(title='Тест', content=long_content)
        
        # При вызове full_clean() должна возникнуть ошибка валидации
        with self.assertRaises(Exception):
            note.full_clean()
