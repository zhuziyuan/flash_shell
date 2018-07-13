# coding: utf-8
from flask import Flask
from flask import render_template, request
import ansible.runner
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        cmd = request.form.get('cmd', type=str, default=None)
        ip = request.form.get('ip', type=str, default=None)
        host_cfg = os.path.join(BASE_DIR, 'host.cfg')
        print cmd, ip, host_cfg
        # 1 or None None or 1
        # 1 and None None or 1
        # if cmd or ip:
        # 对比结果
        if cmd and ip:
            runner = ansible.runner.Runner(
                host_list=os.path.join(BASE_DIR, host_cfg),
                module_name='shell',
                module_args=cmd,
                pattern=ip,
                forks=10
            )
            datastructure = runner.run()
            for key, value in datastructure.items():
                if 'contacted' in key:
                    exec_result = value
            return render_template('index.html', result=exec_result, ip=ip, cmd=cmd)
        else:
            return render_template('index.html')
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)
