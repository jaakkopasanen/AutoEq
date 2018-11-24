# Westone W40

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 5.7; 60 4.9; 66 4.3; 72 3.8; 79 3.2; 87 2.5; 96 1.7; 106 0.8; 116 -0.1; 128 -0.9; 141 -1.7; 155 -2.2; 170 -2.8; 187 -3.4; 206 -3.9; 227 -4.0; 249 -4.0; 274 -3.7; 302 -3.4; 332 -3.2; 365 -3.0; 402 -2.7; 442 -2.1; 486 -1.5; 535 -0.7; 588 -0.1; 647 0.6; 712 1.0; 783 1.1; 861 0.9; 947 0.5; 1042 -0.3; 1146 -0.7; 1261 -0.9; 1387 -1.0; 1526 -0.9; 1678 -0.2; 1846 1.0; 2031 2.5; 2234 4.2; 2457 5.9; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.9; 9330 -6.1; 10263 -4.1; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone W40 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone W40 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 45 Hz   | 0.34 | 7.8 dB  |
| Peaking | 520 Hz  | 0.18 | -8.3 dB |
| Peaking | 663 Hz  | 0.88 | 7.5 dB  |
| Peaking | 3466 Hz | 0.55 | 10.0 dB |
| Peaking | 9517 Hz | 3.62 | -9.3 dB |
| Peaking | 1601 Hz | 3.34 | -1.4 dB |
| Peaking | 2455 Hz | 3.92 | 2.0 dB  |
| Peaking | 3853 Hz | 1.9  | -1.2 dB |
| Peaking | 6392 Hz | 2.57 | 2.2 dB  |
| Peaking | 7355 Hz | 5.8  | -2.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Westone%20W40/Westone%20W40.png)