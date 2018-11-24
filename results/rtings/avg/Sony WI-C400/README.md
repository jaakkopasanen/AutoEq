# Sony WI-C400

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 5.2; 72 4.3; 79 3.2; 87 2.0; 96 0.8; 106 -0.4; 116 -1.5; 128 -2.6; 141 -3.5; 155 -4.1; 170 -4.6; 187 -4.9; 206 -5.0; 227 -5.0; 249 -4.7; 274 -4.6; 302 -4.5; 332 -4.1; 365 -3.6; 402 -3.0; 442 -2.4; 486 -1.8; 535 -1.1; 588 -0.5; 647 0.1; 712 0.6; 783 1.0; 861 1.1; 947 0.5; 1042 -0.3; 1146 -1.1; 1261 -2.1; 1387 -2.5; 1526 -2.6; 1678 -2.9; 1846 -3.3; 2031 -3.6; 2234 -3.2; 2457 -2.7; 2703 -2.9; 2973 -3.6; 3270 -4.4; 3597 -4.9; 3957 -5.4; 4353 -6.3; 4788 -6.8; 5267 -7.3; 5793 -6.6; 6373 -5.2; 7010 -3.0; 7711 -1.8; 8482 -2.9; 9330 -2.8; 10263 -0.1; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -0.2; 16529 -5.2; 18182 -4.9; 20000 0.0
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
| Peaking | 42 Hz    | 0.41 | 7.3 dB  |
| Peaking | 183 Hz   | 0.73 | -7.3 dB |
| Peaking | 1878 Hz  | 2.06 | -2.7 dB |
| Peaking | 4900 Hz  | 1.26 | -7.2 dB |
| Peaking | 17562 Hz | 2.83 | -6.6 dB |
| Peaking | 360 Hz   | 2.54 | -1.2 dB |
| Peaking | 809 Hz   | 1.86 | 2.2 dB  |
| Peaking | 1276 Hz  | 3.61 | -1.4 dB |
| Peaking | 12733 Hz | 1.27 | 3.0 dB  |
| Peaking | 13804 Hz | 0.71 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20WI-C400/Sony%20WI-C400.png)