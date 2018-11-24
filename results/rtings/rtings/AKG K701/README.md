# AKG K701

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.6; 31 5.2; 34 4.8; 37 4.5; 41 4.2; 45 3.9; 49 3.6; 54 3.3; 60 3.0; 66 2.6; 72 2.3; 79 1.9; 87 1.5; 96 1.1; 106 0.6; 116 0.2; 128 -0.2; 141 -0.6; 155 -0.8; 170 -1.0; 187 -1.1; 206 -1.1; 227 -1.1; 249 -1.0; 274 -1.2; 302 -1.2; 332 -1.2; 365 -1.2; 402 -1.3; 442 -1.3; 486 -1.1; 535 -0.4; 588 0.4; 647 0.4; 712 0.9; 783 0.9; 861 0.7; 947 0.3; 1042 -0.2; 1146 -0.6; 1261 -0.9; 1387 -1.4; 1526 -1.9; 1678 -3.2; 1846 -5.0; 2031 -6.0; 2234 -6.9; 2457 -6.3; 2703 -5.3; 2973 -4.0; 3270 -3.0; 3597 -1.9; 3957 -1.6; 4353 -1.4; 4788 -1.0; 5267 -1.1; 5793 -2.8; 6373 -6.1; 7010 -7.0; 7711 -6.4; 8482 -7.2; 9330 -6.3; 10263 -4.6; 11289 -4.5; 12418 -2.0; 13660 0.0; 15026 0.0; 16529 -0.8; 18182 -4.5; 20000 -1.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K701 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K701 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 1.09 | 6.1 dB  |
| Peaking | 55 Hz    | 1.78 | 2.3 dB  |
| Peaking | 2256 Hz  | 2.03 | -7.0 dB |
| Peaking | 8233 Hz  | 1.51 | -7.5 dB |
| Peaking | 18665 Hz | 2.77 | -5.0 dB |
| Peaking | 534 Hz   | 0.48 | -2.7 dB |
| Peaking | 745 Hz   | 1.05 | 3.6 dB  |
| Peaking | 5299 Hz  | 2.78 | 1.9 dB  |
| Peaking | 6387 Hz  | 6.31 | -2.9 dB |
| Peaking | 14365 Hz | 3.89 | 1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/AKG%20K701/AKG%20K701.png)