# KEF M500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -3.0; 23 -3.0; 25 -3.1; 28 -3.1; 31 -3.1; 34 -3.1; 37 -3.1; 41 -3.1; 45 -3.1; 49 -3.0; 54 -3.0; 60 -3.2; 66 -3.4; 72 -3.5; 79 -3.7; 87 -3.7; 96 -3.8; 106 -4.1; 116 -4.5; 128 -5.2; 141 -5.6; 155 -5.4; 170 -5.3; 187 -5.2; 206 -5.0; 227 -5.1; 249 -4.3; 274 -3.5; 302 -2.6; 332 -1.7; 365 -1.2; 402 -0.9; 442 -1.1; 486 -2.1; 535 -2.7; 588 -2.4; 647 -2.4; 712 -2.1; 783 -1.7; 861 -1.0; 947 -0.2; 1042 0.4; 1146 1.1; 1261 1.2; 1387 1.0; 1526 0.9; 1678 0.8; 1846 0.9; 2031 0.7; 2234 0.1; 2457 -0.2; 2703 -1.0; 2973 -1.7; 3270 -2.2; 3597 -1.5; 3957 0.3; 4353 1.8; 4788 3.3; 5267 4.4; 5793 5.9; 6373 3.8; 7010 2.3; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KEF M500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KEF M500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.23 | -2.9 dB |
| Peaking | 175 Hz  | 0.98 | -4.5 dB |
| Peaking | 613 Hz  | 3.01 | -2.3 dB |
| Peaking | 3270 Hz | 4.21 | -3.0 dB |
| Peaking | 5613 Hz | 2.77 | 6.0 dB  |
| Peaking | 239 Hz  | 6.76 | -0.9 dB |
| Peaking | 380 Hz  | 4.76 | 0.8 dB  |
| Peaking | 806 Hz  | 2.72 | -1.1 dB |
| Peaking | 1271 Hz | 1.51 | 1.5 dB  |
| Peaking | 8320 Hz | 4.17 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/KEF%20M500/KEF%20M500.png)