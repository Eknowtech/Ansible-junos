import xlsxwriter



file = open("Result/Hynix_cj_summary.txt", 'r')
data = file.readlines()
workbook = xlsxwriter.Workbook('Result/Hynix_cj_result.xlsx')
worksheet = workbook.add_worksheet('Result')

row = 1
col = 0
worksheet.write(0, 0, 'Hostname')
worksheet.write(0, 1, 'IP')
worksheet.write(0, 2, 'Model')
worksheet.write(0, 3, 'Serial')
worksheet.write(0, 4, 'Memory')
worksheet.write(0, 5, 'CPU')
worksheet.write(0, 6, 'Module')
worksheet.write(0, 7, 'Power')
worksheet.write(0, 8, 'Fan')
worksheet.write(0, 9, 'Interface')
worksheet.write(0, 10, 'Version')
worksheet.write(0, 11, 'Log 및특이사항')
worksheet.write(0, 12, '점검결과')


for i in data:
    for j in i.split('|'):
        worksheet.write(row, col, j)
        col += 1
    col = 0
    row += 1


workbook.close()
