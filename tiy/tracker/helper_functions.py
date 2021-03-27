'''
A modul to create custom functions for the whole app in order to keep the code clean.
'''

from .models import AssetAccount

# For models.py
'''
After a trade, three assetAccounts are effected: 1) asset bought, 2) asset sold, 3) fee
'''
def create_assetAccounts_afterTrade(trade):
    # 1) Asset bought
    aa_buy = AssetAccount(
        date = trade.date,
        trade = trade,
        asset = trade.asset_buy,
        asset_quantity = trade.asset_buy_quantity,
        price = trade.asset_sell_quantity / trade.asset_buy_quantity,
        price_asset = trade.asset_sell,
        posting_type = 'B',
        open_quantity = trade.asset_buy_quantity
    )
    aa_buy.save()

    # 2) Asset sold
    aa_sell = AssetAccount(
        date = trade.date,
        trade = trade,
        asset = trade.asset_sell,
        asset_quantity = trade.asset_sell_quantity,
        price = trade.asset_sell_quantity / trade.asset_buy_quantity,
        price_asset = trade.asset_sell,
        posting_type = 'S',
        open_quantity = trade.asset_sell_quantity
    )
    aa_sell.save()

    # 3) Fee
    if trade.fee_quantity != 0.0:
        aa_fee = AssetAccount(
            date = trade.date,
            trade = trade,
            asset = trade.fee,
            asset_quantity = trade.fee_quantity,
            posting_type = 'F',
            open_quantity = trade.fee_quantity
        )
        aa_fee.save()
    