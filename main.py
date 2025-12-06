"""Guwendao Anki integration"""

from guwendao import Client

def main():
    """Main function"""
    client = Client()
    client.get_article_from_url("https://www.gushiwen.cn/shiwenv_e0022a7b82a0.aspx")


if __name__ == "__main__":
    main()
