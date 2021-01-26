letter = ['a','b','c','d','e','f','g',
'h','i','j','k','l','m','n','o','p','q','r',
's','t','u','v','w','x','y','z','a','b','c','d','e','f','g',
'h','i','j','k','l','m','n','o','p','q','r',
's','t','u','v','w','x','y','z']


guide_start = input("What do you want to,'encode' or 'decode?:\n")
text        = input("Type your message:\n").lower()
shift       = int(input("choose the change number:\n"))

# def encryption(want_en, number_to):
#     create_text = ""
#     for n in want_en:
#         ori_position = letter.index(n)
#         new_position = ori_position + number_to
#         new_letters  = letter[new_position]
#         create_text += new_letters
#     return(f"the encryword: {create_text}")
# def decodence(want_de, number_de):
#     deco_text = ""
#     for n in want_de:
#         ori_position = letter.index(n)
#         new_position = ori_position - number_de
#         new_letters  = letter[new_position]
#         deco_text   += new_letters
#     return(f"the decryword: {deco_text}")
def all_code(enter_text, choose_num, guide):
    the_text = ""
    for n in enter_text:
        posit = letter.index(n)
        if guide == "decode":
            choose_num = - abs(choose_num)
        new_posit = posit + choose_num
        the_text += letter[new_posit]
    print(f'The {guide_start} text is {the_text}')

all_code(enter_text=text, choose_num=shift, guide=guide_start)

# if guide_start == "encode":
#     en = encryption(want_en=text, number_to=shift)
#     print(en)
# elif guide_start == "decode":
#     de = decodence(want_de=text, number_de=shift)
#     print(de)
# else:
#     print("system wrong")
#     quit()


# def all_code(enter_text, choose_num, guide):
#     the_text = ""
#     for n in enter_text:
#         posit = letter.index(n)
#         if guide == "decode":
#             choose_num *= -1
#         new_posit = posit + choose_num
#         the_text += letter[new_posit]
#     print(f'The {guide_start} text is {the_text}')

# all_code(enter_text=text, choose_num=shift, guide=guide_start)

