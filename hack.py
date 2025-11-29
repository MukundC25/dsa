    non_fraud_codes = set(non_fraud_codes.strip().split(','))
    fraud_codes = set(fraud_codes.strip().split(','))
    min_charges = int(min_charges.strip())

    mcc_to_threshold = {}
    for row in mcc_thresholds:
        row = row.strip()
        if not row:
            continue
        mcc, val = row.split(',')
        val = val.strip()
        if '.' in val:
            mcc_to_threshold[mcc] = float(val)
        else:
            mcc_to_threshold[mcc] = int(val)

    merchant_to_mcc = {}
    for row in merchant_mcc_map:
        if not row.strip():
            continue
        acct, mcc = row.strip().split(',')
        merchant_to_mcc[acct] = mcc

    charge_to_merchant = {}
    charge_to_code = {}
    merchant_stats = {}
    fraudulent_merchants = set()
    disputes = set()
    pending_disputes = set()

    def evaluate(acct):
        if acct not in merchant_to_mcc or acct not in merchant_stats:
            return
        total = merchant_stats[acct]["total"]
        fraud = merchant_stats[acct]["fraud"]
        if total < min_charges:
            fraudulent_merchants.discard(acct)
            return
        mcc = merchant_to_mcc.get(acct)
        if mcc not in mcc_to_threshold:
            return
        threshold = mcc_to_threshold[mcc]
        if isinstance(threshold, int):
            if fraud >= threshold:
                fraudulent_merchants.add(acct)
            else:
                fraudulent_merchants.discard(acct)
        else:
            ratio = fraud / total if total else 0
            if round(ratio + 1e-10, 6) >= round(threshold - 1e-10, 6):
                fraudulent_merchants.add(acct)
            else:
                fraudulent_merchants.discard(acct)

    for line in charges:
        if not line.strip():
            continue
        parts = line.strip().split(',')
        if parts[0] == "DISPUTE":
            _, ch_id = parts
            if ch_id in charge_to_merchant and ch_id not in disputes:
                acct = charge_to_merchant[ch_id]
                code = charge_to_code[ch_id]
                if code in fraud_codes:
                    merchant_stats[acct]["fraud"] = max(0, merchant_stats[acct]["fraud"] - 1)
                    evaluate(acct)
                disputes.add(ch_id)
            else:
                pending_disputes.add(ch_id)
            continue

        if parts[0] == "CHARGE":
            _, ch_id, acct, amt, code = parts
            charge_to_merchant[ch_id] = acct
            charge_to_code[ch_id] = code

            if acct not in merchant_stats:
                merchant_stats[acct] = {"total": 0, "fraud": 0}

            merchant_stats[acct]["total"] += 1

            if code in fraud_codes and ch_id not in disputes:
                merchant_stats[acct]["fraud"] += 1

            if ch_id in pending_disputes:
                if code in fraud_codes and ch_id not in disputes:
                    merchant_stats[acct]["fraud"] = max(0, merchant_stats[acct]["fraud"] - 1)
                disputes.add(ch_id)
                pending_disputes.discard(ch_id)

            evaluate(acct)

    for acct in merchant_stats:
        evaluate(acct)

    return ','.join(sorted(fraudulent_merchants))    

