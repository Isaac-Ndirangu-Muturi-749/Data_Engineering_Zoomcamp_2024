variable "credentials" {
    description = "My Credentials"
    default = "./keys/my-creds.json"
}

variable "project" {
  description = "Project"
  default     = "direct-disk-412820"
}

variable "region" {
  description = "Region"
  default     = "europe-north1"
}

variable "location" {
  description = "Project Location"
  default     = "europe-north1"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "direct-disk-412820-terra-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}
