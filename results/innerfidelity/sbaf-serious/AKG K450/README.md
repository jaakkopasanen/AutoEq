# AKG K450
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.9; 34 5.5; 37 5.0; 41 4.5; 45 4.1; 49 3.7; 54 3.3; 60 3.0; 66 2.7; 72 2.4; 79 2.1; 87 1.8; 96 1.4; 106 1.1; 116 0.8; 128 0.5; 141 0.0; 155 -0.2; 170 -0.3; 187 -0.5; 206 -0.6; 227 -0.7; 249 -0.9; 274 -0.7; 302 -0.8; 332 -0.9; 365 -0.8; 402 -0.4; 442 -0.5; 486 -0.8; 535 -1.0; 588 -0.5; 647 -0.3; 712 -0.1; 783 -0.0; 861 -0.0; 947 0.4; 1042 0.8; 1146 1.0; 1261 2.0; 1387 2.9; 1526 3.9; 1678 4.9; 1846 5.6; 2031 6.0; 2234 6.0; 2457 6.0; 2703 5.5; 2973 3.5; 3270 1.2; 3597 0.1; 3957 1.4; 4353 2.8; 4788 5.7; 5267 6.0; 5793 5.4; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K450 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K450 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.36 | 6.2 dB  |
| Peaking | 1378 Hz | 0.09 | -1.5 dB |
| Peaking | 2226 Hz | 0.93 | 7.9 dB  |
| Peaking | 3545 Hz | 3.28 | -4.2 dB |
| Peaking | 5508 Hz | 2.07 | 6.6 dB  |
| Peaking | 197 Hz  | 3.25 | -0.2 dB |
| Peaking | 6556 Hz | 8.64 | 1.9 dB  |
| Peaking | 7623 Hz | 3.84 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K450/AKG%20K450.png)