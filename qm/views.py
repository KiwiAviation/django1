from django.shortcuts import render
from .forms import spreadForm
from .spreadsheet import Sheet

def qm(request):
    if request.method == 'POST':
        form = spreadForm(request.POST)
        if form.is_valid():
            sheet = form.cleaned_data.get('sheet')

            action = form.cleaned_data.get('action')
            value = None # disabling for now, might remove completely
            row = form.cleaned_data.get('Item')
            col = form.cleaned_data.get('Attribute')
            new = form.cleaned_data.get('Value').split(', ')

            mSheet = Sheet('Master_qm')
            tSheet = Sheet('Tent_db')

            row_list = []

            if sheet == 'Master_qm':
                try:
                    result = mSheet.execute(action=action, value=value, row=row, col=col, new=new)
                    row_list = mSheet.get_row(row)
                    sheet_all = mSheet.get_all()
                    while len(row_list) < 6:
                        row_list.append('')
                    result1 = result
                    while len(result1) < 6:
                        result1.append('')

                except ValueError as exc:
                    error_context = {'Error_type': 'ValueError', 'Error': exc}
                    return render(request, 'qm/fail.html', error_context)
                except Exception as exc:
                    error_context = {'Error_type': 'Unexpected Error', 'Error': exc}
                    return render(request, 'qm/fail.html', error_context)
            elif sheet == 'Tent_db':
                try:
                    result = tSheet.execute(action=action, value=value, row=row, col=col, new=new)
                    row_list = tSheet.get_row(row)
                    sheet_all = tSheet.get_all()
                    while len(row_list) < 6:
                        row_list.append('')
                    result1 = result
                    while len(result1) < 6:
                        result1.append('')
                        
                except ValueError as exc:
                    error_context = {'Error_type': 'ValueError', 'Error': exc}
                    return render(request, 'qm/fail.html', error_context)
                except Exception as exc:
                    error_context = {'Error_type': 'Unexpected Error', 'Error': exc}
                    return render(request, 'qm/fail.html', error_context)

            context = {
                    'result': result,
                    'result1': result1,
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
        return render (request, 'qm/fail.html')
    else:
        form = spreadForm()
        return render(request, 'qm/spreadsheet.html', {'title': 'Submit', 'form': form})
