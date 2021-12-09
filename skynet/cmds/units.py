from typing import Dict

# The rest of the codebase uses synts everywhere.
# Only use these units for user facing interfaces.
units: Dict[str, int] = {
    "skynet": 10 ** 12,  # 1 skynet (XNT) is 1,000,000,000,000 synt (1 trillion)
    "synt": 1,
    "colouredcoin": 10 ** 3,  # 1 coloured coin is 1000 colouredcoin synts
}
