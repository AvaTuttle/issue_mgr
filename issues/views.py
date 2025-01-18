from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from .models import Issue
from .forms import IssueForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, UpdateView


class IssueListView(ListView):
    model = Issue
    template_name = 'issues/issue_list.html'
    context_object_name = 'issues'
    def get_queryset(self):
        return Issue.objects.all().order_by('status')


class IssueDetailView(DetailView):
    model = Issue
    template_name = 'issues/issue_detail.html'
    context_object_name = 'issue'


from django.urls import reverse_lazy

class IssueUpdateView(UpdateView):
    model = Issue
    fields = ['status']
    template_name = 'issues/issue_update.html'
    success_url = reverse_lazy('issues:issue_list')  # Redirect to the issue list view
    def form_valid(self, form):
        if not self.request.user.has_perm('issues.change_issue'):
            return HttpResponseForbidden("You do not have permission to update the issue.")
        return super().form_valid(form)

    
@login_required
def issue_create(request):
    if not request.user.groups.filter(name='Product Owners').exists():
        return HttpResponseForbidden("You do not have permission to create issues.")

    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.reporter = request.user  
            issue.save()
            return redirect('issues:issue_list')
    else:
        form = IssueForm()
    return render(request, 'issues/issue_create.html', {'form': form})
