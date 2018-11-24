# Sony MDR-ZX700

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 5.6; 60 4.1; 66 3.0; 72 2.5; 79 2.8; 87 2.8; 96 1.3; 106 -0.4; 116 -1.2; 128 -1.6; 141 -2.0; 155 -1.9; 170 -1.0; 187 -2.0; 206 -2.3; 227 -2.6; 249 -2.6; 274 -2.5; 302 -3.0; 332 -3.9; 365 -4.0; 402 -3.5; 442 -3.4; 486 -3.0; 535 -2.4; 588 -1.5; 647 -0.6; 712 0.0; 783 -0.2; 861 0.1; 947 0.2; 1042 -0.1; 1146 -0.0; 1261 -0.3; 1387 -1.2; 1526 -2.5; 1678 -4.1; 1846 -5.8; 2031 -7.3; 2234 -7.2; 2457 -6.1; 2703 -4.9; 2973 -3.8; 3270 -1.5; 3597 1.4; 3957 5.4; 4353 6.0; 4788 6.0; 5267 3.3; 5793 3.8; 6373 3.7; 7010 2.5; 7711 -4.2; 8482 -10.7; 9330 -9.5; 10263 -2.6; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-ZX700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-ZX700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.4dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 34 Hz   | 1    | 7.2 dB   |
| Peaking | 2279 Hz | 1.54 | -8.3 dB  |
| Peaking | 4236 Hz | 3.35 | 6.1 dB   |
| Peaking | 6684 Hz | 1.15 | 6.9 dB   |
| Peaking | 8662 Hz | 3.36 | -16.9 dB |
| Peaking | 90 Hz   | 1.18 | 2.5 dB   |
| Peaking | 120 Hz  | 1.94 | -3.2 dB  |
| Peaking | 217 Hz  | 1.13 | -1.5 dB  |
| Peaking | 395 Hz  | 1.35 | -3.6 dB  |
| Peaking | 956 Hz  | 1.39 | 1.6 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-ZX700/Sony%20MDR-ZX700.png)