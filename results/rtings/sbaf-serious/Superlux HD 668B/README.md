# Superlux HD 668B

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.8dB
GraphicEQ: 21 0.0; 23 4.5; 25 3.7; 28 2.6; 31 1.5; 34 0.6; 37 -0.2; 41 -1.1; 45 -1.8; 49 -2.3; 54 -2.8; 60 -3.3; 66 -3.7; 72 -3.9; 79 -4.1; 87 -4.4; 96 -4.5; 106 -4.5; 116 -4.4; 128 -4.2; 141 -3.8; 155 -3.3; 170 -2.6; 187 -2.0; 206 -1.8; 227 -1.7; 249 -1.7; 274 -1.5; 302 -1.5; 332 -1.4; 365 -0.9; 402 -0.8; 442 -0.8; 486 -0.6; 535 0.3; 588 0.0; 647 -0.1; 712 -0.1; 783 -0.2; 861 -0.1; 947 -0.1; 1042 0.2; 1146 0.4; 1261 0.3; 1387 -0.4; 1526 -1.5; 1678 -2.9; 1846 -4.3; 2031 -5.2; 2234 -4.7; 2457 -3.8; 2703 -2.5; 2973 -1.1; 3270 -0.0; 3597 2.0; 3957 2.6; 4353 3.0; 4788 3.2; 5267 -3.7; 5793 -4.0; 6373 -1.3; 7010 -0.7; 7711 -3.3; 8482 -7.1; 9330 -8.8; 10263 -6.8; 11289 -2.6; 12418 0.0; 13660 0.0; 15026 -2.3; 16529 -1.3; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Superlux HD 668B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-57**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Superlux HD 668B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 1.29 | 6.1 dB  |
| Peaking | 90 Hz    | 0.6  | -4.8 dB |
| Peaking | 2120 Hz  | 2.46 | -5.6 dB |
| Peaking | 4111 Hz  | 3.88 | 4.3 dB  |
| Peaking | 9269 Hz  | 2.66 | -9.3 dB |
| Peaking | 1189 Hz  | 3.92 | 1.2 dB  |
| Peaking | 4851 Hz  | 7.28 | 4.3 dB  |
| Peaking | 5462 Hz  | 5.86 | -6.6 dB |
| Peaking | 6879 Hz  | 5.33 | 2.1 dB  |
| Peaking | 15738 Hz | 7.18 | -2.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Superlux%20HD%20668B/Superlux%20HD%20668B.png)