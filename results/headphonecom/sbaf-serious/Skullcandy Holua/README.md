# Skullcandy Holua

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -9.9; 23 -9.8; 25 -9.8; 28 -9.7; 31 -9.6; 34 -9.6; 37 -9.5; 41 -9.5; 45 -9.4; 49 -9.3; 54 -9.3; 60 -9.3; 66 -9.3; 72 -9.2; 79 -9.2; 87 -9.1; 96 -8.9; 106 -8.7; 116 -8.5; 128 -8.2; 141 -8.0; 155 -7.6; 170 -7.3; 187 -6.8; 206 -6.3; 227 -5.8; 249 -5.2; 274 -4.7; 302 -4.0; 332 -3.3; 365 -2.6; 402 -2.0; 442 -1.7; 486 -1.2; 535 -0.6; 588 -0.1; 647 0.3; 712 0.7; 783 0.8; 861 0.7; 947 0.3; 1042 -0.2; 1146 -0.5; 1261 -1.0; 1387 -2.0; 1526 -3.7; 1678 -5.3; 1846 -6.5; 2031 -7.8; 2234 -9.3; 2457 -8.6; 2703 -3.6; 2973 0.8; 3270 4.4; 3597 6.0; 3957 5.2; 4353 2.3; 4788 -0.4; 5267 -1.6; 5793 1.8; 6373 5.3; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Holua GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Holua ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 30 Hz   | 0.24 | -9.6 dB  |
| Peaking | 160 Hz  | 0.81 | -3.9 dB  |
| Peaking | 2286 Hz | 2.07 | -13.2 dB |
| Peaking | 3226 Hz | 1.36 | 5.9 dB   |
| Peaking | 3580 Hz | 4.47 | 4.3 dB   |
| Peaking | 295 Hz  | 2.52 | -0.8 dB  |
| Peaking | 788 Hz  | 1.38 | 1.8 dB   |
| Peaking | 1666 Hz | 5.15 | -1.9 dB  |
| Peaking | 5160 Hz | 5.55 | -3.9 dB  |
| Peaking | 6345 Hz | 6.05 | 5.6 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Skullcandy%20Holua/Skullcandy%20Holua.png)