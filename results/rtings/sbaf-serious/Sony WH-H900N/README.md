# Sony WH-H900N

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.1dB
GraphicEQ: 21 -1.6; 23 -1.4; 25 -1.2; 28 -1.2; 31 -1.2; 34 -1.2; 37 -1.2; 41 -1.3; 45 -1.3; 49 -1.3; 54 -1.3; 60 -1.3; 66 -1.4; 72 -1.4; 79 -1.4; 87 -1.4; 96 -1.6; 106 -1.7; 116 -1.9; 128 -1.9; 141 -1.8; 155 -1.6; 170 -1.2; 187 -1.0; 206 -0.6; 227 -0.2; 249 0.2; 274 0.6; 302 1.0; 332 1.4; 365 1.8; 402 2.2; 442 2.5; 486 2.7; 535 2.5; 588 2.1; 647 1.9; 712 1.6; 783 2.7; 861 1.9; 947 0.5; 1042 -0.2; 1146 -0.6; 1261 -0.5; 1387 -0.3; 1526 -1.6; 1678 -2.4; 1846 -2.5; 2031 -2.0; 2234 -1.0; 2457 0.8; 2703 0.5; 2973 -1.5; 3270 1.5; 3597 4.4; 3957 -1.9; 4353 -2.7; 4788 1.9; 5267 2.8; 5793 4.2; 6373 5.0; 7010 2.5; 7711 0.3; 8482 -1.5; 9330 -0.8; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WH-H900N GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-50**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WH-H900N ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 469 Hz  |  0.83 | 4.6 dB  |
| Peaking | 540 Hz  |  0.05 | -2.1 dB |
| Peaking | 820 Hz  |  4.46 | 2.3 dB  |
| Peaking | 3512 Hz |  9.29 | 6.4 dB  |
| Peaking | 6099 Hz |  3.13 | 6.9 dB  |
| Peaking | 12 Hz   |  1.95 | -1.4 dB |
| Peaking | 1807 Hz |  5.17 | -1.3 dB |
| Peaking | 2532 Hz |  7.85 | 3.0 dB  |
| Peaking | 4183 Hz | 11.36 | -5.1 dB |
| Peaking | 4840 Hz |  6.97 | 2.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sony%20WH-H900N/Sony%20WH-H900N.png)