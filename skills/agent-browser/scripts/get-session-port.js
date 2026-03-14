#!/usr/bin/env node

function printHelp() {
  console.log(`Usage: node scripts/get-session-port.js <session-name>

Compute the Windows agent-browser daemon port for a session name.

Examples:
  node scripts/get-session-port.js default
  node scripts/get-session-port.js my-session`);
}

function toSignedInt32(value) {
  const wrapped = value >>> 0;
  return wrapped >= 0x80000000 ? wrapped - 0x100000000 : wrapped;
}

function unsignedAbsInt32(value) {
  // Match Rust i32::unsigned_abs(), including the i32::MIN case.
  return value === -0x80000000 ? 0x80000000 : Math.abs(value);
}

function getPortForSession(session) {
  let hash = 0;

  for (const ch of session) {
    hash = toSignedInt32(((hash << 5) - hash) + ch.codePointAt(0));
  }

  return 49152 + (unsignedAbsInt32(hash) % 16383);
}

function main(argv) {
  const [arg] = argv;

  if (arg === "--help" || arg === "-h") {
    printHelp();
    return 0;
  }

  if (argv.length === 0) {
    printHelp();
    return 1;
  }

  if (argv.length !== 1) {
    console.error("Expected exactly one session name. Use --help for usage.");
    return 1;
  }

  console.log(getPortForSession(arg));
  return 0;
}

process.exit(main(process.argv.slice(2)));
