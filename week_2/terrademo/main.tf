terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.14.0"
    }
  }
}

provider "google" {
  # Configuration options
  credentials = "./keys/my-creds.json"
  project = "direct-disk-412820"
  region  = "europe-north1"
}

resource "google_storage_bucket" "demo-bucket" {
  name          = "direct-disk-412820-terra-bucket"
  location      = "europe-north1"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 3
    }
    action {
      type = "Delete"
    }
  }

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}
