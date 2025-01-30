import os
import subprocess

def run_command(command):
    """Function to execute a shell command"""
    print(f"Running command: {command}")
    subprocess.run(command, shell=True, check=True)

def main():
    # Get user inputs
    reference_genome = input("Enter the path to the reference genome (reference.fasta): ").strip()
    input_fastqs = input("Enter the path(s) to the input FASTQ file(s) (comma separated if more than one): ").strip().split(',')
    combine_fastqs = input("Do you want to combine the FASTQ files? (yes/no): ").strip().lower()

    # Step 1: Index the reference genome using minimap2
    reference_mmi = "reference.mmi"
    run_command(f"minimap2 -d {reference_mmi} {reference_genome}")

    # Step 2: Combine the FASTQ files if the user wants to
    combined_fastq = "combined.fastq"
    if combine_fastqs == "yes":
        combined_fastq = "combined.fastq"
        combine_command = f"cat {' '.join([fastq.strip() for fastq in input_fastqs])} > {combined_fastq}"
        run_command(combine_command)

    # Step 3: Align the reads using minimap2
    if combine_fastqs == "yes":
        run_command(f"minimap2 -ax map-ont {reference_mmi} {combined_fastq} > combined_alignment.sam")
        alignment_file = "combined_alignment.sam"
    else:
        # If no combination, assume single fastq
        run_command(f"minimap2 -ax map-ont {reference_mmi} {input_fastqs[0].strip()} > alignment.sam")
        alignment_file = "alignment.sam"

    # Step 4: Convert and sort the alignment using samtools
    run_command(f"samtools view -Sb {alignment_file} | samtools sort -o {alignment_file.replace('.sam', '.sorted.bam')}")

    # Step 5: Index the BAM file
    run_command(f"samtools index {alignment_file.replace('.sam', '.sorted.bam')}")

    print("Pipeline completed successfully!")

if __name__ == "__main__":
    main()

