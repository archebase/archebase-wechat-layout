import fs from 'node:fs/promises';
import path from 'node:path';
import process from 'node:process';
import { renderMarkdown } from '../runtime/renderer';

async function main(): Promise<void> {
  const args = process.argv.slice(2);
  const input = args[0];
  if (!input) {
    console.error('Usage: render_wechat_html.ts <markdown-file> [--output <html-file>]');
    process.exit(2);
  }

  const markdownPath = path.resolve(input);
  const markdown = await fs.readFile(markdownPath, 'utf8');
  const css = await fs.readFile(new URL('../assets/archebase-wechat-safe.css', import.meta.url), 'utf8');
  const result = await renderMarkdown(markdown, css, markdownPath);
  const outputIndex = args.indexOf('--output');
  if (outputIndex >= 0 && args[outputIndex + 1]) {
    await fs.writeFile(path.resolve(args[outputIndex + 1]), result.html, 'utf8');
  } else {
    process.stdout.write(result.html);
  }
  process.stderr.write(JSON.stringify({ warnings: result.warnings, wordCount: result.wordCount, imageCount: result.imageCount, totalSizeKB: result.totalSizeKB }) + '\n');
}

main().catch(error => {
  console.error(error instanceof Error ? error.message : String(error));
  process.exit(1);
});
