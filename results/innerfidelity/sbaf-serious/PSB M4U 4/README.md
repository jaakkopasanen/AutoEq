# PSB M4U 4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.2; 23 -1.5; 25 -1.8; 28 -2.0; 31 -2.2; 34 -2.3; 37 -2.4; 41 -2.5; 45 -2.5; 49 -2.4; 54 -2.4; 60 -2.4; 66 -2.4; 72 -2.4; 79 -2.4; 87 -2.4; 96 -2.4; 106 -2.2; 116 -2.1; 128 -1.9; 141 -1.8; 155 -1.6; 170 -1.3; 187 -1.1; 206 -0.8; 227 -0.4; 249 -0.2; 274 0.1; 302 0.3; 332 0.6; 365 0.8; 402 0.9; 442 1.2; 486 1.2; 535 1.2; 588 1.5; 647 1.5; 712 1.2; 783 1.2; 861 0.8; 947 0.3; 1042 -0.1; 1146 -0.7; 1261 -0.7; 1387 -1.0; 1526 -1.7; 1678 -1.9; 1846 -1.8; 2031 -1.6; 2234 -1.5; 2457 -0.9; 2703 -0.2; 2973 0.7; 3270 1.3; 3597 1.5; 3957 2.1; 4353 1.4; 4788 3.3; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`PSB M4U 4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `PSB M4U 4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 66 Hz   | 0.3  | -2.6 dB |
| Peaking | 698 Hz  | 0.51 | 3.2 dB  |
| Peaking | 2453 Hz | 0.37 | -4.5 dB |
| Peaking | 3293 Hz | 1.49 | 4.1 dB  |
| Peaking | 5698 Hz | 2.22 | 8.5 dB  |
| Peaking | 6635 Hz | 7.29 | 2.4 dB  |
| Peaking | 7117 Hz | 2.03 | -1.9 dB |
| Peaking | 8825 Hz | 0.7  | 0.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/PSB%20M4U%204/PSB%20M4U%204.png)