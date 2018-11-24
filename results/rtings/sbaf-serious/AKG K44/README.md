# AKG K44

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.7; 37 5.2; 41 4.6; 45 4.2; 49 3.9; 54 3.6; 60 3.4; 66 3.2; 72 3.2; 79 3.2; 87 3.3; 96 3.3; 106 3.2; 116 3.0; 128 2.8; 141 2.6; 155 2.5; 170 2.3; 187 2.2; 206 2.1; 227 2.1; 249 2.0; 274 1.9; 302 1.8; 332 1.8; 365 1.8; 402 1.7; 442 1.4; 486 1.6; 535 2.4; 588 2.7; 647 1.5; 712 1.6; 783 2.7; 861 2.3; 947 0.5; 1042 -0.2; 1146 0.1; 1261 1.2; 1387 2.4; 1526 3.6; 1678 5.3; 1846 6.0; 2031 6.0; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K44 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K44 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.76 | 5.7 dB  |
| Peaking | 117 Hz  | 0.39 | 2.5 dB  |
| Peaking | 569 Hz  | 3.11 | 1.7 dB  |
| Peaking | 2367 Hz | 1.11 | 6.0 dB  |
| Peaking | 5037 Hz | 1.66 | 5.4 dB  |
| Peaking | 819 Hz  | 5.86 | 2.4 dB  |
| Peaking | 1064 Hz | 2.59 | -2.1 dB |
| Peaking | 1717 Hz | 5.63 | 1.8 dB  |
| Peaking | 6388 Hz | 4.64 | 3.4 dB  |
| Peaking | 7568 Hz | 1.79 | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/AKG%20K44/AKG%20K44.png)