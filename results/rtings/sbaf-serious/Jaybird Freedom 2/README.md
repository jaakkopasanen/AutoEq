# Jaybird Freedom 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.1dB
GraphicEQ: 21 -6.9; 23 -7.1; 25 -7.4; 28 -7.6; 31 -7.9; 34 -8.1; 37 -8.2; 41 -8.4; 45 -8.5; 49 -8.6; 54 -8.8; 60 -9.0; 66 -9.1; 72 -9.1; 79 -9.1; 87 -9.1; 96 -9.1; 106 -9.3; 116 -9.5; 128 -9.6; 141 -9.5; 155 -9.6; 170 -9.8; 187 -9.6; 206 -9.1; 227 -8.5; 249 -7.8; 274 -6.9; 302 -5.9; 332 -5.1; 365 -4.2; 402 -3.4; 442 -2.5; 486 -1.6; 535 -0.8; 588 -0.0; 647 0.8; 712 1.6; 783 1.6; 861 1.1; 947 0.4; 1042 -0.2; 1146 -1.0; 1261 -1.6; 1387 -2.2; 1526 -2.7; 1678 -2.7; 1846 -2.9; 2031 -3.4; 2234 -4.2; 2457 -5.0; 2703 -4.6; 2973 -2.0; 3270 1.0; 3597 2.8; 3957 2.4; 4353 1.1; 4788 1.3; 5267 1.8; 5793 0.7; 6373 -4.7; 7010 -8.8; 7711 -6.2; 8482 -3.0; 9330 -3.6; 10263 -6.0; 11289 -5.3; 12418 -0.9; 13660 0.0; 15026 -0.4; 16529 -0.7; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jaybird Freedom 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-30**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jaybird Freedom 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 43 Hz    | 0.33 | -8.2 dB |
| Peaking | 148 Hz   | 0.94 | -4.7 dB |
| Peaking | 244 Hz   | 1.46 | -3.9 dB |
| Peaking | 7103 Hz  | 5.62 | -9.2 dB |
| Peaking | 10617 Hz | 3.54 | -6.4 dB |
| Peaking | 757 Hz   | 2.37 | 3.1 dB  |
| Peaking | 2840 Hz  | 1.03 | -8.2 dB |
| Peaking | 3525 Hz  | 2.17 | 9.2 dB  |
| Peaking | 5487 Hz  | 2.98 | 3.7 dB  |
| Peaking | 6488 Hz  | 8.4  | -2.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Jaybird%20Freedom%202/Jaybird%20Freedom%202.png)