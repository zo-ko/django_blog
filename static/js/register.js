$(function() {
    // 1. 正确声明函数
    function bindCaptchaBtnClick() {
        $("#captcha_button").click(function(event) {
            let $this = $(this);
            let email = $("input[name='email']").val();
            
            if(!email) {
                alert("请先输入邮箱！");
                return;
            }
            
            // 2. 禁用按钮，并防止重复点击 (更优做法)
            $this.prop('disabled', true);
            $.ajax({
                url: '/user/send_email?email=' + encodeURIComponent(email), // 编码邮箱参数
                method: 'GET',
                success: function (result) {
                    console.log('验证码发送成功:', result);
                    // 在这里处理成功响应，例如开始倒计时
                },
                error: function (xhr, status, error) {
                    console.error('验证码发送失败:', status, error);
                    // 在这里处理错误，例如提示用户
                    if (xhr.status === 400) {
                        alert('请求参数错误');
                    } else if (xhr.status === 429) {
                        alert('请求过于频繁，请稍后再试');
                    } else {
                        alert('网络错误，请稍后重试');
                    }
                }
            })
            
            // 3. 开始倒计时
            let countdown = 6;
            let timer = setInterval(function() {
                if(countdown <= 0) {
                    // 倒计时结束：恢复按钮文本和状态
                    $this.text('获取验证码').prop('disabled', false);
                    clearInterval(timer);
                    // 注意：这里不需要重新绑定事件！
                } else {
                    $this.text(countdown + 's');
                    countdown--;
                }
            }, 1000);
            
            // 4. 【重要】这里应该发送AJAX请求到你的后端
            // $.ajax({
            //     url: '/your-captcha-api/',
            //     method: 'POST',
            //     data: { email: email },
            //     success: function(response) {
            //         console.log('验证码发送成功');
            //     },
            //     error: function(xhr) {
            //         alert('发送失败: ' + (xhr.responseJSON?.message || '请稍后重试'));
            //         // 出错时立即恢复按钮
            //         clearInterval(timer);
            //         $this.text('获取验证码').prop('disabled', false);
            //     }
            // });
        });
    }
    
    // 初始绑定一次即可
    bindCaptchaBtnClick();
});