Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/precise64"
  config.vm.hostname = "massa-vagrant"
  config.vm.network :private_network, ip: "33.33.33.10"

  config.vm.synced_folder ".", "/vagrant",
    type: "rsync",
    rsync__exclude: [".git/", ".virtualenv"]

  config.ssh.forward_agent = true

  config.vm.provider "virtualbox" do |v|
    v.name = "massa-vagrant"
  end

  config.vm.provision :ansible do |ansible|
    ansible.inventory_path = "provisioning/development.ini"
    ansible.playbook = "provisioning/site.yml"
    ansible.host_key_checking = false
    ansible.verbose = false
    ansible.limit = "development"
  end
end
