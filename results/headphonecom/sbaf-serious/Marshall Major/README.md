# Marshall Major

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 5.8; 116 5.2; 128 4.5; 141 4.1; 155 3.5; 170 3.3; 187 3.0; 206 2.7; 227 2.5; 249 2.6; 274 2.9; 302 2.2; 332 2.1; 365 2.3; 402 2.1; 442 1.9; 486 2.2; 535 2.9; 588 3.5; 647 3.7; 712 3.6; 783 3.1; 861 2.3; 947 1.0; 1042 -0.4; 1146 -0.7; 1261 -2.3; 1387 -5.0; 1526 -7.2; 1678 -8.2; 1846 -8.4; 2031 -6.4; 2234 -3.6; 2457 -0.5; 2703 2.1; 2973 3.9; 3270 4.8; 3597 5.2; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 5.1; 6373 1.2; 7010 -3.2; 7711 -2.1; 8482 -1.4; 9330 -3.0; 10263 -0.5; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Marshall Major GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Marshall Major ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 32 Hz   | 0.19 | 5.7 dB   |
| Peaking | 89 Hz   | 1.08 | 1.3 dB   |
| Peaking | 702 Hz  | 1.28 | 3.9 dB   |
| Peaking | 1739 Hz | 1.9  | -10.7 dB |
| Peaking | 3861 Hz | 1.46 | 7.7 dB   |
| Peaking | 2138 Hz | 5.93 | -1.2 dB  |
| Peaking | 2936 Hz | 2.42 | 2.1 dB   |
| Peaking | 3635 Hz | 2.9  | -2.0 dB  |
| Peaking | 5667 Hz | 2.54 | 7.4 dB   |
| Peaking | 6919 Hz | 1.68 | -6.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Marshall%20Major/Marshall%20Major.png)