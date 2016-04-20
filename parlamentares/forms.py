from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Fieldset, Layout, Submit
from django import forms
from django.db import transaction
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from floppyforms import ClearableFileInput

import crispy_layout_mixin
from crispy_layout_mixin import form_actions

from .models import Dependente, Filiacao, Legislatura, Mandato, Parlamentar


class ImageThumbnailFileInput(ClearableFileInput):
    template_name = 'floppyforms/image_thumbnail.html'


class ParlamentarForm(ModelForm):

    class Meta:
        model = Parlamentar
        exclude = []
        widgets = {'fotografia': ImageThumbnailFileInput,
                   'biografia': forms.Textarea(
                        attrs={'id': 'texto-rico'})}


class ParlamentarCreateForm(ParlamentarForm):

    legislatura = forms.ModelChoiceField(
        label=_('Legislatura'),
        required=True,
        queryset=Legislatura.objects.all().order_by('-data_inicio'),
        empty_label='----------',
    )

    data_expedicao_diploma = forms.DateField(
        label=_('Expedição do Diploma'),
        required=True,
    )

    @transaction.atomic
    def save(self, commit=True):
        parlamentar = super(ParlamentarCreateForm, self).save(commit)
        legislatura = self.cleaned_data['legislatura']
        Mandato.objects.create(
            parlamentar=parlamentar,
            legislatura=legislatura,
            data_fim_mandato=legislatura.data_fim,
            data_expedicao_diploma=self.cleaned_data['data_expedicao_diploma'])
        return parlamentar


class MandatoForm(ModelForm):

    legislatura = forms.ModelChoiceField(
        label=_('Legislatura'),
        required=True,
        queryset=Legislatura.objects.all().order_by('-data_inicio'),
        empty_label='----------',
    )

    class Meta:
        model = Mandato
        fields = ['legislatura',
                  'coligacao',
                  'votos_recebidos',
                  'data_fim_mandato',
                  'data_expedicao_diploma',
                  'tipo_afastamento',
                  'observacao']

    def __init__(self, *args, **kwargs):

        row1 = crispy_layout_mixin.to_row(
            [('legislatura', 4),
             ('coligacao', 4),
             ('votos_recebidos', 4)])

        row2 = crispy_layout_mixin.to_row(
            [('data_fim_mandato', 6),
             ('data_expedicao_diploma', 6)])

        row3 = crispy_layout_mixin.to_row(
            [('tipo_afastamento', 12)])

        row4 = crispy_layout_mixin.to_row(
            [('observacao', 12)])

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(_('Adicionar Mandato'), row1, row2, row3, row4,
                     form_actions())

        )
        super(MandatoForm, self).__init__(
            *args, **kwargs)


class MandatoEditForm(MandatoForm):

    def __init__(self, *args, **kwargs):
        super(MandatoEditForm, self).__init__(
            *args, **kwargs)

        self.helper.layout[0][-1:] = form_actions(more=[
            HTML('&nbsp;'),
            Submit('excluir', 'Excluir',
                   css_class='btn btn-primary')])


class DependenteForm(ModelForm):

    class Meta:
        model = Dependente
        fields = ['nome',
                  'data_nascimento',
                  'tipo',
                  'sexo',
                  'cpf',
                  'rg',
                  'titulo_eleitor']

    def __init__(self, *args, **kwargs):

        row1 = crispy_layout_mixin.to_row(
            [('nome', 12)])

        row2 = crispy_layout_mixin.to_row(
            [('tipo', 4),
             ('sexo', 4),
             ('data_nascimento', 4)])

        row3 = crispy_layout_mixin.to_row(
            [('cpf', 4),
             ('rg', 4),
             ('titulo_eleitor', 4)])

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(_('Cadastro de Dependentes'),
                     row1, row2, row3,
                     form_actions())

        )
        super(DependenteForm, self).__init__(
            *args, **kwargs)


class DependenteEditForm(DependenteForm):

    def __init__(self, *args, **kwargs):
        super(DependenteEditForm, self).__init__(
            *args, **kwargs)

        self.helper.layout[0][-1:] = form_actions(more=[
            HTML('&nbsp;'),
            Submit('excluir', 'Excluir',
                   css_class='btn btn-primary')])


class FiliacaoForm(ModelForm):

    class Meta:
        model = Filiacao
        fields = ['partido',
                  'data',
                  'data_desfiliacao']

    def __init__(self, *args, **kwargs):

        row1 = crispy_layout_mixin.to_row(
            [('partido', 4),
             ('data', 4),
             ('data_desfiliacao', 4)])

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(_('Adicionar Filiação'), row1,
                     form_actions())

        )
        super(FiliacaoForm, self).__init__(
            *args, **kwargs)


class FiliacaoEditForm(FiliacaoForm):

    def __init__(self, *args, **kwargs):
        super(FiliacaoEditForm, self).__init__(
            *args, **kwargs)

        self.helper.layout[0][-1:] = form_actions(more=[
            HTML('&nbsp;'),
            Submit('excluir', 'Excluir',
                   css_class='btn btn-primary')])
