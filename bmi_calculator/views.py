from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import FormView

# Create your views here.
from bmi_calculator.forms import BMIForm


# @method_decorator(login_required(login_url=reverse_lazy('accounts:login')), name='dispatch') we can also use this
class BMIView(FormView):
    form_class = BMIForm
    template_name = 'bmi/bmi_calculator.html'
    success_url = reverse_lazy('bmi:bmi-calculator')

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            messages.info(self.request, 'For calculate BMI you should login', 'danger')
            return redirect(self.success_url)

        weight = form.cleaned_data['weight']
        height = form.cleaned_data['height']
        bmi = weight / height ** 2
        context = self.get_context_data()
        context['bmi'] = bmi
        return self.render_to_response(context=context)
