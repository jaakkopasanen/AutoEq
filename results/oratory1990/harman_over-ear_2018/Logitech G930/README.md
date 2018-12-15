# Logitech G930

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.9; 25 5.7; 28 5.1; 31 4.4; 34 3.9; 37 3.5; 41 3.2; 45 2.9; 49 2.8; 54 2.9; 60 3.3; 66 4.2; 72 4.6; 79 3.3; 87 1.6; 96 1.0; 106 -0.5; 116 -2.3; 128 -3.4; 141 -3.9; 155 -3.9; 170 -3.3; 187 -3.3; 206 -2.1; 227 -0.8; 249 0.8; 274 1.8; 302 1.3; 332 1.0; 365 0.5; 402 0.3; 442 0.1; 486 0.1; 535 0.0; 588 -0.1; 647 -0.2; 712 -0.2; 783 0.2; 861 0.3; 947 0.1; 1042 -0.0; 1146 -0.7; 1261 -1.5; 1387 -1.2; 1526 -0.4; 1678 -0.3; 1846 -0.1; 2031 0.9; 2234 0.9; 2457 0.7; 2703 2.0; 2973 4.8; 3270 6.0; 3597 6.0; 3957 5.6; 4353 -2.5; 4788 -2.2; 5267 -1.7; 5793 -4.3; 6373 -3.8; 7010 1.8; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -1.0; 13660 -3.0; 15026 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech G930 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech G930 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 17 Hz    | 0.55 | 6.4 dB  |
| Peaking | 71 Hz    | 2.79 | 3.8 dB  |
| Peaking | 145 Hz   | 2.09 | -5.0 dB |
| Peaking | 3593 Hz  | 2.43 | 10.7 dB |
| Peaking | 4630 Hz  | 1.61 | -6.4 dB |
| Peaking | 285 Hz   | 4.32 | 2.3 dB  |
| Peaking | 1321 Hz  | 4.24 | -1.8 dB |
| Peaking | 6153 Hz  | 7.22 | -7.5 dB |
| Peaking | 6610 Hz  | 2.7  | 4.1 dB  |
| Peaking | 13290 Hz | 7.24 | -3.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Logitech%20G930/Logitech%20G930.png)