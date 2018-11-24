# AKG K581LE

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.7; 31 5.2; 34 4.7; 37 4.2; 41 3.7; 45 3.3; 49 3.1; 54 2.8; 60 1.9; 66 1.2; 72 1.0; 79 0.7; 87 -0.5; 96 -0.8; 106 0.3; 116 -0.4; 128 -1.5; 141 -2.7; 155 -3.0; 170 -2.6; 187 -2.1; 206 -1.8; 227 -2.1; 249 -1.3; 274 -0.9; 302 -1.2; 332 -0.7; 365 -0.1; 402 0.7; 442 1.0; 486 1.1; 535 1.1; 588 1.2; 647 1.0; 712 0.8; 783 0.7; 861 0.4; 947 0.1; 1042 -0.0; 1146 -0.1; 1261 0.1; 1387 -0.6; 1526 -1.0; 1678 -0.9; 1846 -0.5; 2031 0.4; 2234 1.2; 2457 2.4; 2703 3.5; 2973 4.3; 3270 4.8; 3597 4.8; 3957 4.7; 4353 4.2; 4788 4.8; 5267 3.1; 5793 5.7; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K581LE GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K581LE ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 24 Hz   |  0.88 | 6.2 dB  |
| Peaking | 52 Hz   |  2.74 | 1.1 dB  |
| Peaking | 167 Hz  |  1.58 | -3.1 dB |
| Peaking | 3590 Hz |  1.68 | 5.2 dB  |
| Peaking | 6108 Hz |  4.34 | 5.2 dB  |
| Peaking | 557 Hz  |  1.93 | 1.4 dB  |
| Peaking | 1656 Hz |  2.31 | -1.7 dB |
| Peaking | 2648 Hz |  5.19 | 1.3 dB  |
| Peaking | 4788 Hz | 10.58 | 1.6 dB  |
| Peaking | 8299 Hz |  3.2  | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K581LE/AKG%20K581LE.png)