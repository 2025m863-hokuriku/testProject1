from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
 class Meta:
    model = Post # 翻訳対象のモデルを指定
    # どのフィールドを翻訳（JSONに含める）するかを指定
    fields = ['id', 'content', 'created_at']
