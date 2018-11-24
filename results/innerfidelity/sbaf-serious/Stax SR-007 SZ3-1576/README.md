# Stax SR-007 SZ3-1576

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.9; 34 5.3; 37 4.6; 41 4.0; 45 3.8; 49 4.0; 54 4.7; 60 4.8; 66 3.9; 72 2.5; 79 2.5; 87 3.0; 96 3.1; 106 3.1; 116 3.2; 128 3.2; 141 3.2; 155 3.2; 170 3.0; 187 3.0; 206 3.0; 227 3.0; 249 2.9; 274 3.0; 302 2.8; 332 2.7; 365 2.6; 402 2.5; 442 2.4; 486 2.2; 535 3.7; 588 3.6; 647 2.3; 712 1.6; 783 1.1; 861 0.3; 947 -0.0; 1042 0.5; 1146 0.7; 1261 3.8; 1387 5.1; 1526 0.9; 1678 0.1; 1846 2.6; 2031 4.3; 2234 5.7; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 5.9; 4788 3.9; 5267 4.7; 5793 5.9; 6373 3.9; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-007 SZ3-1576 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-007 SZ3-1576 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.25 | 6.3 dB  |
| Peaking | 221 Hz  | 0.57 | 2.7 dB  |
| Peaking | 563 Hz  | 5.46 | 2.9 dB  |
| Peaking | 3084 Hz | 1.02 | 6.5 dB  |
| Peaking | 5804 Hz | 4.43 | 3.9 dB  |
| Peaking | 1050 Hz | 2.12 | -3.0 dB |
| Peaking | 1346 Hz | 5.89 | 4.0 dB  |
| Peaking | 1352 Hz | 1.04 | 2.1 dB  |
| Peaking | 1604 Hz | 4.79 | -4.7 dB |
| Peaking | 8670 Hz | 2.89 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-007%20SZ3-1576/Stax%20SR-007%20SZ3-1576.png)