# Astro A50

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.5; 25 4.1; 28 3.5; 31 3.1; 34 2.7; 37 2.4; 41 2.1; 45 1.7; 49 1.4; 54 1.1; 60 0.8; 66 0.5; 72 0.3; 79 0.2; 87 0.0; 96 -0.1; 106 -0.3; 116 -0.5; 128 -0.7; 141 -0.7; 155 -0.5; 170 -0.4; 187 -0.2; 206 -0.1; 227 0.0; 249 0.1; 274 0.2; 302 0.5; 332 0.8; 365 1.2; 402 2.0; 442 2.9; 486 3.6; 535 4.2; 588 5.5; 647 5.9; 712 4.5; 783 3.5; 861 2.9; 947 0.5; 1042 -0.1; 1146 0.1; 1261 0.4; 1387 0.6; 1526 0.9; 1678 1.3; 1846 2.1; 2031 2.5; 2234 3.2; 2457 4.0; 2703 4.7; 2973 4.9; 3270 5.5; 3597 6.0; 3957 6.0; 4353 4.9; 4788 4.6; 5267 2.9; 5793 4.3; 6373 -0.5; 7010 -0.3; 7711 0.3; 8482 -0.4; 9330 -0.4; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Astro A50 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Astro A50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.68 | 5.1 dB  |
| Peaking | 128 Hz  | 1.21 | -1.0 dB |
| Peaking | 607 Hz  | 2.03 | 5.9 dB  |
| Peaking | 3526 Hz | 1.29 | 6.3 dB  |
| Peaking | 850 Hz  | 3.74 | 2.2 dB  |
| Peaking | 992 Hz  | 2.58 | -2.4 dB |
| Peaking | 2293 Hz | 3.7  | 0.9 dB  |
| Peaking | 5834 Hz | 5.51 | 4.8 dB  |
| Peaking | 6327 Hz | 3.39 | -4.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Astro%20A50/Astro%20A50.png)