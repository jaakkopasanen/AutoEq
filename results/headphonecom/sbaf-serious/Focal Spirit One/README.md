# Focal Spirit One

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 21 -4.8; 23 -4.9; 25 -4.9; 28 -4.9; 31 -5.0; 34 -5.1; 37 -5.1; 41 -5.0; 45 -5.0; 49 -5.1; 54 -5.2; 60 -5.1; 66 -5.1; 72 -5.2; 79 -5.2; 87 -5.0; 96 -4.5; 106 -5.2; 116 -6.3; 128 -6.7; 141 -6.7; 155 -6.6; 170 -6.4; 187 -6.5; 206 -5.9; 227 -5.5; 249 -4.9; 274 -4.4; 302 -3.8; 332 -3.3; 365 -2.8; 402 -2.6; 442 -2.8; 486 -2.8; 535 -2.6; 588 -2.5; 647 -2.2; 712 -1.8; 783 -1.1; 861 -0.7; 947 -0.5; 1042 -0.0; 1146 -1.1; 1261 -0.9; 1387 -1.0; 1526 -1.4; 1678 -1.5; 1846 -0.8; 2031 0.2; 2234 1.6; 2457 3.0; 2703 4.3; 2973 4.9; 3270 4.8; 3597 3.5; 3957 1.4; 4353 0.4; 4788 0.6; 5267 1.8; 5793 5.1; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Spirit One GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-59**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Spirit One ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 1.06 | -3.7 dB |
| Peaking | 44 Hz    | 1.14 | -2.2 dB |
| Peaking | 160 Hz   | 0.45 | -6.1 dB |
| Peaking | 3017 Hz  | 2.94 | 5.6 dB  |
| Peaking | 6184 Hz  | 5.2  | 6.2 dB  |
| Peaking | 347 Hz   | 2.79 | 0.9 dB  |
| Peaking | 574 Hz   | 3.11 | -0.9 dB |
| Peaking | 1622 Hz  | 4.07 | -1.8 dB |
| Peaking | 24000 Hz | 1.84 | 0.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Focal%20Spirit%20One/Focal%20Spirit%20One.png)