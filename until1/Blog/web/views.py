from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.urls import reverse
from .models import User
from . import models
from django.views import View
from django.http import HttpResponse
from pure_pagination import PageNotAnInteger, Paginator
from django.shortcuts import render, redirect
from .forms import CommentForm


# Create your views here.

def Blog(request):
    articles = models.Article.objects.all().order_by('-id')
    count_nums = models.Counts.objects.first()
    blog_nums = count_nums.blog_nums
    cate_nums = count_nums.category_nums
    tag_nums = count_nums.tag_nums
    count_nums.visit_nums += 1
    count_nums.save()
    all_category = models.Category.objects.all().order_by('id')
    # 分页
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(articles, 2, request=request)
    articles = p.page(page)

    return render(request, 'index.html', {
        'all_category': all_category,
        'articles': articles,
        'blog_nums': blog_nums,
        'cate_nums': cate_nums,
        'tag_nums': tag_nums
    })


def article(request, article_id):
    contents1 = models.Article.objects.get(pk=article_id)
    # 博客点击数+1, 评论数统计
    contents1.views += 1
    contents1.save()
    # 获取评论内容

    # 实现博客上一篇与下一篇功能

    has_prev = False
    has_next = False
    id_prev = id_next = int(article_id)
    blog_id_max = models.Article.objects.all().order_by('-id').first()
    id_max = blog_id_max.id
    while not has_prev and id_prev >= 1:
        blog_prev = models.Article.objects.filter(id=id_prev - 1).first()
        if not blog_prev:
            id_prev -= 1
        else:
            has_prev = True
    while not has_next and id_next <= id_max:
        blog_next = models.Article.objects.filter(id=id_next + 1).first()
        if not blog_next:
            id_next += 1
        else:
            has_next = True

    return render(request, 'article_page.html', {
        'article': contents1,
        'blog_prev': blog_prev,
        'blog_next': blog_next,
        'has_prev': has_prev,
        'has_next': has_next,

    })


def blogs_with_type(request, cate_id):
    cate = models.Category.objects.get(pk=cate_id)
    articles = models.Article.objects.filter(category=cate)
    count_nums = models.Counts.objects.first()
    blog_nums = count_nums.blog_nums
    cate_nums = count_nums.category_nums
    tag_nums = count_nums.tag_nums
    all_category = models.Category.objects.all().order_by('id')
    # 分页
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(articles, 2, request=request)
    articles = p.page(page)
    return render(request, 'index.html', {
        'all_category': all_category,
        'articles': articles,
        'blog_nums': blog_nums,
        'cate_nums': cate_nums,
        'tag_nums': tag_nums
    })


class ArichiveView(View):
    """
    归档
    """

    def get(self, request):
        all_blog = models.Article.objects.all().order_by('-created_time')
        all_category = models.Category.objects.all().order_by('id')
        user = models.User.objects.first()
        # 博客、标签、分类数目统计
        count_nums = models.Counts.objects.get(id=1)
        blog_nums = count_nums.blog_nums
        cate_nums = count_nums.category_nums
        tag_nums = count_nums.tag_nums
        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_blog, 5, request=request)
        all_blog = p.page(page)

        return render(request, 'archive.html', {
            'all_blog': all_blog,
            'all_category': all_category,
            'blog_nums': blog_nums,
            'cate_nums': cate_nums,
            'tag_nums': tag_nums,

        })


class AddCommentView(View):
    """
    评论
    """
    def post(self, request):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
            return HttpResponse('{"status": "success"}', content_type='application/json')
        else:
            return HttpResponse('{"status": "fail"}', content_type='application/json')


