from django.http import HttpResponse
from django.views import View
from .models import Book, Member, Loan

def book_list(request):
    books = Book.objects.all()
    output = []

    for book in books:
        categories = ", ".join([c.name for c in book.categories.all()])
        output.append(f"{book.title} | {book.author.name} | {categories}")

    return HttpResponse("<br>".join(output))  


class CreateLoanView(View):
    def post(self, request, book_id):
        member_id = request.POST.get("member_id")

        book = Book.objects.get(id=book_id)
        member = Member.objects.get(id=member_id)

      
        Loan.objects.create(book=book, member=member)

        
        if book.available_copies > 0:
            book.available_copies -= 1
            book.save()

        return HttpResponse("Loan created successfully")
    
def books_never_loaned(request):
    books = Book.objects.filter(loan__isnull=True)

    titles = [book.title for book in books]
    return HttpResponse(", ".join(titles))


def science_books_by_newton(request):
    books = Book.objects.filter(
        categories__name="Science",
        author__name="Isaac Newton"
    )

    titles = [book.title for book in books]
    return HttpResponse(", ".join(titles))


from django.db.models import Count

def top_members(request):
    members = Member.objects.annotate(
        loan_count=Count("loan")
    ).order_by("-loan_count")[:3]

    result = []
    for m in members:
        result.append(f"{m.first_name} {m.last_name} ({m.loan_count})")

    return HttpResponse("<br>".join(result))


def books_per_category(request):
    categories = Category.objects.annotate(
        book_count=Count("books")
    )

    result = []
    for c in categories:
        result.append(f"{c.name}: {c.book_count}")

    return HttpResponse("<br>".join(result))


