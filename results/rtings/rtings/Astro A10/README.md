# Astro A10

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.9; 28 5.5; 31 4.7; 34 4.0; 37 3.4; 41 2.8; 45 2.2; 49 1.8; 54 1.4; 60 1.0; 66 0.7; 72 0.5; 79 0.4; 87 0.3; 96 0.4; 106 0.5; 116 0.7; 128 0.9; 141 1.3; 155 1.7; 170 2.1; 187 2.7; 206 3.3; 227 3.7; 249 3.5; 274 3.7; 302 3.5; 332 4.5; 365 4.9; 402 5.3; 442 5.7; 486 6.0; 535 6.0; 588 6.0; 647 6.0; 712 6.0; 783 6.0; 861 4.2; 947 1.3; 1042 -0.6; 1146 -1.1; 1261 -0.5; 1387 0.1; 1526 1.6; 1678 2.9; 1846 4.3; 2031 5.9; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 3.9; 7010 2.1; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Astro A10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Astro A10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 23 Hz   | 1.3  | 6.4 dB   |
| Peaking | 788 Hz  | 4.98 | 1.8 dB   |
| Peaking | 1100 Hz | 0.34 | 10.8 dB  |
| Peaking | 1167 Hz | 1.35 | -12.6 dB |
| Peaking | 4872 Hz | 1.99 | 3.4 dB   |
| Peaking | 97 Hz   | 2.45 | -0.8 dB  |
| Peaking | 1605 Hz | 4.31 | -1.3 dB  |
| Peaking | 3203 Hz | 0.77 | 1.4 dB   |
| Peaking | 5989 Hz | 3.68 | 3.8 dB   |
| Peaking | 6408 Hz | 0.9  | -3.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Astro%20A10/Astro%20A10.png)