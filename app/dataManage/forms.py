from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, SelectField
from wtforms.validators import Required, Length, Email, DataRequired
from ..models import LAND_SELL_INFO_TEST_LXY
import datetime

year = str(datetime.datetime.now().year)
month = str(datetime.datetime.now().month)
day = str(datetime.datetime.now().day)
detester_e = year + '-' + month + '-' + day
detester_s = year + '-01-01'
date_s = datetime.datetime.strptime(detester_s, '%Y-%m-%d')
date_e = datetime.datetime.strptime(detester_e, '%Y-%m-%d')


class LandSellSearch(Form):
    start = DateField('DatePicker', format='%Y-%m-%d', default=date_s)
    end = DateField('DatePicker', format='%Y-%m-%d', default=date_e)
    land_location = SelectField(
        validators=[DataRequired("请选择大区")],
        default='全部'
    )
    assignment_method = SelectField(
        validators=[DataRequired("请选择出让方式")],
        choices=[("全部", "全部"), ("划拨", "划拨"), ("出让", "出让"), ("拍卖", "拍卖"), ("其他", "其他")],
        default='全部'
    )
    submit = SubmitField('查询')

    def __init__(self, *args, **kwargs):
        super(LandSellSearch, self).__init__(*args, **kwargs)
        self.land_location.choices = [("全部", "全部")]
        self.land_location.choices.extend([(v.LAND_LOCATION, v.LAND_LOCATION) for v in
                                           LAND_SELL_INFO_TEST_LXY.query.with_entities(
                                               LAND_SELL_INFO_TEST_LXY.LAND_LOCATION).order_by(
                                               LAND_SELL_INFO_TEST_LXY.LAND_LOCATION.desc()).distinct().all()])
