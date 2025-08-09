from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .forms import QuoteForm


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
            # Send email (console backend prints to terminal)
            send_mail(
                subject=f"New Quote Request - {quote.service}",
                message=f"Name: {quote.name}\nEmail: {quote.email}\nPhone: {quote.phone}\n\n{quote.description}",
                from_email=None,  # uses DEFAULT_FROM_EMAIL
                recipient_list=["you@yourdomain.co.uk"],  # change to your email
            )
            messages.success(request, "Thanks — we will get in touch with you soon.")
            return redirect("quote")
    else:
        form = QuoteForm()
    return render(request, "quote.html", {"form": form})
