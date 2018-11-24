# SteelSeries Arctis 7

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.4dB
GraphicEQ: 21 -0.7; 23 -0.8; 25 -0.9; 28 -0.9; 31 -0.7; 34 -0.5; 37 -0.2; 41 -0.0; 45 -0.3; 49 -0.7; 54 -1.5; 60 -2.4; 66 -3.3; 72 -4.0; 79 -4.7; 87 -5.3; 96 -5.8; 106 -6.1; 116 -6.4; 128 -6.5; 141 -6.7; 155 -6.7; 170 -6.6; 187 -6.3; 206 -6.0; 227 -5.9; 249 -5.8; 274 -5.4; 302 -5.1; 332 -5.0; 365 -4.9; 402 -4.6; 442 -4.1; 486 -3.6; 535 -2.9; 588 -2.4; 647 -2.0; 712 -1.1; 783 -0.5; 861 -0.5; 947 -0.3; 1042 0.3; 1146 0.3; 1261 -0.2; 1387 -1.1; 1526 -1.9; 1678 -3.4; 1846 -4.5; 2031 -4.7; 2234 -4.1; 2457 -3.4; 2703 -2.6; 2973 -2.6; 3270 -2.6; 3597 -2.8; 3957 -1.2; 4353 1.2; 4788 4.3; 5267 0.6; 5793 -1.2; 6373 -0.5; 7010 -0.2; 7711 -0.6; 8482 -3.0; 9330 -4.8; 10263 -4.3; 11289 -2.9; 12418 -2.4; 13660 -1.6; 15026 -0.7; 16529 -0.5; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SteelSeries Arctis 7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-44**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SteelSeries Arctis 7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 169 Hz   | 0.48 | -6.9 dB |
| Peaking | 1996 Hz  | 3.02 | -4.5 dB |
| Peaking | 3352 Hz  | 1.97 | -2.5 dB |
| Peaking | 4772 Hz  | 6.19 | 5.7 dB  |
| Peaking | 10033 Hz | 2.07 | -4.7 dB |
| Peaking | 46 Hz    | 2.37 | 1.7 dB  |
| Peaking | 86 Hz    | 2.63 | -1.0 dB |
| Peaking | 429 Hz   | 3.18 | -1.1 dB |
| Peaking | 1046 Hz  | 2.69 | 1.5 dB  |
| Peaking | 13206 Hz | 4.5  | -0.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/SteelSeries%20Arctis%207/SteelSeries%20Arctis%207.png)