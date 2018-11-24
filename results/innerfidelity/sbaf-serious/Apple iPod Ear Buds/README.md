# Apple iPod Ear Buds

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 6.0; 128 6.0; 141 6.0; 155 5.2; 170 3.7; 187 2.4; 206 1.2; 227 0.2; 249 -0.5; 274 -1.0; 302 -1.2; 332 -1.3; 365 -1.1; 402 -0.7; 442 -0.1; 486 0.1; 535 0.2; 588 0.4; 647 0.1; 712 -0.1; 783 0.0; 861 -0.0; 947 -0.0; 1042 0.0; 1146 0.1; 1261 0.0; 1387 -0.4; 1526 -0.9; 1678 -1.2; 1846 -1.0; 2031 -0.1; 2234 1.0; 2457 0.3; 2703 -2.5; 2973 -5.2; 3270 -4.1; 3597 -1.1; 3957 -0.0; 4353 -1.0; 4788 -1.2; 5267 -0.4; 5793 -2.6; 6373 -5.6; 7010 -3.5; 7711 -2.4; 8482 -3.2; 9330 -1.3; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Apple iPod Ear Buds GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Apple iPod Ear Buds ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 61 Hz   | 0.2  | 6.6 dB  |
| Peaking | 231 Hz  | 2.9  | -2.4 dB |
| Peaking | 325 Hz  | 1.29 | -4.1 dB |
| Peaking | 3045 Hz | 5.79 | -5.6 dB |
| Peaking | 6638 Hz | 2.88 | -4.9 dB |
| Peaking | 141 Hz  | 5.99 | 1.3 dB  |
| Peaking | 1631 Hz | 4.44 | -1.4 dB |
| Peaking | 6481 Hz | 0.35 | 0.4 dB  |
| Peaking | 8568 Hz | 7.7  | -2.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Apple%20iPod%20Ear%20Buds/Apple%20iPod%20Ear%20Buds.png)