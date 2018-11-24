# Panasonic RP-HJE120

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.5dB
GraphicEQ: 21 -1.4; 23 -1.8; 25 -2.2; 28 -2.6; 31 -3.0; 34 -3.4; 37 -3.6; 41 -4.0; 45 -4.2; 49 -4.4; 54 -4.8; 60 -5.2; 66 -5.6; 72 -5.8; 79 -6.1; 87 -6.4; 96 -6.9; 106 -7.4; 116 -7.8; 128 -8.3; 141 -8.7; 155 -8.9; 170 -8.8; 187 -8.9; 206 -8.8; 227 -8.4; 249 -7.8; 274 -7.1; 302 -6.4; 332 -6.0; 365 -5.3; 402 -4.5; 442 -3.7; 486 -2.7; 535 -1.7; 588 -0.9; 647 0.4; 712 1.2; 783 1.2; 861 0.8; 947 0.2; 1042 -0.1; 1146 -0.2; 1261 -0.4; 1387 -0.7; 1526 -1.2; 1678 -1.5; 1846 -1.6; 2031 -1.6; 2234 -1.3; 2457 -1.0; 2703 -0.7; 2973 -0.1; 3270 0.8; 3597 1.3; 3957 0.1; 4353 -2.1; 4788 -3.1; 5267 -3.2; 5793 -0.8; 6373 2.2; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -1.9; 10263 -0.2; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Panasonic RP-HJE120 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-35**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Panasonic RP-HJE120 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 108 Hz  | 0.25 | -3.9 dB |
| Peaking | 231 Hz  | 0.48 | -6.9 dB |
| Peaking | 1254 Hz | 0.28 | 6.5 dB  |
| Peaking | 1791 Hz | 0.8  | -7.3 dB |
| Peaking | 4897 Hz | 3.96 | -5.2 dB |
| Peaking | 718 Hz  | 2.86 | 3.1 dB  |
| Peaking | 724 Hz  | 1.56 | -2.0 dB |
| Peaking | 2638 Hz | 8.24 | -0.5 dB |
| Peaking | 6702 Hz | 9.42 | 3.3 dB  |
| Peaking | 9479 Hz | 5.9  | -2.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Panasonic%20RP-HJE120/Panasonic%20RP-HJE120.png)