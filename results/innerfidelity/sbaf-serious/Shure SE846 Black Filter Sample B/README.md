# Shure SE846 Black Filter Sample B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -5.1; 23 -5.1; 25 -5.1; 28 -5.1; 31 -5.0; 34 -5.0; 37 -4.9; 41 -4.9; 45 -4.9; 49 -4.8; 54 -4.8; 60 -4.8; 66 -4.8; 72 -4.8; 79 -4.8; 87 -4.9; 96 -4.9; 106 -4.7; 116 -4.6; 128 -4.5; 141 -4.4; 155 -4.1; 170 -3.9; 187 -3.6; 206 -3.4; 227 -3.1; 249 -2.8; 274 -2.6; 302 -2.3; 332 -2.0; 365 -1.7; 402 -1.5; 442 -1.2; 486 -1.1; 535 -0.8; 588 -0.3; 647 -0.0; 712 0.1; 783 0.4; 861 0.3; 947 0.1; 1042 -0.1; 1146 -0.2; 1261 -0.3; 1387 -0.6; 1526 -0.8; 1678 -0.7; 1846 -0.3; 2031 0.4; 2234 1.3; 2457 3.2; 2703 5.3; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE846 Black Filter Sample B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE846 Black Filter Sample B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.35 | -4.6 dB |
| Peaking | 124 Hz  | 0.46 | -3.8 dB |
| Peaking | 3129 Hz | 2.53 | 5.0 dB  |
| Peaking | 5519 Hz | 1.33 | 6.8 dB  |
| Peaking | 8051 Hz | 1.87 | -2.9 dB |
| Peaking | 805 Hz  | 1.88 | 1.0 dB  |
| Peaking | 1800 Hz | 0.94 | -1.4 dB |
| Peaking | 2606 Hz | 5.58 | 2.0 dB  |
| Peaking | 4083 Hz | 4.91 | 1.2 dB  |
| Peaking | 5263 Hz | 9.11 | -0.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SE846%20Black%20Filter%20Sample%20B/Shure%20SE846%20Black%20Filter%20Sample%20B.png)