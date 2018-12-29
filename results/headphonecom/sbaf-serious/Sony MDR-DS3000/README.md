# Sony MDR-DS3000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 5.9; 106 5.4; 116 5.1; 128 4.7; 141 4.5; 155 4.2; 170 4.3; 187 4.3; 206 4.2; 227 4.5; 249 4.5; 274 4.7; 302 4.8; 332 5.0; 365 4.6; 402 3.9; 442 3.5; 486 3.2; 535 3.0; 588 2.7; 647 2.4; 712 1.9; 783 1.4; 861 1.5; 947 0.5; 1042 -0.1; 1146 -0.3; 1261 -0.4; 1387 -0.6; 1526 -1.8; 1678 -3.3; 1846 -5.4; 2031 -5.9; 2234 -4.1; 2457 -2.1; 2703 -1.5; 2973 -0.1; 3270 1.6; 3597 2.2; 3957 1.2; 4353 -0.8; 4788 -0.0; 5267 4.1; 5793 5.9; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-DS3000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-DS3000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 40 Hz   | 0.24 | 6.2 dB  |
| Peaking | 364 Hz  | 0.78 | 3.4 dB  |
| Peaking | 1971 Hz | 2.56 | -6.4 dB |
| Peaking | 3450 Hz | 5.82 | 2.7 dB  |
| Peaking | 5977 Hz | 4.13 | 6.8 dB  |
| Peaking | 156 Hz  | 4.96 | -0.3 dB |
| Peaking | 4552 Hz | 7.38 | -4.5 dB |
| Peaking | 4837 Hz | 2.84 | 2.0 dB  |
| Peaking | 8195 Hz | 3.93 | -0.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-DS3000/Sony%20MDR-DS3000.png)