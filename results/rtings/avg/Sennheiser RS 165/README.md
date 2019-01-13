# Sennheiser RS 165
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.8; 23 -1.9; 25 -1.8; 28 -1.8; 31 -1.6; 34 -1.3; 37 -1.0; 41 -0.5; 45 -0.1; 49 0.3; 54 0.7; 60 0.9; 66 0.5; 72 0.1; 79 -0.4; 87 -1.2; 96 -2.0; 106 -2.7; 116 -3.1; 128 -3.2; 141 -3.1; 155 -2.7; 170 -2.2; 187 -1.4; 206 -0.3; 227 0.9; 249 1.9; 274 2.0; 302 1.7; 332 2.0; 365 3.0; 402 4.2; 442 4.7; 486 4.3; 535 3.7; 588 3.1; 647 2.7; 712 2.9; 783 2.0; 861 1.2; 947 0.3; 1042 -0.0; 1146 0.3; 1261 -0.0; 1387 0.1; 1526 0.6; 1678 1.6; 1846 1.7; 2031 2.0; 2234 2.6; 2457 3.1; 2703 3.3; 2973 4.0; 3270 5.1; 3597 6.0; 3957 6.0; 4353 6.0; 4788 5.7; 5267 2.1; 5793 2.2; 6373 0.2; 7010 1.2; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser RS 165 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser RS 165 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 2.24 | -2.1 dB |
| Peaking | 136 Hz  | 1.57 | -3.8 dB |
| Peaking | 249 Hz  | 4.84 | 1.7 dB  |
| Peaking | 464 Hz  | 1.41 | 4.7 dB  |
| Peaking | 3762 Hz | 1.5  | 6.4 dB  |
| Peaking | 58 Hz   | 3.65 | 1.5 dB  |
| Peaking | 735 Hz  | 4.43 | 1.5 dB  |
| Peaking | 1452 Hz | 0.76 | -1.2 dB |
| Peaking | 1739 Hz | 3.35 | 1.5 dB  |
| Peaking | 2323 Hz | 4.1  | 1.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20RS%20165/Sennheiser%20RS%20165.png)