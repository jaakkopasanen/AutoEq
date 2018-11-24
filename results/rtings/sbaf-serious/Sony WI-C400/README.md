# Sony WI-C400

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.9; 66 5.1; 72 4.3; 79 3.4; 87 2.4; 96 1.3; 106 0.1; 116 -1.0; 128 -2.0; 141 -2.9; 155 -3.5; 170 -4.0; 187 -4.3; 206 -4.5; 227 -4.5; 249 -4.2; 274 -4.0; 302 -3.7; 332 -3.2; 365 -2.6; 402 -2.0; 442 -1.3; 486 -0.6; 535 0.0; 588 0.6; 647 1.1; 712 1.4; 783 1.5; 861 1.3; 947 0.5; 1042 -0.3; 1146 -0.9; 1261 -1.8; 1387 -2.5; 1526 -2.9; 1678 -3.3; 1846 -3.3; 2031 -3.2; 2234 -2.7; 2457 -2.2; 2703 -2.1; 2973 -2.0; 3270 -1.8; 3597 -1.7; 3957 -3.0; 4353 -5.0; 4788 -5.2; 5267 -4.4; 5793 -2.7; 6373 -1.4; 7010 0.2; 7711 -0.3; 8482 -3.5; 9330 -4.0; 10263 -0.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WI-C400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WI-C400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 39 Hz    | 0.41 | 7.0 dB  |
| Peaking | 183 Hz   | 0.89 | -6.5 dB |
| Peaking | 1834 Hz  | 2.04 | -3.5 dB |
| Peaking | 4740 Hz  | 2.16 | -5.1 dB |
| Peaking | 22256 Hz | 2.16 | -1.4 dB |
| Peaking | 336 Hz   | 2.45 | -1.3 dB |
| Peaking | 745 Hz   | 1.55 | 2.4 dB  |
| Peaking | 1314 Hz  | 2.97 | -1.3 dB |
| Peaking | 7271 Hz  | 4.84 | 2.0 dB  |
| Peaking | 8930 Hz  | 6.01 | -4.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sony%20WI-C400/Sony%20WI-C400.png)