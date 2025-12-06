"""Guwendao Anki integration"""

from guwendao import Client

def main():
    """Main function"""
    client = Client()
    article = client.get_article_from_url("https://www.gushiwen.cn/shiwenv_e0022a7b82a0.aspx")
    article.get_world_explanations()
    


if __name__ == "__main__":
    main()
