from cudatext import *

class Command:
    
    def __init__(self):
        self.what = [
            'Python 3.',
            'Loading project: ',
            'Startup: ',
            'Tab Icons: ',
            "Detect Indent for '",
        ]

    def run(self):
        hcons = app_proc(PROC_GET_CONSOLE_FORM, '')
        h_in = dlg_proc(hcons, DLG_CTL_HANDLE, name='memo')
        memo = Editor(h_in)
        
        to_remove = []
        
        for line in range(memo.get_line_count()):
            s = memo.get_text_line(line)
            if [w for w in self.what if s.startswith(w)]:
                to_remove.append(line)
                
        memo.set_prop(PROP_RO, False)
        
        for line in reversed(range(memo.get_line_count())):
            if line in to_remove:
                memo.replace_lines(line, line, [])
        
        memo.set_prop(PROP_RO, True)

    def on_start2(self, ed_self):
        self.run()
        timer_proc(TIMER_START, lambda _: self.run(), 1000)

