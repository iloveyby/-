from tkinter import *
from py2fcapi import FCAPI

class Tool_GUI(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # 标题
        self.master.title("凤巢拓词工具内测版本-Felix制作_v0.5")
        # 窗口大小
        self.master.geometry('600x400+500+200')
        # 初始化数据变量
        self.acc = StringVar()
        self.psw = StringVar()
        self.token = StringVar()
        # # 标签
        self.init_data_label = Label(self.master, text="基础信息", font=(
            '微软雅黑', 16), anchor="nw", width=20, height=2).place(x=5, y=5)
        self.init_data_label = Label(
            self.master, text="账号：", font=('微软雅黑', 12)).place(x=5, y=40)
        self.init_data_label = Label(
            self.master, text="密码：", font=('微软雅黑', 12)).place(x=5, y=70)
        self.init_data_label = Label(
            self.master, text="token：", font=('微软雅黑', 12)).place(x=5, y=100)
        self.init_data_label = Label(self.master, text="关键词输入(以回车分割)", font=(
            '微软雅黑', 16), anchor="nw", width=20, height=2).place(x=300, y=5)
        self.init_data_label = Label(self.master, text="拓词数量:", font=(
            '微软雅黑', 12), anchor="nw", width=20, height=2).place(x=300, y=130)
        self.init_data_label = Label(self.master, text="结果", font=(
            '微软雅黑', 14), anchor="nw", width=20, height=2).place(x=5, y=170)
        self.init_data_label = Label(self.master, text="日志", font=(
            '微软雅黑', 14), anchor="nw", width=20, height=2).place(x=300, y=170)
        # 文本框
        self.acc_entry = Entry(
            self.master, textvariable=self.acc).place(x=65, y=40)  # 账号
        self.psw_entry = Entry(
            self.master, textvariable=self.psw, show='*').place(x=65, y=70)  # 密码
        self.token_entry = Entry(
            self.master, textvariable=self.token).place(x=65, y=100)  # token
        self.kws_text = Text(self.master, width=40, height=6)
        self.kws_text.place(x=300, y=40)  # 关键词输入
        # 输出框
        self.output = Text(self.master, height=10, width=40)
        self.output.place(x=5, y=220)
        self.logput = Text(self.master, height=10, width=40)
        self.logput.place(x=300, y=220)
        # 按钮
        self.run = Button(self.master, text="开始拓词",
                          command=self.run).place(x=65, y=130)
        self.out_file = Button(self.master, text="导出文档",
                               command=self.out).place(x=150, y=130)
        # 单选框
        self.maxnum = IntVar()
        self.maxnum.set(100)
        self.ten = Radiobutton(self.master, text="10",
                               value=10, variable=self.maxnum)
        self.hun = Radiobutton(self.master, text="100",
                               value=100, variable=self.maxnum)
        self.tho = Radiobutton(self.master, text="1000",
                               value=1000, variable=self.maxnum)
        self.ten.place(x=380, y=130)
        self.hun.place(x=430, y=130)
        self.tho.place(x=480, y=130)

    def run(self):
        self.acc_get = self.acc.get()
        self.psw_get = self.psw.get()
        self.token_get = self.token.get()
        self.maxnum_get = self.maxnum.get()
        self.kws_get = self.kws_text.get(1.0, END).split('\n')
        a = FCAPI(self.acc_get, self.psw_get,
                  self.token_get, maxnum=self.maxnum_get)
        for i in self.kws_get:
            if len(i) == 0:
                continue
            result = a.getKeywords(i)
            self.logput.insert(1.0, a.status+'\n')
            for r in result:
                self.output.insert(1.0, str(
                    r['word'])+'\t'+str(r['pcPV'])+'\t' + str(r['mobPV'])+'\t'+str(r['pv'])+'\n')

    def out(self):
        from tkinter import filedialog, dialog
        file_path = filedialog.asksaveasfilename(title=u'保存文件')
        file_text = self.output.get('1.0', END)
        if file_path is not None:
            with open(file=file_path, mode='a+', encoding='utf-8') as file:
                file.write('word'+'\t'+'pcPV'+'\t'+'mobPV'+'\t'+'totalPV'+'\n')
                file.write(file_text)
            dialog.Dialog(None, {'title': 'File Modified', 'text': '保存完成', 'bitmap': 'warning', 'default': 0,
                                 'strings': 'OK'})


if __name__ == "__main__":
    app = Tk()
    gui = Tool_GUI(master=app)
    app.mainloop()
