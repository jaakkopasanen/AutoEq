# Denon AH-GC20

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -8.4; 23 -8.6; 25 -8.9; 28 -9.1; 31 -9.3; 34 -9.3; 37 -9.3; 41 -9.3; 45 -9.3; 49 -9.2; 54 -9.1; 60 -8.7; 66 -8.4; 72 -7.9; 79 -7.3; 87 -6.8; 96 -6.3; 106 -5.8; 116 -5.4; 128 -4.9; 141 -4.3; 155 -3.7; 170 -3.0; 187 -2.5; 206 -1.9; 227 -1.4; 249 -1.0; 274 -0.8; 302 -0.9; 332 -1.1; 365 -1.7; 402 -2.6; 442 -3.3; 486 -3.1; 535 -1.8; 588 -0.5; 647 0.4; 712 0.6; 783 0.2; 861 -0.4; 947 -0.5; 1042 0.8; 1146 3.0; 1261 5.1; 1387 6.0; 1526 6.0; 1678 6.0; 1846 6.0; 2031 6.0; 2234 6.0; 2457 6.0; 2703 3.5; 2973 3.9; 3270 6.0; 3597 4.1; 3957 -0.9; 4353 3.3; 4788 1.4; 5267 5.1; 5793 6.0; 6373 2.4; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-GC20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-GC20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 39 Hz   | 0.36 | -9.7 dB |
| Peaking | 460 Hz  | 3.84 | -3.3 dB |
| Peaking | 1416 Hz | 3.22 | 4.1 dB  |
| Peaking | 2263 Hz | 1.21 | 5.8 dB  |
| Peaking | 5690 Hz | 4.94 | 5.9 dB  |
| Peaking | 930 Hz  | 1.47 | 1.4 dB  |
| Peaking | 934 Hz  | 3.68 | -3.3 dB |
| Peaking | 2818 Hz | 8.54 | -3.5 dB |
| Peaking | 3368 Hz | 3.91 | 4.0 dB  |
| Peaking | 3873 Hz | 9.58 | -5.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Denon%20AH-GC20/Denon%20AH-GC20.png)