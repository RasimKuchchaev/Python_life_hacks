import re
import xlsxwriter

FILE = 'spy.csv'
XLSX = 'spy.xlsx'
COUNT_STOCKS = 100
INF = 0.025


def analysis(file):
    handle = open(file)
    lines = handle.readlines()
    handle.close()
    lines.reverse()
    years = {}
    for line in lines:
        matches = re.findall(r'(\d{4})-\d{2}-\d{2}\s*Dividend\s*\$(\d+\.\d+)\s*', line)
        year = int(matches[0][0])
        amount = float(matches[0][1])
        if year not in years:
            years[year] = [0.0, 0.0, 0.0]
        years[year][0] += amount

    total_inf = 1
    old = []
    for year in years:
        if len(old):
            years[year][1] = round((years[year][0] / old[0] - 1) * 100, 2)
        years[year][2] = round(COUNT_STOCKS * years[year][0] * total_inf, 2)
        old = years[year]
        total_inf *= (1 - INF)
    create_report(years)


def create_report(years):
    workbook = xlsxwriter.Workbook(XLSX)
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': True})
    bold.set_align('center')
    center = workbook.add_format({'align': 'center'})
    worksheet.set_column('B:C', 20)
    worksheet.set_column('D:D', 50)
    worksheet.write('A1', 'Год', bold)
    worksheet.write('B1', 'Сумма', bold)
    worksheet.write('C1', 'Рост в процентах', bold)
    worksheet.write('D1', 'Сумма с учётом инфляции (' + str(INF * 100) + '%) на ' + str(COUNT_STOCKS) + ' акц.', bold)

    row = 2
    for year in years:
        worksheet.write('A' + str(row), year, center)
        worksheet.write('B' + str(row), '$' + str(round(years[year][0], 2)), center)
        worksheet.write('C' + str(row), str(years[year][1]) + '%', center)
        worksheet.write('D' + str(row), '$' + str(years[year][2]), center)
        row += 1

    workbook.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    analysis(FILE)

