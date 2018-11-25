# 1MORE Piston Classic

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.9; 25 5.7; 28 5.1; 31 4.4; 34 3.9; 37 3.4; 41 2.8; 45 2.3; 49 1.8; 54 1.1; 60 0.2; 66 -0.5; 72 -1.2; 79 -1.9; 87 -2.8; 96 -3.6; 106 -4.5; 116 -5.3; 128 -6.1; 141 -6.8; 155 -7.2; 170 -7.5; 187 -7.8; 206 -7.8; 227 -7.8; 249 -7.5; 274 -7.4; 302 -7.2; 332 -6.8; 365 -6.3; 402 -5.7; 442 -5.0; 486 -4.2; 535 -3.2; 588 -2.1; 647 -1.2; 712 -0.3; 783 0.0; 861 -0.0; 947 -0.1; 1042 0.3; 1146 0.8; 1261 1.1; 1387 1.7; 1526 2.5; 1678 3.3; 1846 4.1; 2031 4.7; 2234 5.5; 2457 6.0; 2703 5.7; 2973 3.8; 3270 0.7; 3597 -1.1; 3957 -1.5; 4353 -2.2; 4788 -1.8; 5267 -1.3; 5793 -1.0; 6373 -1.6; 7010 0.5; 7711 0.3; 8482 0.0; 9330 -2.1; 10263 -2.4; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1MORE Piston Classic GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Piston Classic ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.42 | 6.5 dB  |
| Peaking | 206 Hz  | 0.5  | -8.6 dB |
| Peaking | 2778 Hz | 0.88 | 16.2 dB |
| Peaking | 3475 Hz | 1.18 | -9.9 dB |
| Peaking | 3627 Hz | 0.44 | -3.6 dB |
| Peaking | 419 Hz  | 2.66 | -0.9 dB |
| Peaking | 725 Hz  | 2.22 | 1.5 dB  |
| Peaking | 1053 Hz | 1.63 | -0.7 dB |
| Peaking | 9267 Hz | 1.91 | 2.1 dB  |
| Peaking | 9791 Hz | 5.63 | -5.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/1MORE%20Piston%20Classic/1MORE%20Piston%20Classic.png)