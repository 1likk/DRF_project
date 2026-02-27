import pytest
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from apps.notes.models import Note


class TestNoteAPISimple(TestCase):
    """Простые API тесты без DRF сложностей"""
    
    def setUp(self):
        self.client = APIClient()
        self.note = Note.objects.create(
            title='Тестовая заметка',
            content='Содержание тестовой заметки'
        )
    
    def test_note_model_creation(self):
        """Тест создания заметки через модель"""
        note = Note.objects.create(
            title='Новая заметка',
            content='Содержание новой заметки'
        )
        
        self.assertEqual(note.title, 'Новая заметка')
        self.assertEqual(note.content, 'Содержание новой заметки')
        self.assertIsNotNone(note.created_at)
        self.assertIsNotNone(note.updated_at)
    
    def test_note_str_method(self):
        """Тест строкового представления"""
        self.assertEqual(str(self.note), 'Тестовая заметка')
    
    def test_note_ordering(self):
        """Тест сортировки заметок"""
        note2 = Note.objects.create(title='Вторая', content='Содержание')
        notes = Note.objects.all()
        
        # Первой должна быть самая новая (note2)
        self.assertEqual(notes.first(), note2)
    
    def test_content_validation(self):
        """Тест валидации длины контента"""
        from django.core.exceptions import ValidationError
        
        # Создаем заметку с очень длинным содержанием
        long_content = 'a' * 10001
        note = Note(title='Тест', content=long_content)
        
        # Проверяем что валидация не пройдет
        with self.assertRaises(ValidationError):
            note.full_clean()
    
    def test_admin_display(self):
        """Тест отображения в админке"""
        # Проверяем что поля для админки настроены
        from apps.notes.admin import NoteAdmin
        
        admin = NoteAdmin(Note, None)
        self.assertIn('title', admin.list_display)
        self.assertIn('created_at', admin.list_display)
        self.assertIn('title', admin.search_fields)
