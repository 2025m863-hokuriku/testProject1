from .models import Post 
from .serializers import PostSerializer
 # DRFのジェネリックビューをインポート
from rest_framework import generics
 #Postモデルの一覧を返す、API専門のクラスベースビュー
class PostListAPIView(generics.ListAPIView): 
    # どのデータの一覧を返すか
    queryset = Post.objects.all() 
    # どの翻訳者（シリアライザ）を使ってJSONに変換するか
    serializer_class = PostSerializer

# Create your views here.
