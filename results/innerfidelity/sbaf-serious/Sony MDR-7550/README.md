# Sony MDR-7550

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.7; 25 4.5; 28 4.1; 31 3.9; 34 3.6; 37 3.4; 41 3.2; 45 2.9; 49 2.7; 54 2.4; 60 2.0; 66 1.6; 72 1.3; 79 0.9; 87 0.5; 96 0.0; 106 -0.3; 116 -0.5; 128 -0.9; 141 -1.2; 155 -1.4; 170 -1.5; 187 -1.7; 206 -1.7; 227 -1.7; 249 -1.7; 274 -1.5; 302 -1.5; 332 -1.3; 365 -1.1; 402 -0.9; 442 -0.5; 486 -0.4; 535 -0.2; 588 0.3; 647 0.5; 712 0.6; 783 0.8; 861 0.5; 947 0.2; 1042 -0.0; 1146 -0.1; 1261 -1.0; 1387 -2.1; 1526 -3.1; 1678 -3.5; 1846 -3.3; 2031 -2.4; 2234 -0.9; 2457 1.5; 2703 3.9; 2973 5.9; 3270 6.0; 3597 6.0; 3957 6.0; 4353 2.5; 4788 -1.8; 5267 -2.0; 5793 3.4; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-7550 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7550 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 1.38 | 4.9 dB  |
| Peaking | 45 Hz   | 2.09 | 2.2 dB  |
| Peaking | 1772 Hz | 2.31 | -4.6 dB |
| Peaking | 3242 Hz | 2.41 | 7.4 dB  |
| Peaking | 6354 Hz | 7.69 | 5.7 dB  |
| Peaking | 228 Hz  | 0.94 | -1.9 dB |
| Peaking | 759 Hz  | 2.03 | 1.2 dB  |
| Peaking | 4050 Hz | 6.87 | 3.7 dB  |
| Peaking | 5072 Hz | 4.01 | -5.5 dB |
| Peaking | 5813 Hz | 6.23 | 3.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-7550/Sony%20MDR-7550.png)