def main():
    file_edit = 'r'
    main_input = ''
    method = input('Read or write to file? (Default is read) ')

    if method == 'read' or method == 'r':
        file_edit = 'r'
    elif method == 'write' or method == 'w':
        file_edit = 'w'
        main_input = input('Enter your text: ')
    else:
        print('Your input is incorrect! Default: Read File')

    directory = input('Enter the directory: ')
    file_name = input('Enter the filename (leave blank to create a new file called output) : ')
    try:
        if file_name == '':
            if file_edit == 'r':
                print('Cannot read empty file!')
            elif file_edit == 'w':
                file_object = open(f'{directory}\\output.txt', 'w')
                file_object.write(main_input)
                file_object.close()
                print(
                    f'output.txt created and your text has been written to that file! If output.txt existed before then your text has been overwritten')
        else:
            if file_edit == 'r':
                file_object = open(f'{directory}\\{file_name}.txt', 'r')
                file_content = file_object.read()
                file_object.close()
                print(f'File reads: {file_content}')
            elif file_edit == 'w':
                file_object = open(f'{directory}\\{file_name}.txt', 'w')
                file_object.write(main_input)
                file_object.close()
                print('Text written to file!')

    except Exception as e:
        print(f'Something went wrong! Check your text or directory inputs.\nError Details: {e}')


while True:
    main()
    cancel_confirm = input('Type exit to exit or press enter to continue ')
    if cancel_confirm == 'exit':
        break
    else:
        pass
