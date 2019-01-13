# Creative Fatal1ty
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.6; 25 -0.0; 28 -0.8; 31 -1.4; 34 -1.9; 37 -2.4; 41 -2.9; 45 -3.2; 49 -3.5; 54 -3.7; 60 -4.0; 66 -4.1; 72 -4.2; 79 -4.4; 87 -4.6; 96 -4.5; 106 -4.3; 116 -4.3; 128 -4.4; 141 -4.3; 155 -4.1; 170 -3.6; 187 -3.4; 206 -3.0; 227 -2.4; 249 -1.8; 274 -1.3; 302 -0.4; 332 0.3; 365 1.1; 402 1.5; 442 2.1; 486 2.2; 535 1.8; 588 1.4; 647 0.7; 712 0.1; 783 0.4; 861 -0.0; 947 -0.1; 1042 0.1; 1146 0.4; 1261 0.5; 1387 0.3; 1526 0.5; 1678 1.1; 1846 2.2; 2031 3.7; 2234 5.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative Fatal1ty GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative Fatal1ty ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 1.14 | 3.6 dB  |
| Peaking | 56 Hz   | 0.31 | -2.3 dB |
| Peaking | 294 Hz  | 0.18 | -3.8 dB |
| Peaking | 447 Hz  | 0.93 | 5.9 dB  |
| Peaking | 3427 Hz | 0.74 | 7.4 dB  |
| Peaking | 1659 Hz | 3.82 | -1.0 dB |
| Peaking | 2353 Hz | 3.03 | 1.6 dB  |
| Peaking | 3434 Hz | 2.42 | -1.2 dB |
| Peaking | 6237 Hz | 2.23 | 5.4 dB  |
| Peaking | 7444 Hz | 1.47 | -4.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Creative%20Fatal1ty/Creative%20Fatal1ty.png)