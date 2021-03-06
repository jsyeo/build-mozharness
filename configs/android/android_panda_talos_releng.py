# This is a template config file for panda android tests on production.
import socket
import os

config = {
    # Values for the foopies
    "exes": {
        'python': '/tools/buildbot/bin/python',
        'virtualenv': ['/tools/buildbot/bin/python', '/tools/misc-python/virtualenv.py'],
    },
    "run_file_names": {
        "preflight_talos": "remotePerfConfigurator.py",
        "talos": "run_tests.py",
    },
    "retry_url":  "http://build.mozilla.org/talos/zips/retry.zip",
    "verify_path":  "/builds/sut_tools/verify.py",
    "install_app_path":  "/builds/sut_tools/installApp.py",
    "talos_from_code_url": "http://hg.mozilla.org/%s/raw-file/%s/testing/talos/talos_from_code.py",
    "talos_json_url": "http://hg.mozilla.org/%s/raw-file/%s/testing/talos/talos.json",
    "datazilla_urls": ["https://datazilla.mozilla.org/talos"],
    "datazilla_authfile": os.path.join(os.getcwd(), "oauth.txt"),
    #remotePerfConfigurator.py options
    "preflight_talos_options": [
        "-v", "-e", "%(app_name)s",
        "-t", "%(hostname)s",
        "--branchName=%(talos_branch)s",
        "--resultsServer=graphs.mozilla.org",
        "--resultsLink=/server/collect.cgi",
        "--noChrome",
        "--symbolsPath=../symbols",
        "--remoteDevice=%(device_ip)s",
        "--sampleConfig=remote.config",
        "--output=local.yml",
        "--webServer=bm-remote.build.mozilla.org",
        "--browserWait=60"
    ],
    #run_tests.py options
    "talos_options": [
        "--noisy",
        "local.yml"
    ],
    "all_talos_suites": {
        "remote-troboprovider":  ["--activeTests=tprovider", "--noChrome", "--fennecIDs=../fennec_ids.txt"],
        "remote-ts":  ["--activeTests=ts", "--mozAfterPaint", "--noChrome"],
        #currently disabled
        "remote-tsvgx":  ["--activeTests=tsvgx", "--noChrome"],
        "remote-tcanvasmark":  ["--activeTests=tcanvasmark", "--noChrome"],
        "remote-tsspider":  ["--activeTests=tsspider", "--noChrome"],
        #end currently disabled
        "remote-trobopan":  ["--activeTests=trobopan", "--noChrome", "--fennecIDs=../fennec_ids.txt"],
        "remote-tsvg":  ["--activeTests=tsvg", "--noChrome"],
        "remote-tp4m_nochrome":  ["--activeTests=tp4m", "--noChrome", "--rss"],
        "remote-trobocheck2":  ["--activeTests=tcheck2", "--noChrome", "--fennecIDs=../fennec_ids.txt"],
    },
    "find_links": ["http://repos/python/packages"],
    "buildbot_json_path": "buildprops.json",
    "mobile_imaging_format": "http://mobile-imaging-%03i.p%i.releng.scl1.mozilla.com",
    "mozpool_assignee": socket.gethostname(),
    "default_actions": [
        'clobber',
        'read-buildbot-config',
        'download-and-extract',
        'clone-talos',
        'create-virtualenv',
        'request-device',
        'run-test',
        'close-request',
    ],
}
