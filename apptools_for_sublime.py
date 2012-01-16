import logging
import sublime
import sublime_plugin


class AppToolsForSublime(sublime_plugin.WindowCommand):

    def run_cake_command(self):
        pass

    def output(self):
        pass

    def status(self, message):
        sublime.status_message('AppTools: ' + str(message))

    def run(self, edit=None):
        self.status('COOL, "' + str(self.__class.__.__name__))
        print 'cool'


class AppToolsRunCommand(AppToolsForSublime):

    def run(self):
        self.status('COOL')
        print 'COOL'
        logging.info('COOL')


class AppToolsCompileCommand(AppToolsForSublime):

    def run(self, edit=None):
        self.status('COOL, "' + str(self.__class.__.__name__))
        print 'cool'


class AppToolsServeCommand(AppToolsForSublime):

    def run(self, edit=None):
        self.status('COOL, "' + str(self.__class.__.__name__))
        print 'cool'


class AppToolsUpdateCommand(AppToolsForSublime):

    def run(self, edit=None):
        self.status('COOL, "' + str(self.__class.__.__name__))
        print 'cool'


class AppToolsScaffoldCommand(AppToolsForSublime):

    def run(self, edit=None):
        self.status('COOL, "' + str(self.__class.__.__name__))
        print 'cool'


class AppToolsMinifyCommand(AppToolsForSublime):

    def run(self, edit=None):
        self.status('COOL, "' + str(self.__class.__.__name__))
        print 'cool'
