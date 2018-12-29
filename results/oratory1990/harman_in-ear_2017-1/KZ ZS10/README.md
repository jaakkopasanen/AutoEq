# KZ ZS10

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -5.9; 23 -6.7; 25 -7.1; 28 -6.9; 31 -6.8; 34 -6.9; 37 -7.0; 41 -6.9; 45 -6.9; 49 -7.0; 54 -7.3; 60 -7.4; 66 -7.8; 72 -7.7; 79 -7.9; 87 -8.0; 96 -7.5; 106 -7.8; 116 -7.4; 128 -7.4; 141 -7.2; 155 -6.8; 170 -6.6; 187 -6.3; 206 -6.0; 227 -5.6; 249 -5.2; 274 -4.8; 302 -4.3; 332 -3.6; 365 -3.1; 402 -2.6; 442 -2.1; 486 -1.6; 535 -1.1; 588 -0.7; 647 -0.3; 712 0.0; 783 0.1; 861 0.4; 947 0.3; 1042 -0.3; 1146 -1.1; 1261 -1.8; 1387 -2.4; 1526 -2.9; 1678 -3.5; 1846 -4.3; 2031 -5.0; 2234 -4.9; 2457 -3.5; 2703 -2.1; 2973 -1.6; 3270 -1.2; 3597 -2.3; 3957 -0.4; 4353 4.1; 4788 6.0; 5267 2.9; 5793 5.3; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.7; 9330 -0.0; 10263 0.0; 11289 0.0; 12418 -1.4; 13660 -12.3; 15026 -18.9; 16529 -18.5; 18182 -18.8; 20000 -20.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ZS10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ZS10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 43 Hz    | 0.2  | -6.7 dB  |
| Peaking | 198 Hz   | 0.46 | -2.9 dB  |
| Peaking | 2153 Hz  | 0.79 | -10.9 dB |
| Peaking | 7907 Hz  | 0.21 | 23.0 dB  |
| Peaking | 16767 Hz | 0.27 | -34.9 dB |
| Peaking | 3781 Hz  | 4.14 | -7.0 dB  |
| Peaking | 4276 Hz  | 1.86 | 4.9 dB   |
| Peaking | 8027 Hz  | 4.74 | -3.2 dB  |
| Peaking | 11845 Hz | 4.6  | 7.0 dB   |
| Peaking | 19161 Hz | 0.19 | -1.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/KZ%20ZS10/KZ%20ZS10.png)