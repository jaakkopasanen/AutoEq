# Apple EarPods

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.9; 45 5.0; 49 3.8; 54 2.4; 60 1.0; 66 -0.2; 72 -1.1; 79 -1.9; 87 -2.6; 96 -3.1; 106 -3.5; 116 -3.6; 128 -3.5; 141 -3.4; 155 -3.3; 170 -3.0; 187 -2.8; 206 -2.6; 227 -2.5; 249 -2.2; 274 -1.9; 302 -1.6; 332 -1.4; 365 -1.4; 402 -1.3; 442 -1.0; 486 -0.9; 535 -0.7; 588 -0.7; 647 -0.2; 712 0.2; 783 0.5; 861 0.6; 947 0.3; 1042 -0.2; 1146 -0.7; 1261 -1.6; 1387 -3.0; 1526 -4.5; 1678 -5.3; 1846 -5.3; 2031 -4.9; 2234 -4.1; 2457 -3.3; 2703 -2.1; 2973 -0.6; 3270 1.2; 3597 2.0; 3957 1.0; 4353 -1.2; 4788 -2.0; 5267 -2.4; 5793 -4.0; 6373 -4.1; 7010 -2.2; 7711 -1.5; 8482 -1.7; 9330 -1.1; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Apple EarPods GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Apple EarPods ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.53 | 9.5 dB  |
| Peaking | 90 Hz   | 0.53 | -7.3 dB |
| Peaking | 1872 Hz | 1.92 | -5.8 dB |
| Peaking | 3576 Hz | 4.34 | 3.6 dB  |
| Peaking | 6033 Hz | 2.16 | -4.1 dB |
| Peaking | 863 Hz  | 2.82 | 1.3 dB  |
| Peaking | 1527 Hz | 3.72 | -2.0 dB |
| Peaking | 2042 Hz | 1.22 | 1.8 dB  |
| Peaking | 2412 Hz | 2.79 | -2.0 dB |
| Peaking | 4479 Hz | 8.89 | -0.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Apple%20EarPods/Apple%20EarPods.png)