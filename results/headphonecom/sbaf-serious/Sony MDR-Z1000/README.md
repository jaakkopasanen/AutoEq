# Sony MDR-Z1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.9; 66 5.1; 72 4.3; 79 3.5; 87 2.8; 96 2.5; 106 2.0; 116 1.3; 128 0.4; 141 -0.2; 155 -0.2; 170 0.4; 187 0.5; 206 0.8; 227 1.2; 249 1.7; 274 2.7; 302 1.7; 332 0.8; 365 0.2; 402 -0.2; 442 -0.4; 486 -0.6; 535 -0.4; 588 -0.2; 647 0.0; 712 0.3; 783 -0.0; 861 0.1; 947 -0.1; 1042 0.1; 1146 -0.1; 1261 -0.7; 1387 -1.7; 1526 -3.0; 1678 -4.0; 1846 -4.2; 2031 -3.8; 2234 -1.9; 2457 -0.5; 2703 0.9; 2973 2.5; 3270 4.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -2.9; 9330 -7.1; 10263 -2.9; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-Z1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-Z1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 36 Hz   | 0.62 | 6.8 dB   |
| Peaking | 275 Hz  | 5.8  | 2.5 dB   |
| Peaking | 1919 Hz | 1.7  | -6.7 dB  |
| Peaking | 4642 Hz | 0.73 | 7.3 dB   |
| Peaking | 9255 Hz | 3.56 | -10.2 dB |
| Peaking | 40 Hz   | 2.76 | -1.0 dB  |
| Peaking | 64 Hz   | 2.45 | 1.4 dB   |
| Peaking | 141 Hz  | 3.87 | -1.6 dB  |
| Peaking | 474 Hz  | 4.26 | -0.8 dB  |
| Peaking | 1098 Hz | 4.49 | 0.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-Z1000/Sony%20MDR-Z1000.png)