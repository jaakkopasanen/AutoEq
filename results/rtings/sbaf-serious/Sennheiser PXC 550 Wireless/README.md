# Sennheiser PXC 550 Wireless

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.2dB
GraphicEQ: 21 0.0; 23 2.1; 25 1.3; 28 0.5; 31 -0.2; 34 -0.6; 37 -0.9; 41 -1.1; 45 -1.2; 49 -1.1; 54 -0.9; 60 -0.7; 66 -0.5; 72 -0.3; 79 -0.3; 87 -0.3; 96 -0.5; 106 -0.9; 116 -1.3; 128 -1.6; 141 -1.7; 155 -1.8; 170 -1.8; 187 -1.8; 206 -1.7; 227 -1.6; 249 -1.4; 274 -0.9; 302 -0.4; 332 -0.0; 365 0.2; 402 0.2; 442 -0.1; 486 -0.3; 535 -0.5; 588 -0.4; 647 -0.1; 712 0.2; 783 0.3; 861 0.3; 947 0.2; 1042 -0.1; 1146 -0.4; 1261 -0.2; 1387 -1.7; 1526 -3.8; 1678 -5.4; 1846 -5.5; 2031 -5.9; 2234 -5.0; 2457 -3.6; 2703 -2.5; 2973 -1.6; 3270 -0.0; 3597 -0.1; 3957 1.7; 4353 6.1; 4788 0.7; 5267 -2.4; 5793 2.7; 6373 4.0; 7010 2.2; 7711 -1.4; 8482 -6.2; 9330 -8.4; 10263 -4.5; 11289 -0.0; 12418 0.0; 13660 -2.9; 15026 -2.0; 16529 0.0; 18182 0.0; 20000 -0.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PXC 550 Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC 550 Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 21 Hz    |  3.09 | 3.1 dB  |
| Peaking | 1963 Hz  |  2.07 | -6.4 dB |
| Peaking | 4323 Hz  |  9.03 | 7.1 dB  |
| Peaking | 6480 Hz  |  5.05 | 5.6 dB  |
| Peaking | 9144 Hz  |  3.73 | -9.4 dB |
| Peaking | 13 Hz    |  1.02 | 2.3 dB  |
| Peaking | 43 Hz    |  1.68 | -1.4 dB |
| Peaking | 170 Hz   |  1.36 | -2.0 dB |
| Peaking | 5143 Hz  | 14.22 | -4.1 dB |
| Peaking | 14244 Hz |  7.17 | -3.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sennheiser%20PXC%20550%20Wireless/Sennheiser%20PXC%20550%20Wireless.png)