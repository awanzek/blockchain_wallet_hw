# blockchain_wallet_hw

In this process we used hd-wallet-derive tool to make unique wallet addresses from a BIP 39 mnemonic phrase using the derive wallets aspect of hd-wallet-derive.

## Getting HD-WALLET-DERIVE
The first process was cloning the hd-wallet-derive repository to the directory where the wallets would be made. The following commands were run in terminal to complete the hd-wallet-derive install.

*git clone https://github.com/dan-da/hd-wallet-derive*
*cd hd-wallet-derive*
*php -r "readfile('https://getcomposer.org/installer');" | php*
*php -d pcre.jit=0 composer.phar install*


Using the following command in terminal a sym link was made to directly call the wallet derive function with *./derive* instead of a longer *./hd-wallet-derive/hd-wallet derive.php*.

*ln -s hd-wallet-derive/hd-wallet-derive.php derive*

## What Does the Wallet Do?
The wallet that has been created is designed to send and recieve crypto currency transaction. It has a mnemonic pass phrase that is original to its seed. Using the hd-wallet-derive tools, the wallet was created and it was given an unique address for which a public and private key are provided. The public key or address is what is shared on the network for the wallet to send or recieve a transaction. The private key is what is used to digitally sign and confirm the transaction can be sent from the wallet when sending.

## Test Transactions






