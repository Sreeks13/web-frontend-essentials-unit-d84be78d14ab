from pathlib import Path
from html.parser import HTMLParser


html = Path("index.html").read_text(encoding="utf-8")


def test_html5_doctype():
    assert "<!DOCTYPE html>" in html


def test_semantic_structure():
    assert "<header" in html
    assert "<main" in html
    assert "<form" in html
    assert "<footer" in html


def test_form_has_labels():
    assert "<label" in html
    assert 'for="name"' in html
    assert 'for="email"' in html
    assert 'for="book"' in html


def test_required_fields():
    assert 'required' in html


def test_email_validation():
    assert 'type="email"' in html