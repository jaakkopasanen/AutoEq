# Astro A20

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.7dB
GraphicEQ: 21 0.0; 23 1.5; 25 1.0; 28 0.1; 31 -0.7; 34 -1.4; 37 -2.0; 41 -2.7; 45 -3.3; 49 -3.8; 54 -4.2; 60 -4.6; 66 -5.0; 72 -5.1; 79 -5.1; 87 -5.2; 96 -5.2; 106 -5.2; 116 -5.1; 128 -5.0; 141 -4.7; 155 -4.2; 170 -3.8; 187 -3.4; 206 -2.8; 227 -2.2; 249 -1.4; 274 -1.0; 302 -1.1; 332 0.3; 365 1.5; 402 2.1; 442 1.2; 486 0.8; 535 -0.0; 588 -0.5; 647 -0.1; 712 0.5; 783 -0.2; 861 -0.2; 947 -0.2; 1042 0.4; 1146 1.2; 1261 1.8; 1387 1.8; 1526 1.5; 1678 1.4; 1846 1.6; 2031 2.2; 2234 2.5; 2457 2.6; 2703 1.8; 2973 -0.2; 3270 -1.1; 3597 -1.6; 3957 -3.6; 4353 -3.8; 4788 -3.7; 5267 -6.6; 5793 -5.6; 6373 -5.6; 7010 -5.3; 7711 -5.4; 8482 -8.0; 9330 -6.9; 10263 -0.3; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Astro A20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-27**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Astro A20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 70 Hz    | 1.06 | -4.6 dB |
| Peaking | 138 Hz   | 1.35 | -3.8 dB |
| Peaking | 2157 Hz  | 1.06 | 3.1 dB  |
| Peaking | 5445 Hz  | 1.27 | -6.3 dB |
| Peaking | 8722 Hz  | 5.3  | -7.2 dB |
| Peaking | 22 Hz    | 2.57 | 2.8 dB  |
| Peaking | 376 Hz   | 1.01 | -1.5 dB |
| Peaking | 390 Hz   | 2.65 | 3.9 dB  |
| Peaking | 1774 Hz  | 6.05 | -0.5 dB |
| Peaking | 10810 Hz | 5.19 | 2.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Astro%20A20/Astro%20A20.png)