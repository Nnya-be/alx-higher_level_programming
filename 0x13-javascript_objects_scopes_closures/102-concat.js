#!/usr/bin/node
const fs = require('fs');

const concatFiles = (sourceFile1, sourceFile2, destinationFile) => {
  try {
    const content1 = fs.readFileSync(sourceFile1, 'utf-8');
    const content2 = fs.readFileSync(sourceFile2, 'utf-8');

    const concatenatedContent = content1 + content2;

    fs.writeFileSync(destinationFile, concatenatedContent);
  } catch (error) {
    console.error(`Error: ${error.message}`);
  }
};

// Command line arguments: node concatFiles.js sourceFile1.txt sourceFile2.txt destinationFile.txt
const [, , sourceFile1, sourceFile2, destinationFile] = process.argv;

concatFiles(sourceFile1, sourceFile2, destinationFile);
