# NVX EX10S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.9; 45 5.7; 49 5.4; 54 5.1; 60 4.6; 66 4.3; 72 4.0; 79 3.5; 87 3.1; 96 2.6; 106 2.3; 116 2.2; 128 1.8; 141 1.6; 155 1.5; 170 1.3; 187 1.2; 206 1.3; 227 1.3; 249 1.3; 274 1.4; 302 1.5; 332 1.6; 365 1.7; 402 1.7; 442 2.0; 486 1.8; 535 1.8; 588 2.0; 647 1.9; 712 1.6; 783 1.5; 861 0.9; 947 0.3; 1042 -0.2; 1146 -0.4; 1261 -0.7; 1387 -0.7; 1526 -0.3; 1678 1.4; 1846 2.6; 2031 4.4; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NVX EX10S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NVX EX10S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.42 | 6.2 dB  |
| Peaking | 553 Hz  | 0.71 | 1.9 dB  |
| Peaking | 1381 Hz | 1.39 | -4.2 dB |
| Peaking | 2584 Hz | 0.92 | 6.9 dB  |
| Peaking | 5351 Hz | 2.21 | 4.6 dB  |
| Peaking | 2856 Hz | 5.49 | -0.6 dB |
| Peaking | 4034 Hz | 2.57 | 1.3 dB  |
| Peaking | 6430 Hz | 4.42 | 4.3 dB  |
| Peaking | 6843 Hz | 1.41 | -2.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NVX%20EX10S/NVX%20EX10S.png)