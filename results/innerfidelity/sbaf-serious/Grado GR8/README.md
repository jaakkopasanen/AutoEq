# Grado GR8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.3; 25 3.3; 28 3.2; 31 3.1; 34 3.0; 37 2.9; 41 2.7; 45 2.6; 49 2.4; 54 2.2; 60 1.8; 66 1.5; 72 1.1; 79 0.7; 87 0.3; 96 -0.2; 106 -0.5; 116 -0.7; 128 -1.1; 141 -1.4; 155 -1.6; 170 -1.7; 187 -1.8; 206 -1.9; 227 -2.0; 249 -2.0; 274 -2.0; 302 -1.9; 332 -1.8; 365 -1.7; 402 -1.6; 442 -1.4; 486 -1.3; 535 -0.7; 588 -0.3; 647 0.0; 712 0.3; 783 0.5; 861 0.4; 947 0.2; 1042 -0.1; 1146 -0.3; 1261 -0.4; 1387 -0.7; 1526 -1.1; 1678 -1.2; 1846 -0.9; 2031 -0.6; 2234 -0.4; 2457 0.5; 2703 3.3; 2973 6.0; 3270 6.0; 3597 5.3; 3957 -0.5; 4353 -1.1; 4788 0.7; 5267 2.0; 5793 0.5; 6373 -2.5; 7010 1.0; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado GR8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado GR8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.66 | 3.2 dB  |
| Peaking | 53 Hz    | 1.19 | 1.4 dB  |
| Peaking | 224 Hz   | 0.65 | -2.2 dB |
| Peaking | 3167 Hz  | 4.32 | 7.2 dB  |
| Peaking | 21749 Hz | 2.17 | -0.2 dB |
| Peaking | 779 Hz   | 2.94 | 1.1 dB  |
| Peaking | 1722 Hz  | 2.15 | -1.4 dB |
| Peaking | 3614 Hz  | 7.98 | 3.7 dB  |
| Peaking | 4066 Hz  | 4.68 | -3.5 dB |
| Peaking | 5159 Hz  | 8.65 | 2.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20GR8/Grado%20GR8.png)