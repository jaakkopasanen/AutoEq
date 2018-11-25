# Sony WH-CH500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.6; 34 4.0; 37 2.3; 41 0.3; 45 -1.2; 49 -2.5; 54 -3.6; 60 -4.5; 66 -5.2; 72 -5.5; 79 -5.5; 87 -5.2; 96 -4.8; 106 -4.2; 116 -3.7; 128 -3.0; 141 -2.3; 155 -1.7; 170 -1.1; 187 -0.6; 206 -0.2; 227 0.2; 249 0.4; 274 0.6; 302 0.7; 332 0.7; 365 0.9; 402 1.4; 442 1.3; 486 0.7; 535 0.3; 588 0.1; 647 0.5; 712 0.7; 783 0.6; 861 0.4; 947 0.1; 1042 0.1; 1146 0.1; 1261 -0.3; 1387 -0.4; 1526 -0.4; 1678 -0.3; 1846 -0.1; 2031 0.2; 2234 1.0; 2457 1.5; 2703 1.3; 2973 0.5; 3270 0.6; 3597 1.2; 3957 3.9; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 4.1; 7010 1.4; 7711 -0.7; 8482 -3.3; 9330 -6.9; 10263 -5.3; 11289 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WH-CH500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WH-CH500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 1.24 | 7.6 dB  |
| Peaking | 73 Hz    | 1.05 | -6.8 dB |
| Peaking | 4462 Hz  | 3.43 | 5.2 dB  |
| Peaking | 5792 Hz  | 3.14 | 5.5 dB  |
| Peaking | 9476 Hz  | 4.11 | -8.2 dB |
| Peaking | 255 Hz   | 2.95 | 0.9 dB  |
| Peaking | 414 Hz   | 2.32 | 1.4 dB  |
| Peaking | 2431 Hz  | 6.13 | 1.2 dB  |
| Peaking | 10716 Hz | 4.86 | 1.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Sony%20WH-CH500/Sony%20WH-CH500.png)