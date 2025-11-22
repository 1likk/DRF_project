import factory
from factory.django import DjangoModelFactory
from apps.notes.models import Note


class NoteFactory(DjangoModelFactory):
    """Фабрика для создания тестовых заметок"""
    
    class Meta:
        model = Note
    
    title = factory.Faker('sentence', nb_words=4)
    content = factory.Faker('paragraph', nb_sentences=5)
