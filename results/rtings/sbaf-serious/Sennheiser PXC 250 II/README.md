# Sennheiser PXC 250 II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.7; 45 4.8; 49 3.9; 54 3.1; 60 2.3; 66 1.7; 72 1.4; 79 1.1; 87 0.9; 96 0.6; 106 0.3; 116 0.2; 128 0.1; 141 0.1; 155 0.2; 170 0.3; 187 0.3; 206 0.5; 227 0.8; 249 1.0; 274 1.2; 302 1.4; 332 1.6; 365 1.7; 402 1.9; 442 2.1; 486 2.4; 535 2.5; 588 2.6; 647 2.7; 712 2.6; 783 2.1; 861 1.4; 947 0.6; 1042 -0.4; 1146 -1.6; 1261 -3.2; 1387 -5.1; 1526 -6.6; 1678 -6.3; 1846 -6.9; 2031 -6.7; 2234 -5.6; 2457 -4.6; 2703 -3.4; 2973 -2.1; 3270 -0.5; 3597 2.3; 3957 4.8; 4353 6.0; 4788 5.1; 5267 5.3; 5793 6.0; 6373 4.5; 7010 0.2; 7711 -2.6; 8482 -4.7; 9330 -6.4; 10263 -6.4; 11289 -2.5; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PXC 250 II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC 250 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 29 Hz    | 0.93 | 6.8 dB   |
| Peaking | 787 Hz   | 0.69 | 7.1 dB   |
| Peaking | 1930 Hz  | 0.57 | -13.1 dB |
| Peaking | 4817 Hz  | 0.71 | 12.5 dB  |
| Peaking | 9114 Hz  | 1.76 | -10.9 dB |
| Peaking | 3187 Hz  | 5.66 | -1.4 dB  |
| Peaking | 4644 Hz  | 2.08 | 1.8 dB   |
| Peaking | 4927 Hz  | 7.07 | -3.4 dB  |
| Peaking | 10644 Hz | 6.19 | -2.5 dB  |
| Peaking | 11938 Hz | 3.89 | 2.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sennheiser%20PXC%20250%20II/Sennheiser%20PXC%20250%20II.png)