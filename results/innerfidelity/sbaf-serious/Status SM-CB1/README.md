# Status SM-CB1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.5; 25 4.9; 28 3.9; 31 3.0; 34 2.2; 37 1.5; 41 0.6; 45 -0.1; 49 -0.6; 54 -1.1; 60 -1.6; 66 -2.0; 72 -2.0; 79 -2.3; 87 -2.5; 96 -2.5; 106 -2.1; 116 -2.0; 128 -2.4; 141 -2.6; 155 -2.8; 170 -2.2; 187 -2.5; 206 -2.6; 227 -2.5; 249 -2.4; 274 -1.8; 302 -1.2; 332 -0.9; 365 -0.4; 402 0.2; 442 0.9; 486 1.0; 535 0.8; 588 0.4; 647 -0.3; 712 -0.7; 783 -0.9; 861 -1.1; 947 -0.3; 1042 -0.8; 1146 -1.4; 1261 -1.5; 1387 -1.6; 1526 -1.8; 1678 -1.9; 1846 -1.7; 2031 -0.8; 2234 0.3; 2457 1.8; 2703 2.8; 2973 1.7; 3270 0.6; 3597 0.7; 3957 1.2; 4353 1.9; 4788 3.2; 5267 3.7; 5793 1.7; 6373 2.1; 7010 2.5; 7711 0.3; 8482 -3.1; 9330 -4.3; 10263 -0.1; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Status SM-CB1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Status SM-CB1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.13 | 6.3 dB  |
| Peaking | 107 Hz  | 0.47 | -2.9 dB |
| Peaking | 4984 Hz | 2.48 | 3.4 dB  |
| Peaking | 6823 Hz | 7.78 | 2.9 dB  |
| Peaking | 9010 Hz | 6.12 | -5.5 dB |
| Peaking | 236 Hz  | 3.11 | -1.0 dB |
| Peaking | 478 Hz  | 2.24 | 2.1 dB  |
| Peaking | 1288 Hz | 0.47 | -0.8 dB |
| Peaking | 1658 Hz | 1.99 | -1.4 dB |
| Peaking | 2646 Hz | 4.11 | 3.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Status%20SM-CB1/Status%20SM-CB1.png)