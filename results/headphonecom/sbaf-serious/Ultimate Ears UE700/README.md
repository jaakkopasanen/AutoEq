# Ultimate Ears UE700

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.0; 25 2.0; 28 2.0; 31 1.9; 34 1.7; 37 1.6; 41 1.5; 45 1.4; 49 1.2; 54 1.0; 60 0.7; 66 0.4; 72 0.1; 79 -0.2; 87 -0.5; 96 -0.8; 106 -1.1; 116 -1.3; 128 -1.6; 141 -1.9; 155 -2.1; 170 -2.3; 187 -2.3; 206 -2.3; 227 -2.4; 249 -2.4; 274 -2.2; 302 -2.0; 332 -1.9; 365 -1.5; 402 -1.3; 442 -1.1; 486 -0.9; 535 -0.6; 588 -0.1; 647 0.1; 712 0.3; 783 0.4; 861 0.3; 947 0.1; 1042 -0.2; 1146 -0.4; 1261 -0.7; 1387 -1.1; 1526 -1.5; 1678 -1.6; 1846 -1.2; 2031 -0.6; 2234 0.4; 2457 2.0; 2703 4.1; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 4.9; 5267 5.6; 5793 5.9; 6373 4.4; 7010 1.8; 7711 -2.1; 8482 -7.1; 9330 -8.2; 10263 -1.5; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.9; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultimate Ears UE700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears UE700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 0.46 | 2.1 dB   |
| Peaking | 196 Hz   | 0.63 | -2.6 dB  |
| Peaking | 3306 Hz  | 2.7  | 5.4 dB   |
| Peaking | 5563 Hz  | 1.55 | 6.2 dB   |
| Peaking | 8859 Hz  | 3.84 | -11.1 dB |
| Peaking | 889 Hz   | 1    | 2.7 dB   |
| Peaking | 1522 Hz  | 0.57 | -3.0 dB  |
| Peaking | 2743 Hz  | 3.82 | 2.9 dB   |
| Peaking | 4142 Hz  | 6.07 | 2.0 dB   |
| Peaking | 10812 Hz | 8.5  | 2.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultimate%20Ears%20UE700/Ultimate%20Ears%20UE700.png)