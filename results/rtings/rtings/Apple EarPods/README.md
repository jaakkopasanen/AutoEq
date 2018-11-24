# Apple EarPods

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.3; 49 4.1; 54 2.8; 60 1.3; 66 -0.0; 72 -1.1; 79 -2.1; 87 -3.0; 96 -3.6; 106 -3.9; 116 -4.1; 128 -4.1; 141 -3.9; 155 -3.9; 170 -3.7; 187 -3.4; 206 -3.1; 227 -2.9; 249 -2.7; 274 -2.6; 302 -2.4; 332 -2.4; 365 -2.4; 402 -2.4; 442 -2.2; 486 -2.1; 535 -1.9; 588 -1.8; 647 -1.3; 712 -0.6; 783 0.1; 861 0.4; 947 0.3; 1042 -0.2; 1146 -0.9; 1261 -1.9; 1387 -3.0; 1526 -4.1; 1678 -4.9; 1846 -5.4; 2031 -5.3; 2234 -4.6; 2457 -3.7; 2703 -2.7; 2973 -1.7; 3270 -0.7; 3597 -0.2; 3957 -0.2; 4353 -1.2; 4788 -1.8; 5267 -2.8; 5793 -5.4; 6373 -6.6; 7010 -4.8; 7711 -2.6; 8482 -2.1; 9330 -2.6; 10263 -0.6; 11289 0.0; 12418 0.0; 13660 -1.7; 15026 -1.3; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Apple EarPods GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Apple EarPods ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 43 Hz    | 0.42 | 14.6 dB  |
| Peaking | 83 Hz    | 0.42 | -13.0 dB |
| Peaking | 1913 Hz  | 1.97 | -5.7 dB  |
| Peaking | 6309 Hz  | 3.33 | -6.8 dB  |
| Peaking | 9167 Hz  | 3.93 | -1.7 dB  |
| Peaking | 535 Hz   | 2.46 | -0.8 dB  |
| Peaking | 880 Hz   | 2.94 | 1.8 dB   |
| Peaking | 3192 Hz  | 1.28 | -1.1 dB  |
| Peaking | 3599 Hz  | 2.92 | 2.1 dB   |
| Peaking | 14343 Hz | 7.53 | -2.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Apple%20EarPods/Apple%20EarPods.png)