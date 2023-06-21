## CALCULATE NETWORK AVERAGE LOCK TIME

This action will use the current height and calculate the average block height based on input sample size. Meaning it will take the current block minus sample size
and then calculate the mean between the time differences of the blocks from the sample size.

This pipeline will save the calculated value into a GITHUB ACTION ENVIRONMENT VAR *AVERAGE_BLOCK_TIME*

### Required Vars:
 - AVG_TIME_SAMPLE_SIZE: 10
 - RPC_URL: https://{COSMOS_RPC_URL}:26657

```yaml
      - name: "CALCULATE:AVERAGE:NETWORK:BLOCKTIME"
        uses: gzukel/CosmosComposites/average_network_blocktime@main
        with:
          avg_time_sample_size: 10
          rpc_url: "${{ env.NODE }}"
```
