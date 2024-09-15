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
            username='boostcode', password='code@123')
        self.access_token = AccessToken.for_user(self.user)
        self.authorization_header = f'Bearer {self.access_token}'

    def test_create_post(self):
        response = self.client.post(
            '/api/post/', {'title': 'Novo Post', 'content': 'Conteúdo do novo post'}, HTTP_AUTHORIZATION=self.authorization_header)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        post = Post.objects.first()
        self.assertEqual(post.title, 'Novo Post')
        self.assertEqual(post.content, 'Conteúdo do novo post')

    def test_retrieve_post(self):
        post = Post.objects.create(title='Post', content='Conteúdo')
        response = self.client.get(
            f'/api/post/{post.id}/', HTTP_AUTHORIZATION=self.authorization_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], post.title)
        self.assertEqual(response.data['content'], post.content)

    def test_update_post(self):
        post = Post.objects.create(title='Post', content='Conteúdo')
        response = self.client.patch(
            f'/api/post/{post.id}/', {'title': 'Post Atualizado'}, HTTP_AUTHORIZATION=self.authorization_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Post.objects.get().title, 'Post Atualizado')

    def test_delete_post(self):
        post = Post.objects.create(title='Post', content='Conteúdo')
        response = self.client.delete(
            f'/api/post/{post.id}/', HTTP_AUTHORIZATION=self.authorization_header)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)

    def test_create_post_unauthenticated(self):
        response = self.client.post('/api/post/', {'title': 'Novo Post', 'content': 'Conteúdo do novo post'},
                                    HTTP_AUTHORIZATIO='')
        self.assertEqual(response.status_code, 401)


class CategoryAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create_user(
            username='boostcode', password='code@123')
        self.access_token = AccessToken.for_user(self.user)
        self.authorization_header = f'Bearer {self.access_token}'

    def test_create_category(self):
        response = self.client.post(
            '/api/category/', {'name': 'Nova Categoria'}, HTTP_AUTHORIZATION=self.authorization_header)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        category = Category.objects.first()
        self.assertEqual(category.name, 'Nova Categoria')

    def test_retrieve_category(self):
        category = Category.objects.create(name='Categoria')
        response = self.client.get(
            f'/api/category/{category.id}/', HTTP_AUTHORIZATION=self.authorization_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], category.name)

    def test_update_category(self):
        category = Category.objects.create(name='Categoria')
        response = self.client.patch(
            f'/api/category/{category.id}/', {'name': 'Categoria Atualizada'}, HTTP_AUTHORIZATION=self.authorization_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Category.objects.get().name, 'Categoria Atualizada')

    def test_delete_category(self):
        category = Category.objects.create(name='Categoria')
        response = self.client.delete(
            f'/api/category/{category.id}/', HTTP_AUTHORIZATION=self.authorization_header)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.count(), 0)

    def test_create_category_unauthenticated(self):
        response = self.client.post('/api/category/', {'name': 'Nova Categoria'},
                                    HTTP_AUTHORIZATIO='')
        self.assertEqual(response.status_code, 401)


class CommentAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create_user(
            username='boostcode', password='code@123')
        self.access_token = AccessToken.for_user(self.user)
        self.authorization_header = f'Bearer {self.access_token}'

    def test_create_comment(self):
        post = Post.objects.create(title='Post', content='Conteúdo')
        response = self.client.post(
            '/api/comment/', {'post': post.id, 'author': 'Saulo', 'content': 'Comentário'}, HTTP_AUTHORIZATION=self.authorization_header)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 1)
        comment = Comment.objects.first()
        self.assertEqual(comment.post, post)
        self.assertEqual(comment.author, 'Saulo')
        self.assertEqual(comment.content, 'Comentário')

    def test_retrieve_comment(self):
        post = Post.objects.create(title='Post', content='Conteúdo')
        comment = Comment.objects.create(
            post=post, author='Saulo', content='Comentário')
        response = self.client.get(
            f'/api/comment/{comment.id}/', HTTP_AUTHORIZATION=self.authorization_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['post'], post.id)
        self.assertEqual(response.data['author'], 'Saulo')
        self.assertEqual(response.data['content'], 'Comentário')

    def test_update_comment(self):
        post = Post.objects.create(title='Post', content='Conteúdo')
        comment = Comment.objects.create(
            post=post, author='Saulo', content='Comentário')
        response = self.client.patch(
            f'/api/comment/{comment.id}/', {'author': 'Saulo Justiniano'}, HTTP_AUTHORIZATION=self.authorization_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Comment.objects.get().author, 'Saulo Justiniano')

    def test_delete_comment(self):
        post = Post.objects.create(title='Post', content='Conteúdo')
        comment = Comment.objects.create(
            post=post, author='Saulo', content='Comentário')
        response = self.client.delete(
            f'/api/comment/{comment.id}/', HTTP_AUTHORIZATION=self.authorization_header)
        self.assertEqual
