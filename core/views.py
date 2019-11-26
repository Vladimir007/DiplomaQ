from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import SingleObjectMixin

from DiplomaQ.vars import USER_ROLES
from DiplomaQ.utils import StreamingResponseView

from core.models import DiplomaFile, CuratorStudent
from core.utils import DiplomaGenerator


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        is_student = self.request.user.role == USER_ROLES[0][0]
        context['is_student'] = is_student
        if is_student:
            context['user_link'] = CuratorStudent.objects.filter(student=self.request.user)\
                .select_related('curator').first()
            context['files'] = DiplomaFile.objects.filter(user_link__student=self.request.user).order_by('-date')
        else:
            context['students'] = CuratorStudent.objects.filter(curator=self.request.user)\
                .annotate(files_num=Count('files')).select_related('student')\
                .order_by('student__last_name', 'student__first_name')
        return context


class StudentView(LoginRequiredMixin, ListView):
    template_name = 'core/student.html'

    def get_queryset(self):
        return DiplomaFile.objects.filter(
            user_link__curator=self.request.user,
            user_link__student_id=self.kwargs['student_id']
        ).order_by('-date')

    def get_context_data(self, *args, **kwargs):
        context = super(StudentView, self).get_context_data(*args, **kwargs)
        CuratorStudent.objects.filter()
        context['user_link'] = get_object_or_404(
            CuratorStudent.objects.select_related('student'),
            student_id=self.kwargs['student_id'], curator=self.request.user
        )
        return context


class DonwloadFileView(LoginRequiredMixin, SingleObjectMixin, StreamingResponseView):
    model = DiplomaFile

    def get_generator(self):
        return DiplomaGenerator(self.get_object())
