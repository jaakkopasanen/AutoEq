# Sony MDR-V700

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 5.2; 72 3.8; 79 2.4; 87 1.3; 96 0.5; 106 0.4; 116 0.3; 128 0.4; 141 0.6; 155 0.8; 170 1.4; 187 1.7; 206 1.9; 227 2.3; 249 3.0; 274 3.5; 302 3.8; 332 3.9; 365 3.7; 402 5.1; 442 4.4; 486 2.7; 535 0.5; 588 -0.6; 647 -0.6; 712 -0.1; 783 1.0; 861 -0.8; 947 -0.5; 1042 0.5; 1146 1.2; 1261 0.6; 1387 -1.0; 1526 -2.4; 1678 -3.5; 1846 -3.5; 2031 -4.2; 2234 -4.9; 2457 -4.6; 2703 -3.9; 2973 -2.3; 3270 -0.8; 3597 0.7; 3957 2.9; 4353 4.8; 4788 6.0; 5267 6.0; 5793 4.3; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -1.2; 9330 -4.3; 10263 -0.9; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-V700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-V700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.74 | 6.9 dB  |
| Peaking | 352 Hz  | 1.56 | 4.6 dB  |
| Peaking | 2404 Hz | 1.38 | -6.4 dB |
| Peaking | 5059 Hz | 1.29 | 7.4 dB  |
| Peaking | 9219 Hz | 4.14 | -5.8 dB |
| Peaking | 63 Hz   | 2.14 | 4.2 dB  |
| Peaking | 83 Hz   | 0.72 | -2.7 dB |
| Peaking | 193 Hz  | 1.02 | 1.2 dB  |
| Peaking | 608 Hz  | 5.51 | -2.0 dB |
| Peaking | 1179 Hz | 6.69 | 2.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-V700/Sony%20MDR-V700.png)