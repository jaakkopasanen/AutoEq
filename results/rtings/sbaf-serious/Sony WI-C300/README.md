# Sony WI-C300

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.9; 34 5.6; 37 5.0; 41 4.4; 45 3.8; 49 3.3; 54 2.6; 60 1.8; 66 1.1; 72 0.6; 79 0.0; 87 -0.6; 96 -1.3; 106 -2.1; 116 -2.8; 128 -3.5; 141 -4.1; 155 -4.4; 170 -4.5; 187 -4.7; 206 -4.8; 227 -4.6; 249 -4.1; 274 -3.5; 302 -2.9; 332 -2.5; 365 -2.1; 402 -1.7; 442 -1.2; 486 -0.6; 535 -0.0; 588 0.5; 647 1.0; 712 1.4; 783 1.4; 861 1.1; 947 0.5; 1042 -0.4; 1146 -1.2; 1261 -2.0; 1387 -2.4; 1526 -3.2; 1678 -3.6; 1846 -3.6; 2031 -3.5; 2234 -3.0; 2457 -2.3; 2703 -1.7; 2973 -1.2; 3270 -0.6; 3597 -0.6; 3957 -2.0; 4353 -4.1; 4788 -4.3; 5267 -2.3; 5793 1.1; 6373 3.3; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -1.2; 10263 -1.9; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WI-C300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WI-C300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 0.7  | 6.5 dB  |
| Peaking | 176 Hz   | 0.92 | -5.4 dB |
| Peaking | 1843 Hz  | 1.99 | -4.0 dB |
| Peaking | 4672 Hz  | 3.79 | -5.0 dB |
| Peaking | 6474 Hz  | 5.16 | 4.8 dB  |
| Peaking | 351 Hz   | 1.55 | -0.8 dB |
| Peaking | 755 Hz   | 1.5  | 2.4 dB  |
| Peaking | 1258 Hz  | 2.44 | -1.3 dB |
| Peaking | 9852 Hz  | 6.86 | -3.5 dB |
| Peaking | 10277 Hz | 2.39 | 0.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sony%20WI-C300/Sony%20WI-C300.png)