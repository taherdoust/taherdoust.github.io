# from django.db import models

# class Post(models.Model):
#     PRIVACY_CHOICES = [
#         ('public', 'Public'),
#         ('private', 'Private')
#     ]
    
#     CLASSIFICATION_CHOICES = [
#         ('professional', 'Professional Weblog'),
#         ('social', 'Social Weblog'),
#         ('portfolio', 'Portfolio'),
#         ('personal', 'Personal Weblog'),
#         ('coaching', 'Coaching Page')
#     ]

#     title = models.CharField(max_length=255)
#     passage = models.TextField()
#     album = models.JSONField(default=list)  # Store multiple images
#     summary = models.TextField()
#     post_pic = models.URLField(blank=True, null=True)  # URL for selected picture
#     classification = models.CharField(max_length=20, choices=CLASSIFICATION_CHOICES)
#     privacy = models.CharField(max_length=10, choices=PRIVACY_CHOICES, default='public')
#     datetime = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)  # Mandatory
    passage = models.TextField(blank=True, null=True)  # Optional
    album = models.ImageField(upload_to='albums/', blank=True, null=True)  # Optional
    summary = models.TextField(blank=True, null=True)  # Optional
    selected_picture = models.ImageField(upload_to='selected_pics/', blank=True, null=True)  # Optional
    classification = models.CharField(
        max_length=50,
        choices=[
            ('professional', 'Professional Weblog'),
            ('social', 'Social Weblog'),
            ('portfolio', 'Portfolio'),
            ('personal', 'Personal Weblog'),
            ('coaching', 'Coaching Page')
        ],
        blank=True, null=True  # Optional
    )
    privacy = models.CharField(
        max_length=10,
        choices=[('public', 'Public'), ('private', 'Private')],
        blank=True, null=True  # Optional
    )
    datetime = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    

    def __str__(self):
        return self.title  # Return title for admin display
