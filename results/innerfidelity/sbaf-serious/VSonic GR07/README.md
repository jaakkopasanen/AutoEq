# VSonic GR07
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.5; 25 3.2; 28 2.7; 31 2.4; 34 2.1; 37 1.8; 41 1.5; 45 1.3; 49 1.0; 54 0.8; 60 0.5; 66 0.1; 72 -0.1; 79 -0.5; 87 -0.8; 96 -1.2; 106 -1.3; 116 -1.5; 128 -1.7; 141 -1.9; 155 -2.1; 170 -2.1; 187 -2.1; 206 -2.1; 227 -2.0; 249 -2.0; 274 -1.9; 302 -1.8; 332 -1.6; 365 -1.5; 402 -1.2; 442 -0.9; 486 -0.9; 535 -0.7; 588 -0.2; 647 -0.0; 712 0.0; 783 0.3; 861 0.2; 947 0.1; 1042 -0.0; 1146 -0.1; 1261 -0.3; 1387 -0.6; 1526 -0.9; 1678 -0.8; 1846 -0.5; 2031 -0.4; 2234 0.3; 2457 1.4; 2703 2.5; 2973 4.2; 3270 5.7; 3597 6.0; 3957 5.6; 4353 3.1; 4788 1.2; 5267 0.3; 5793 -0.5; 6373 1.0; 7010 2.3; 7711 0.3; 8482 -0.0; 9330 -0.4; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`VSonic GR07 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic GR07 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 14 Hz    | 0.45 | 4.5 dB  |
| Peaking | 182 Hz   | 0.62 | -2.4 dB |
| Peaking | 1771 Hz  | 2.33 | -1.3 dB |
| Peaking | 3497 Hz  | 2.41 | 6.7 dB  |
| Peaking | 21732 Hz | 2.07 | -0.4 dB |
| Peaking | 788 Hz   | 3.24 | 0.7 dB  |
| Peaking | 4033 Hz  | 9.36 | 1.3 dB  |
| Peaking | 5896 Hz  | 2.42 | -1.9 dB |
| Peaking | 6815 Hz  | 5.85 | 3.3 dB  |
| Peaking | 9039 Hz  | 5    | -0.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/VSonic%20GR07/VSonic%20GR07.png)