Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/precise64"
  config.vm.network :private_network, ip: "33.33.33.10"

  config.ssh.forward_agent = true

  config.vm.provider "virtualbox" do |v|
    v.name = "massa"
  end

  config.vm.provision :ansible do |ansible|
    ansible.inventory_path = "ansible/inventory"
    ansible.playbook = "ansible/playbook.yml"
    ansible.host_key_checking = false
    ansible.verbose = false
    ansible.limit = "vagrant"
  end
end
