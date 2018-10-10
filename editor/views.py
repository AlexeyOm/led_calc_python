from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import permission_required
#from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Vendor
from .models import Cabinet
from .forms import CabinetForm
from .serializers import cabinet_serializer

@permission_required('cabinet.can_add', login_url='/loginpage/')
def editor_main(request):
    vendors = Vendor.objects.all()
    return render(request, 'editor/main.html', {'vendors': vendors})


@permission_required('cabinet.can_add', login_url='/loginpage/')
def cabinets(request, pk):
    cabinets = Cabinet.objects.filter(vendor = pk)
    return render(request, 'editor/cabinets.html', {'cabinets': cabinets})

@permission_required('cabinet.can_add', login_url='/loginpage/')
def cabinet_editor(request, pk):
    cabinet = get_object_or_404(Cabinet, pk=pk)
    if request.method == "POST":
        form = CabinetForm(request.POST, instance = cabinet)
        if form.is_valid():
            cabinet = form.save(commit=False)
            cabinet.author = request.user
            cabinet.save()
            return redirect('cabinets', pk=Vendor.objects.get(brand=cabinet.vendor).pk)
    else:
        form = CabinetForm(instance=cabinet)
        return render(request, 'editor/cabinet_editor.html', {'form': form})

@permission_required('cabinet.can_add', login_url='/loginpage/')
def cabinet_add(request):
    if request.method == "POST":
        form = CabinetForm(request.POST)
        if form.is_valid():
            cabinet = form.save(commit=False)
            cabinet.author = request.user
            cabinet.save()
            return redirect('cabinets', pk=Vendor.objects.get(brand=cabinet.vendor).pk)
    else:
        form = CabinetForm()
        return render(request, 'editor/cabinet_editor.html', {'form': form})



@api_view(['GET'])
def get_data(request):
    if request.user.has_perm('cabinet.can_view'):
        queryset = Cabinet.objects.all()
        serializer = cabinet_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({}, status=status.HTTP_401_UNAUTHORIZED)