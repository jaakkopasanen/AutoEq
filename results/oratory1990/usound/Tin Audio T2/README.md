# Tin Audio T2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.7; 31 5.3; 34 4.9; 37 4.6; 41 4.1; 45 3.8; 49 3.4; 54 3.0; 60 2.6; 66 2.1; 72 1.7; 79 1.2; 87 0.7; 96 0.2; 106 -0.3; 116 -0.7; 128 -1.1; 141 -1.4; 155 -1.7; 170 -1.9; 187 -2.0; 206 -2.0; 227 -2.2; 249 -2.4; 274 -2.4; 302 -2.3; 332 -2.3; 365 -2.1; 402 -2.0; 442 -1.9; 486 -1.7; 535 -1.4; 588 -1.1; 647 -0.8; 712 -0.4; 783 0.1; 861 0.5; 947 0.1; 1042 0.3; 1146 0.5; 1261 0.6; 1387 1.0; 1526 1.6; 1678 2.4; 1846 3.3; 2031 3.9; 2234 4.0; 2457 3.5; 2703 2.5; 2973 1.9; 3270 2.0; 3597 2.2; 3957 2.2; 4353 1.6; 4788 -0.2; 5267 -0.8; 5793 1.9; 6373 3.7; 7010 1.9; 7711 -1.5; 8482 -1.3; 9330 0.0; 10263 0.0; 11289 -0.3; 12418 -2.1; 13660 -1.5; 15026 -1.7; 16529 -0.4; 18182 -0.0; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Tin Audio T2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Tin Audio T2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.65 | 6.0 dB  |
| Peaking | 58 Hz    | 1.15 | 1.2 dB  |
| Peaking | 240 Hz   | 0.55 | -2.6 dB |
| Peaking | 2122 Hz  | 1.57 | 4.1 dB  |
| Peaking | 3833 Hz  | 3.4  | 1.5 dB  |
| Peaking | 453 Hz   | 4.36 | -0.3 dB |
| Peaking | 5193 Hz  | 5.28 | -3.2 dB |
| Peaking | 6448 Hz  | 2.54 | 4.6 dB  |
| Peaking | 7822 Hz  | 5.6  | -3.6 dB |
| Peaking | 22166 Hz | 0.1  | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Tin%20Audio%20T2/Tin%20Audio%20T2.png)