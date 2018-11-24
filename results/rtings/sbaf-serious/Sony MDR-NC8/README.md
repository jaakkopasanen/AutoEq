# Sony MDR-NC8

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.8; 66 4.9; 72 4.2; 79 3.6; 87 3.0; 96 2.4; 106 1.6; 116 1.2; 128 1.4; 141 2.2; 155 3.4; 170 4.4; 187 3.9; 206 3.1; 227 3.3; 249 3.7; 274 4.4; 302 5.3; 332 5.9; 365 6.0; 402 6.0; 442 6.0; 486 6.0; 535 5.9; 588 5.4; 647 5.6; 712 4.1; 783 2.5; 861 2.9; 947 0.8; 1042 0.2; 1146 1.9; 1261 3.6; 1387 4.0; 1526 3.9; 1678 4.3; 1846 4.9; 2031 5.6; 2234 6.0; 2457 5.7; 2703 5.7; 2973 5.8; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.1; 8482 -3.5; 9330 -2.2; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-NC8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-NC8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 34 Hz    | 0.53 | 6.6 dB  |
| Peaking | 349 Hz   | 1.02 | 5.1 dB  |
| Peaking | 571 Hz   | 2.61 | 2.9 dB  |
| Peaking | 3849 Hz  | 0.49 | 6.8 dB  |
| Peaking | 8679 Hz  | 3.2  | -7.1 dB |
| Peaking | 117 Hz   | 3.66 | -1.5 dB |
| Peaking | 170 Hz   | 5.69 | 2.3 dB  |
| Peaking | 1008 Hz  | 7.89 | -2.9 dB |
| Peaking | 6186 Hz  | 6.45 | 1.8 dB  |
| Peaking | 13476 Hz | 1.39 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sony%20MDR-NC8/Sony%20MDR-NC8.png)