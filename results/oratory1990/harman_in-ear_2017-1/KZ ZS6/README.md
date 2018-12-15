# KZ ZS6

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.6; 25 3.4; 28 3.3; 31 3.1; 34 2.9; 37 2.7; 41 2.3; 45 2.0; 49 1.6; 54 0.9; 60 0.2; 66 -0.7; 72 -1.1; 79 -2.0; 87 -2.3; 96 -2.7; 106 -3.5; 116 -3.7; 128 -4.4; 141 -4.6; 155 -5.0; 170 -5.4; 187 -5.7; 206 -5.8; 227 -5.9; 249 -5.7; 274 -5.3; 302 -4.9; 332 -4.3; 365 -3.8; 402 -3.3; 442 -2.9; 486 -2.4; 535 -1.9; 588 -1.4; 647 -1.0; 712 -0.5; 783 -0.1; 861 0.1; 947 0.1; 1042 -0.2; 1146 -0.8; 1261 -1.2; 1387 -1.3; 1526 -0.9; 1678 -0.3; 1846 0.2; 2031 0.1; 2234 -0.5; 2457 -1.0; 2703 -0.6; 2973 -0.1; 3270 -0.2; 3597 -0.3; 3957 4.1; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 -2.8; 8482 -4.9; 9330 -4.6; 10263 -5.9; 11289 -7.5; 12418 -11.0; 13660 -19.8; 15026 -27.0; 16529 -25.4; 18182 -20.3; 20000 -19.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ZS6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ZS6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 24 Hz    | 0.47 | 4.1 dB   |
| Peaking | 208 Hz   | 0.47 | -6.4 dB  |
| Peaking | 2932 Hz  | 0.44 | -11.8 dB |
| Peaking | 5289 Hz  | 0.39 | 27.4 dB  |
| Peaking | 15699 Hz | 0.48 | -36.7 dB |
| Peaking | 1311 Hz  | 3.33 | -2.0 dB  |
| Peaking | 2634 Hz  | 0.4  | 0.9 dB   |
| Peaking | 3482 Hz  | 6.87 | -3.0 dB  |
| Peaking | 8160 Hz  | 6.63 | -4.1 dB  |
| Peaking | 11638 Hz | 4.77 | 3.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/KZ%20ZS6/KZ%20ZS6.png)