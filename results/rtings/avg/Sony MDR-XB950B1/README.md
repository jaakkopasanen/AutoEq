# Sony MDR-XB950B1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -6.5; 23 -6.7; 25 -6.8; 28 -7.0; 31 -7.1; 34 -7.1; 37 -7.0; 41 -6.9; 45 -6.8; 49 -6.8; 54 -6.8; 60 -6.9; 66 -7.2; 72 -7.4; 79 -7.7; 87 -8.1; 96 -8.4; 106 -8.6; 116 -8.7; 128 -8.7; 141 -8.4; 155 -7.8; 170 -7.0; 187 -6.9; 206 -6.0; 227 -4.5; 249 -3.1; 274 -1.2; 302 1.2; 332 3.7; 365 5.1; 402 3.8; 442 1.5; 486 -0.0; 535 -0.8; 588 -1.1; 647 -1.1; 712 -1.0; 783 -0.7; 861 -0.4; 947 -0.2; 1042 0.3; 1146 1.1; 1261 1.2; 1387 1.6; 1526 1.9; 1678 2.0; 1846 2.5; 2031 2.7; 2234 3.4; 2457 4.6; 2703 5.8; 2973 6.0; 3270 6.0; 3597 6.0; 3957 5.8; 4353 2.4; 4788 5.8; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-XB950B1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB950B1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.84 | -5.1 dB |
| Peaking | 134 Hz  | 0.37 | -8.6 dB |
| Peaking | 351 Hz  | 2.11 | 10.0 dB |
| Peaking | 3041 Hz | 1.11 | 6.0 dB  |
| Peaking | 5743 Hz | 3.31 | 5.0 dB  |
| Peaking | 257 Hz  | 2.17 | 1.1 dB  |
| Peaking | 383 Hz  | 0.93 | -1.2 dB |
| Peaking | 405 Hz  | 4.08 | 1.7 dB  |
| Peaking | 1249 Hz | 2.56 | 1.0 dB  |
| Peaking | 8412 Hz | 3.67 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20MDR-XB950B1/Sony%20MDR-XB950B1.png)