# GenomeAligner

**Author:** Guilherme Moreira  

## Description
GenomeAligner is a command-line pipeline for aligning sequencing reads to a reference genome using Minimap2 and Samtools. The script automates indexing, alignment, and BAM file processing for efficient genome analysis.

## Features
- Indexes the reference genome using Minimap2
- Merges multiple FASTQ files (if selected by the user)
- Aligns sequencing reads to the reference genome
- Converts SAM files to sorted BAM files
- Indexes the final BAM file using Samtools

## Requirements
Ensure the following dependencies are installed before running GenomeAligner:
- Python 3
- Minimap2
- Samtools

## Installation
Clone this repository or download the script:
```bash
git clone https://github.com/your-repo/genomeAligner.git
cd genomeAligner
```

## Usage
Run the script using:
```bash
python genomeAligner.py
```

### User Inputs:
- Path to the reference genome (FASTA file)
- Path(s) to the input FASTQ file(s) (comma-separated if multiple files)
- Whether to combine multiple FASTQ files (yes/no)

### Example Run
```plaintext
Enter the path to the reference genome (reference.fasta): reference.fasta
Enter the path(s) to the input FASTQ file(s) (comma separated if more than one): sample1.fastq,sample2.fastq
Do you want to combine the FASTQ files? (yes/no): yes
```

### Output Files:
- `reference.mmi`: Indexed reference genome
- `combined.fastq` (if multiple FASTQ files are merged)
- `alignment.sam` / `combined_alignment.sam`: SAM alignment file
- `alignment.sorted.bam`: Sorted BAM file
- `alignment.sorted.bam.bai`: Indexed BAM file

## Notes
- Ensure Minimap2 and Samtools are installed and accessible in your system’s PATH.
- Large FASTQ files may require significant computational resources.

## License
This project is licensed under the MIT License.

## Author Contact
For questions or issues, contact Guilherme Moreira at gmoreiravet@gmail.com.

