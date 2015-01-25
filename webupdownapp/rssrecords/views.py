from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.shortcuts import get_object_or_404


from .models import Rssrecord
from .forms import RssRecordsForm
from .forms import CsvUploadForm


@login_required()
def rssrecord_summary(request):

    total = Rssrecord.objects.filter(owner=request.user).count()
    totalup = Rssrecord.objects.filter(owner=request.user, upordown='UP').count()
    totaldown = Rssrecord.objects.filter(owner=request.user, upordown='DOWN').count()
    totalnotchecked = Rssrecord.objects.filter(owner=request.user, upordown='not yet checked').count()

    return render(request, 'rssrecords/rssrecord_summary.html', {'totalup': totalup, 'total': total, 'totaldown':totaldown, 'totalnotchecked': totalnotchecked })



class RssRecordList(ListView):

    model = Rssrecord
    paginate_by = 10
    template_name = 'rssrecords/rssrecord_list.html'
    context_object_name = 'rssrecords'

    def get_queryset(self):
        try:
            a = self.request.GET.get('rssrecord',)
        except KeyError:
            a = None
        if a:
            rssrecords_list = Rssrecord.objects.filter(
                name__icontains=a,
                owner=self.request.user,
            )
        else:
            rssrecords_list = Rssrecord.objects.filter(owner=self.request.user)
        return rssrecords_list

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(RssRecordList, self).dispatch(*args, **kwargs)

class RssUpList(ListView):

    model = Rssrecord
    #paginate_by = 10
    template_name = 'rssrecords/rssup_list.html'
    context_object_name = 'rssup'

    def get_queryset(self):

        rssup_list = Rssrecord.objects.filter(owner=self.request.user, upordown='UP')
        return rssup_list

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(RssUpList, self).dispatch(*args, **kwargs)

class RssDownList(ListView):

    model = Rssrecord
    #paginate_by = 10
    template_name = 'rssrecords/rssdown_list.html'
    context_object_name = 'rssdown'

    def get_queryset(self):

        rssdown_list = Rssrecord.objects.filter(owner=self.request.user, upordown='DOWN')
        return rssdown_list

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(RssDownList, self).dispatch(*args, **kwargs)

class RssNotCheckedList(ListView):

    model = Rssrecord
    #paginate_by = 10
    template_name = 'rssrecords/rssnotchecked_list.html'
    context_object_name = 'rssnotchecked'

    def get_queryset(self):

        rssnotchecked_list = Rssrecord.objects.filter(owner=self.request.user, upordown='not yet checked')
        return rssnotchecked_list

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(RssNotCheckedList, self).dispatch(*args, **kwargs)


@login_required()
def rssrecord_detail(request, uuid):

    rssrecord = Rssrecord.objects.get(uuid=uuid)
    if rssrecord.owner != request.user:
            return HttpResponseForbidden()

    variables = {
        'rssrecord': rssrecord,
    }
    return render(request, 'rssrecords/rssrecord_detail.html', variables)

@login_required()
def rssrecord_cru(request, uuid=None):
    import csv

    if uuid:
        rssrecord = get_object_or_404(Rssrecord, uuid=uuid)
        if rssrecord.owner != request.user:
            return HttpResponseForbidden()
    else:
        rssrecord = Rssrecord(owner=request.user)

    if request.POST:
        form = RssRecordsForm(request.POST)
        if form.is_valid():
            rssrecord = form.save(commit=False)
            rssrecord.owner = request.user
            rssrecord.save()
            redirect_url = reverse(
                'webupdownapp.rssrecords.views.rssrecord_detail',
                args=(rssrecord.uuid,)
            )
            return HttpResponseRedirect(redirect_url)
    else:
        form = RssRecordsForm()

    variables = {
        'form': form,
        'rssrecord': rssrecord
    }

    template = 'rssrecords/rssrecord_cru.html'

    return render(request, template, variables)

@login_required()
def rssrecord_upload(request, uuid=None):
    import csv

    if request.POST:
        form = CsvUploadForm(request.POST)
        if form.is_valid():
            rssrecord = form.save(commit=False)
            rssrecord.owner = request.user
            rssrecord.save()
            redirect_url = reverse(
                'webupdownapp.rssrecords.views.rssrecord_detail',
                args=(rssrecord.uuid,)
            )
            return HttpResponseRedirect(redirect_url)
    else:
        form = RssRecordsForm()

    variables = {
        'form': form,
    }

    template = 'rssrecords/rssrecord_upload.html'

    return render(request, template, variables)



