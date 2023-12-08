# custom_storage.py
from cloudinary_storage.storage import MediaCloudinaryStorage

class CustomCloudinaryStorage(MediaCloudinaryStorage):
    def _save(self, name, content):
        self.options.update({'folder': 'dripz'})
        return super()._save(name, content)