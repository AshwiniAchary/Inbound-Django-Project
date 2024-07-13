from django.shortcuts import render, redirect
from .forms import ReceiptForm
from .models import Pallet

def create_receipt(request):
    if request.method == 'POST':
        form = ReceiptForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('pallet_list')  # Redirect to another view after saving
    else:
        form = ReceiptForm()  # Create a new instance of the form

    return render(request, 'create_receipt.html', {'form': form})
def pallet_list(request):
    pallets = Pallet.objects.all()
    return render(request, 'pallet_list.html', {'pallets': pallets})
# def create_receipt(request):
#     if request.method == 'POST':
#         form = ReceiptForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('pallet_list')
#     else:
#         form = ReceiptForm()
#     return render(request, 'create_receipt.html', {'form': form})

# def pallet_list(request):
#     pallets = Pallet.objects.all()
#     return render(request, 'pallet_list.html', {'pallets': pallets})
# from django.shortcuts import render, redirect
# from .forms import ReceiptForm
# from .models import Pallet, Bin

# # def create_receipt(request):
# #     if request.method == 'POST':
# #         form = ReceiptForm(request.POST)
# #         if form.is_valid():
# #             pallet = form.save(commit=False)
# #             bin_allocation_logic(pallet)
# #             pallet.save()
# #             return redirect('pallet_list')
# #     else:
# #         form = ReceiptForm()
# #     return render(request, 'create_receipt.html', {'form': form})
# def create_receipt(request):
#     if request.method == 'POST':
#         form = ReceiptForm(request.POST)
#         if form.is_valid():
#             pallet = form.save(commit=False)
#             bin_allocation_logic(pallet)
#             pallet.save()
#             return redirect('pallet_list')
#     else:
#         form = ReceiptForm()
#     return render(request, 'create_receipt.html', {'form': form})

# def pallet_list(request):
#     pallets = Pallet.objects.all()
#     return render(request, 'pallet_list.html', {'pallets': pallets})

# # def bin_allocation_logic(pallet):
# #     bin_number = find_bin(pallet)
# #     if bin_number:
# #         pallet.bin_number = bin_number
# #         pallet.status = "Assigned"
# #     else:
# #         pallet.status = "Pending"
        
# def bin_allocation_logic(pallet):
#     bin_number = find_bin(pallet)
#     if bin_number:
#         pallet.bin_number = bin_number
#         pallet.status = "Assigned"
#     else:
#         pallet.status = "Pending"
#     # Save the pallet object after updating status and bin_number
#     pallet.save()

# # def find_bin(pallet):
# #     bins = Bin.objects.filter(current_load__lt=('capacity'))
# #     for bin in bins:
# #         if bin.current_load + pallet.process_order_qty <= bin.capacity:
# #             bin.current_load += pallet.process_order_qty
# #             bin.save()
# #             return bin.bin_number
# #     return None




# def find_bin(pallet):
#     if pallet.capacity is not None:
#         bins = Bin.objects.filter(current_load__lt=pallet.capacity)
#         for bin in bins:
#             if bin.current_load + pallet.process_order_qty <= bin.capacity:
#                 bin.current_load += pallet.process_order_qty
#                 bin.save()
#                 return bin.bin_number
#     return None
