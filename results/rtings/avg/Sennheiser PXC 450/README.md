# Sennheiser PXC 450

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.9; 23 -1.2; 25 -1.2; 28 -0.7; 31 -0.0; 34 0.5; 37 0.8; 41 1.1; 45 1.2; 49 1.3; 54 1.3; 60 1.4; 66 1.3; 72 1.1; 79 0.8; 87 0.5; 96 0.2; 106 -0.3; 116 -0.6; 128 -0.9; 141 -1.1; 155 -1.1; 170 -0.9; 187 -0.4; 206 0.2; 227 0.1; 249 -0.2; 274 -0.7; 302 -1.2; 332 -1.5; 365 -1.9; 402 -2.4; 442 -2.8; 486 -3.1; 535 -3.4; 588 -3.5; 647 -3.4; 712 -3.0; 783 -2.3; 861 -1.3; 947 -0.4; 1042 0.4; 1146 1.3; 1261 1.9; 1387 2.5; 1526 3.5; 1678 4.8; 1846 6.0; 2031 6.0; 2234 6.0; 2457 2.0; 2703 -0.4; 2973 5.5; 3270 5.9; 3597 3.3; 3957 5.9; 4353 6.0; 4788 6.0; 5267 6.0; 5793 3.3; 6373 4.3; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -4.0; 13660 -3.6; 15026 -0.9; 16529 -3.1; 18182 -7.5; 20000 -4.7
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
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 567 Hz   | 1.26 | -4.0 dB |
| Peaking | 1840 Hz  | 2.08 | 5.8 dB  |
| Peaking | 4674 Hz  | 1.22 | 6.3 dB  |
| Peaking | 15816 Hz | 2.92 | 5.7 dB  |
| Peaking | 17870 Hz | 0.69 | -8.4 dB |
| Peaking | 59 Hz    | 1.45 | 1.6 dB  |
| Peaking | 137 Hz   | 2.92 | -1.2 dB |
| Peaking | 2640 Hz  | 7.98 | -9.5 dB |
| Peaking | 2719 Hz  | 3.03 | 4.5 dB  |
| Peaking | 7827 Hz  | 9.62 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20PXC%20450/Sennheiser%20PXC%20450.png)