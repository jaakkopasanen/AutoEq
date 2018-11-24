# Sennheiser MM 550-X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 5.6; 116 5.4; 128 5.4; 141 5.4; 155 5.6; 170 5.8; 187 5.7; 206 5.7; 227 5.9; 249 6.0; 274 5.9; 302 5.9; 332 5.8; 365 5.4; 402 5.0; 442 4.6; 486 3.9; 535 3.1; 588 2.2; 647 1.4; 712 0.5; 783 -0.3; 861 -0.4; 947 -0.1; 1042 0.2; 1146 0.6; 1261 0.8; 1387 0.6; 1526 0.2; 1678 -0.9; 1846 -3.6; 2031 -7.0; 2234 -7.2; 2457 -3.9; 2703 -1.7; 2973 0.6; 3270 3.3; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 4.2; 7010 2.5; 7711 0.3; 8482 -1.9; 9330 -3.0; 10263 -1.7; 11289 -3.1; 12418 -2.4; 13660 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser MM 550-X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser MM 550-X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 41 Hz   | 0.17 | 6.1 dB   |
| Peaking | 318 Hz  | 1.1  | 3.8 dB   |
| Peaking | 2209 Hz | 2.61 | -10.8 dB |
| Peaking | 5041 Hz | 0.71 | 8.7 dB   |
| Peaking | 9266 Hz | 1.18 | -6.7 dB  |
| Peaking | 480 Hz  | 3.71 | 0.9 dB   |
| Peaking | 821 Hz  | 2.65 | -1.8 dB  |
| Peaking | 1419 Hz | 2.75 | 1.0 dB   |
| Peaking | 3348 Hz | 2.52 | -1.9 dB  |
| Peaking | 3551 Hz | 5.49 | 3.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Sennheiser%20MM%20550-X/Sennheiser%20MM%20550-X.png)