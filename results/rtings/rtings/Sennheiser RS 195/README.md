# Sennheiser RS 195

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -9.4; 23 -9.3; 25 -9.2; 28 -8.9; 31 -8.7; 34 -8.3; 37 -8.0; 41 -7.6; 45 -7.5; 49 -7.7; 54 -8.1; 60 -8.6; 66 -8.7; 72 -7.8; 79 -5.7; 87 -3.1; 96 -0.9; 106 0.4; 116 1.4; 128 2.1; 141 2.0; 155 1.4; 170 1.0; 187 0.9; 206 1.4; 227 2.1; 249 2.6; 274 2.6; 302 2.2; 332 1.7; 365 1.3; 402 0.9; 442 0.4; 486 -0.2; 535 -0.5; 588 -0.5; 647 -0.4; 712 -0.2; 783 0.1; 861 0.1; 947 0.1; 1042 -0.2; 1146 -0.8; 1261 -1.7; 1387 -2.9; 1526 -3.7; 1678 -2.9; 1846 2.2; 2031 5.8; 2234 -2.9; 2457 -7.3; 2703 -8.3; 2973 -8.2; 3270 -7.0; 3597 -4.6; 3957 -2.9; 4353 -0.3; 4788 3.1; 5267 5.2; 5793 5.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -3.3; 10263 -6.4; 11289 -3.5; 12418 -0.1; 13660 -0.3; 15026 -3.3; 16529 -1.3; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser RS 195 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser RS 195 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 1.1  | -9.8 dB |
| Peaking | 62 Hz    | 2.88 | -7.9 dB |
| Peaking | 2982 Hz  | 2.5  | -9.8 dB |
| Peaking | 5756 Hz  | 2.26 | 7.0 dB  |
| Peaking | 10123 Hz | 3.71 | -7.1 dB |
| Peaking | 76 Hz    | 4.49 | -2.6 dB |
| Peaking | 126 Hz   | 2.24 | 2.9 dB  |
| Peaking | 269 Hz   | 1.97 | 2.8 dB  |
| Peaking | 1861 Hz  | 1.69 | -5.7 dB |
| Peaking | 1976 Hz  | 6.21 | 14.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Sennheiser%20RS%20195/Sennheiser%20RS%20195.png)