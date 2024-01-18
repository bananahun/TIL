# 아래에 코드를 작성하시오.
import settings
import create_url

settings.NAME
settings.MAIN_URL

result = create_url.create_url(settings.NAME,settings.MAIN_URL,page_num=1)
print(result)