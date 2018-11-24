# Sony WI-SP600N

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.4dB
GraphicEQ: 21 -8.3; 23 -8.7; 25 -9.0; 28 -9.4; 31 -9.6; 34 -9.8; 37 -9.8; 41 -9.9; 45 -9.9; 49 -9.7; 54 -9.6; 60 -9.6; 66 -9.4; 72 -9.2; 79 -8.9; 87 -8.7; 96 -8.5; 106 -8.5; 116 -8.5; 128 -8.5; 141 -8.3; 155 -8.0; 170 -7.8; 187 -7.8; 206 -7.6; 227 -7.2; 249 -6.7; 274 -6.0; 302 -5.3; 332 -4.6; 365 -4.0; 402 -3.5; 442 -3.0; 486 -2.4; 535 -1.9; 588 -1.4; 647 -0.8; 712 -0.4; 783 -0.2; 861 -0.1; 947 -0.1; 1042 -0.0; 1146 -0.9; 1261 -2.0; 1387 -2.8; 1526 -3.3; 1678 -3.3; 1846 -2.8; 2031 -2.3; 2234 -1.4; 2457 -0.5; 2703 -0.1; 2973 0.0; 3270 0.2; 3597 0.5; 3957 0.7; 4353 0.5; 4788 1.5; 5267 3.2; 5793 2.3; 6373 -3.7; 7010 1.1; 7711 0.3; 8482 0.0; 9330 -0.1; 10263 -5.6; 11289 -5.9; 12418 -0.3; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -3.1; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WI-SP600N GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-34**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WI-SP600N ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.1dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 42 Hz    | 0.27 | -9.5 dB |
| Peaking | 215 Hz   | 0.85 | -4.1 dB |
| Peaking | 1641 Hz  | 2.83 | -3.6 dB |
| Peaking | 10733 Hz | 5.9  | -7.8 dB |
| Peaking | 832 Hz   | 3.07 | 1.0 dB  |
| Peaking | 5845 Hz  | 2.51 | 4.8 dB  |
| Peaking | 6325 Hz  | 8.18 | -7.8 dB |
| Peaking | 16841 Hz | 1.51 | 1.0 dB  |
| Peaking | 18240 Hz | 2.76 | -4.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sony%20WI-SP600N/Sony%20WI-SP600N.png)