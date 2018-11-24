# Koss QZ900

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -12.1; 23 -11.9; 25 -11.7; 28 -11.6; 31 -11.4; 34 -11.3; 37 -11.1; 41 -11.0; 45 -10.8; 49 -10.7; 54 -10.6; 60 -10.5; 66 -10.4; 72 -10.2; 79 -10.0; 87 -10.0; 96 -10.2; 106 -10.6; 116 -10.9; 128 -10.9; 141 -10.9; 155 -10.7; 170 -10.3; 187 -9.8; 206 -9.3; 227 -8.7; 249 -7.8; 274 -6.1; 302 -5.3; 332 -5.0; 365 -4.2; 402 -3.4; 442 -2.7; 486 -2.4; 535 -2.3; 588 -2.2; 647 -2.1; 712 -1.7; 783 -1.2; 861 -0.6; 947 -0.1; 1042 0.1; 1146 0.0; 1261 -0.4; 1387 -1.2; 1526 -1.8; 1678 -4.1; 1846 -5.8; 2031 -5.8; 2234 -2.2; 2457 2.2; 2703 -7.5; 2973 -8.2; 3270 -1.4; 3597 2.7; 3957 4.4; 4353 3.6; 4788 6.0; 5267 3.0; 5793 5.4; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss QZ900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss QZ900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 13 Hz   |  1.35 | -11.8 dB |
| Peaking | 34 Hz   |  0.42 | -8.9 dB  |
| Peaking | 151 Hz  |  0.63 | -8.0 dB  |
| Peaking | 226 Hz  |  1.74 | -1.2 dB  |
| Peaking | 1909 Hz |  3.56 | -6.2 dB  |
| Peaking | 653 Hz  |  3.09 | -0.8 dB  |
| Peaking | 1034 Hz |  3.32 | 1.0 dB   |
| Peaking | 2446 Hz | 10.75 | 7.1 dB   |
| Peaking | 2863 Hz |  4.29 | -12.2 dB |
| Peaking | 4479 Hz |  1.2  | 6.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Koss%20QZ900/Koss%20QZ900.png)