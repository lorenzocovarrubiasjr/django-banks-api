from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Branch, Employee

# Create your views here.

def api(request):
  branch_query = Branch.objects.all()
  employee_query = Employee.objects.all()
  branches = []
  employees = []
  for branch in branch_query:
    data = {}
    data["id"] = branch.id
    data["address"] = branch.address
    data["city"] = branch.city
    data["state"] = branch.state
    data["zipcode"] = branch.zipcode
    branches.append(data)
  for employee in employee_query:
    data = {}
    data["id"] = employee.id
    data["firstname"] = employee.firstname
    data["lastname"] = employee.lastname
    data["branch_id"] = employee.branch_id
    data["position"] = employee.position
    data["start_date"] = employee.start_date
    employees.append(data)
  return JsonResponse({"Branches": branches, "Employess": employees})

def api_branches(request):
  branch_query = Branch.objects.all()
  branches = []
  for branch in branch_query:
    data = {}
    data["id"] = branch.id
    data["address"] = branch.address
    data["city"] = branch.city
    data["state"] = branch.state
    data["zipcode"] = branch.zipcode
    branches.append(data)
  return JsonResponse({"Branches": branches})

def api_branch(request, id):
  branch_query = Branch.objects.get(id=id)
  branch = [] 
  employee_query = Employee.objects.filter(branch_id=id)
  employees = []
  data = {}
  data["id"] = branch_query.id
  data["address"] = branch_query.address
  data["city"] = branch_query.city
  data["state"] = branch_query.state
  data["zipcode"] = branch_query.zipcode
  branch.append(data)
  for employee in employee_query:
    data = {}
    data["id"] = employee.id
    data["firstname"] = employee.firstname
    data["lastname"] = employee.lastname
    data["branch_id"] = employee.branch_id
    data["position"] = employee.position
    data["start_date"] = employee.start_date
    employees.append(data)
  return JsonResponse({"Branches": branch, "Employess": employees})

def api_branch_new(request, address, city, state, zipcode):
  branch = Branch(address=address, city=city, state=state, zipcode=int(zipcode))
  branch.save()
  print(branch)
  jBranch = []
  data = {}
  data["id"] = branch.id
  data["address"] = branch.address
  data["city"] = branch.city
  data["state"] = branch.state
  data["zipcode"] = branch.zipcode
  jBranch.append(data)
  return JsonResponse({"Branch": jBranch})     

def api_branch_delete(request, id):
  branch = Branch.objects.get(id=id) 
  branch.delete()
  return redirect('api')              

def api_employees(request):
  employee_query = Employee.objects.all()
  employees = []
  for employee in employee_query:
    data = {}
    data["id"] = employee.id
    data["firstname"] = employee.firstname
    data["lastname"] = employee.lastname
    data["branch_id"] = employee.branch_id
    data["position"] = employee.position
    data["start_date"] = employee.start_date
    employees.append(data)
  return JsonResponse({"Employess": employees})

def api_employee_new(request, firstname, lastname, branch_id, position, start_date):
  employee = Employee(firstname=firstname, lastname=lastname, branch_id=int(branch_id), position=position, start_date=start_date)
  employee.save()
  print(employee)
  jemployee = []
  data = {}
  data["id"] = employee.id
  data["firstname"] = employee.firstname
  data["lastname"] = employee.lastname
  data["branch_id"] = employee.branch_id
  data["position"] = employee.position
  data["start_date"] = employee.start_date
  jemployee.append(data)
  return JsonResponse({"employee": jemployee})     

def api_employee_delete(request, id):
  employee = Employee.objects.get(id=id)
  employee.delete()
  return redirect('api') 
  