from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from csvapp.serializers import UserSerializer
import csv
import io


class UserCsvView(APIView):
    def get(self, request):
        try:
            queryset = get_user_model().objects.all()
            serializer = UserSerializer(queryset, many=True)
            data = serializer.data

            # Writing the csv data to a string buffer
            csv_buffer = io.StringIO()
            writer = csv.DictWriter(csv_buffer, fieldnames=data[0].keys())
            writer.writeheader()
            for row in data:
                writer.writerow(row)

            # Create the HTTP response with CSV content and set Content-Disposition header
            response = HttpResponse(csv_buffer.getvalue(), content_type="text/csv")
            response["Content-Disposition"] = "attachment; filename=data.csv"

            return response

        except Exception as e:
            return HttpResponse("An error occurred during loading process", status=500)


