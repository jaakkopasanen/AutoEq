# Koss QZPro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.8; 49 4.7; 54 3.1; 60 1.4; 66 -0.0; 72 -1.2; 79 -2.1; 87 -2.6; 96 -2.9; 106 -3.0; 116 -2.9; 128 -2.9; 141 -2.6; 155 -2.4; 170 -2.1; 187 -1.9; 206 -1.7; 227 -1.5; 249 -1.2; 274 -1.0; 302 -0.7; 332 -0.4; 365 -0.3; 402 -0.2; 442 -0.4; 486 -0.3; 535 0.2; 588 0.8; 647 0.9; 712 1.4; 783 2.4; 861 1.5; 947 0.5; 1042 -0.3; 1146 -0.4; 1261 0.5; 1387 1.7; 1526 3.3; 1678 4.9; 1846 6.0; 2031 6.0; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
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
| Peaking | 41 Hz   | 0.5  | 10.2 dB |
| Peaking | 83 Hz   | 0.65 | -8.7 dB |
| Peaking | 2376 Hz | 0.92 | 8.0 dB  |
| Peaking | 4237 Hz | 0.36 | -3.5 dB |
| Peaking | 5179 Hz | 1.2  | 7.7 dB  |
| Peaking | 800 Hz  | 2.48 | 3.2 dB  |
| Peaking | 1062 Hz | 1.49 | -2.7 dB |
| Peaking | 1734 Hz | 4.57 | 2.0 dB  |
| Peaking | 6443 Hz | 6.85 | 2.0 dB  |
| Peaking | 7638 Hz | 4.4  | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Koss%20QZPro/Koss%20QZPro.png)