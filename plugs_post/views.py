# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	Post,
	PostSection,
)


class PostCreateView(CreateView):

    model = Post


class PostDeleteView(DeleteView):

    model = Post


class PostDetailView(DetailView):

    model = Post


class PostUpdateView(UpdateView):

    model = Post


class PostListView(ListView):

    model = Post


class PostSectionCreateView(CreateView):

    model = PostSection


class PostSectionDeleteView(DeleteView):

    model = PostSection


class PostSectionDetailView(DetailView):

    model = PostSection


class PostSectionUpdateView(UpdateView):

    model = PostSection


class PostSectionListView(ListView):

    model = PostSection

