# Astro A10

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.9; 28 5.5; 31 4.7; 34 4.0; 37 3.4; 41 2.8; 45 2.2; 49 1.8; 54 1.4; 60 1.0; 66 0.7; 72 0.5; 79 0.4; 87 0.3; 96 0.4; 106 0.5; 116 0.7; 128 0.9; 141 1.3; 155 1.7; 170 2.1; 187 2.7; 206 3.3; 227 3.7; 249 3.5; 274 3.7; 302 3.5; 332 4.5; 365 4.9; 402 5.3; 442 5.7; 486 6.0; 535 6.0; 588 6.0; 647 6.0; 712 6.0; 783 6.0; 861 4.2; 947 1.3; 1042 -0.6; 1146 -1.1; 1261 -0.5; 1387 0.1; 1526 1.6; 1678 2.9; 1846 4.3; 2031 5.9; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 5.8; 5793 4.7; 6373 2.6; 7010 1.4; 7711 0.3; 8482 0.0
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
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 24 Hz   | 1.29 | 6.4 dB   |
| Peaking | 792 Hz  | 5.12 | 1.8 dB   |
| Peaking | 1058 Hz | 0.35 | 10.4 dB  |
| Peaking | 1156 Hz | 1.38 | -12.3 dB |
| Peaking | 4386 Hz | 1.67 | 3.4 dB   |
| Peaking | 95 Hz   | 2.4  | -0.8 dB  |
| Peaking | 1616 Hz | 3.15 | -1.9 dB  |
| Peaking | 2148 Hz | 1.1  | 1.5 dB   |
| Peaking | 5613 Hz | 2.51 | 3.4 dB   |
| Peaking | 6260 Hz | 0.87 | -2.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Astro%20A10/Astro%20A10.png)