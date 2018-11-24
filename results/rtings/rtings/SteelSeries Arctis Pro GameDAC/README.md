# SteelSeries Arctis Pro GameDAC

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -4.2; 23 -4.1; 25 -4.0; 28 -3.8; 31 -3.4; 34 -2.8; 37 -2.1; 41 -1.2; 45 -0.6; 49 -0.2; 54 -0.2; 60 -0.3; 66 -0.5; 72 -0.6; 79 -0.8; 87 -1.0; 96 -1.2; 106 -1.3; 116 -1.4; 128 -1.4; 141 -1.6; 155 -1.7; 170 -1.7; 187 -1.6; 206 -1.6; 227 -1.7; 249 -2.0; 274 -2.3; 302 -2.6; 332 -2.8; 365 -3.0; 402 -3.1; 442 -3.2; 486 -3.2; 535 -3.2; 588 -3.0; 647 -2.8; 712 -1.9; 783 -0.9; 861 -1.0; 947 -0.4; 1042 0.1; 1146 0.4; 1261 0.8; 1387 1.4; 1526 1.9; 1678 0.1; 1846 -0.8; 2031 -1.0; 2234 -0.5; 2457 0.2; 2703 0.2; 2973 1.1; 3270 4.2; 3597 6.0; 3957 6.0; 4353 1.7; 4788 -0.8; 5267 -0.6; 5793 -1.2; 6373 -3.0; 7010 -2.4; 7711 -0.6; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -0.0; 13660 -1.3; 15026 -0.8; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SteelSeries Arctis Pro GameDAC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SteelSeries Arctis Pro GameDAC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 1.52 | -4.4 dB |
| Peaking | 204 Hz   | 0.64 | -1.5 dB |
| Peaking | 481 Hz   | 1.42 | -2.9 dB |
| Peaking | 3687 Hz  | 4.12 | 7.2 dB  |
| Peaking | 6381 Hz  | 3    | -3.1 dB |
| Peaking | 654 Hz   | 7.1  | -0.9 dB |
| Peaking | 1603 Hz  | 2.26 | 3.6 dB  |
| Peaking | 1752 Hz  | 4.32 | -2.6 dB |
| Peaking | 2046 Hz  | 2.59 | -1.6 dB |
| Peaking | 14244 Hz | 5.15 | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/SteelSeries%20Arctis%20Pro%20GameDAC/SteelSeries%20Arctis%20Pro%20GameDAC.png)