# MSA_Docker_SEL
محمد نامدار، حمیدرضا دهباشی

# طرح مسئله

در این آزمایش تصمیم گرفتیم تا ذخیره، بروزرسانی و حذف کتاب ها را به صورت میکروسرویس پیاده سازی کنیم.

ساختار کلی سیستم به این صورت است که درخواست هایی که از سوی کلاینت ها می آید به وسیله یک load balancer (در اینجا از nginx استفاده کردیم) بین 3 کانتینر مربوط به backend تقسیم می شوند و پس از پردازش اطلاعات در هر backend، تغییرات مربوطه در دیتابیس صورت می گیرد. هر کانتینر backend به دیتابیس متصل است و برای دیتابیس از postgre استفاده کردیم (همان image مربوط به postgre که در docker-hub موجود بود).

روند پیاده سازی به این صورت بود که ابتدا یک سیستم backend را به صورت مینیمال پیاده سازی کردیم. سپس برای تست این قسمت backend یک نمونه دیتابیس را بالا آوردیم. 

در قسمت بعدی برای تنظیمات load balancing از nginx استفاده کردیم و در کانفیگ مربوط به آن اطلاعات الگوریتم load balancing و backend هایی را که میخواهیم load balancing روی آنها انجام شود، وارد کردیم.

در گام بعدی، Dockerfile های مربوط به backend و nginx را نوشتیم.

و در انتها نیز docker-compose را تکمیل کردیم و اجزای مختلف سیستم را و ارتباطات و dependency ها را در آن قرار دادیم. سپس docker-compose را اجرا کردیم.

![image](https://github.com/MoNam97/MSA_Docker_SEL/blob/main/images/docker-compose1.PNG)

![image](https://github.com/MoNam97/MSA_Docker_SEL/blob/main/images/docker-compose2.PNG)

تصویر مربوط  به وجود image ها و container های خواسته شده توسط گزارش در زیر آورده شده است:

![image](https://github.com/MoNam97/MSA_Docker_SEL/blob/main/images/command1.PNG)

![image](https://github.com/MoNam97/MSA_Docker_SEL/blob/main/images/command2.PNG)

همچنین تست هایی را نیز در رابطه با عملیات های متفاوت در سیستم انجام دادیم و تصاویر و توضیحات مربوط به آن ها در زیر آورده شده است.
- ابتدا دو کتاب اضافه کردیم و لیست تمامی کتاب ها را Get کردیم.

 ![image](https://github.com/MoNam97/MSA_Docker_SEL/blob/main/images/test_create.PNG)

 ![image](https://github.com/MoNam97/MSA_Docker_SEL/blob/main/images/test_create2.PNG)
 
- مقادیر مربوط به یک کتاب را تغییر دادیم و لیست تمامی کتابها را مشاهده کردیم.
 
  ![image](https://github.com/MoNam97/MSA_Docker_SEL/blob/main/images/test_update.PNG)
  
- یک کتاب را حذف کردیم و لیست تمامی کتاب ها را مشاهده کردیم.

 ![image](https://github.com/MoNam97/MSA_Docker_SEL/blob/main/images/test_delete1.PNG)

 ![image](https://github.com/MoNam97/MSA_Docker_SEL/blob/main/images/test_delete2.PNG)

همانطور که در تصاویر مشخص است روند اجرای برنامه صحیح است.
همچنین راجع به load-balancing، از یک url مخصوص استفاده کردیم /test و همانطور که در تصویرهای زیر مشخص است با هر دفعه reload پاسخی که دریافت می¬کنیم از یک backend متفاوت است و این به این معناست که load balancing به درستی انجام می شود.

![image](https://github.com/MoNam97/MSA_Docker_SEL/blob/main/images/load-balanser1.PNG)

![image](https://github.com/MoNam97/MSA_Docker_SEL/blob/main/images/load-balanser2.PNG)

![image](https://github.com/MoNam97/MSA_Docker_SEL/blob/main/images/load-balanser3.PNG)


در رابطه با مورد 6، پاسخ به این صورت خواهد بود که باید مکانیزمی تعریف شود که طی آن فشار بر روی سرورها توزیع شود اما تمامی سرور ها از یک دیتابیس استفاده کنند. به این منظور مانند سیستم پیاده سازی شده در این آزمایش باید از یک load balancer استفاده کنیم تا درخواست ها را میان سرور ها تقسیم کند و هر سرور درخواست های دیتابیسی خود را به یک دیتابیس مشترک ارائه کند. مابقی اتفاقات از قبیل هندل کردن کانکرنسی connection های دیتابیس در خود دیتابیس ها در نظر گرفته خواهد شد.
