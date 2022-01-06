from django.db import models

from wagtail.admin.edit_handlers  import FieldPanel, MultiFieldPanel, FieldRowPanel, InlinePanel
from modelcluster.fields 		  import ParentalKey
from wagtail.core.fields 		  import RichTextField
from wagtail.contrib.forms.models import AbstractFormField, AbstractForm



class FormField(AbstractFormField):
    page = ParentalKey("AccountsPage", on_delete = models.CASCADE, related_name = "form_fields")



class AccountsPage(AbstractForm):
    template = "contact/contact_page.html"

    subpage_types = [] # přidáno kvůli jaký parrent může mít children
    parent_page_types = ["home.HomePage"] # přidáno kvůli jaký parrent může mít children

    company      = RichTextField(blank = True)
    contact_user = RichTextField(blank = True)

    content_panels = AbstractForm.content_panels + [
        FieldPanel("company"),
        InlinePanel("form_fields", label = "Form Fields"),
        FieldPanel("contact_user"),
    ]


