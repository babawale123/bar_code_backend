from django.db import models
import qrcode
from io import BytesIO
from PIL import Image
from django.core.files.base import ContentFile


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    qr_code = models.ImageField(blank=True, upload_to='qr_code/')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

    def save(self, *args, **kwargs):
        if not self.qr_code:
            qrcode_img = qrcode.make(self.title)
            canvas = Image.new('RGB', (qrcode_img.pixel_size, qrcode_img.pixel_size), 'white')
            canvas.paste(qrcode_img)
            fname = f'qr_code-{self.title}.png'
            buffer = BytesIO()
            canvas.save(buffer, 'PNG')
            self.qr_code.save(fname, ContentFile(buffer.getvalue()), save=False)
        super().save(*args, **kwargs)