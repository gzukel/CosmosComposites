## CALCULATE:PROPOSAL:DATETIME

This action will calculate the date in the future the provided upgrade height would occur. This is used for calculating when proposals will execute.

### Required Vars:
 - upgrade_height: "${{ env.UPGRADE_HEIGHT }}"
 - average_block_time: "${{ env.AVERAGE_BLOCK_TIME }}"
 - rpc_url: "${{ env.NODE }}"

```yaml
      #THIS SETS THE AVERAGE BLOCK TIME ENV VAR.
      - name: "CALCULATE:AVERAGE:NETWORK:BLOCKTIME"
        uses: gzukel/CosmosComposites/average_network_blocktime@main
        with:
          avg_time_sample_size: 10
          rpc_url: "${{ env.NODE }}"
          
      - name: "CALCULATE:PROPOSAL:DATETIME"
        uses: gzukel/CosmosComposites/time_to_upgrade_proposal@main
        with:
          upgrade_height: "${{ env.UPGRADE_HEIGHT }}"
          average_block_time: "${{ env.AVERAGE_BLOCK_TIME }}"
          rpc_url: "${{ env.NODE }}"
```
