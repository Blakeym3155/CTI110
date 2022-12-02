text = str(input())
end_text = ['done', 'd', 'Done']
while text not in end_text:
    print(text[::-1])
    text = str(input())