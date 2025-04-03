provider "aws" {
  region = "us-north-2"
}

resource "aws_instance" "my_instance" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"
}
