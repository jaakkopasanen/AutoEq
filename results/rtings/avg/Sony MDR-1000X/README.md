# Sony MDR-1000X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.6dB
GraphicEQ: 21 -5.6; 23 -5.2; 25 -4.9; 28 -4.5; 31 -4.2; 34 -3.9; 37 -3.7; 41 -3.5; 45 -3.4; 49 -3.4; 54 -3.5; 60 -3.7; 66 -4.0; 72 -4.3; 79 -4.7; 87 -5.0; 96 -5.4; 106 -5.7; 116 -5.9; 128 -6.1; 141 -6.1; 155 -5.9; 170 -5.6; 187 -5.2; 206 -4.7; 227 -4.1; 249 -4.0; 274 -4.2; 302 -3.9; 332 -3.3; 365 -2.7; 402 -2.7; 442 -3.2; 486 -3.2; 535 -2.9; 588 -1.5; 647 -2.1; 712 -3.7; 783 -2.8; 861 -1.0; 947 -0.8; 1042 0.7; 1146 2.4; 1261 2.0; 1387 0.5; 1526 -1.9; 1678 -3.3; 1846 -4.1; 2031 -3.6; 2234 -2.4; 2457 -0.6; 2703 0.1; 2973 -0.4; 3270 -0.3; 3597 -0.6; 3957 -3.1; 4353 -4.7; 4788 -4.2; 5267 -5.3; 5793 -5.5; 6373 -3.4; 7010 -1.1; 7711 -2.7; 8482 -4.1; 9330 -1.7; 10263 0.0
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
| Peaking | 19 Hz   | 0.78 | -5.2 dB |
| Peaking | 136 Hz  | 0.57 | -5.8 dB |
| Peaking | 528 Hz  | 1.56 | -1.8 dB |
| Peaking | 1878 Hz | 4.82 | -4.2 dB |
| Peaking | 5403 Hz | 1.79 | -5.5 dB |
| Peaking | 740 Hz  | 7.81 | -2.5 dB |
| Peaking | 1180 Hz | 4.89 | 3.5 dB  |
| Peaking | 7016 Hz | 6.46 | 2.6 dB  |
| Peaking | 8605 Hz | 3.23 | -4.5 dB |
| Peaking | 9702 Hz | 2.52 | 2.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20MDR-1000X/Sony%20MDR-1000X.png)