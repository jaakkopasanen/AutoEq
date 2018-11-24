# KZ ZS-10

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.4dB
GraphicEQ: 21 0.0; 23 1.5; 25 1.2; 28 0.9; 31 0.7; 34 0.6; 37 0.4; 41 0.2; 45 0.0; 49 -0.1; 54 -0.4; 60 -0.9; 66 -1.4; 72 -1.8; 79 -2.3; 87 -2.8; 96 -3.4; 106 -4.0; 116 -4.6; 128 -5.1; 141 -5.5; 155 -5.8; 170 -5.9; 187 -6.1; 206 -6.0; 227 -5.9; 249 -5.6; 274 -5.2; 302 -4.8; 332 -4.3; 365 -3.8; 402 -3.3; 442 -2.8; 486 -2.2; 535 -1.5; 588 -0.9; 647 -0.2; 712 0.4; 783 0.8; 861 0.9; 947 0.6; 1042 -0.5; 1146 -1.5; 1261 -2.2; 1387 -2.8; 1526 -3.5; 1678 -4.4; 1846 -5.5; 2031 -6.7; 2234 -7.2; 2457 -6.6; 2703 -5.6; 2973 -5.1; 3270 -5.9; 3597 -6.8; 3957 -6.9; 4353 -3.4; 4788 1.7; 5267 0.5; 5793 -4.1; 6373 -2.2; 7010 2.2; 7711 0.3; 8482 -0.2; 9330 -5.2; 10263 -7.5; 11289 -4.5; 12418 -1.6; 13660 -2.6; 15026 -2.9; 16529 -0.2; 18182 0.0; 20000 -1.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ZS-10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-24**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ZS-10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.0dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 188 Hz   |  0.74 | -6.5 dB |
| Peaking | 2193 Hz  |  1.79 | -7.1 dB |
| Peaking | 3689 Hz  |  4.17 | -6.1 dB |
| Peaking | 10324 Hz |  3.89 | -8.0 dB |
| Peaking | 20619 Hz |  3.07 | -3.3 dB |
| Peaking | 20 Hz    |  1.03 | 1.8 dB  |
| Peaking | 818 Hz   |  3.36 | 2.3 dB  |
| Peaking | 7054 Hz  | 10.99 | 3.0 dB  |
| Peaking | 8136 Hz  |  7.2  | 1.6 dB  |
| Peaking | 14478 Hz |  4.1  | -3.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/KZ%20ZS-10/KZ%20ZS-10.png)