from django.contrib import admin
from .models import Post
from .models.comments import Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # فیلدهایی که در لیست کلی پست‌ها نمایش داده می‌شوند
    list_display = ('id', 'user', 'get_caption_preview', 'like_count_display', 'created_at')
    
    # فیلدهایی که در سمت راست برای فیلتر کردن ظاهر می‌شوند
    list_filter = ('created_at', 'user')
    
    # قابلیت جستجو بر اساس شماره موبایل کاربر (چون USERNAME_FIELD شماست) و متن کپشن
    search_fields = ('user__phone_number', 'caption')
    
    # فیلدهایی که فقط خواندنی هستند (مثل زمان ساخت یا propertyها)
    readonly_fields = ('created_at', 'updated_at', 'like_count_display')
    
    # فیلدهایی که در صفحه ایجاد یا ویرایش پست نمایش داده می‌شوند
    fields = ('user', 'img', 'caption', 'like_count_display', 'created_at', 'updated_at')

    # متدی برای نمایش تعداد لایک‌ها در لیست (چون property مستقیماً در list_display نمی‌آید)
    @admin.display(description='Likes')
    def like_count_display(self, obj):
        return obj.like_count

    # متدی برای کوتاه کردن کپشن در لیست ادمین (برای زیبایی ظاهر)
    @admin.display(description='Caption Preview')
    def get_caption_preview(self, obj):
        if obj.caption:
            return obj.caption[:50] + "..." if len(obj.caption) > 50 else obj.caption
        return "-"
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    ...