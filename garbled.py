garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
first_word = garbled[:15:-2]
second_word = garbled [18:29:-2]
third_word = garbled[-11:-16:2]
fourth_word = garbled[-5:-8:2]
fifth_word = garbled[-1]

message = fifth_word +" "+ fourth_word +" "+ third_word +" "+ second_word +" "+ first_word