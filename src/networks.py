# Main network and testnet3 definitions updated for Darkcoin

params = {
    'Darkcoin_main': {
        'pubkey_address': 125,
        'script_address': 5,
        'genesis_hash': '00000bb6b5dcf5e81dee7f18ebd51055228d5fb3e41cc62f4034488f8eaf4448'
    },
    'Darkcoin_test': {
        'pubkey_address': 139, #Darkcoin src/chainparams.cpp L137
        'script_address': 19, #Darkcoin src/chainparams.cpp L138
        'genesis_hash': '00000bafbc94add76cb75e2ec92894837288a481e5c005f6563d91623bf8bc2c' #Darkcoin src/chainparams.cpp L129
    }
}
