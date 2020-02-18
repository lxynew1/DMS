from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, SelectField
from wtforms.validators import Required, Length, Email, DataRequired
from ..models import LAND_SELL_INFO, DICT_REGION, DICT_LAND_USE
import datetime

year = str(datetime.datetime.now().year)
month = str(datetime.datetime.now().month)
day = str(datetime.datetime.now().day)
detester_e = year + '-' + month + '-' + day
detester_s = year + '-01-01'
date_s = datetime.datetime.strptime(detester_s, '%Y-%m-%d')
date_e = datetime.datetime.strptime(detester_e, '%Y-%m-%d')

years = [("全部", "全部")]
a = int(year) - 5
a1 = int(year) + 5
while a <= a1:
    years.extend([(a, a)])
    a = a + 1


class LandSellSearch(Form):
    start = DateField('DatePicker', format='%Y-%m-%d', default=date_s)
    end = DateField('DatePicker', format='%Y-%m-%d', default=date_e)
    land_location = SelectField(
        validators=[DataRequired("请选择土地坐落")],
        default='全部'
    )
    assignment_method = SelectField(
        validators=[DataRequired("请选择出让方式")],
        choices=[("全部", "全部"), ("拍卖", "拍卖"), ("挂牌", "挂牌"), ("招标", "招标"), ("协议", "协议")],
        default='全部'
    )
    assignment_limit = SelectField(
        validators=[DataRequired("请选择出让年限")],
        choices=years,
        default='全部'
    )
    region_name = SelectField(
        validators=[DataRequired("请选择行政区")],
        default='全部'
    )
    # PLAN_USE
    plan_use_custom = SelectField(
        validators=[DataRequired("请选择用途分类")],
        default='全部'
    )

    submit = SubmitField('查询')

    def __init__(self, *args, **kwargs):
        super(LandSellSearch, self).__init__(*args, **kwargs)
        self.land_location.choices = [("全部", "全部")]
        self.land_location.choices.extend([(v.LAND_LOCATION, v.LAND_LOCATION) for v in
                                           LAND_SELL_INFO.query.with_entities(
                                               LAND_SELL_INFO.LAND_LOCATION).order_by(
                                               LAND_SELL_INFO.LAND_LOCATION.desc()).limit(10).distinct().all()])
        self.region_name.choices = [("全部", "全部")]
        self.region_name.choices.extend([(v.REGION_CODE, v.REGION_NAME) for v in
                                         DICT_REGION.query.with_entities(
                                             DICT_REGION.REGION_CODE, DICT_REGION.REGION_NAME).order_by(
                                             DICT_REGION.REGION_CODE.desc()).distinct().all()])

        self.plan_use_custom.choices = [("全部", "全部")]
        self.plan_use_custom.choices.extend([(str(v.USE_NAME), str(v.USE_NAME)) for v in
                                        DICT_LAND_USE.query.filter(
                                        DICT_LAND_USE.GRADE == 'CUSTOM_USE_1').all()])
