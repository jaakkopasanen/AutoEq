# Astro A10

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.6; 31 4.8; 34 4.0; 37 3.3; 41 2.6; 45 2.0; 49 1.5; 54 1.1; 60 0.8; 66 0.6; 72 0.5; 79 0.6; 87 0.6; 96 0.8; 106 1.0; 116 1.2; 128 1.5; 141 1.8; 155 2.3; 170 2.8; 187 3.3; 206 3.8; 227 4.2; 249 4.1; 274 4.4; 302 4.4; 332 5.5; 365 5.9; 402 6.0; 442 6.0; 486 6.0; 535 6.0; 588 6.0; 647 6.0; 712 6.0; 783 6.0; 861 4.4; 947 1.3; 1042 -0.6; 1146 -0.9; 1261 -0.2; 1387 0.1; 1526 1.2; 1678 2.6; 1846 4.3; 2031 6.0; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Astro A10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Astro A10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 24 Hz   | 1.35 | 6.3 dB   |
| Peaking | 314 Hz  | 0.67 | 1.8 dB   |
| Peaking | 1205 Hz | 1.4  | -12.3 dB |
| Peaking | 1211 Hz | 0.36 | 10.4 dB  |
| Peaking | 5114 Hz | 2.04 | 3.6 dB   |
| Peaking | 626 Hz  | 1.94 | -0.9 dB  |
| Peaking | 841 Hz  | 2.09 | 2.2 dB   |
| Peaking | 965 Hz  | 5.37 | -2.9 dB  |
| Peaking | 6346 Hz | 4.86 | 2.9 dB   |
| Peaking | 7980 Hz | 1.74 | -2.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Astro%20A10/Astro%20A10.png)