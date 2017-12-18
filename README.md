# Readme

This project is migrated from my wagtail_tuto, the project structure is similar.

## Env

Python3 + Django 1.11, I use pyenv to setup this env

## How to setup

```shell

git clone git@github.com:michael-yin/wagtail_streamfield.git wagtail_tuto
cd wagtail_tuto

#setup virtualenv
pip install -r requirements.txt
./manage.py runserver

# goto http://127.0.0.1:8000/ to check
# cms admin entry  http://127.0.0.1:8000/admin/
# username:password admin:admin
```

You can see I use wagtailmenu to manage the top menu of this blog app, to edit the menu, you can go to `http://127.0.0.1:8000/admin/wagtailmenus/mainmenu/edit/2/`

In `http://127.0.0.1:8000/admin/`, you can check and edit the blog home page, and blog post pages. All the pages support StreamField. You can check `blog/models.py` for more config detail.

## Theme

I use bootstrap theme and the css sourc file is in `blog/static/blog/css`, you can add your custom css code to `blog-home.css`

## Template

In `blog/templates/blog` you can ses

```shell
├── base.html
├── blog_page.html
└── post_page.html
```

`blog_page.html` is for blog home page, and `post_page.html` is for blog post page, both pages extend the `base.html`
