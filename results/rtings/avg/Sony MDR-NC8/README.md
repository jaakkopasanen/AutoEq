# Sony MDR-NC8

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.9; 66 5.0; 72 4.2; 79 3.4; 87 2.6; 96 1.9; 106 1.1; 116 0.6; 128 0.9; 141 1.6; 155 2.8; 170 3.8; 187 3.4; 206 2.6; 227 2.8; 249 3.1; 274 3.7; 302 4.5; 332 5.0; 365 5.5; 402 5.9; 442 6.0; 486 5.6; 535 4.8; 588 4.3; 647 4.6; 712 3.2; 783 2.0; 861 2.8; 947 0.8; 1042 0.1; 1146 1.7; 1261 3.4; 1387 4.0; 1526 4.3; 1678 4.7; 1846 4.8; 2031 5.2; 2234 5.9; 2457 5.3; 2703 4.8; 2973 4.3; 3270 4.4; 3597 5.5; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 -0.4; 8482 -3.0; 9330 -1.1; 10263 0.0; 11289 -0.0; 12418 -0.6; 13660 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-NC8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-NC8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.64 | 6.8 dB  |
| Peaking | 174 Hz  | 5.57 | 2.2 dB  |
| Peaking | 421 Hz  | 1.13 | 5.9 dB  |
| Peaking | 2139 Hz | 1.14 | 5.0 dB  |
| Peaking | 4887 Hz | 1.81 | 6.0 dB  |
| Peaking | 62 Hz   | 3.85 | 1.5 dB  |
| Peaking | 116 Hz  | 4.31 | -1.6 dB |
| Peaking | 1015 Hz | 8.85 | -2.5 dB |
| Peaking | 6390 Hz | 5.55 | 3.0 dB  |
| Peaking | 8409 Hz | 4.12 | -4.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20MDR-NC8/Sony%20MDR-NC8.png)