.PHONY: env_production env_development env_testing test

env_production:
	ln -sf .env.production .env

env_development:
	ln -sf .env.development .env

env_testing:
	ln -sf .env.testing .env

test:
	py.test
