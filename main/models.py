from django.db import models

# Create your models here.
class Currency(models.Model):
    symbol = models.CharField(max_length=50,null = False, default='')
    name = models.CharField(max_length=50,null = False, default='')

class Price(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    l_15m_price = models.DecimalField(max_digits=10, decimal_places=4)
    l_15m_prev = models.DecimalField(max_digits=10, decimal_places=4)
    l_15m_change = models.DecimalField(max_digits=10, decimal_places=4)
    l_15m_per = models.DecimalField(max_digits=10, decimal_places=4)

    l_30m_price = models.DecimalField(max_digits=10, decimal_places=4)
    l_30m_prev = models.DecimalField(max_digits=10, decimal_places=4)
    l_30m_change = models.DecimalField(max_digits=10, decimal_places=4)
    l_30m_per = models.DecimalField(max_digits=10, decimal_places=4)
    
    l_60m_price = models.DecimalField(max_digits=10, decimal_places=4)
    l_60m_prev = models.DecimalField(max_digits=10, decimal_places=4)
    l_60m_change = models.DecimalField(max_digits=10, decimal_places=4)
    l_60m_per = models.DecimalField(max_digits=10, decimal_places=4)

    l_90m_price = models.DecimalField(max_digits=10, decimal_places=4)
    l_90m_prev = models.DecimalField(max_digits=10, decimal_places=4)
    l_90m_change = models.DecimalField(max_digits=10, decimal_places=4)
    l_90m_per = models.DecimalField(max_digits=10, decimal_places=4)

    l_1h_price = models.DecimalField(max_digits=10, decimal_places=4)
    l_1h_prev = models.DecimalField(max_digits=10, decimal_places=4)
    l_1h_change = models.DecimalField(max_digits=10, decimal_places=4)
    l_1h_per = models.DecimalField(max_digits=10, decimal_places=4)

    l_1d_price = models.DecimalField(max_digits=10, decimal_places=4)
    l_1d_prev = models.DecimalField(max_digits=10, decimal_places=4)
    l_1d_change = models.DecimalField(max_digits=10, decimal_places=4)
    l_1d_per = models.DecimalField(max_digits=10, decimal_places=4)

    l_5d_price = models.DecimalField(max_digits=10, decimal_places=4)
    l_5d_prev = models.DecimalField(max_digits=10, decimal_places=4)
    l_5d_change = models.DecimalField(max_digits=10, decimal_places=4)
    l_5d_per = models.DecimalField(max_digits=10, decimal_places=4)

    l_1w_price = models.DecimalField(max_digits=10, decimal_places=4)
    l_1w_prev = models.DecimalField(max_digits=10, decimal_places=4)
    l_1w_change = models.DecimalField(max_digits=10, decimal_places=4)
    l_1w_per = models.DecimalField(max_digits=10, decimal_places=4)

    l_1mo_price = models.DecimalField(max_digits=10, decimal_places=4)
    l_1mo_prev = models.DecimalField(max_digits=10, decimal_places=4)
    l_1mo_change = models.DecimalField(max_digits=10, decimal_places=4)
    l_1mo_per = models.DecimalField(max_digits=10, decimal_places=4)

    l_3mo_price = models.DecimalField(max_digits=10, decimal_places=4)
    l_3mo_prev = models.DecimalField(max_digits=10, decimal_places=4)
    l_3mo_change = models.DecimalField(max_digits=10, decimal_places=4)
    l_3mo_per = models.DecimalField(max_digits=10, decimal_places=4)

    l_6mo_price = models.DecimalField(max_digits=10, decimal_places=4)
    l_6mo_prev = models.DecimalField(max_digits=10, decimal_places=4)
    l_6mo_change = models.DecimalField(max_digits=10, decimal_places=4)
    l_6mo_per = models.DecimalField(max_digits=10, decimal_places=4)

    l_1y_price = models.DecimalField(max_digits=10, decimal_places=4)
    l_1y_prev = models.DecimalField(max_digits=10, decimal_places=4)
    l_1y_change = models.DecimalField(max_digits=10, decimal_places=4)
    l_1y_per = models.DecimalField(max_digits=10, decimal_places=4)

    l_2y_price = models.DecimalField(max_digits=10, decimal_places=4)
    l_2y_prev = models.DecimalField(max_digits=10, decimal_places=4)
    l_2y_change = models.DecimalField(max_digits=10, decimal_places=4)
    l_2y_per = models.DecimalField(max_digits=10, decimal_places=4)

    created_at = models.DateTimeField(auto_now_add=True)

    
    
    