## "SEND:DISCORD:MESSAGE"

This action will send a discord message to specific channel.

### Required Vars:
 - discord_token: "${{ secrets.DISCORD_TOKEN }}"
 - discord_channel_id: "${{ secrets.DISCORD_CHANNEL_ID }}"
 - discord_message: |
   discord message to send
   formatted.

```yaml
      - name: "SEND:DISCORD:MESSAGE"
        uses: gzukel/CosmosComposites/send_discord_message@main
        with:
          discord_token: "${{ secrets.DISCORD_TOKEN }}"
          discord_channel_id: "${{ secrets.DISCORD_CHANNEL_ID }}"
          discord_message: |
            discord message to send
            formatted.
```
