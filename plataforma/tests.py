from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import AccessToken

from .models import Category, Comment, Post


class PostAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create_user(
            username='admin', password='admin')
        self.access_token = AccessToken.for_user(self.user)
        self.authorization_header = f'Bearer {self.access_token}'

        self.category = Category.objects.create(name='Categoria Teste')

    def create_post(self, title='Post', content='Conteúdo', category=None):
        return Post.objects.create(
            title=title,
            content=content,
            category=category or self.category
        )

    def test_create_post(self):
        response = self.client.post(
            '/api/post/', {'title': 'Novo Post',
                           'content': 'Conteúdo do novo post', 'category': self.category.id},
            HTTP_AUTHORIZATION=self.authorization_header
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        post = Post.objects.first()
        self.assertEqual(post.title, 'Novo Post')
        self.assertEqual(post.content, 'Conteúdo do novo post')

    def test_retrieve_post(self):
        post = self.create_post(title='Post', content='Conteúdo')
        response = self.client.get(
            f'/api/post/{post.id}/', HTTP_AUTHORIZATION=self.authorization_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], post.title)
        self.assertEqual(response.data['content'], post.content)

    def test_update_post(self):
        post = self.create_post()
        response = self.client.patch(
            f'/api/post/{post.id}/', {'title': 'Post Atualizado'},
            HTTP_AUTHORIZATION=self.authorization_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Post.objects.get(id=post.id).title, 'Post Atualizado')

    def test_delete_post(self):
        post = self.create_post()
        response = self.client.delete(
            f'/api/post/{post.id}/', HTTP_AUTHORIZATION=self.authorization_header)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)


class CommentAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create_user(
            username='admin', password='admin')
        self.access_token = AccessToken.for_user(self.user)
        self.authorization_header = f'Bearer {self.access_token}'

        self.category = Category.objects.create(name='Categoria Teste')
        self.post = Post.objects.create(
            title='Post', content='Conteúdo', category=self.category)

    def create_comment(self, post=None, author='Autor', content='Conteúdo'):
        return Comment.objects.create(
            post=post or self.post,
            author=author,
            content=content
        )

    def test_create_comment(self):
        response = self.client.post(
            '/api/comment/', {'post': self.post.id,
                              'author': 'Autor', 'content': 'Conteúdo do comentário'},
            HTTP_AUTHORIZATION=self.authorization_header
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 1)
        comment = Comment.objects.first()
        self.assertEqual(comment.author, 'Autor')
        self.assertEqual(comment.content, 'Conteúdo do comentário')

    def test_retrieve_comment(self):
        comment = self.create_comment(author='Autor', content='Conteúdo')
        response = self.client.get(
            f'/api/comment/{comment.id}/', HTTP_AUTHORIZATION=self.authorization_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['author'], comment.author)
        self.assertEqual(response.data['content'], comment.content)

    def test_update_comment(self):
        comment = self.create_comment()
        response = self.client.patch(
            f'/api/comment/{comment.id}/', {'author': 'Autor Atualizado'},
            HTTP_AUTHORIZATION=self.authorization_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Comment.objects.get(
            id=comment.id).author, 'Autor Atualizado')

    def test_delete_comment(self):
        comment = self.create_comment()
        response = self.client.delete(
            f'/api/comment/{comment.id}/', HTTP_AUTHORIZATION=self.authorization_header)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Comment.objects.count(), 0)


class CategoryAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create_user(
            username='admin', password='admin')
        self.access_token = AccessToken.for_user(self.user)
        self.authorization_header = f'Bearer {self.access_token}'

    def create_category(self, name='Categoria'):
        return Category.objects.create(name=name)

    def test_create_category(self):
        response = self.client.post(
            '/api/category/', {'name': 'Nova Categoria'},
            HTTP_AUTHORIZATION=self.authorization_header
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        category = Category.objects.first()
        self.assertEqual(category.name, 'Nova Categoria')

    def test_retrieve_category(self):
        category = self.create_category(name='Categoria')
        response = self.client.get(
            f'/api/category/{category.id}/', HTTP_AUTHORIZATION=self.authorization_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], category.name)

    def test_update_category(self):
        category = self.create_category()
        response = self.client.patch(
            f'/api/category/{category.id}/', {'name': 'Categoria Atualizada'},
            HTTP_AUTHORIZATION=self.authorization_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Category.objects.get(
            id=category.id).name, 'Categoria Atualizada')

    def test_delete_category(self):
        category = self.create_category()
        response = self.client.delete(
            f'/api/category/{category.id}/', HTTP_AUTHORIZATION=self.authorization_header)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.count(), 0)
