# Sleek SA6 Neutral

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.8; 25 2.6; 28 2.4; 31 2.2; 34 2.0; 37 1.8; 41 1.6; 45 1.3; 49 1.1; 54 0.8; 60 0.4; 66 0.2; 72 -0.3; 79 -0.7; 87 -1.0; 96 -1.3; 106 -1.5; 116 -1.8; 128 -2.1; 141 -2.4; 155 -2.6; 170 -2.8; 187 -2.9; 206 -2.8; 227 -2.8; 249 -2.8; 274 -2.6; 302 -2.4; 332 -2.1; 365 -2.0; 402 -2.1; 442 -1.9; 486 -1.6; 535 -1.3; 588 -0.8; 647 -0.4; 712 -0.2; 783 0.2; 861 0.3; 947 0.2; 1042 -0.1; 1146 -0.4; 1261 -0.7; 1387 -1.2; 1526 -1.6; 1678 -1.8; 1846 -1.9; 2031 -1.6; 2234 -0.8; 2457 0.8; 2703 3.3; 2973 5.8; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sleek SA6 Neutral GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sleek SA6 Neutral ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.55 | 0.3 dB  |
| Peaking | 20 Hz   | 0.48 | 2.8 dB  |
| Peaking | 196 Hz  | 0.57 | -3.1 dB |
| Peaking | 1951 Hz | 1.78 | -4.6 dB |
| Peaking | 3860 Hz | 0.93 | 7.5 dB  |
| Peaking | 843 Hz  | 3.66 | 0.9 dB  |
| Peaking | 2976 Hz | 6.2  | 2.2 dB  |
| Peaking | 5995 Hz | 0.68 | -2.4 dB |
| Peaking | 6246 Hz | 2.07 | 5.5 dB  |
| Peaking | 7546 Hz | 2.99 | -2.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sleek%20SA6%20Neutral/Sleek%20SA6%20Neutral.png)