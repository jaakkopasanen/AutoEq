# Bedphones
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 6.0; 128 6.0; 141 6.0; 155 6.0; 170 5.6; 187 4.6; 206 3.5; 227 2.8; 249 2.1; 274 1.6; 302 1.3; 332 0.9; 365 0.8; 402 0.6; 442 0.8; 486 0.6; 535 0.7; 588 1.3; 647 0.9; 712 0.5; 783 0.6; 861 0.3; 947 0.0; 1042 -0.1; 1146 -0.3; 1261 -0.4; 1387 -0.6; 1526 -0.6; 1678 0.2; 1846 1.9; 2031 4.0; 2234 5.9; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bedphones GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bedphones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 62 Hz   | 0.7  | -3.8 dB |
| Peaking | 66 Hz   | 0.25 | 9.9 dB  |
| Peaking | 310 Hz  | 0.67 | -2.9 dB |
| Peaking | 2673 Hz | 2    | 5.6 dB  |
| Peaking | 4939 Hz | 1.57 | 6.1 dB  |
| Peaking | 162 Hz  | 5.46 | 1.1 dB  |
| Peaking | 1495 Hz | 2.53 | -2.0 dB |
| Peaking | 2139 Hz | 5.77 | 2.1 dB  |
| Peaking | 6426 Hz | 4.58 | 3.5 dB  |
| Peaking | 7516 Hz | 1.79 | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bedphones/Bedphones.png)