# Ultrasone HFi-780
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.8; 66 5.6; 72 5.8; 79 5.9; 87 5.9; 96 5.7; 106 5.7; 116 5.9; 128 6.0; 141 6.0; 155 6.0; 170 6.0; 187 6.0; 206 6.0; 227 6.0; 249 4.7; 274 3.2; 302 1.3; 332 -0.1; 365 -0.5; 402 -1.1; 442 -1.2; 486 -1.0; 535 -0.5; 588 0.1; 647 0.4; 712 0.6; 783 0.6; 861 0.4; 947 0.1; 1042 -0.0; 1146 0.6; 1261 -0.4; 1387 -1.4; 1526 -1.9; 1678 -1.9; 1846 -1.6; 2031 -1.1; 2234 5.7; 2457 4.6; 2703 3.1; 2973 2.8; 3270 2.3; 3597 1.2; 3957 2.5; 4353 5.8; 4788 3.9; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -1.1; 10263 -2.7; 11289 -0.1; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone HFi-780 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone HFi-780 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 66 Hz   | 0.21 | 6.7 dB   |
| Peaking | 1168 Hz | 0.23 | -1.9 dB  |
| Peaking | 2372 Hz | 6.19 | 6.7 dB   |
| Peaking | 5718 Hz | 1.05 | 8.5 dB   |
| Peaking | 8688 Hz | 1.31 | -4.6 dB  |
| Peaking | 19 Hz   | 1.88 | 1.2 dB   |
| Peaking | 228 Hz  | 1    | 8.7 dB   |
| Peaking | 340 Hz  | 0.55 | -10.8 dB |
| Peaking | 662 Hz  | 0.55 | 6.0 dB   |
| Peaking | 1673 Hz | 2.42 | -2.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultrasone%20HFi-780/Ultrasone%20HFi-780.png)