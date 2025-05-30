from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SavedCode
from .serializers import SavedCodeSerializer
import subprocess
import tempfile

@api_view(["POST"])
def run_code(request):
    code = request.data.get("code")
    user_input = request.data.get("input", "")

    try:
        # Save the code temporarily
        with tempfile.NamedTemporaryFile(suffix=".py", mode='w+', delete=False) as tmp_file:
            tmp_file.write(code)
            tmp_file.flush()

            # Run the code with input using subprocess
            process = subprocess.run(
                ["python", tmp_file.name],
                input=user_input,
                capture_output=True,
                text=True,
                timeout=5,
            )

        output = process.stdout + process.stderr
        return Response({"output": output})
    except Exception as e:
        return Response({"output": f"Error: {str(e)}"})


@api_view(["POST"])
def save_code(request):
    title = request.data.get("title", "Untitled")
    code = request.data.get("code", "")
    input_data = request.data.get("input", "")

    saved = SavedCode.objects.create(
        title=title,
        code=code,
        input_data=input_data
    )
    return Response({"message": "Code saved successfully", "id": saved.id})

@api_view(["GET"])
def get_saved_codes(request):
    codes = SavedCode.objects.all().order_by('-created_at')  # latest first
    serializer = SavedCodeSerializer(codes, many=True)
    return Response(serializer.data)
