# Sony WH-H900N

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.5dB
GraphicEQ: 21 -2.0; 23 -1.7; 25 -1.5; 28 -1.3; 31 -1.2; 34 -1.2; 37 -1.1; 41 -1.0; 45 -1.0; 49 -1.0; 54 -1.0; 60 -1.0; 66 -1.2; 72 -1.4; 79 -1.5; 87 -1.8; 96 -2.0; 106 -2.2; 116 -2.4; 128 -2.4; 141 -2.4; 155 -2.2; 170 -1.9; 187 -1.5; 206 -1.1; 227 -0.7; 249 -0.3; 274 -0.1; 302 0.2; 332 0.4; 365 0.7; 402 1.1; 442 1.4; 486 1.5; 535 1.3; 588 1.0; 647 0.9; 712 0.8; 783 2.2; 861 1.7; 947 0.5; 1042 -0.2; 1146 -0.8; 1261 -0.7; 1387 -0.3; 1526 -1.2; 1678 -2.0; 1846 -2.5; 2031 -2.4; 2234 -1.5; 2457 0.3; 2703 -0.3; 2973 -3.1; 3270 -1.1; 3597 1.3; 3957 -4.3; 4353 -4.0; 4788 0.3; 5267 -0.2; 5793 0.3; 6373 1.3; 7010 2.5; 7711 0.3; 8482 -1.0; 9330 -0.1; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WH-H900N GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-34**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WH-H900N ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.4dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 10 Hz   |  0.24 | -1.8 dB |
| Peaking | 125 Hz  |  1.49 | -2.5 dB |
| Peaking | 1888 Hz |  3.21 | -2.8 dB |
| Peaking | 4153 Hz | 10.41 | -6.8 dB |
| Peaking | 6781 Hz |  7.8  | 3.3 dB  |
| Peaking | 468 Hz  |  2.06 | 1.7 dB  |
| Peaking | 818 Hz  |  4.82 | 2.4 dB  |
| Peaking | 1113 Hz |  2.89 | -0.7 dB |
| Peaking | 4845 Hz |  9.38 | 1.2 dB  |
| Peaking | 6108 Hz |  0.41 | -0.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20WH-H900N/Sony%20WH-H900N.png)