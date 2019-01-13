# Aedle VK1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.3; 45 4.0; 49 2.8; 54 1.3; 60 -0.2; 66 -1.6; 72 -2.7; 79 -3.8; 87 -4.6; 96 -5.1; 106 -5.1; 116 -4.9; 128 -4.7; 141 -4.4; 155 -4.1; 170 -3.7; 187 -3.4; 206 -3.1; 227 -2.7; 249 -2.4; 274 -2.0; 302 -1.4; 332 -0.9; 365 -1.1; 402 -0.7; 442 -0.2; 486 0.2; 535 0.8; 588 -0.1; 647 -0.1; 712 1.5; 783 2.2; 861 1.7; 947 0.7; 1042 -0.5; 1146 -1.7; 1261 -3.0; 1387 -4.4; 1526 -5.6; 1678 -5.8; 1846 -4.2; 2031 -3.9; 2234 -2.8; 2457 -1.2; 2703 0.5; 2973 2.7; 3270 4.1; 3597 5.3; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 5.5; 6373 4.2; 7010 2.4; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Aedle VK1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Aedle VK1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.53 | 9.8 dB  |
| Peaking | 88 Hz   | 0.59 | -9.3 dB |
| Peaking | 847 Hz  | 1.57 | 3.6 dB  |
| Peaking | 1644 Hz | 1.22 | -7.1 dB |
| Peaking | 4272 Hz | 1.22 | 7.6 dB  |
| Peaking | 571 Hz  | 3.37 | 1.6 dB  |
| Peaking | 618 Hz  | 7.84 | -3.0 dB |
| Peaking | 4544 Hz | 4.26 | -1.8 dB |
| Peaking | 6300 Hz | 1.5  | 3.7 dB  |
| Peaking | 7591 Hz | 1.53 | -3.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Aedle%20VK1/Aedle%20VK1.png)