# Sony WH-CH500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.6; 34 4.0; 37 2.3; 41 0.3; 45 -1.2; 49 -2.5; 54 -3.6; 60 -4.5; 66 -5.2; 72 -5.5; 79 -5.5; 87 -5.2; 96 -4.8; 106 -4.2; 116 -3.7; 128 -3.0; 141 -2.3; 155 -1.7; 170 -1.1; 187 -0.6; 206 -0.2; 227 0.2; 249 0.4; 274 0.6; 302 0.7; 332 0.7; 365 0.9; 402 1.4; 442 1.3; 486 0.7; 535 0.3; 588 0.1; 647 0.5; 712 0.7; 783 0.6; 861 0.4; 947 0.1; 1042 0.1; 1146 0.1; 1261 -0.3; 1387 -0.4; 1526 -0.4; 1678 -0.3; 1846 -0.1; 2031 0.2; 2234 1.1; 2457 1.5; 2703 1.1; 2973 0.0; 3270 -0.2; 3597 0.1; 3957 2.7; 4353 5.6; 4788 6.0; 5267 4.7; 5793 5.4; 6373 2.9; 7010 0.8; 7711 -1.1; 8482 -2.4; 9330 -4.2; 10263 -3.0; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WH-CH500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WH-CH500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 1.23 | 7.6 dB  |
| Peaking | 73 Hz   | 1.07 | -6.7 dB |
| Peaking | 1512 Hz | 4.26 | -0.6 dB |
| Peaking | 5062 Hz | 2.19 | 6.5 dB  |
| Peaking | 9273 Hz | 3.28 | -5.0 dB |
| Peaking | 129 Hz  | 1.98 | -1.1 dB |
| Peaking | 281 Hz  | 0.67 | 1.0 dB  |
| Peaking | 418 Hz  | 5.46 | 0.9 dB  |
| Peaking | 2448 Hz | 6.02 | 1.3 dB  |
| Peaking | 3353 Hz | 5.62 | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20WH-CH500/Sony%20WH-CH500.png)