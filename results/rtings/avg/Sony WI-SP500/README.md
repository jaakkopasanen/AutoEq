# Sony WI-SP500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 5.1; 72 4.0; 79 2.7; 87 1.4; 96 0.3; 106 -0.8; 116 -1.7; 128 -2.5; 141 -3.1; 155 -3.5; 170 -3.8; 187 -4.1; 206 -4.2; 227 -4.4; 249 -4.5; 274 -4.6; 302 -4.7; 332 -4.8; 365 -5.0; 402 -5.1; 442 -5.1; 486 -4.9; 535 -4.7; 588 -4.2; 647 -3.5; 712 -2.4; 783 -1.2; 861 -0.2; 947 0.1; 1042 -0.1; 1146 -0.2; 1261 -0.1; 1387 0.3; 1526 0.8; 1678 0.9; 1846 0.5; 2031 -0.2; 2234 -0.7; 2457 -0.7; 2703 0.1; 2973 1.7; 3270 2.9; 3597 3.1; 3957 2.5; 4353 0.7; 4788 -2.2; 5267 -6.9; 5793 -6.3; 6373 -2.2; 7010 -0.2; 7711 -0.9; 8482 -2.0; 9330 -0.4; 10263 0.0; 11289 -1.4; 12418 -2.6; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -1.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WI-SP500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WI-SP500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 50 Hz    | 0.42 | 9.8 dB  |
| Peaking | 169 Hz   | 0.35 | -7.8 dB |
| Peaking | 3660 Hz  | 2.39 | 4.1 dB  |
| Peaking | 5451 Hz  | 4.56 | -8.8 dB |
| Peaking | 11314 Hz | 1.69 | -1.3 dB |
| Peaking | 113 Hz   | 4.99 | -0.4 dB |
| Peaking | 542 Hz   | 2.25 | -1.7 dB |
| Peaking | 896 Hz   | 3.04 | 1.8 dB  |
| Peaking | 1638 Hz  | 1.78 | 1.5 dB  |
| Peaking | 2320 Hz  | 3.39 | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20WI-SP500/Sony%20WI-SP500.png)