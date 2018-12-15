# KZ ES4

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.2; 25 0.0; 28 0.2; 31 0.2; 34 0.1; 37 0.1; 41 -0.1; 45 -0.3; 49 -0.5; 54 -1.1; 60 -1.7; 66 -2.4; 72 -2.7; 79 -3.5; 87 -3.7; 96 -3.9; 106 -4.5; 116 -4.7; 128 -5.2; 141 -5.3; 155 -5.5; 170 -5.7; 187 -5.9; 206 -6.0; 227 -5.9; 249 -5.6; 274 -5.2; 302 -4.6; 332 -4.0; 365 -3.4; 402 -2.9; 442 -2.5; 486 -2.0; 535 -1.5; 588 -1.1; 647 -0.7; 712 -0.3; 783 0.1; 861 0.3; 947 0.3; 1042 -0.3; 1146 -1.0; 1261 -1.8; 1387 -2.4; 1526 -2.8; 1678 -3.3; 1846 -4.1; 2031 -4.9; 2234 -5.3; 2457 -4.6; 2703 -3.0; 2973 -1.6; 3270 -1.7; 3597 -3.0; 3957 -2.3; 4353 3.3; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 -0.2; 11289 -1.3; 12418 -4.7; 13660 -11.6; 15026 -16.2; 16529 -18.6; 18182 -22.2; 20000 -21.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ES4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ES4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 196 Hz   | 0.53 | -6.4 dB  |
| Peaking | 2252 Hz  | 0.69 | -17.9 dB |
| Peaking | 3767 Hz  | 4.32 | -8.2 dB  |
| Peaking | 4673 Hz  | 0.28 | 21.0 dB  |
| Peaking | 18105 Hz | 0.35 | -27.9 dB |
| Peaking | 35 Hz    | 1.79 | 1.0 dB   |
| Peaking | 6421 Hz  | 2.24 | 2.1 dB   |
| Peaking | 7601 Hz  | 2.56 | -4.5 dB  |
| Peaking | 11687 Hz | 1.77 | 4.3 dB   |
| Peaking | 14269 Hz | 2.97 | -4.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/KZ%20ES4/KZ%20ES4.png)