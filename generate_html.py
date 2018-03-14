import sys, sqlite3

def fixed_part1():
    print("""<!DOCTYPE html>
<html>
<head>
    <title>Atcoder Finder</title>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/semantic-ui@2.3.0/dist/semantic.min.css">
    <script src="https://cdn.jsdelivr.net/npm/jquery@3.3.1/dist/jquery.min.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/semantic-ui@2.3.0/dist/semantic.min.js"></script>
    <script defer src="https://use.fontawesome.com/releases/v5.0.8/js/all.js"></script>
    <script src="./js/filter.js"></script>
    <link rel="stylesheet" href="./css/style.css">
</head>
<body>
    <div class="ui inverted menu">
        <a class="active item">
            <h3>Atcoder Finder</h3>
        </a>
    </div>
    <div class="ui container">""")

def filter():
    print("        <h4 class='ui top attached header'>タグを選ぶ</h4>")
    print("        <div class='ui attached segment'>")
    print("            <div class='filter-container'>")
    print("                <div class='filters ui form'>")
    print("                    <div class='inline fields'>")

    tags = ['グラフ', '数論', '幾何', '動的計画法', 'データ構造', '文字列', '確率・組合せ', 'ゲーム', 'その他']
    print("                        <div class='field'>")
    print("                            <div class='ui radio checkbox'>")
    print("                                <input type='radio' autocomplete='off' class='filter' name='タグ' placeholder='タグ' value=''><label>すべて</label>")
    print("                            </div>")
    print("                        </div>")
    for tag in tags:
        print("                        <div class='field'>")
        print("                            <div class='ui radio checkbox'>")
        print("                                <input type='radio' autocomplete='off' class='filter' name='タグ' placeholder='タグ' value='" + tag + "'><label>" + tag + "</label>")
        print("                            </div>")
        print("                        </div>")
    print("                    </div>")
    print("                </div>")
    print("            </div>")
    print("        </div>")

def table(type):
    if type == 0:
        print("        <h3 class='ui block header'>Atcoder Grand Contest</h3>")
    elif type == 1:
        print("        <h3 class='ui block header'>Atcoder Beginner Contest</h3>")
    elif type == 2:
        print("        <h3 class='ui block header'>Atcoder Regular Contest</h3>")

    print("""        <table class="ui striped table">
            <thead>
                <tr>
                    <th>問題番号</th>
                    <th>問題名</th>
                    <th>タグ</th>
                </tr>
            </thead>""")
    print("            <tbody>")


    sql = sqlite3.connect('./database/problems.db')
    cur = sql.cursor()
    if type == 0:
        cur.execute("SELECT * FROM sqlite_master where type='table' and name='AGC'")
        ok = cur.fetchone()
        if ok != None:
            cur.execute('select * from AGC')
    elif type == 1:
        cur.execute("SELECT * FROM sqlite_master where type='table' and name='ABC'")
        ok = cur.fetchone()
        if ok != None:
            cur.execute('select * from ABC')
    else:
        cur.execute("SELECT * FROM sqlite_master where type='table' and name='ARC'")
        ok = cur.fetchone()
        if ok != None:
            cur.execute('select * from ARC')
    res = cur.fetchall()
    for row in res:
        print('                <tr>')
        print('                    <td>' + row[0] + '</td>')
        print('                    <td><a href="' + row[2] + '">' + row[1] + '</a></td>')
        print('                    <td>' + row[3] + '</td>')
        print('                </tr>')
    cur.close()
    sql.close()

    print("            </tbody>")
    print("        </table>")

def fixed_part2():
    print("""    </div>
    <div class="ui inverted vertical footer segment">
        <div class="ui center aligned container">
            <h4 class="ui inverted header">Created by Koki Yamaguchi</h4>
            <p>Twitter @Ymgch_K</p>
        </div>
    </div>
</body>
</html>""")

def generate():
    file = open("index.html", "w")
    sys.stdout = file
    fixed_part1()
    filter()
    table(0)
    table(1)
    table(2)
    fixed_part2()
    sys.stdout = sys.__stdout__

if __name__ == '__main__':
    generate()
