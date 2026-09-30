# Related messages

> SYNTHETIC TRAINING MATERIAL. All organizations, people, domains, IPs and account numbers are fictional.

The client's IT contractor pulled these messages from mailboxes on 16 and 17 March 2026. Headers are trimmed to the fields that matter; the full suspicious email is in `02-suspicious-email.eml`. Message IDs (M1 to M7) are yours to use in notes and on the case graph.

## M1: the real invoice (3 March)

Where found: shared mailbox `ap@orrinvalley.example`, Inbox.

```
Date: Tue, 3 Mar 2026 09:47:02 -0500
From: Dana Whitlock <dwhitlock@castellanhardwood.example>
To: ap@orrinvalley.example
Cc: Jordan Pike <jpike@orrinvalley.example>
Subject: [EXTERNAL] Invoice CHS-20417
Message-ID: <20260303144702.GA11873@mail.castellanhardwood.example>
Authentication-Results: gw01.orrinvalley.example; spf=pass smtp.mailfrom=castellanhardwood.example;
	dkim=pass header.d=castellanhardwood.example; dmarc=pass (p=quarantine) header.from=castellanhardwood.example
Attachment: CHS-20417.pdf
```

```
Good morning,

Please find attached invoice CHS-20417 for the February white oak and
hard maple order (PO 7719), total $48,612.50, net 10.

Thank you for your business.

Dana Whitlock
Accounts Receivable Manager
Castellan Hardwood Supply
Tel. 555-0112 | accounts@castellanhardwood.example
```

The attached invoice PDF names the payee as "Castellan Hardwood Supply Inc." with remittance to Vellacourt Commercial Bank, account ending 4471. It has been Castellan's account on file since 2019.

## M2: the suspicious email (10 March)

See `02-suspicious-email.eml`.

## M3: "Jordan" to the controller (11 March)

Where found: `mbeaulieu` Inbox. No copy exists in Jordan's Sent Items or Deleted Items.

```
Date: Wed, 11 Mar 2026 09:52:44 -0400
From: Jordan Pike <jpike@orrinvalley.example>
To: Maren Beaulieu <mbeaulieu@orrinvalley.example>
Subject: Castellan banking update - vendor change for Friday run
Message-ID: <a81f3c07e2d94b6e@mbx01.orrinvalley.example>
Attachment: Castellan_Bank_Letter_2026.pdf
```

```
Hi Maren,

Castellan sent over their updated banking letter (attached) - they moved
banks as part of their annual audit and the old account closes on the 16th.
Can you update the vendor master before Friday's run? They also asked that
remittance advices go to ar@castellan-hardwood.example from now on.

Dana mentioned their phones are down this week while they switch systems,
so no need to call, she said email is best.

Thanks!
Jordan
```

Text of the attachment, `Castellan_Bank_Letter_2026.pdf`, as extracted by IT:

```
CASTELLAN HARDWOOD SUPPLY LTD.
1400 Ferrule Road, Wrenmoor Crossing  |  Tel. 555-0148  |  ar@castellan-hardwood.example

9 March 2026

To our valued customers,

RE: CHANGE OF BANKING DETAILS

Following our annual financial audit, Castellan Hardwood Supply has
transferred its receivables to a new banking partner. Effective immediately,
please remit all payments to:

    Bank:            Pellbrook Savings & Trust
    Account name:    Castellan Hardwood Supply Ltd.
    Account ending:  8830

Our previous account will be closed on 16 March 2026. Payments sent to the
previous account after that date will be returned and may incur late fees.

Please direct any questions to our Accounts Receivable team at
ar@castellan-hardwood.example.

Sincerely,

Dana Whitlock                          G. Castellan
Accounts Receivable Manager            Chief Financial Officer
```

Document metadata for the attachment, from `exiftool Castellan_Bank_Letter_2026.pdf` run by IT:

```
File Size                       : 41 kB
PDF Version                     : 1.7
Page Count                      : 1
Producer                        : LibreOffice 7.6
Creator                         : Writer
Author                          : user
Title                           : vendor_letter_v3
Create Date                     : 2026:02:26 19:12:44-05:00
Modify Date                     : 2026:03:09 22:41:03-04:00
```

SHA-256 (as recorded by the mail gateway): `5d0c7a1e9b43f26c8e7a0d51b9f4c3e2a6d8b17f04e9c5a2d3b6f8e1c7a9042b`

## M4: the controller's reply (11 March)

Where found: `mbeaulieu` Sent Items, and Jordan's `RSS Subscriptions` folder, marked as read.

```
Date: Wed, 11 Mar 2026 11:06:12 -0400
From: Maren Beaulieu <mbeaulieu@orrinvalley.example>
To: Jordan Pike <jpike@orrinvalley.example>
Subject: RE: Castellan banking update - vendor change for Friday run
```

```
Done, updated in the vendor master (bank + remittance email). Please save
the letter to the Castellan vendor file. M.
```

## M5: the real reminder (12 March)

Where found: Jordan's `RSS Subscriptions` folder, marked as read. The copy in `ap@` Inbox is unread.

```
Date: Thu, 12 Mar 2026 12:05:38 -0400
From: Dana Whitlock <dwhitlock@castellanhardwood.example>
To: ap@orrinvalley.example
Cc: Jordan Pike <jpike@orrinvalley.example>
Subject: [EXTERNAL] Reminder: CHS-20417 due 13 March
Authentication-Results: gw01.orrinvalley.example; spf=pass smtp.mailfrom=castellanhardwood.example;
	dkim=pass header.d=castellanhardwood.example; dmarc=pass (p=quarantine) header.from=castellanhardwood.example
```

```
Hi Jordan,

Friendly reminder that CHS-20417 ($48,612.50) is due tomorrow. Our
banking details are unchanged from the invoice.

Thanks,
Dana
Tel. 555-0112
```

## M6: the attacker's follow-up (12 March)

Where found: Jordan's `RSS Subscriptions` folder, marked as read.

```
Date: Thu, 12 Mar 2026 12:39:58 -0400
From: "Dana Whitlock | Castellan Hardwood Supply" <dana.whitlock@castellan-hardwood.example>
Reply-To: <dwhitlock.castellan@freemail.example>
To: Jordan Pike <jpike@orrinvalley.example>
Subject: [EXTERNAL] RE: Invoice CHS-20417 - updated remittance details
Authentication-Results: gw01.orrinvalley.example; spf=pass smtp.mailfrom=castellan-hardwood.example;
	dkim=none; dmarc=none header.from=castellan-hardwood.example
```

```
Hi Jordan,

Just confirming the update went through on your side. Could you send the
remittance advice as soon as the payment is released tomorrow? Our auditors
need it for the account transition.

Thanks again for your help with this,
Dana
```

## M7: the automated remittance advice (13 March)

Where found: mail gateway trace only (outbound). The ERP sends remittance advices automatically to the remittance address on the vendor record.

```
Date: Fri, 13 Mar 2026 15:02:07 -0400
From: Orrin Valley Millworks Payables <erp-noreply@orrinvalley.example>
To: ar@castellan-hardwood.example
Subject: Remittance advice - Orrin Valley Millworks - payment 000731
```

```
Payment 000731 has been released.
Payee: Castellan Hardwood Supply Ltd.   Amount: $48,612.50
Invoices: CHS-20417
Remitted to: Pellbrook Savings & Trust, account ending 8830
```
