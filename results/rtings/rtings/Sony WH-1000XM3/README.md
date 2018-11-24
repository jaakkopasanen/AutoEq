# Sony WH-1000XM3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.4dB
GraphicEQ: 21 -6.8; 23 -6.7; 25 -6.6; 28 -6.6; 31 -6.6; 34 -6.5; 37 -6.4; 41 -6.2; 45 -6.1; 49 -6.0; 54 -6.0; 60 -6.1; 66 -6.3; 72 -6.6; 79 -6.9; 87 -7.2; 96 -7.5; 106 -7.8; 116 -7.9; 128 -7.8; 141 -7.4; 155 -6.8; 170 -6.0; 187 -5.1; 206 -4.1; 227 -3.3; 249 -2.5; 274 -2.0; 302 -1.6; 332 -1.4; 365 -1.3; 402 -1.4; 442 -1.5; 486 -1.8; 535 -2.0; 588 -2.0; 647 -2.0; 712 -1.1; 783 -0.9; 861 -0.9; 947 -0.3; 1042 0.2; 1146 0.6; 1261 0.3; 1387 -0.2; 1526 -2.2; 1678 -2.9; 1846 -3.2; 2031 -3.8; 2234 -3.3; 2457 -1.5; 2703 0.2; 2973 0.5; 3270 0.9; 3597 0.9; 3957 0.6; 4353 2.0; 4788 4.3; 5267 2.8; 5793 2.9; 6373 0.3; 7010 -0.1; 7711 -1.8; 8482 -4.8; 9330 -7.0; 10263 -6.3; 11289 -1.7; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WH-1000XM3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-44**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WH-1000XM3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 1.41 | -6.5 dB |
| Peaking | 29 Hz   | 0.52 | -5.1 dB |
| Peaking | 121 Hz  | 0.78 | -6.9 dB |
| Peaking | 1952 Hz | 3.51 | -4.2 dB |
| Peaking | 9567 Hz | 4.06 | -8.2 dB |
| Peaking | 600 Hz  | 2.82 | -1.6 dB |
| Peaking | 1159 Hz | 5.82 | 1.2 dB  |
| Peaking | 4805 Hz | 3.93 | 3.9 dB  |
| Peaking | 5715 Hz | 5.28 | 2.1 dB  |
| Peaking | 8376 Hz | 6.32 | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Sony%20WH-1000XM3/Sony%20WH-1000XM3.png)