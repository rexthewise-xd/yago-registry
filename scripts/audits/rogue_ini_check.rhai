// Rogue d3dx.ini audit check
// Scans for accidental rogue d3dx.ini placed directly inside Mods/

log_info("Running rogue d3dx.ini audit check...");

if fs_exists("Mods/d3dx.ini") {
    emit_warning(
        "Warning",
        "Registry Audit: Rogue d3dx.ini",
        "Found d3dx.ini placed directly inside the Mods/ directory. This can override game-level loader settings."
    );
}
