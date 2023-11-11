class printcolor():
    @staticmethod
    def print_red(text):
        """赤い文字でテキストを出力"""
        red_text = f"\033[31m{text}\033[0m"  # ANSIエスケープコードを使って赤文字に設定
        print(red_text)

    @staticmethod
    def print_green(text):
        """緑の文字でテキストを出力"""
        green_text = f"\033[32m{text}\033[0m"  # ANSIエスケープコードを使って緑文字に設定
        print(green_text)

    @staticmethod
    def print_yellow(text):
        """黄の文字でテキストを出力"""
        yellow_text = f"\033[33m{text}\033[0m"  # ANSIエスケープコードを使って黄文字に設定
        print(yellow_text)

    @staticmethod
    def print_blue(text):
        """青の文字でテキストを出力"""
        blue_text = f"\033[34m{text}\033[0m"  # ANSIエスケープコードを使って青文字に設定
        print(blue_text)

    @staticmethod
    def print_magenta(text):
        """マゼンタの文字でテキストを出力"""
        magenta_text = f"\033[35m{text}\033[0m"  # ANSIエスケープコードを使ってマゼンタ文字に設定
        print(magenta_text)

    @staticmethod
    def print_cyan(text):
        """シアンの文字でテキストを出力"""
        cyan_text = f"\033[36m{text}\033[0m"  # ANSIエスケープコードを使ってシアン文字に設定
        print(cyan_text)

    @staticmethod
    def print_white(text):
        """白の文字でテキストを出力"""
        white_text = f"\033[37m{text}\033[0m"  # ANSIエスケープコードを使って白文字に設定
        print(white_text)

    @staticmethod
    def print_black(text):
        """黒の文字でテキストを出力"""
        black_text = f"\033[30m{text}\033[0m"  # ANSIエスケープコードを使って黒文字に設定
        print(black_text)

    @staticmethod
    def print_bright_red(text):
        """明るい赤の文字でテキストを出力"""
        bright_red_text = f"\033[91m{text}\033[0m"  # ANSIエスケープコードを使って明るい赤文字に設定
        print(bright_red_text)

    @staticmethod
    def print_bright_green(text):
        """明るい緑の文字でテキストを出力"""
        bright_green_text = f"\033[92m{text}\033[0m"  # ANSIエスケープコードを使って明るい緑文字に設定
        print(bright_green_text)

    @staticmethod
    def print_bright_yellow(text):
        """明るい黄の文字でテキストを出力"""
        bright_yellow_text = f"\033[93m{text}\033[0m"  # ANSIエスケープコードを使って明るい黄文字に設定
        print(bright_yellow_text)

    @staticmethod
    def print_bright_blue(text):
        """明るい青の文字でテキストを出力"""
        bright_blue_text = f"\033[94m{text}\033[0m"  # ANSIエスケープコードを使って明るい青文字に設定
        print(bright_blue_text)

    @staticmethod
    def print_bright_magenta(text):
        """明るいマゼンタの文字でテキストを出力"""
        bright_magenta_text = f"\033[95m{text}\033[0m"  # ANSIエスケープコードを使って明るいマゼンタ文字に設定
        print(bright_magenta_text)

    @staticmethod
    def print_bright_cyan(text):
        """明るいシアンの文字でテキストを出力"""
        bright_cyan_text = f"\033[96m{text}\033[0m"  # ANSIエスケープコードを使って明るいシアン文字に設定
        print(bright_cyan_text)

    @staticmethod
    def print_bright_white(text):
        """明るい白の文字でテキストを出力"""
        bright_white_text = f"\033[97m{text}\033[0m"  #ANSIエスケープコードを使って明るい白文字に設定
        print(bright_white_text)

    @staticmethod
    def print_dark_black(text):
        """暗い黒の文字でテキストを出力"""
        dark_black_text = f"\033[90m{text}\033[0m"  # ANSIエスケープコードを使って暗い黒文字に設定
        print(dark_black_text)