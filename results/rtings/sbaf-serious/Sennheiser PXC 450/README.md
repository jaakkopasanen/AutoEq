# Sennheiser PXC 450

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.5; 23 -0.9; 25 -1.0; 28 -0.5; 31 0.1; 34 0.5; 37 0.7; 41 0.9; 45 1.0; 49 1.0; 54 1.0; 60 1.1; 66 1.1; 72 1.1; 79 1.0; 87 0.8; 96 0.6; 106 0.2; 116 -0.1; 128 -0.4; 141 -0.5; 155 -0.5; 170 -0.3; 187 0.2; 206 0.7; 227 0.6; 249 0.3; 274 -0.0; 302 -0.4; 332 -0.5; 365 -0.9; 402 -1.3; 442 -1.6; 486 -1.9; 535 -2.2; 588 -2.4; 647 -2.4; 712 -2.1; 783 -1.8; 861 -1.1; 947 -0.3; 1042 0.5; 1146 1.5; 1261 2.1; 1387 2.4; 1526 3.1; 1678 4.4; 1846 6.0; 2031 6.0; 2234 6.0; 2457 2.5; 2703 0.4; 2973 5.9; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PXC 450 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC 450 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 62 Hz   | 1.62 | 1.3 dB  |
| Peaking | 225 Hz  | 4.89 | 1.0 dB  |
| Peaking | 603 Hz  | 1.37 | -2.9 dB |
| Peaking | 1868 Hz | 2.1  | 5.4 dB  |
| Peaking | 4506 Hz | 1.25 | 6.6 dB  |
| Peaking | 2639 Hz | 8.01 | -7.9 dB |
| Peaking | 2828 Hz | 2.38 | 3.8 dB  |
| Peaking | 4390 Hz | 3.01 | -1.4 dB |
| Peaking | 6353 Hz | 3.03 | 4.7 dB  |
| Peaking | 7296 Hz | 1.62 | -3.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sennheiser%20PXC%20450/Sennheiser%20PXC%20450.png)