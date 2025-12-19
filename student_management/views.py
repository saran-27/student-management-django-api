from django.db.models.expressions import result
from .models import StudentPerformance
from .serializer import Student_serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')

class RankApi(APIView):

    def post(self,request):

        tamil=int(request.data['tamil'])
        english = int(request.data['english'])
        maths = int(request.data['maths'])
        science = int(request.data['science'])
        computer = int(request.data['computer'])

        total_mark = tamil+english+maths+science+computer

        average_mark=total_mark/5

        if tamil>=35 and english>=35 and maths>=35 and science>=35 and computer>=35:

            result="pass"
        else:
            result="Fail"

        all_cal=StudentPerformance(student_name=request.data["student_name"],tamil=tamil,english=english,maths=maths
                                   ,science=science,computer=computer,total=total_mark,average=average_mark,
                                   result=result)

        all_cal.save()

        return Response({
            "total":total_mark,
            "average":average_mark,
            "result":result
        })

    def get(self,request,id=None):


        if (id==None):
            all_rank = StudentPerformance.objects.all()

            new_rank=Student_serializer(all_rank,many=True).data

            return Response(new_rank)
        else:

            rank=StudentPerformance.objects.get(id=id)

            new_rank=Student_serializer(rank).data

            return Response(new_rank)

    def put(self,request,id=None):


        update_mark=StudentPerformance.objects.get(id=id)

        tamil = int(request.data['tamil'])
        english = int(request.data['english'])
        maths = int(request.data['maths'])
        science = int(request.data['science'])
        computer = int(request.data['computer'])

        total_mark = tamil + english + maths + science + computer

        average_mark = total_mark / 5

        if tamil >= 35 and english >= 35 and maths >= 35 and science >= 35 and computer >= 35:

            result = "pass"
        else:
            result = "Fail"

        update_mark.student_name=request.data["student_name"]
        update_mark.tamil = tamil
        update_mark.english = english
        update_mark.maths = maths
        update_mark.science = science
        update_mark.computer = computer
        update_mark.result = result
        update_mark.average = average_mark
        update_mark.total = total_mark


        update_mark.save()

        return Response({
            "message": "Updated successfully",
            "total": total_mark,
            "average": average_mark,
            "result": result
        })

    def delete(self,request,id=None):
        remove_data=StudentPerformance.objects.get(id=id)

        remove_data.delete()

        return  Response("Your Rank deleted")
