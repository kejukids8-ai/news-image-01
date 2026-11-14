// Entry point for the news-image-01 make.fun bounty.
//
// The rendered 1024x1024 front page lives in entry.png beside this file. The
// grader reads exactly the bytes we copy, so this program hands the image over
// verbatim: it copies entry.png into the directory named by MAKEFUN_OUTPUT_DIR
// (falling back to /output) under the fixed filename entry.png.
//
// Outside the grader there is no /output, so run it against a local directory:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

// Resolve the source image relative to this script, not the process cwd, so
// the copy works no matter which directory the command is launched from.
const scriptDir: string = dirname(fileURLToPath(import.meta.url));
const sourcePath: string = join(scriptDir, 'entry.png');

const outputDir: string = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const targetPath: string = join(outputDir, 'entry.png');

copyFileSync(sourcePath, targetPath);
console.log(`copied entry.png -> ${targetPath}`);
