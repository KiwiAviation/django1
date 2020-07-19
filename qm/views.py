from django.shortcuts import render
from .forms import spreadForm
from .spreadsheet import Sheet

def qm(request):
    if request.method == 'POST':
        form = spreadForm(request.POST)
        if form.is_valid():
            sheet = form.cleaned_data.get('sheet')

            action = form.cleaned_data.get('action')
            value = form.cleaned_data.get('search_value')
            row = form.cleaned_data.get('row')
            col = form.cleaned_data.get('col')
            new = form.cleaned_data.get('new').split(', ')

            print(sheet, action, value, row, col, new)

            mSheet = Sheet('Master_qm')
            tSheet = Sheet('Tent_db')

            if sheet == 'Master_qm':
                try:
                    mSheet.execute(action=action, value=value, row=row, col=col, new=new)
                except:
                    return render(request, 'qm/fail.html', {'title': 'Submit', 'form': form})
            elif sheet == 'Tent_db':
                try:
                    tSheet.execute(action=action, value=value, row=row, col=col, new=new)
                except:
                    return render(request, 'qm/fail.html', {'title': 'Submit', 'form': form})

            return render(request, 'qm/spreadsheet.html', {'title': 'Submit', 'form': form})
    else:
        form = spreadForm()
        return render(request, 'qm/spreadsheet.html', {'title': 'Submit', 'form': form})
