# VSonic GR07 Classic
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.6; 25 1.2; 28 0.8; 31 0.4; 34 0.2; 37 -0.1; 41 -0.3; 45 -0.5; 49 -0.7; 54 -1.0; 60 -1.3; 66 -1.5; 72 -1.7; 79 -2.1; 87 -2.3; 96 -2.6; 106 -2.8; 116 -2.8; 128 -3.0; 141 -3.1; 155 -3.1; 170 -3.1; 187 -3.0; 206 -2.9; 227 -2.8; 249 -2.7; 274 -2.4; 302 -2.2; 332 -2.0; 365 -1.8; 402 -1.6; 442 -1.2; 486 -1.1; 535 -0.8; 588 -0.2; 647 -0.0; 712 0.2; 783 0.5; 861 0.4; 947 0.2; 1042 -0.0; 1146 -0.2; 1261 -0.4; 1387 -0.8; 1526 -1.6; 1678 -2.0; 1846 -2.0; 2031 -1.8; 2234 -1.3; 2457 -0.0; 2703 1.9; 2973 4.3; 3270 6.0; 3597 6.0; 3957 5.8; 4353 3.0; 4788 0.5; 5267 -0.9; 5793 0.4; 6373 4.2; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`VSonic GR07 Classic GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic GR07 Classic ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 1.35 | 2.4 dB  |
| Peaking | 152 Hz   | 0.55 | -3.3 dB |
| Peaking | 1990 Hz  | 2.08 | -3.1 dB |
| Peaking | 3446 Hz  | 2.25 | 7.1 dB  |
| Peaking | 23652 Hz | 2.3  | 1.0 dB  |
| Peaking | 21 Hz    | 0.98 | 0.4 dB  |
| Peaking | 801 Hz   | 2.74 | 1.0 dB  |
| Peaking | 4098 Hz  | 6.12 | 2.3 dB  |
| Peaking | 5592 Hz  | 1.9  | -3.6 dB |
| Peaking | 6427 Hz  | 4.87 | 6.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/VSonic%20GR07%20Classic/VSonic%20GR07%20Classic.png)