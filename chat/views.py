# chatbot_app/views.py
from rest_framework.response import Response
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from chatterbot.ext.django_chatterbot import settings
from rest_framework.decorators import api_view
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

chatbot = ChatBot('Chat1', read_only=False, 
              logic_adapters=[
                  {
                      'import_path':'chatterbot.logic.BestMatch',
                      'default_response':'Xin lỗi, tôi chưa hiểu ý của bạn',
                      'maximum_similarity_threshold':0.85
                   }])

trainer = ListTrainer(chatbot)

# Đọc dữ liệu từ tệp văn bản
file_path = 'chat/data.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.read().split('---')

# Xử lý từng cặp câu hỏi và câu trả lời
for pair in lines:
    conversation = pair.strip().split('\n')
    question = conversation[0]
    answers = conversation[1:]

    # Đảm bảo sử dụng toàn bộ nội dung của câu trả lời
    response = ' '.join(answers)
    trainer.train([question, response])


@api_view(['POST'])
def chatbot_api(request):
    # Nhận dữ liệu đầu vào từ yêu cầu POST
    data = request.data
    user_input = data.get('message')

    # Sử dụng chatbot để nhận câu trả lời
    response = chatbot.get_response(user_input)

    # Trả về câu trả lời dưới dạng JSON
    return Response({'message': str(response)})