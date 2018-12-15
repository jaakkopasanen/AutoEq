# KZ ZS10

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.9; 25 2.6; 28 2.7; 31 2.8; 34 2.6; 37 2.4; 41 2.2; 45 2.0; 49 1.6; 54 0.8; 60 0.2; 66 -0.7; 72 -1.2; 79 -1.9; 87 -2.5; 96 -2.6; 106 -3.4; 116 -3.7; 128 -4.3; 141 -4.6; 155 -4.7; 170 -5.1; 187 -5.3; 206 -5.5; 227 -5.4; 249 -5.2; 274 -4.8; 302 -4.3; 332 -3.6; 365 -3.1; 402 -2.6; 442 -2.1; 486 -1.6; 535 -1.1; 588 -0.7; 647 -0.3; 712 0.0; 783 0.1; 861 0.4; 947 0.3; 1042 -0.3; 1146 -1.1; 1261 -1.8; 1387 -2.4; 1526 -2.9; 1678 -3.5; 1846 -4.3; 2031 -5.0; 2234 -4.9; 2457 -3.5; 2703 -2.1; 2973 -1.6; 3270 -1.2; 3597 -2.3; 3957 -0.4; 4353 4.1; 4788 6.0; 5267 2.9; 5793 5.3; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.7; 9330 -0.0; 10263 0.0; 11289 0.0; 12418 -1.4; 13660 -12.3; 15026 -18.9; 16529 -18.5; 18182 -18.8; 20000 -20.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ZS10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ZS10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.54 | 3.6 dB   |
| Peaking | 199 Hz   | 0.5  | -6.1 dB  |
| Peaking | 2148 Hz  | 0.77 | -11.2 dB |
| Peaking | 7854 Hz  | 0.2  | 23.7 dB  |
| Peaking | 16738 Hz | 0.26 | -35.5 dB |
| Peaking | 3790 Hz  | 4.01 | -7.7 dB  |
| Peaking | 4181 Hz  | 1.9  | 5.4 dB   |
| Peaking | 8136 Hz  | 3.59 | -4.0 dB  |
| Peaking | 12121 Hz | 3.1  | 6.6 dB   |
| Peaking | 14321 Hz | 4.08 | -6.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/KZ%20ZS10/KZ%20ZS10.png)