from wsgiref.util import FileWrapper
from core.models import DiplomaFile


class DiplomaGenerator(FileWrapper):
    def __init__(self, diploma_obj):
        assert isinstance(diploma_obj, DiplomaFile), 'Unknown error'
        self.name = diploma_obj.name
        self.size = len(diploma_obj.file)
        super().__init__(diploma_obj.file, 8192)
