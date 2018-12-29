# KZ ES4

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -8.9; 23 -9.5; 25 -9.7; 28 -9.5; 31 -9.4; 34 -9.4; 37 -9.3; 41 -9.3; 45 -9.2; 49 -9.1; 54 -9.2; 60 -9.3; 66 -9.5; 72 -9.3; 79 -9.5; 87 -9.2; 96 -8.8; 106 -8.9; 116 -8.4; 128 -8.4; 141 -7.9; 155 -7.6; 170 -7.3; 187 -6.9; 206 -6.5; 227 -6.1; 249 -5.6; 274 -5.2; 302 -4.6; 332 -4.0; 365 -3.4; 402 -2.9; 442 -2.5; 486 -2.0; 535 -1.5; 588 -1.1; 647 -0.7; 712 -0.3; 783 0.1; 861 0.3; 947 0.3; 1042 -0.3; 1146 -1.0; 1261 -1.8; 1387 -2.4; 1526 -2.8; 1678 -3.3; 1846 -4.1; 2031 -4.9; 2234 -5.3; 2457 -4.6; 2703 -3.0; 2973 -1.6; 3270 -1.7; 3597 -3.0; 3957 -2.3; 4353 3.3; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 -0.2; 11289 -1.3; 12418 -4.7; 13660 -11.6; 15026 -16.2; 16529 -18.6; 18182 -22.2; 20000 -21.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ES4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ES4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 45 Hz    | 0.13 | -9.5 dB  |
| Peaking | 2246 Hz  | 0.66 | -18.9 dB |
| Peaking | 3770 Hz  | 4.21 | -8.4 dB  |
| Peaking | 4656 Hz  | 0.27 | 22.8 dB  |
| Peaking | 18052 Hz | 0.33 | -28.8 dB |
| Peaking | 3616 Hz  | 1.57 | -0.7 dB  |
| Peaking | 6123 Hz  | 1.07 | 1.5 dB   |
| Peaking | 7728 Hz  | 2.86 | -4.2 dB  |
| Peaking | 11701 Hz | 1.93 | 4.0 dB   |
| Peaking | 14266 Hz | 3.04 | -4.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/KZ%20ES4/KZ%20ES4.png)