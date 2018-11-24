# Jaybird Freedom 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.8dB
GraphicEQ: 21 -7.3; 23 -7.5; 25 -7.6; 28 -7.8; 31 -7.9; 34 -8.0; 37 -8.1; 41 -8.2; 45 -8.2; 49 -8.3; 54 -8.4; 60 -8.7; 66 -8.9; 72 -9.1; 79 -9.3; 87 -9.4; 96 -9.6; 106 -9.8; 116 -10.0; 128 -10.1; 141 -10.1; 155 -10.2; 170 -10.5; 187 -10.1; 206 -9.6; 227 -9.0; 249 -8.3; 274 -7.6; 302 -6.8; 332 -6.0; 365 -5.2; 402 -4.4; 442 -3.6; 486 -2.8; 535 -2.0; 588 -1.1; 647 -0.2; 712 0.7; 783 1.1; 861 0.9; 947 0.4; 1042 -0.3; 1146 -1.2; 1261 -1.9; 1387 -2.2; 1526 -2.4; 1678 -2.4; 1846 -3.0; 2031 -3.9; 2234 -4.7; 2457 -5.5; 2703 -5.2; 2973 -3.1; 3270 -0.8; 3597 0.6; 3957 1.2; 4353 1.1; 4788 1.4; 5267 1.4; 5793 -0.7; 6373 -7.2; 7010 -11.3; 7711 -7.3; 8482 -3.4; 9330 -5.1; 10263 -9.4; 11289 -9.8; 12418 -5.3; 13660 -2.1; 15026 -3.5; 16529 -4.0; 18182 -0.2; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jaybird Freedom 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-18**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jaybird Freedom 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 0.28 | -7.2 dB  |
| Peaking | 134 Hz   | 0.67 | -5.5 dB  |
| Peaking | 239 Hz   | 0.99 | -4.4 dB  |
| Peaking | 6998 Hz  | 6.01 | -11.2 dB |
| Peaking | 10874 Hz | 2.31 | -10.1 dB |
| Peaking | 788 Hz   | 2.73 | 2.8 dB   |
| Peaking | 2621 Hz  | 1.16 | -9.2 dB  |
| Peaking | 3762 Hz  | 0.94 | 6.6 dB   |
| Peaking | 6487 Hz  | 8.74 | -3.7 dB  |
| Peaking | 16128 Hz | 3.86 | -4.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Jaybird%20Freedom%202/Jaybird%20Freedom%202.png)