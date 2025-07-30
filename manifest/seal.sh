for file in "${REQUIRED[@]}"; do
    if [ ! -f "$file" ]; then
        echo "⟁ Missing: $file"
        MISSING=1
    else
        chmod 544 "$file"
        # chattr +i "$file"
    fi
done
