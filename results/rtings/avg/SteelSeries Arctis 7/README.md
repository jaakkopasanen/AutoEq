# SteelSeries Arctis 7

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.6dB
GraphicEQ: 21 -0.7; 23 -0.8; 25 -0.9; 28 -0.9; 31 -0.7; 34 -0.5; 37 -0.2; 41 -0.0; 45 -0.3; 49 -0.7; 54 -1.5; 60 -2.4; 66 -3.3; 72 -4.0; 79 -4.7; 87 -5.3; 96 -5.8; 106 -6.1; 116 -6.4; 128 -6.5; 141 -6.7; 155 -6.7; 170 -6.6; 187 -6.3; 206 -6.0; 227 -5.9; 249 -5.8; 274 -5.4; 302 -5.1; 332 -5.0; 365 -4.9; 402 -4.6; 442 -4.1; 486 -3.6; 535 -2.9; 588 -2.4; 647 -2.0; 712 -1.1; 783 -0.5; 861 -0.5; 947 -0.3; 1042 0.3; 1146 0.3; 1261 -0.2; 1387 -1.1; 1526 -1.9; 1678 -3.4; 1846 -4.5; 2031 -4.7; 2234 -4.0; 2457 -3.4; 2703 -2.9; 2973 -3.1; 3270 -3.3; 3597 -3.8; 3957 -2.4; 4353 -0.1; 4788 2.5; 5267 -2.0; 5793 -3.6; 6373 -1.7; 7010 -1.0; 7711 -1.9; 8482 -3.6; 9330 -3.4; 10263 -2.5; 11289 -3.7; 12418 -5.6; 13660 -4.9; 15026 -3.3; 16529 -3.5; 18182 -3.1; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SteelSeries Arctis 7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-26**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SteelSeries Arctis 7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 169 Hz   | 0.48 | -6.9 dB |
| Peaking | 2019 Hz  | 2.83 | -4.7 dB |
| Peaking | 3345 Hz  | 3.58 | -3.1 dB |
| Peaking | 12581 Hz | 0.85 | -4.7 dB |
| Peaking | 17680 Hz | 2.66 | -2.0 dB |
| Peaking | 43 Hz    | 3.23 | 1.9 dB  |
| Peaking | 427 Hz   | 3.08 | -1.1 dB |
| Peaking | 1049 Hz  | 2.78 | 1.5 dB  |
| Peaking | 4839 Hz  | 7.62 | 4.7 dB  |
| Peaking | 5610 Hz  | 6.17 | -3.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/SteelSeries%20Arctis%207/SteelSeries%20Arctis%207.png)