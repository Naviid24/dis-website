from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import QuoteForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
import mimetypes


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def kitchens(request):
    return render(request, "kitchens.html")


def bathrooms(request):
    return render(request, "bathrooms.html")


def quote_view(request):
    if request.method == "POST":
        form = QuoteForm(request.POST, request.FILES)
        if form.is_valid():
            quote = form.save()

            # Render HTML content for the email
            html_content = render_to_string("quote_email.html", {"quote": quote})

            # Create email
            email = EmailMultiAlternatives(
                subject=f"New Quote Request - {quote.service}",
                body=f"New quote request from {quote.name}",
                from_email=None,  # uses DEFAULT_FROM_EMAIL
                to=["dsipropertysolutions@gmail.com"],  # your email
            )

            # Attach HTML content
            email.attach_alternative(html_content, "text/html")

            # Attach uploaded image if exists
            if quote.image:
                # Guess MIME type
                mime_type, _ = mimetypes.guess_type(quote.image.name)
                if not mime_type:
                    mime_type = "application/octet-stream"
                email.attach(quote.image.name, quote.image.read(), mime_type)

            # Send the email via SendGrid
            email.send(fail_silently=False)

            messages.success(request, "Thanks — we will get in touch with you soon.")
            return redirect("quote")
    else:
        form = QuoteForm()
    return render(request, "quote.html", {"form": form})
