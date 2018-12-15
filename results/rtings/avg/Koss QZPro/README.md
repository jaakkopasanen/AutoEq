# Koss QZPro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.9; 49 5.0; 54 3.4; 60 1.7; 66 0.1; 72 -1.2; 79 -2.3; 87 -3.0; 96 -3.3; 106 -3.5; 116 -3.5; 128 -3.4; 141 -3.2; 155 -3.0; 170 -2.8; 187 -2.5; 206 -2.2; 227 -2.0; 249 -1.8; 274 -1.7; 302 -1.5; 332 -1.4; 365 -1.3; 402 -1.3; 442 -1.6; 486 -1.5; 535 -1.0; 588 -0.3; 647 -0.2; 712 0.6; 783 1.9; 861 1.3; 947 0.4; 1042 -0.3; 1146 -0.6; 1261 0.3; 1387 1.8; 1526 3.6; 1678 5.3; 1846 6.0; 2031 6.0; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss QZPro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss QZPro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 43 Hz   | 0.49 | 10.4 dB |
| Peaking | 86 Hz   | 0.69 | -8.5 dB |
| Peaking | 953 Hz  | 0.04 | -1.2 dB |
| Peaking | 2384 Hz | 0.87 | 7.2 dB  |
| Peaking | 5243 Hz | 1.59 | 5.7 dB  |
| Peaking | 814 Hz  | 2.84 | 3.3 dB  |
| Peaking | 1153 Hz | 1.21 | -2.7 dB |
| Peaking | 1668 Hz | 3.25 | 2.7 dB  |
| Peaking | 6464 Hz | 6.61 | 2.2 dB  |
| Peaking | 7692 Hz | 3.76 | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Koss%20QZPro/Koss%20QZPro.png)