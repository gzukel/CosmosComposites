## CALCULATE:PROPOSAL:DATETIME

This action will calculate the date in the future the provided upgrade height would occur. This is used for calculating when proposals will execute.

### Required Vars:
 - upgrade_height: "${{ env.UPGRADE_HEIGHT }}"
 - average_block_time: "${{ env.AVERAGE_BLOCK_TIME }}"
 - rpc_url: "${{ env.NODE }}"

```yaml
      - name: "CALCULATE:PROPOSAL:DATETIME"
        uses: gzukel/CosmosComposites/time_to_upgrade_proposal@main
        with:
          upgrade_height: "${{ env.UPGRADE_HEIGHT }}"
          average_block_time: "${{ env.AVERAGE_BLOCK_TIME }}"
          rpc_url: "${{ env.NODE }}"
          upgrade_buffer_seconds: "${{ env.UPGRADE_BUFFER_SECONDS }}"
```
