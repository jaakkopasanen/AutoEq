# Ultimate Ears UE500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -10.5; 23 -10.4; 25 -10.3; 28 -10.1; 31 -9.8; 34 -9.6; 37 -9.4; 41 -9.1; 45 -8.9; 49 -8.7; 54 -8.5; 60 -8.3; 66 -8.2; 72 -8.1; 79 -7.9; 87 -7.8; 96 -7.5; 106 -7.2; 116 -7.0; 128 -6.8; 141 -6.7; 155 -6.4; 170 -6.2; 187 -5.8; 206 -5.5; 227 -5.1; 249 -4.7; 274 -4.3; 302 -3.8; 332 -3.3; 365 -2.7; 402 -2.2; 442 -1.8; 486 -1.3; 535 -0.8; 588 -0.3; 647 0.1; 712 0.5; 783 0.6; 861 0.5; 947 0.3; 1042 -0.2; 1146 -0.7; 1261 -1.0; 1387 -0.4; 1526 -0.2; 1678 -0.7; 1846 -1.2; 2031 -1.6; 2234 -1.5; 2457 -1.1; 2703 0.6; 2973 3.3; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultimate Ears UE500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears UE500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 17 Hz   | 0.15 | -10.0 dB |
| Peaking | 196 Hz  | 0.83 | -3.0 dB  |
| Peaking | 2017 Hz | 2.37 | -2.9 dB  |
| Peaking | 2490 Hz | 4.76 | -2.8 dB  |
| Peaking | 4152 Hz | 1.05 | 7.2 dB   |
| Peaking | 756 Hz  | 2.8  | 1.2 dB   |
| Peaking | 1223 Hz | 5.55 | -1.1 dB  |
| Peaking | 4357 Hz | 5.79 | -1.1 dB  |
| Peaking | 6356 Hz | 2.61 | 4.5 dB   |
| Peaking | 7507 Hz | 1.77 | -3.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultimate%20Ears%20UE500/Ultimate%20Ears%20UE500.png)