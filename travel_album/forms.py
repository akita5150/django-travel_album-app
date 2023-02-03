from django import forms
from travel_album.models import Photo, Album, Diary

class AlbumAddForms(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('location',)
    # class Meta:
    #     model = Album
    #     fields = ['location']
    #     def form_valid(self, form):
    #         object = form.save(commit=False)
    #         # urlのpkからdiary抽出 ※リスト型で抽出される
    #         diary = Diary.objects.filter(id=self.kwargs['diary_pk'])
    #         object.diary = diary[0]
    #         # object保存
    #         object.save()
    #         return super().form_valid(form)

class PhotoAddForms(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('photo',)

