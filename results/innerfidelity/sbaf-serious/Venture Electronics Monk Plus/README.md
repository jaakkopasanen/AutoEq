# Venture Electronics Monk Plus

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 5.9; 87 4.8; 96 3.5; 106 2.3; 116 1.2; 128 0.1; 141 -0.9; 155 -1.8; 170 -2.1; 187 -2.4; 206 -2.1; 227 -2.2; 249 -2.2; 274 -2.0; 302 -1.6; 332 -1.2; 365 -0.8; 402 -2.5; 442 -0.6; 486 -0.3; 535 -0.2; 588 0.2; 647 0.3; 712 0.3; 783 0.4; 861 0.3; 947 0.1; 1042 -0.1; 1146 -0.3; 1261 -0.8; 1387 -1.9; 1526 -3.5; 1678 -5.0; 1846 -6.4; 2031 -7.5; 2234 -8.2; 2457 -7.5; 2703 -6.5; 2973 -4.1; 3270 -1.4; 3597 -0.0; 3957 -0.7; 4353 -2.8; 4788 -4.3; 5267 -2.7; 5793 -2.0; 6373 0.3; 7010 -4.4; 7711 -5.9; 8482 -4.7; 9330 -0.8; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -3.2; 15026 -7.1; 16529 -2.8; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Venture Electronics Monk Plus GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Venture Electronics Monk Plus ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 41 Hz    | 0.75 | 7.3 dB  |
| Peaking | 2209 Hz  | 1.85 | -8.6 dB |
| Peaking | 7755 Hz  | 4.17 | -6.2 dB |
| Peaking | 15126 Hz | 2.9  | -6.7 dB |
| Peaking | 24000 Hz | 1.64 | -4.4 dB |
| Peaking | 20 Hz    | 2.99 | 2.5 dB  |
| Peaking | 83 Hz    | 2.24 | 3.4 dB  |
| Peaking | 193 Hz   | 0.8  | -3.4 dB |
| Peaking | 2748 Hz  | 0.07 | 0.6 dB  |
| Peaking | 4881 Hz  | 6.28 | -4.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Venture%20Electronics%20Monk%20Plus/Venture%20Electronics%20Monk%20Plus.png)