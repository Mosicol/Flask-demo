
from wtforms import Form,StringField,IntegerField,BooleanField,SelectField
from wtforms.validators import Length,EqualTo,Email,InputRequired,NumberRange
from wtforms.validators import Regexp,URL,ValidationError

class RegistForm(Form):
    username = StringField(validators=[Length(min=3,max=10,message='用户名必须在3到10位之间')])
    password = StringField(validators=[Length(min=6,max=10,message='密码必须6到10位之间')])
    password_repeat = StringField(validators=[Length(min=6,max=10),
                                              EqualTo("password",message='密码不一致')])


class LoginForm(Form):
    email = StringField(validators=[Email(message='邮箱格式不正确')])
    username = StringField(validators=[InputRequired(message='这个字段必须要填')])
    age = IntegerField(validators=[NumberRange(min=18,max=100)])
    phone = StringField(validators=[Regexp(r'1[38745]\d{9}')])
    homepage = StringField(validators=[URL()])
    captcha = StringField(validators=[Length(4,4)])

    # 自定义验证器
    def validate_captcha(self,field):
        if field.data != '1234':      #field.data：用户提交过来的数据
            raise ValidationError('验证码错误')          #如果验证失败，就抛出验证失败的异常


class SettingsForm(Form):
    username = StringField(label="用户名：",validators=[InputRequired(message='这个字段必须要填')])
    age = IntegerField('年龄:',validators=[NumberRange(min=18, max=100)])
    remeber = BooleanField('记住我')
    tags = SelectField('标签',choices=[(1,'python'),(2,'django')])
