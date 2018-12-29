# Monster DNA Pro2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 21 0.0; 23 4.3; 25 3.2; 28 1.8; 31 0.7; 34 -0.1; 37 -0.7; 41 -1.1; 45 -1.4; 49 -1.4; 54 -1.4; 60 -1.3; 66 -1.3; 72 -1.3; 79 -1.3; 87 -1.3; 96 -1.2; 106 -1.3; 116 -1.4; 128 -1.7; 141 -1.8; 155 -1.9; 170 -1.5; 187 -1.6; 206 -1.6; 227 -1.3; 249 -1.3; 274 -0.6; 302 0.2; 332 1.1; 365 1.9; 402 3.1; 442 1.4; 486 -0.2; 535 -0.7; 588 -0.8; 647 -1.0; 712 -1.2; 783 -1.0; 861 -0.9; 947 -0.6; 1042 0.5; 1146 1.8; 1261 2.8; 1387 3.1; 1526 2.8; 1678 1.7; 1846 0.2; 2031 -1.4; 2234 -3.5; 2457 -4.9; 2703 -4.4; 2973 -2.5; 3270 -0.5; 3597 0.8; 3957 -3.1; 4353 -2.9; 4788 -0.2; 5267 5.3; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster DNA Pro2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster DNA Pro2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 21 Hz   |  3.48 | 5.5 dB  |
| Peaking | 1426 Hz |  3.17 | 3.9 dB  |
| Peaking | 2486 Hz |  3.34 | -5.7 dB |
| Peaking | 4296 Hz |  5.74 | -5.1 dB |
| Peaking | 5781 Hz |  3.15 | 7.2 dB  |
| Peaking | 23 Hz   |  1.54 | 2.8 dB  |
| Peaking | 89 Hz   |  0.21 | -1.7 dB |
| Peaking | 391 Hz  |  3.18 | 4.2 dB  |
| Peaking | 660 Hz  |  1.87 | -1.1 dB |
| Peaking | 3535 Hz | 11.4  | 1.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20DNA%20Pro2/Monster%20DNA%20Pro2.png)