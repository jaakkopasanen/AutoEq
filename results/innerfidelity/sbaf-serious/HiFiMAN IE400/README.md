# HiFiMAN IE400

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.7; 25 3.7; 28 3.6; 31 3.5; 34 3.4; 37 3.3; 41 3.2; 45 3.0; 49 2.8; 54 2.6; 60 2.3; 66 2.0; 72 1.7; 79 1.3; 87 0.9; 96 0.5; 106 0.2; 116 -0.1; 128 -0.4; 141 -0.7; 155 -0.9; 170 -1.0; 187 -1.0; 206 -1.1; 227 -1.1; 249 -1.1; 274 -1.0; 302 -0.8; 332 -0.6; 365 -0.5; 402 -0.3; 442 0.1; 486 0.1; 535 0.4; 588 0.9; 647 1.0; 712 1.0; 783 1.1; 861 0.7; 947 0.3; 1042 -0.2; 1146 -0.8; 1261 -1.5; 1387 -2.5; 1526 -3.6; 1678 -4.6; 1846 -5.1; 2031 -4.9; 2234 -3.1; 2457 -0.3; 2703 1.9; 2973 5.4; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 5.5; 5267 5.1; 5793 3.6; 6373 3.0; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN IE400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN IE400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.62 | 3.7 dB  |
| Peaking | 54 Hz   | 1.26 | 1.4 dB  |
| Peaking | 189 Hz  | 1.28 | -1.5 dB |
| Peaking | 1943 Hz | 1.87 | -8.5 dB |
| Peaking | 3593 Hz | 1.02 | 7.9 dB  |
| Peaking | 751 Hz  | 1.88 | 1.5 dB  |
| Peaking | 1637 Hz | 1.8  | -1.2 dB |
| Peaking | 1853 Hz | 5.09 | 1.5 dB  |
| Peaking | 6740 Hz | 1.85 | 3.0 dB  |
| Peaking | 7805 Hz | 1.68 | -3.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20IE400/HiFiMAN%20IE400.png)