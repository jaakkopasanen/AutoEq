# Beyerdynamic Custom One Pro linear bass position

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.4; 23 -0.8; 25 -1.2; 28 -1.7; 31 -2.0; 34 -2.3; 37 -2.4; 41 -2.5; 45 -2.4; 49 -1.9; 54 -1.1; 60 0.1; 66 1.9; 72 -0.1; 79 2.1; 87 5.2; 96 1.9; 106 -0.2; 116 -0.7; 128 -1.3; 141 -1.5; 155 -1.4; 170 -2.4; 187 -4.5; 206 -4.4; 227 -4.3; 249 -4.5; 274 -4.3; 302 -3.9; 332 -3.5; 365 -3.1; 402 -2.8; 442 -2.5; 486 -2.3; 535 -2.0; 588 -1.5; 647 -1.3; 712 -1.3; 783 -0.3; 861 -0.2; 947 -0.2; 1042 -0.0; 1146 0.0; 1261 -0.3; 1387 -0.9; 1526 -1.9; 1678 -3.0; 1846 -3.9; 2031 -4.9; 2234 -4.9; 2457 -3.5; 2703 -1.6; 2973 -0.1; 3270 1.0; 3597 1.7; 3957 2.0; 4353 4.5; 4788 5.9; 5267 6.0; 5793 6.0; 6373 3.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -1.1; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic Custom One Pro linear bass position GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic Custom One Pro linear bass position ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 38 Hz   |  1.82 | -2.8 dB |
| Peaking | 86 Hz   |  5.2  | 6.3 dB  |
| Peaking | 256 Hz  |  0.91 | -4.6 dB |
| Peaking | 2112 Hz |  2.5  | -5.7 dB |
| Peaking | 5134 Hz |  2.08 | 6.9 dB  |
| Peaking | 158 Hz  | 11.38 | 1.1 dB  |
| Peaking | 910 Hz  |  0.88 | -1.5 dB |
| Peaking | 991 Hz  |  1.51 | 2.2 dB  |
| Peaking | 6232 Hz |  4.81 | 1.1 dB  |
| Peaking | 8833 Hz |  2.8  | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20Custom%20One%20Pro%20linear%20bass%20position/Beyerdynamic%20Custom%20One%20Pro%20linear%20bass%20position.png)