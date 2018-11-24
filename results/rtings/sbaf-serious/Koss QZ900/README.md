# Koss QZ900

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -11.6; 23 -11.6; 25 -11.5; 28 -11.4; 31 -11.4; 34 -11.3; 37 -11.3; 41 -11.2; 45 -11.1; 49 -11.1; 54 -11.0; 60 -10.8; 66 -10.5; 72 -10.2; 79 -9.8; 87 -9.6; 96 -9.8; 106 -10.1; 116 -10.4; 128 -10.4; 141 -10.4; 155 -10.1; 170 -9.7; 187 -9.2; 206 -8.8; 227 -8.3; 249 -7.2; 274 -5.4; 302 -4.5; 332 -4.1; 365 -3.2; 402 -2.3; 442 -1.6; 486 -1.2; 535 -1.1; 588 -1.1; 647 -1.0; 712 -0.8; 783 -0.7; 861 -0.4; 947 -0.1; 1042 0.1; 1146 0.2; 1261 -0.2; 1387 -1.2; 1526 -2.2; 1678 -4.5; 1846 -5.8; 2031 -5.3; 2234 -1.7; 2457 2.7; 2703 -6.9; 2973 -7.1; 3270 0.4; 3597 4.9; 3957 5.2; 4353 3.6; 4788 6.0; 5267 3.5; 5793 5.8; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss QZ900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss QZ900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 12 Hz   |  0.79 | -11.1 dB |
| Peaking | 46 Hz   |  0.45 | -8.9 dB  |
| Peaking | 146 Hz  |  0.95 | -6.1 dB  |
| Peaking | 231 Hz  |  1.8  | -3.0 dB  |
| Peaking | 1870 Hz |  3.97 | -6.4 dB  |
| Peaking | 485 Hz  |  3.99 | 0.2 dB   |
| Peaking | 2443 Hz | 10.01 | 7.7 dB   |
| Peaking | 2889 Hz |  3.35 | -14.3 dB |
| Peaking | 3584 Hz |  1.83 | 9.4 dB   |
| Peaking | 6061 Hz |  4.05 | 5.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Koss%20QZ900/Koss%20QZ900.png)