# Accidentally Extraordinary Bamboo
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.6; 25 3.0; 28 2.2; 31 1.5; 34 0.9; 37 0.4; 41 -0.2; 45 -0.8; 49 -1.4; 54 -2.0; 60 -2.7; 66 -3.3; 72 -3.9; 79 -4.6; 87 -5.2; 96 -5.9; 106 -6.3; 116 -6.7; 128 -7.2; 141 -7.5; 155 -7.9; 170 -8.1; 187 -8.1; 206 -8.2; 227 -8.0; 249 -7.8; 274 -7.4; 302 -7.0; 332 -6.4; 365 -5.7; 402 -4.9; 442 -4.0; 486 -3.4; 535 -2.6; 588 -1.5; 647 -0.9; 712 0.6; 783 0.7; 861 1.0; 947 0.4; 1042 -0.2; 1146 -0.8; 1261 -1.9; 1387 -3.3; 1526 -5.2; 1678 -6.8; 1846 -7.8; 2031 -7.8; 2234 -6.8; 2457 -4.5; 2703 -1.6; 2973 1.7; 3270 4.7; 3597 6.0; 3957 5.8; 4353 3.9; 4788 2.9; 5267 2.3; 5793 -0.1; 6373 -6.0; 7010 -6.3; 7711 -2.1; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Accidentally Extraordinary Bamboo GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Accidentally Extraordinary Bamboo ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.37 | 4.6 dB  |
| Peaking | 175 Hz  | 0.58 | -8.7 dB |
| Peaking | 2036 Hz | 2.02 | -9.9 dB |
| Peaking | 3703 Hz | 1.65 | 7.8 dB  |
| Peaking | 6711 Hz | 5.15 | -9.1 dB |
| Peaking | 173 Hz  | 1.07 | 2.9 dB  |
| Peaking | 235 Hz  | 0.45 | -2.5 dB |
| Peaking | 799 Hz  | 1.38 | 3.4 dB  |
| Peaking | 1438 Hz | 4.51 | -0.8 dB |
| Peaking | 1613 Hz | 5.47 | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Accidentally%20Extraordinary%20Bamboo/Accidentally%20Extraordinary%20Bamboo.png)