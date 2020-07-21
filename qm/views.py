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

            mSheet = Sheet('Master_qm')
            tSheet = Sheet('Tent_db')

            row_list = []

            if sheet == 'Master_qm':
                try:
                    mSheet.execute(action=action, value=value, row=row, col=col, new=new)
                    row_list = tSheet.get_row(row)
                except:
                    return render(request, 'qm/fail.html')
            elif sheet == 'Tent_db':
                try:
                    result = tSheet.execute(action=action, value=value, row=row, col=col, new=new)
                    row_list = tSheet.get_row(row)
                    sheet_all = tSheet.get_all()
                    while len(row_list) < 6:
                        row_list.append('')
                except:
                    return render(request, 'qm/fail.html')

            context = {
                    'result': result,
                    'sheet': sheet,
                    'action': action,
                    'row': row,
                    'col': col,
                    'new': new,
                    'value': value,
                    'row_list': row_list,
                    'sheet_all': sheet_all
                    }
            return render(request, 'qm/results.html', context)
    else:
        form = spreadForm()
        return render(request, 'qm/spreadsheet.html', {'title': 'Submit', 'form': form})
