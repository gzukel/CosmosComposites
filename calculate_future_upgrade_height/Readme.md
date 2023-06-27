## CALCULATE:PROPOSAL:DATETIME

This action will calculate the future upgrade height based on datetime passed in, in UTC time.
ex. 6/28/2023 14:30

```yaml
      #THIS SETS THE AVERAGE BLOCK TIME ENV VAR.
      - name: "CALCULATE:AVERAGE:NETWORK:BLOCKTIME"
        uses: gzukel/CosmosComposites/average_network_blocktime@main
        with:
          avg_time_sample_size: 10
          rpc_url: "${{ env.NODE }}"
          
      - name: "CALCULATE:PROPOSAL:HEIGHT:FROM:DATETIME"
        uses: gzukel/CosmosComposites/calculate_future_upgrade_height@main
        with:
          upgrade_date: "${{ github.event.inputs.UPGRADE_DATE }}"
          average_block_time: "${{ env.AVERAGE_BLOCK_TIME }}"
          rpc_url: "${{ env.TENDERMINT_NODE }}"
```
