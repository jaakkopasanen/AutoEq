# Sony MDR-NC8

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.9; 66 5.0; 72 4.2; 79 3.4; 87 2.6; 96 1.9; 106 1.1; 116 0.6; 128 0.9; 141 1.6; 155 2.8; 170 3.8; 187 3.4; 206 2.6; 227 2.8; 249 3.1; 274 3.7; 302 4.5; 332 5.0; 365 5.5; 402 5.9; 442 6.0; 486 5.6; 535 4.8; 588 4.3; 647 4.6; 712 3.2; 783 2.0; 861 2.8; 947 0.8; 1042 0.1; 1146 1.7; 1261 3.4; 1387 4.0; 1526 4.3; 1678 4.7; 1846 4.8; 2031 5.2; 2234 5.9; 2457 5.3; 2703 5.1; 2973 4.7; 3270 5.1; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 -0.3; 8482 -3.9; 9330 -3.7; 10263 -1.2; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-NC8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-NC8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.59 | 6.7 dB  |
| Peaking | 410 Hz  | 0.99 | 5.8 dB  |
| Peaking | 2020 Hz | 1.37 | 3.9 dB  |
| Peaking | 5454 Hz | 0.79 | 7.0 dB  |
| Peaking | 8799 Hz | 2.4  | -8.3 dB |
| Peaking | 61 Hz   | 3.69 | 1.4 dB  |
| Peaking | 118 Hz  | 2.32 | -1.7 dB |
| Peaking | 168 Hz  | 4.59 | 2.3 dB  |
| Peaking | 1038 Hz | 6.53 | -2.6 dB |
| Peaking | 1359 Hz | 4.58 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Sony%20MDR-NC8/Sony%20MDR-NC8.png)