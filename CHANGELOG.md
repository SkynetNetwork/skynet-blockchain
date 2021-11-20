# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project does not yet adhere to [Semantic Versioning](https://semver.org/spec/v2.0.0.html)
for setuptools_scm/PEP 440 reasons.

## 1.0.1 skynet-blockchain 2021-11-20

### Added

- Added support for the CAT1 Standard
- Added RPI4_64bit GUI installation script
- Added keyring support

### Changed

- Change fullnode related from wallet protocol
- Change type decorators
- CoinStore benchmark and performance improvements
- Improve log formatting
- Update clvm_rs version and add hint test

### Fixed

- Fix mypy issues on python 3.9.7
- Fix outdated messages in CLI
- Fix edge case with negative input
- Update Gui bugs

## 1.0.0 skynet-blockchain 2021-10-29

### Added

- Added timelord special x5 fees for first week from bootstart
- Added 130850xnt to prefarm for Airdrop from testnet_09 Top500

### Changed

- Generate new cert for mainnet bootstart
- Change genesis challenge for mainnet bootstart
- Change DIFFICULTY_CONSTANT_FACTOR and DIFFICULTY_STARTING for mainnet bootstart
- Change address prefix from TXNT to XNT

### Fixed

- Fix GUI white screen in some Windows Server versions

## 0.9.92 skynet-blockchain 2021-10-19

### Added

- Added did_rpc test
- Add comments to DID innerpuz
- Added state_change call when coin added
- Added did_info for transaction sent
- Add rust check announcements

### Changed

- Remove python condition parsing, use rust unconditionally
- No need to assert_my_amount, it's done in rust
- Assert my puzzlehash is done in rust, no need to check it in python
- Parent id is checked in rust, no need to do it in python
- My coin ID is checked in rust, no need to do it in python
- Reorder condition checks to have to ones we won't see at the end
- No need for the RUST_CONDITION_CHECKER constant anymore
- Update pool tests to use get_name_puzzle_condition
- Change test so that wallets recover into other wallets
- Rename solution_to_pool_state
- Remove tests dir from packages
- Make DID wallet tests compatible with WalletStateManager lock checking
- Allow getting unconfirmed balance from wallet_state_manager when under lock
- Update DID wallet test to use async check for farmed txnt in wallet setup
- Update hash commit for did_innerpuz.clvm
- Update DID wallet RPC calls
- Re-enable did tests
- Remove unused assignation
- Delete further references to deprecated did_spend function
- Delete did tests related to singleton behaviours as that is tested elsewhere
- Make sure amounts are uint64
- Remove a deadlock from create_new_did_wallet
- Check if removal belongs to the wallet
- Did test cleanup
- Clean up DID Wallet, add test for previously broken case
- Update delete wallet parameters
- Messages are a cons box where the first value denotes type of message
- cc_wallet uses new parameter for get_confired_balance
- Updates to the puzzle
- get_block_reward_mlt generalization.
- Change Update button pointer style

### Fixed

- Fix gui terminal emulator and gui realtime logs viewer.
- Fix bug in wallet state manager related to falsely detecting pool create
- Fix deadlock in DID wallet creation, and introduce create_new_did_wallet API call
- Fixed the bugs related to DID puzzles
- Fix parent_info fetching when recovering
- Fix did_test
- Lint fixes
- Fix bare spend in did_wallet
- Fix small bugs
- Fix temppuzhash to be an innerpuz
- Fix cc wallet bare raise
- Fix duplicating bug with tx store
- Fix unsigned arithmetic error
- Fix top left gui logo vertical position

## 0.9.91 skynet-blockchain 2021-10-07

There was found a mempool bug that where some transactions wich could get stuck in mempool.

### Fixed

- Improved mempool validation (Fixed criticals in mempool_manager).

## 0.9.9 skynet-blockchain 2021-09-25

### Added

- Added random jolly block reward algo basen on block hash with x2, x5, x10 reward moltiplicator.
- Added special classic forever 5XNT block reward for all 99999 blocks before every halving.
- Added timelord 0.1% fee reward for every block processed.

## 0.9.8 skynet-blockchain 2021-09-16

Today we’re releasing version 0.9.8 to address a resource bug with nodes, and we want to stress the importance of updating to it at the earliest convenience. The fix prevents a node from consuming excessive memory when many Bluebox Timelords are active on the chain.

### Changed

- Updated to BLS 1.0.6.
- Updates to the Rust conditions parser.
- Adjusted plot refresh parameter to improve plot loading times.

### Fixed

- Fixed memory utilization issue related to how the node handles compact VDFs generated from blueboxes. We recommend everyone update to this version to avoid memory issues that can impact farming and harvesting.
- Fixed issues with reloading plot files detected as bad (this can happen during plot copying).

## 0.9.7 skynet-blockchain 2021-09-02

### Changed

- Implement async_dns
- Use negative amount to indicate send in wallet get_transactions output.
- Plotting|util|tests: Fix and test re-trying of plots which failed to load.
- Random bluebox proofs.
- RPC updates to support keyring migration and passphrase requirements.
- Search for python newest to oldest.
- Fix type of FileKeyring.keyring_path.
- Calling SpendBundle.additions() or CoinSpend.additions() runs the CLVM program and parses the conditions outputs. It can be expensive and should not be done willy nilly.
- Break problematic dependency where the streamable infrastructure depends on Program, G1Element, G2Element and PrivateKey.
- Simplify the block_tools test facility.
- Make TestCostCalculation deterministic and check against a specific cost.

### Fixed

- Fixed errors in the GUI install script.

## 0.9.6 skynet-blockchain 2021-08-26

### Added

- Enable the rust condition checker unconditionally in testnet.
- Added support for multiple wallets.
- Added a change to config.yaml to tolerate fields that replace network constants in config.yaml that don't exist, but print warning.
- Improvements to sync full nodes faster by improving the concurrency for downloading and validating blocks.
- Added new call for logging peer_host: get_peer_logging that will use the peer_host value, typically an IP address, when the peername cannot be retrieved.
- Added documentation for treehash params.
- Added a py.typed file that allows other projects that pip install skynet-blockchain to type check using our functions with mypy.
- Added an RPC for coin records by multiple coin names.
- Enabled querying AAAA records for DNS Introducer.
- We now set the version for the GUI when doing a manual install using the install-gui.sh script. Uses a python helper to get the version of the skynet install and then converts it into proper npm format and puts that into package.json.
- Added some new class methods to the Program objects to improve ease of use.
- Added an option to sign bytes as well as UTF-8 strings, which is particularly helpful if you're writing Skynetlisp puzzles that require signatures and you want to test them without necessarily writing a whole python script for signing the relevant data.
- Added a first version of .pre-commit-config.yaml and applied the changes required by the following initial hooks in separate commits. To use this you need to install pre-commit, see <https://pre-commit.com/#installation/>.
- We have added many new translations in this release based on community
submissions. Thanks to @RuiZhe for Chinese, Traditional; @HansCZ for Czech;
@LUXDAD for English, Australia; @f00b4r for Finnish; @jimkoen, @ruvado for German; @Arielzikri for Hebrew; @A-Caccese for Italian; @Hodokami for Japanese; @LUXDAD for Latvian; @vaexperience for Lithuanian; @LUXDAD for Russian; @juands1644 for Spanish, Argentina; @MrDyngrak, @ordtrogen for Swedish; @richeyphu for Thai; @Ansugo, @baturman for Turkish.

### Changed

- Thanks @altendky for Correct * to ** kwargs unpacking in time_out_assert().
- Thanks @altendky for changing the default to paginate to skynet wallet get_transactions to address cases such as piping and output redirection to a file where the command previously just hung while waiting for the user to press c for the next page.
- Removed commented-out debug breakpoints.
- Enabled Rust condition checker to add the ability to parse the output conditions from a  generator program in Rust. It also validates some of the conditions in Rust.
- Switched IP address lookup to first use Skynet's service ip.skynet.net.
- Made changes so that when creating SSL certificate and private key files, we ensure that files are written with the proper file permissions.
- Define a new encrypted keyring format to be used to store keys, and which is optionally encrypted to a user-supplied passphrase. GUI for the passphrase will come in an upcoming release.
- Removed initial transaction freeze put in place at mainnet launch as it is no longer necessary.
- Separate locking and non-locking cases for get_confirmed_balance_for_wallet, which will allow calling a few wallet_state_manager methods while already under the wallet_state_manager lock, for example during DID wallet creation.
- Thanks to @Playwo for removing the index on coin_record spent column to speed up querying.
- Made a change to the conditions parser to either ignore or fail when it encounters unknown conditions. It also removes the UNKNOWN enum value from ConditionOpcodes.
- Renamed folder tests/core/types to tests/core/custom_types to address conflicts in debugger in PyCharm.
- Disabled DID wallet tests while DID wallet is under construction.
- Added pairing cache for faster aggregate signature verification.
- Added block height assertions after block farming.
- Added assertions for tx confirmation.

### Fixed

- Fix single coin generator.
- Fixed an issue with duplicate plotnft names.
- Fixed an issue during node shutdown in which some AttributeErrors could be thrown if the shutdown happens before the node fully started up.
- Fixed mempool TX cache cost, where the cost of the mempool TX cache (for spend bundles that can't be included in a block yet) would not be reset when the cache was emptied.
- Fixed a failure to create a keychain_proxy for local keychains.
- Thanks to @mgraczyk for fixing type annotation in sync_store.
- Thanks to @darkverbito for fixing an issue on initial creation of a coloured coin where code always falls into default else clause due to lack of type conversion.
- Fixed NPM publish in clvm_rs.
- Thanks to @skweee for his investigation work on fixing mempool TX cache cost, where the cost of the mempool TX cache (for spend bundles that can't be included in a block yet) would not be reset when the cache was emptied.

## 0.9.5 skynet-blockchain 2021-07-26

### Added

- Added ability to change payout instructions in the GUI.
- Added an option to revert to sequential read. There are some systems (primarily macos+exfat) where the parallel read features results in very long lookup times. This addition makes the parallel feature the default, but adds the ability to disable it and revert back to sequential reads.
- Added backwards compatibility for Coin Solutions in push_tx since renaming it to CoinSpend.
- Added an option to set the default constants on the simulator.
- Added a warning to user to not send money to the pool contract address.
- Added capability to enable use of a backup key in future, to claim funds that were sent to p2_singleton_puzzle_hash, which today are just ignored.
- Thanks @aarcro for adding timing metrics to plot check.
- Thanks @chadwick2143 for adding the ability to set the port to use for the harvester.
- Added more friendly error reporting for peername errors.
- We have added many new translations in this release. Thanks to @L3Sota,  @hodokami and @L3Sota for Japanese; @danielrangel6, @memph1x and @dvd101x for Spanish (Mexico); @fsavaget, @semnosao and @ygalvao for Portuguese (Brazilian); @juands1644 for Spanish (Argentina); @darkflare for Portuguese; @wong8888, @RuiZhe, @LM_MA, @ezio20121225, @GRIP123, @11221206 and @nicko1122 for Chinese Traditional; @atomsymbol for Slovak; @SirGeoff and @rolandfarkasCOM for Hungarian; @ordtrogen for Swedish; @HansCZ and @kafkic for Czech; @SupperDog for Chinese Simplified; @baturman and @Ansugo for Turkish; @thebacktrack for Russian; @itservicelukaswinter for German; @saeed508, @Amirr_ezA and @themehran for Persian; @hgthtung for Vietnamese; @f00b4r for Finnish; @IMIMIM for Latvian; @Rothnita and @vanntha85 for Khmer; @Rothnita and @Gammaubl for Thai; @marcin1990 for Polish; @mydienst for Bosnian; @dvd101x and @darkflare for Spanish; @ATSHOOTER for Albanian; @Munyuk81 for Indonesian; @loppefaaret for Danish; @sharjeelazizn and @nzjake for English; @nzjake for English (New Zealand). We apologize if we missed anyone and welcome corrections.

### Changed

- Updated blspy to 1.0.5.
- Updated skynetpos to 1.0.4.
- Included all Skynetlisp files in source distribution.
- Removed left-over debug logging from test_wallet_pool_store.
- Made changes to allow us to use the name coin_spend everywhere in our code, without changing it in the API requests, both outgoing and incoming. Enables us to decide at a later date when to cut over completely to the coin_spend name.
- Thanks @mishan for your change to 'skynet plotnft show' to display Percent Successful Points.
- Thanks @Playwo for your change to make pool payout instructions case insensitive.
- GUI sees update when plots or harvesters change.
- Increased the cache interval to help large farmers.
- Removed proof limit for mainnet, but not testnet. This helps with pools that have very low difficulties. Thanks to @AlexSSD7 for pointing out the issue.
- We now also allow hex strings prefixed with 0x which is required because we currently prefix the strings in JSON conversion.
- Thanks to @opayen for your help in updating our MacOS icon.

### Fixed

- Thanks to @dfaranha for helping fix a parsing error in Relic inputs for BLS signatures.
- Fixed error type in wallet_blockchain.py.
- Thanks to @seraphik for a fix on our Linux installer that required root privileges.
- Thanks @felixbrucker for helping fix invalid content-type header issues in pool API requests.
- The wallet ignores coins sent by accident to the pool contract address and allows self pooling rewards to be claimed in this case.
- Thanks @mgraczyk for fixing the use of print_exc in farmer.

## 0.9.4 skynet-blockchain 2021-07-20

### Added

- Added terminal emulator and log viewer in the GUI.
- Added bottom bar with system info and version in the GUI.
- Added regional peers location
- Added farmer plot timings

### Changed

- Fix windows version .exe bugs and problems.
- Update electron to 13.1.9 with some fixed changes

## 0.3.0 skynet-blockchain 2021-07-18

### Changed

- Some changes and fixing.

## 0.2.0 skynet-blockchain 2021-07-17

### Changed

- Certs and consensus changes

## 0.1.0 skynet-blockchain 2021-07-16

### Changed

- Branding changes and premine changes