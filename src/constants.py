#  This file is part of SniperCallsBot (https://github.com/Drakkar-Software/SniperCallsBot)
#  Copyright (c) 2023 Drakkar-Software, All rights reserved.
#
#  SniperCallsBot is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either
#  version 3.0 of the License, or (at your option) any later version.
#
#  SniperCallsBot is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  General Public License for more details.
#
#  You should have received a copy of the GNU General Public
#  License along with SniperCallsBot. If not, see <https://www.gnu.org/licenses/>.
import os
import pathlib
import dotenv
import decimal

# --- REPLACEMENT SERVER ---
BASE_OUR_SERVER = os.getenv("BASE_OUR_SERVER", "http://localhost:7500")
# ---------------------------

import SniperCallsbot_commons.os_util as os_util
import SniperCallsbot_commons.enums
import src.enums

# make constants visible
from src import (
    PROJECT_NAME,
    AUTHOR,
    VERSION,
    LONG_VERSION,
)

# load environment variables from .env file if exists
DOTENV_PATH = os.getenv("DOTENV_PATH", os.path.curdir)
dotenv.load_dotenv(os.path.join(DOTENV_PATH, ".env"), verbose=False)

# SniperCallsBot urls
SniperCallsBOT_WEBSITE_URL = BASE_OUR_SERVER
SniperCallsBOT_DOCS_URL = BASE_OUR_SERVER
EXCHANGES_DOCS_URL = BASE_OUR_SERVER
DEVELOPER_DOCS_URL = BASE_OUR_SERVER
SniperCallsBOT_ONLINE = "localhost:7500"
SniperCallsBOT_FEEDBACK = BASE_OUR_SERVER
TENTACLES_REPOSITORY = "tentacles"
BETA_TENTACLES_REPOSITORY = "dev-tentacles"
OFFICIALS = "officials"
TENTACLE_CATEGORY = "full"
TENTACLE_PACKAGE_NAME = "base"
BETA_TENTACLE_PACKAGE_NAME = "beta"
TENTACLE_PACKAGES = "packages"
COMPILED_TENTACLE_CATEGORY = "extra"
DEFAULT_LOCALE = "en"

SniperCallsBOT_DONATION_URL = "https://forms.gle/Bagagc7dyjJGDT1t9"
SniperCallsBOT_FEEDBACK_FORM_URL = "https://goo.gl/forms/vspraniXPY7rvtKN2"
SniperCallsBOT_BETA_PROGRAM_FORM_URL = "https://localhost/docs-join-beta"
AUTOMATION_FEEDBACK_FORM_ID = "n9NKMV"
WELCOME_FEEDBACK_FORM_ID = os.getenv("WELCOME_FEEDBACK_FORM_ID", None)
SniperCallsBOT_EXTENSION_PACKAGE_1_NAME = "Premium SniperCallsBot extension"
SniperCallsBOT_EXTENSION_PACKAGE_1_PRICE = "99.00"

COMMUNITY_FEED_CURRENT_MINIMUM_VERSION = "1.0.0"
COMMUNITY_FEED_CURRENT_EXCLUDED_MAXIMUM_VERSION = "2.0.0"
COMMUNITY_FEED_DEFAULT_TYPE = src.enums.CommunityFeedType.MQTTFeed
COMMUNITY_FEED_URL = "localhost"
COMMUNITY_TRADINGVIEW_WEBHOOK_BASE_URL = f"{BASE_OUR_SERVER}/tradingview"
COMMUNITY_EXTENSIONS_IDENTIFIER = "local"
COMMUNITY_EXTENSIONS_CHECK_ENDPOINT = BASE_OUR_SERVER
COMMUNITY_EXTENSIONS_CHECK_ENDPOINT_KEY = "DISABLED"
COMMUNITY_EXTENSIONS_PACKAGES_IDENTIFIER = ".cloud"
COMMUNITY_FETCH_TIMEOUT = 30

# production env SHOULD ONLY BE USED THROUGH CommunityIdentifiersProvider
# production env
SniperCallsBOT_COMMUNITY_LANDING_URL = os.getenv("COMMUNITY_SERVER_URL", BASE_OUR_SERVER)
SniperCallsBOT_COMMUNITY_API_URL = os.getenv("COMMUNITY_SERVER_URL", f"{SniperCallsBOT_COMMUNITY_LANDING_URL}/api/community")
SniperCallsBOT_COMMUNITY_URL = os.getenv("COMMUNITY_SERVER_URL", BASE_OUR_SERVER)
SniperCallsBOT_COMMUNITY_RECOVER_PASSWORD_URL = SniperCallsBOT_COMMUNITY_URL
# default env
COMMUNITY_BACKEND_URL = os.getenv("COMMUNITY_BACKEND_URL", BASE_OUR_SERVER)
COMMUNITY_BACKEND_KEY = os.getenv("COMMUNITY_BACKEND_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im53aHB2cmd1d2NpaGhpenJueW9lIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTU2NDQxMDcsImV4cCI6MjAxMTIyMDEwN30.AILcgv0l6hl_0IUEPlWh1wiu9RIpgrkGZGERM5uXftE")

# staging env SHOULD ONLY BE USED THROUGH CommunityIdentifiersProvider
STAGING_SniperCallsBOT_COMMUNITY_LANDING_URL = BASE_OUR_SERVER
STAGING_SniperCallsBOT_COMMUNITY_API_URL = f"{BASE_OUR_SERVER}/api/community"
STAGING_SniperCallsBOT_COMMUNITY_URL = BASE_OUR_SERVER
STAGING_COMMUNITY_RECOVER_PASSWORD_URL = BASE_OUR_SERVER
STAGING_COMMUNITY_BACKEND_URL = BASE_OUR_SERVER
STAGING_COMMUNITY_BACKEND_KEY = "DISABLED"

# production env, ignored by CommunityIdentifiersProvider
COMMUNITY_PRODUCTION_BACKEND_URL = BASE_OUR_SERVER
COMMUNITY_PRODUCTION_BACKEND_KEY = "DISABLED"

CONFIG_COMMUNITY = "community"
CONFIG_COMMUNITY_BOT_ID = "bot_id"
CONFIG_COMMUNITY_MQTT_UUID = "mqtt_uuid"
CONFIG_COMMUNITY_PACKAGE_URLS = "package_urls"
CONFIG_COMMUNITY_ENVIRONMENT = "environment"
USE_BETA_EARLY_ACCESS = os_util.parse_boolean_environment_var("USE_BETA_EARLY_ACCESS", "false")
USER_ACCOUNT_EMAIL = os.getenv("USER_ACCOUNT_EMAIL", "")
USER_PASSWORD_TOKEN = os.getenv("USER_PASSWORD_TOKEN", None)
COMMUNITY_BOT_ID = os.getenv("COMMUNITY_BOT_ID", "")
IS_DEMO = os_util.parse_boolean_environment_var("IS_DEMO", "False")
IS_CLOUD_ENV = os_util.parse_boolean_environment_var("IS_CLOUD_ENV", "false")
CAN_INSTALL_TENTACLES = os_util.parse_boolean_environment_var("CAN_INSTALL_TENTACLES", str(not IS_CLOUD_ENV))
TRACKING_ID = ""
PH_TRACKING_ID = ""
# Profiles download urls to import at startup if missing, split by ","
TO_DOWNLOAD_PROFILES = os.getenv("TO_DOWNLOAD_PROFILES", None)
# Profiles to force select at startup, identified by profile id, download url or name
FORCED_PROFILE = os.getenv("FORCED_PROFILE", None)
RUN_IN_MAIN_THREAD = os.getenv("RUN_IN_MAIN_THREAD", False)
PROFILE_UPDATE_RESTART_MIN = float(os.getenv("PROFILE_UPDATE_RESTART_MIN", 5))

SniperCallsBOT_BINARY_PROJECT_NAME = "SniperCallsBot-Binary"

# limits
UNLIMITED_ALLOWED = -1
MAX_ALLOWED_EXCHANGES = int(os.getenv("MAX_ALLOWED_EXCHANGES", str(UNLIMITED_ALLOWED)))
MAX_ALLOWED_SYMBOLS = int(os.getenv("MAX_ALLOWED_SYMBOLS", str(UNLIMITED_ALLOWED)))
MAX_ALLOWED_TIME_FRAMES = int(os.getenv("MAX_ALLOWED_TIME_FRAMES", str(UNLIMITED_ALLOWED)))
MAX_ALLOWED_BACKTESTING_CANDLES_HISTORY = int(os.getenv("MAX_ALLOWED_BACKTESTING_CANDLES_HISTORY",
                                                        str(UNLIMITED_ALLOWED)))
ENABLE_AUTOMATIONS = os_util.parse_boolean_environment_var("ENABLE_AUTOMATIONS", "True")
ENABLE_BACKTESTING = os_util.parse_boolean_environment_var("ENABLE_BACKTESTING", "True")
ENABLE_ADVANCED_INTERFACE = os_util.parse_boolean_environment_var("ENABLE_ADVANCED_INTERFACE", "True")
ENABLE_STRATEGY_OPTIMIZER = os_util.parse_boolean_environment_var("ENABLE_STRATEGY_OPTIMIZER", "True")

# tentacles
ENV_TENTACLES_URL = "TENTACLES_URL"
ENV_COMPILED_TENTACLES_URL = "COMPILED_TENTACLES_URL"
ENV_TENTACLES_REPOSITORY = "TENTACLES_REPOSITORY"
ENV_BETA_TENTACLES_REPOSITORY = "BETA_TENTACLES_REPOSITORY"
ENV_TENTACLES_URL_TAG = "TENTACLES_URL_TAG"
ENV_TENTACLE_PACKAGE_NAME = "TENTACLE_PACKAGE_NAME"
ENV_BETA_TENTACLES_PACKAGE_NAME = "BETA_TENTACLES_PACKAGE_NAME"
ENV_TENTACLES_PACKAGES_TYPE = "TENTACLES_PACKAGES_TYPE"
ENV_TENTACLES_PACKAGES_SOURCE = "TENTACLES_PACKAGES_SOURCE"
ENV_COMPILED_TENTACLES_CATEGORY = "COMPILED_TENTACLES_CATEGORY"
ENV_COMPILED_TENTACLES_PACKAGES_TYPE = "COMPILED_TENTACLES_PACKAGES_TYPE"
ENV_TENTACLE_CATEGORY = "TENTACLE_CATEGORY"
ENV_COMPILED_TENTACLES_SUBCATEGORY = "COMPILED_TENTACLES_SUBCATEGORY"
TENTACLES_REQUIRED_VERSION = f"{os.getenv(ENV_TENTACLES_URL_TAG, LONG_VERSION)}"
# VERSION_PLACEHOLDER will be replaced by the current SniperCallsBot version in ADDITIONAL_TENTACLES_PACKAGE_URL
# ADDITIONAL_TENTACLES_PACKAGE_URL can contain multiple urls separated by a ","
ADDITIONAL_TENTACLES_PACKAGE_URL = os.getenv("ADDITIONAL_TENTACLES_PACKAGE_URL", None)
# url example: 	https://plop.fr/tentacles/123/latest/any_platform.zip
# url example: 	https://plop.fr/tentacles/.../VERSION_PLACEHOLDER/any_platform.zip,https://plop.fr/any_platform.zip
VERSION_PLACEHOLDER = "VERSION_PLACEHOLDER"
URL_SEPARATOR = ","

DEFAULT_TENTACLES_PACKAGE_NAME = "SniperCallsBot-Default-Tentacles"

# logs
LOGS_FOLDER = "logs"
ENV_TRADING_ENABLE_DEBUG_LOGS = os_util.parse_boolean_environment_var("ENV_TRADING_ENABLE_DEBUG_LOGS", "False")

# system
ENABLE_CLOCK_SYNCH = os_util.parse_boolean_environment_var("ENABLE_CLOCK_SYNCH", "True")
ENABLE_SYSTEM_WATCHER = os_util.parse_boolean_environment_var("ENABLE_SYSTEM_WATCHER", "True")
WATCH_RAM = os_util.parse_boolean_environment_var("WATCH_RAM", "False")
DUMP_USED_RESOURCES = os_util.parse_boolean_environment_var("DUMP_USED_RESOURCES", "False")
USED_RESOURCES_OUTPUT = os.getenv("USED_RESOURCES_OUTPUT", "system_resources.csv")

# errors
ERRORS_URL = os.getenv("ERRORS_SniperCallsBOT_ONLINE_URL", f"{BASE_OUR_SERVER}/api/")
ERRORS_POST_ENDPOINT = f"{ERRORS_URL}log"
UPLOAD_ERRORS = os_util.parse_boolean_environment_var("UPLOAD_ERRORS", "True") # Enabled but redirected
DEFAULT_METRICS_ID = "UNSET"

# config types keys
CONFIG_KEY = "config"
TENTACLES_SETUP_CONFIG_KEY = "tentacles_setup"

# terms of service
CONFIG_ACCEPTED_TERMS = "accepted_terms"

# DEBUG
CONFIG_DEBUG_OPTION = "DEV-MODE"
FORCE_ASYNCIO_DEBUG_OPTION = False
EXIT_BEFORE_TENTACLES_AUTO_REINSTALL = os_util.parse_boolean_environment_var("EXIT_BEFORE_TENTACLES_AUTO_REINSTALL", "False")

# Files
# Store the path of the SniperCallsbot directory from this file since it can change depending on the installation path
# (local sources, python site-packages, ...)
SniperCallsBOT_FOLDER = pathlib.Path(__file__).parent.absolute()
CONFIG_FOLDER = f"{SniperCallsBOT_FOLDER}/config"
SCHEMA = "schema"
CONFIG_FILE_SCHEMA = f"{CONFIG_FOLDER}/config_{SCHEMA}.json"
PROFILE_FILE_SCHEMA = f"{CONFIG_FOLDER}/profile_{SCHEMA}.json"
DEFAULT_CONFIG_FILE = f"{CONFIG_FOLDER}/default_config.json"
DEFAULT_PROFILE_FILE = f"{CONFIG_FOLDER}/default_profile.json"
DEFAULT_PROFILE_AVATAR_FILE_NAME = "default_profile.png"
DEFAULT_PROFILE_AVATAR = f"{CONFIG_FOLDER}/{DEFAULT_PROFILE_AVATAR_FILE_NAME}"
LOGGING_CONFIG_FILE = f"{CONFIG_FOLDER}/logging_config.ini"
LOG_FILE = f"{LOGS_FOLDER}/{PROJECT_NAME}.log"

# Optimizer
OPTIMIZER_FORCE_ASYNCIO_DEBUG_OPTION = False
OPTIMIZER_DATA_FILES_FOLDER = f"{SniperCallsBOT_FOLDER}/strategy_optimizer/optimizer_data_files"
OPTIMIZATION_CAMPAIGN_KEY = "optimization_campaign"

OPTIMIZER_RUNS_FOLDER = "optimizer"
OPTIMIZER_DEFAULT_RANDOMLY_CHOSE_RUNS = True
OPTIMIZER_DEFAULT_REQUIRED_IDLE_CORES = 0
OPTIMIZER_DEFAULT_NOTIFY_WHEN_COMPLETE = False
OPTIMIZER_DEFAULT_QUEUE_SIZE = 10000
OPTIMIZER_DEFAULT_MAX_OPTIMIZER_RUNS = 100000
OPTIMIZER_DEFAULT_GENERATIONS_COUNT = 10
OPTIMIZER_DEFAULT_INITIAL_GENERATION_COUNT = OPTIMIZER_DEFAULT_GENERATIONS_COUNT
OPTIMIZER_DEFAULT_RUN_PER_GENERATION = 80
OPTIMIZER_DEFAULT_MUTATION_PERCENT = 20
OPTIMIZER_DEFAULT_MAX_MUTATION_PROBABILITY_PERCENT = decimal.Decimal(95)
OPTIMIZER_DEFAULT_MIN_MUTATION_PROBABILITY_PERCENT = decimal.Decimal(10)
OPTIMIZER_DEFAULT_MAX_MUTATION_NUMBER_MULTIPLIER = 3
OPTIMIZER_DEFAULT_DB_UPDATE_PERIOD = 15

# Databases
DEFAULT_MAX_TOTAL_RUN_DATABASES_SIZE = 1000000000   # 1GB
ENABLE_RUN_DATABASE_LIMIT = os_util.parse_boolean_environment_var("ENABLE_RUN_DATABASE_LIMIT", "True")
MAX_TOTAL_RUN_DATABASES_SIZE = int(os.getenv("MAX_TOTAL_RUN_DATABASES_SIZE", DEFAULT_MAX_TOTAL_RUN_DATABASES_SIZE))

# Channel
SniperCallsBOT_CHANNEL = "SniperCallsBot"

# Initialization
REQUIRED_TOPIC_FOR_DATA_INIT = [
    SniperCallsbot_commons.enums.InitializationEventExchangeTopics.CANDLES,
    SniperCallsbot_commons.enums.InitializationEventExchangeTopics.CONTRACTS,
    SniperCallsbot_commons.enums.InitializationEventExchangeTopics.PRICE,
    SniperCallsbot_commons.enums.InitializationEventExchangeTopics.BALANCE,
]

SniperCallsBOT_KEY = b'uVEw_JJe7uiXepaU_DR4T-ThkjZlDn8Pzl8hYPIv7w0='
