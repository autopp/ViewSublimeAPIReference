import sublime, sublime_plugin
import webbrowser

class ViewSublimeReferenceCommand(sublime_plugin.WindowCommand):
  def run(self):
    setting = sublime.load_settings("ViewSublimeAPIReference.sublime-settings")
    
    self.items = setting.get("item")
    print(self.items)
    self.window.show_quick_panel(self.items, self.on_done)

  def on_done(self, i):
    if i < 0:
      return
      
    item = self.items[i]
    webbrowser.open_new_tab("http://www.sublimetext.com/docs/3/api_reference.html#" + item)
    
