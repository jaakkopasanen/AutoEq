# Sony MDR-1A

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.4dB
GraphicEQ: 21 -2.1; 23 -2.4; 25 -2.7; 28 -3.0; 31 -3.2; 34 -3.2; 37 -3.1; 41 -3.1; 45 -3.0; 49 -3.0; 54 -2.9; 60 -2.8; 66 -3.0; 72 -3.1; 79 -3.4; 87 -3.7; 96 -4.0; 106 -4.2; 116 -4.2; 128 -4.0; 141 -3.6; 155 -3.0; 170 -2.3; 187 -1.5; 206 -0.9; 227 -0.6; 249 -0.9; 274 0.1; 302 1.1; 332 1.6; 365 1.9; 402 1.9; 442 1.8; 486 1.4; 535 1.0; 588 0.6; 647 0.4; 712 0.3; 783 0.2; 861 0.0; 947 -0.0; 1042 -0.0; 1146 -0.1; 1261 -0.3; 1387 -0.6; 1526 -0.9; 1678 -1.2; 1846 -1.6; 2031 -1.7; 2234 -1.0; 2457 0.5; 2703 1.4; 2973 1.9; 3270 2.1; 3597 3.2; 3957 0.2; 4353 0.5; 4788 4.3; 5267 4.4; 5793 4.7; 6373 3.6; 7010 2.4; 7711 -0.3; 8482 -6.0; 9330 -9.2; 10263 -5.2; 11289 -0.1; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-1A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-54**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-1A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 36 Hz    | 0.63 | -3.1 dB  |
| Peaking | 115 Hz   | 1.61 | -3.8 dB  |
| Peaking | 3314 Hz  | 5.24 | 2.1 dB   |
| Peaking | 5878 Hz  | 2.05 | 5.6 dB   |
| Peaking | 9212 Hz  | 4.03 | -11.0 dB |
| Peaking | 301 Hz   | 0.74 | -1.6 dB  |
| Peaking | 375 Hz   | 1.31 | 3.7 dB   |
| Peaking | 1870 Hz  | 3.15 | -2.1 dB  |
| Peaking | 10124 Hz | 7.07 | -2.7 dB  |
| Peaking | 11081 Hz | 3.16 | 2.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Sony%20MDR-1A/Sony%20MDR-1A.png)