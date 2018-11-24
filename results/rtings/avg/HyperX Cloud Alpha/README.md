# HyperX Cloud Alpha

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -2.0; 23 -2.0; 25 -2.1; 28 -2.1; 31 -2.2; 34 -2.2; 37 -2.1; 41 -2.0; 45 -1.9; 49 -1.9; 54 -1.8; 60 -1.7; 66 -1.9; 72 -2.0; 79 -2.2; 87 -2.5; 96 -2.8; 106 -3.2; 116 -3.5; 128 -3.7; 141 -3.8; 155 -3.8; 170 -3.8; 187 -3.6; 206 -3.5; 227 -3.3; 249 -3.1; 274 -3.1; 302 -3.3; 332 -3.2; 365 -2.8; 402 -2.4; 442 -2.0; 486 -1.8; 535 -1.4; 588 -1.0; 647 -0.6; 712 -0.2; 783 -0.1; 861 -0.0; 947 -0.0; 1042 0.0; 1146 -0.3; 1261 -0.7; 1387 -1.4; 1526 -2.2; 1678 -3.0; 1846 -3.6; 2031 -3.7; 2234 -2.8; 2457 -1.8; 2703 -1.3; 2973 -1.0; 3270 -1.0; 3597 0.3; 3957 2.4; 4353 4.6; 4788 6.0; 5267 5.9; 5793 1.7; 6373 0.2; 7010 -0.0; 7711 -2.3; 8482 -3.7; 9330 -4.3; 10263 -3.6; 11289 -0.7; 12418 0.0; 13660 0.0; 15026 -0.0; 16529 -4.8; 18182 -7.2; 20000 -2.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HyperX Cloud Alpha GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HyperX Cloud Alpha ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 155 Hz   | 0.42 | -3.7 dB |
| Peaking | 1989 Hz  | 2.12 | -3.9 dB |
| Peaking | 4863 Hz  | 3.3  | 7.3 dB  |
| Peaking | 9036 Hz  | 2.78 | -4.8 dB |
| Peaking | 18119 Hz | 2.18 | -8.1 dB |
| Peaking | 26 Hz    | 1.58 | -1.8 dB |
| Peaking | 348 Hz   | 3.21 | -0.8 dB |
| Peaking | 853 Hz   | 1.89 | 1.0 dB  |
| Peaking | 3227 Hz  | 7.77 | -1.3 dB |
| Peaking | 13827 Hz | 2.9  | 1.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/HyperX%20Cloud%20Alpha/HyperX%20Cloud%20Alpha.png)