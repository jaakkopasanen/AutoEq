# Jaybird Freedom

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.5dB
GraphicEQ: 21 -1.0; 23 -1.2; 25 -1.3; 28 -1.4; 31 -1.5; 34 -1.6; 37 -1.6; 41 -1.7; 45 -1.8; 49 -1.8; 54 -1.9; 60 -2.2; 66 -2.4; 72 -2.5; 79 -2.6; 87 -2.8; 96 -3.1; 106 -3.5; 116 -3.9; 128 -4.2; 141 -4.5; 155 -4.5; 170 -4.5; 187 -4.4; 206 -4.3; 227 -4.4; 249 -4.8; 274 -4.5; 302 -3.7; 332 -3.1; 365 -2.5; 402 -1.9; 442 -1.4; 486 -0.8; 535 -0.2; 588 0.3; 647 0.9; 712 1.2; 783 1.3; 861 0.9; 947 0.4; 1042 -0.3; 1146 -1.1; 1261 -2.1; 1387 -3.2; 1526 -3.8; 1678 -4.2; 1846 -4.2; 2031 -4.4; 2234 -4.6; 2457 -5.0; 2703 -5.2; 2973 -3.6; 3270 -0.8; 3597 1.3; 3957 1.6; 4353 1.0; 4788 2.3; 5267 4.4; 5793 5.3; 6373 3.4; 7010 0.3; 7711 -3.5; 8482 -4.5; 9330 -2.9; 10263 -0.6; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jaybird Freedom GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-54**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jaybird Freedom ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 124 Hz  | 0.68 | -3.9 dB |
| Peaking | 259 Hz  | 1.99 | -3.0 dB |
| Peaking | 2302 Hz | 1.32 | -6.2 dB |
| Peaking | 6177 Hz | 1.15 | 8.2 dB  |
| Peaking | 8040 Hz | 2.19 | -9.8 dB |
| Peaking | 30 Hz   | 1.29 | -1.1 dB |
| Peaking | 771 Hz  | 2.16 | 2.3 dB  |
| Peaking | 1458 Hz | 3.95 | -1.8 dB |
| Peaking | 3680 Hz | 7.14 | 1.9 dB  |
| Peaking | 4488 Hz | 6.97 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Jaybird%20Freedom/Jaybird%20Freedom.png)