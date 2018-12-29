# KZ ZS10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 21 -5.6; 23 -6.4; 25 -6.8; 28 -6.6; 31 -6.5; 34 -6.6; 37 -6.6; 41 -6.6; 45 -6.6; 49 -6.7; 54 -7.0; 60 -7.1; 66 -7.4; 72 -7.4; 79 -7.6; 87 -7.7; 96 -7.2; 106 -7.4; 116 -7.1; 128 -7.1; 141 -6.8; 155 -6.5; 170 -6.3; 187 -6.0; 206 -5.7; 227 -5.3; 249 -4.9; 274 -4.5; 302 -4.0; 332 -3.5; 365 -3.0; 402 -2.5; 442 -2.1; 486 -1.6; 535 -1.2; 588 -0.8; 647 -0.5; 712 -0.1; 783 -0.0; 861 0.3; 947 0.3; 1042 -0.3; 1146 -1.2; 1261 -2.2; 1387 -3.1; 1526 -3.8; 1678 -4.5; 1846 -5.3; 2031 -6.4; 2234 -6.9; 2457 -6.1; 2703 -5.0; 2973 -4.7; 3270 -4.3; 3597 -5.1; 3957 -2.8; 4353 2.1; 4788 5.1; 5267 1.2; 5793 4.6; 6373 5.5; 7010 2.5; 7711 -2.3; 8482 -3.3; 9330 -0.1; 10263 0.0; 11289 0.0; 12418 -0.1; 13660 -4.2; 15026 -3.4; 16529 -0.4; 18182 -3.2; 20000 -9.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ZS10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-59**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ZS10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 44 Hz    | 0.27 | -6.6 dB  |
| Peaking | 174 Hz   | 0.69 | -3.2 dB  |
| Peaking | 2145 Hz  | 1.67 | -6.7 dB  |
| Peaking | 3793 Hz  | 2.31 | -8.3 dB  |
| Peaking | 4596 Hz  | 2.04 | 9.2 dB   |
| Peaking | 863 Hz   | 3.1  | 1.6 dB   |
| Peaking | 5400 Hz  | 8.48 | -5.5 dB  |
| Peaking | 6199 Hz  | 3.42 | 5.6 dB   |
| Peaking | 8055 Hz  | 5.32 | -5.2 dB  |
| Peaking | 20994 Hz | 0.92 | -11.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/KZ%20ZS10/KZ%20ZS10.png)