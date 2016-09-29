# percol configuration
# https://github.com/mooz/percol

# percol.view.PROMPT  = ur"<bold><yellow>X / _ / X</yellow></bold> %q"
# percol.view.PROMPT = ur"<cyan>Input:</cyan> %q"
# Change prompt in response to the status of case sensitivity
percol.view.__class__.PROMPT = property(
    lambda self:
    ur"<bold><yellow>X / _ / X</yellow> [a]</bold> %q" if percol.model.finder.case_insensitive
    else ur"<bold><green>X / _ / X</green> [A]</bold> %q"
)

# Display finder name in RPROMPT
percol.view.prompt_replacees["F"] = lambda self, **args: self.model.finder.get_name()
percol.view.RPROMPT = ur"(%F) [%i/%I]"

# Customizing colors
percol.view.CANDIDATES_LINE_BASIC    = ("on_default", "default")
percol.view.CANDIDATES_LINE_SELECTED = ("bold", "on_blue", "white")
percol.view.CANDIDATES_LINE_MARKED   = ("bold", "on_cyan", "black")
percol.view.CANDIDATES_LINE_QUERY    = ("yellow", "bold")

# Emacs like
percol.import_keymap({
    "C-h" : lambda percol: percol.command.delete_backward_char(),
    "C-d" : lambda percol: percol.command.delete_forward_char(),
    "C-k" : lambda percol: percol.command.kill_end_of_line(),
    "C-y" : lambda percol: percol.command.yank(),
    "C-a" : lambda percol: percol.command.beginning_of_line(),
    "C-e" : lambda percol: percol.command.end_of_line(),
    "C-b" : lambda percol: percol.command.backward_char(),
    "C-f" : lambda percol: percol.command.forward_char(),
    "C-n" : lambda percol: percol.command.select_next(),
    "C-p" : lambda percol: percol.command.select_previous(),
    "C-v" : lambda percol: percol.command.select_next_page(),
    "M-v" : lambda percol: percol.command.select_previous_page(),
    "M-<" : lambda percol: percol.command.select_top(),
    "M->" : lambda percol: percol.command.select_bottom(),
    "C-x" : lambda percol: percol.command.toggle_mark_all(),
    "C-m" : lambda percol: percol.finish(),
    "C-j" : lambda percol: percol.finish(),
    "C-g" : lambda percol: percol.cancel(),
})

# Matching method can be switched dynamically (at run time) by executing
# percol.command.specify_finder(FinderClass) or percol.command.toggle_finder(FinderClass).
# In addition, percol.command.specify_case_sensitive(case_sensitive) and
# percol.command.toggle_case_sensitive() change the matching status of case
# sensitivity.
from percol.finder import FinderMultiQueryRegex
percol.import_keymap({
    "M-c" : lambda percol: percol.command.toggle_case_sensitive(),
    "M-r" : lambda percol: percol.command.toggle_finder(FinderMultiQueryRegex)
})
