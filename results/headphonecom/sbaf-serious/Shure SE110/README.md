# Shure SE110

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.9; 28 5.7; 31 5.6; 34 5.4; 37 5.3; 41 5.1; 45 4.9; 49 4.6; 54 4.4; 60 3.9; 66 3.6; 72 3.3; 79 2.9; 87 2.4; 96 2.1; 106 1.9; 116 1.6; 128 1.1; 141 0.8; 155 0.6; 170 0.4; 187 0.3; 206 0.2; 227 0.2; 249 -0.1; 274 -0.1; 302 0.0; 332 0.2; 365 0.3; 402 0.4; 442 0.5; 486 0.6; 535 0.7; 588 0.8; 647 1.0; 712 0.9; 783 0.9; 861 0.7; 947 0.2; 1042 -0.2; 1146 -0.7; 1261 -1.3; 1387 -2.6; 1526 -4.1; 1678 -4.8; 1846 -4.7; 2031 -3.4; 2234 -1.6; 2457 -0.5; 2703 2.0; 2973 4.9; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE110 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE110 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.61 | 5.6 dB  |
| Peaking | 60 Hz   | 0.93 | 2.2 dB  |
| Peaking | 771 Hz  | 1.28 | 1.3 dB  |
| Peaking | 1804 Hz | 1.63 | -7.1 dB |
| Peaking | 3972 Hz | 0.99 | 7.7 dB  |
| Peaking | 3121 Hz | 7.32 | 2.1 dB  |
| Peaking | 4173 Hz | 1.79 | -1.0 dB |
| Peaking | 5512 Hz | 2.76 | 2.1 dB  |
| Peaking | 6414 Hz | 3.91 | 4.1 dB  |
| Peaking | 7154 Hz | 1.38 | -3.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE110/Shure%20SE110.png)