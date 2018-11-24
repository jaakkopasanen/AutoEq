# SteelSeries Arctis Pro GameDAC

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -3.8; 23 -3.8; 25 -3.8; 28 -3.7; 31 -3.4; 34 -2.9; 37 -2.2; 41 -1.4; 45 -0.9; 49 -0.6; 54 -0.5; 60 -0.6; 66 -0.6; 72 -0.6; 79 -0.6; 87 -0.7; 96 -0.7; 106 -0.8; 116 -0.9; 128 -0.9; 141 -1.0; 155 -1.0; 170 -1.0; 187 -1.0; 206 -1.1; 227 -1.3; 249 -1.5; 274 -1.7; 302 -1.8; 332 -1.8; 365 -2.0; 402 -2.0; 442 -2.1; 486 -2.0; 535 -2.0; 588 -1.9; 647 -1.7; 712 -1.1; 783 -0.4; 861 -0.8; 947 -0.4; 1042 0.2; 1146 0.6; 1261 1.1; 1387 1.3; 1526 1.5; 1678 -0.2; 1846 -0.7; 2031 -0.6; 2234 -0.1; 2457 0.6; 2703 0.8; 2973 2.2; 3270 5.6; 3597 6.0; 3957 6.0; 4353 1.7; 4788 -1.0; 5267 -0.2; 5793 0.2; 6373 -0.4; 7010 0.1; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SteelSeries Arctis Pro GameDAC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SteelSeries Arctis Pro GameDAC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 25 Hz   |  1.34 | -4.0 dB |
| Peaking | 424 Hz  |  1.61 | -0.6 dB |
| Peaking | 947 Hz  |  0.17 | -1.8 dB |
| Peaking | 1300 Hz |  1.72 | 2.9 dB  |
| Peaking | 3571 Hz |  3.07 | 8.1 dB  |
| Peaking | 12 Hz   |  1.66 | -1.4 dB |
| Peaking | 765 Hz  | 11.45 | 0.9 dB  |
| Peaking | 1799 Hz |  9.7  | -0.9 dB |
| Peaking | 4094 Hz | 11.79 | 2.4 dB  |
| Peaking | 4689 Hz |  6.96 | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/SteelSeries%20Arctis%20Pro%20GameDAC/SteelSeries%20Arctis%20Pro%20GameDAC.png)