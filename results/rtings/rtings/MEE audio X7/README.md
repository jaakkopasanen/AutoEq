# MEE audio X7

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.8; 25 5.5; 28 4.9; 31 4.4; 34 3.9; 37 3.6; 41 3.1; 45 2.8; 49 2.4; 54 2.0; 60 1.3; 66 0.6; 72 0.1; 79 -0.4; 87 -0.9; 96 -1.6; 106 -2.3; 116 -2.9; 128 -3.5; 141 -3.9; 155 -4.1; 170 -4.2; 187 -4.3; 206 -4.4; 227 -4.2; 249 -3.9; 274 -3.5; 302 -3.0; 332 -2.5; 365 -1.9; 402 -1.4; 442 -1.0; 486 -0.4; 535 0.3; 588 0.5; 647 0.7; 712 1.1; 783 1.2; 861 0.9; 947 0.3; 1042 -0.1; 1146 -0.6; 1261 -1.0; 1387 -1.2; 1526 -1.5; 1678 -1.9; 1846 -2.5; 2031 -3.0; 2234 -3.2; 2457 -3.5; 2703 -5.2; 2973 -7.5; 3270 -9.1; 3597 -9.6; 3957 -10.6; 4353 -13.4; 4788 -13.6; 5267 -6.7; 5793 -1.3; 6373 -0.2; 7010 0.2; 7711 -0.8; 8482 -2.8; 9330 -2.2; 10263 -0.0; 11289 0.0; 12418 0.0; 13660 -1.6; 15026 -3.4; 16529 -2.6; 18182 -3.1; 20000 -0.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MEE audio X7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MEE audio X7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 0.56 | 6.0 dB   |
| Peaking | 172 Hz   | 0.88 | -5.0 dB  |
| Peaking | 4084 Hz  | 1.77 | -13.1 dB |
| Peaking | 15172 Hz | 4.54 | -3.0 dB  |
| Peaking | 17959 Hz | 2.18 | -3.3 dB  |
| Peaking | 741 Hz   | 2.19 | 2.0 dB   |
| Peaking | 3958 Hz  | 4.94 | 5.3 dB   |
| Peaking | 4091 Hz  | 0.79 | -2.7 dB  |
| Peaking | 4749 Hz  | 5.53 | -5.6 dB  |
| Peaking | 6036 Hz  | 2.46 | 6.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/MEE%20audio%20X7/MEE%20audio%20X7.png)