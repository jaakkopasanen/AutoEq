# Sony MDR-1000X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.6dB
GraphicEQ: 21 -5.6; 23 -5.2; 25 -4.9; 28 -4.5; 31 -4.2; 34 -3.9; 37 -3.7; 41 -3.5; 45 -3.4; 49 -3.4; 54 -3.5; 60 -3.7; 66 -4.0; 72 -4.3; 79 -4.7; 87 -5.0; 96 -5.4; 106 -5.7; 116 -5.9; 128 -6.1; 141 -6.1; 155 -5.9; 170 -5.6; 187 -5.2; 206 -4.7; 227 -4.1; 249 -4.0; 274 -4.2; 302 -3.9; 332 -3.3; 365 -2.7; 402 -2.7; 442 -3.2; 486 -3.2; 535 -2.9; 588 -1.5; 647 -2.1; 712 -3.7; 783 -2.8; 861 -1.0; 947 -0.8; 1042 0.7; 1146 2.4; 1261 2.0; 1387 0.5; 1526 -1.9; 1678 -3.3; 1846 -4.1; 2031 -3.6; 2234 -2.4; 2457 -0.6; 2703 0.3; 2973 0.1; 3270 0.4; 3597 0.4; 3957 -1.8; 4353 -3.4; 4788 -2.4; 5267 -2.7; 5793 -3.1; 6373 -2.2; 7010 -0.2; 7711 -1.3; 8482 -3.4; 9330 -3.1; 10263 -0.5; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-1000X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-25**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-1000X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 1.3  | -5.6 dB |
| Peaking | 23 Hz   | 0.87 | -3.1 dB |
| Peaking | 135 Hz  | 0.55 | -5.8 dB |
| Peaking | 535 Hz  | 1.52 | -1.7 dB |
| Peaking | 1906 Hz | 4.06 | -4.4 dB |
| Peaking | 739 Hz  | 8.46 | -2.5 dB |
| Peaking | 1185 Hz | 4.65 | 3.6 dB  |
| Peaking | 3457 Hz | 2.18 | 4.5 dB  |
| Peaking | 4247 Hz | 1.4  | -5.1 dB |
| Peaking | 8840 Hz | 5.8  | -3.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Sony%20MDR-1000X/Sony%20MDR-1000X.png)