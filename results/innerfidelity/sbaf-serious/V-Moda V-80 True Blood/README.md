# V-Moda V-80 True Blood

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.9dB
GraphicEQ: 21 0.0; 23 0.5; 25 0.2; 28 -0.1; 31 -0.3; 34 -0.5; 37 -0.7; 41 -0.9; 45 -1.0; 49 -1.1; 54 -1.3; 60 -1.5; 66 -1.7; 72 -1.9; 79 -1.9; 87 -2.1; 96 -2.6; 106 -2.8; 116 -2.6; 128 -2.7; 141 -3.0; 155 -3.0; 170 -2.7; 187 -2.7; 206 -2.4; 227 -3.0; 249 -2.3; 274 -1.3; 302 -0.1; 332 0.6; 365 1.1; 402 1.7; 442 2.3; 486 2.9; 535 3.6; 588 4.2; 647 4.0; 712 3.4; 783 2.8; 861 1.7; 947 0.7; 1042 -0.4; 1146 -1.5; 1261 -2.2; 1387 -2.8; 1526 -2.6; 1678 -2.0; 1846 -0.7; 2031 0.7; 2234 1.6; 2457 2.3; 2703 2.2; 2973 1.7; 3270 0.2; 3597 0.7; 3957 2.8; 4353 3.8; 4788 2.6; 5267 4.4; 5793 3.9; 6373 2.9; 7010 2.4; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`V-Moda V-80 True Blood GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-48**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda V-80 True Blood ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.4dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 192 Hz  |  0.45 | -4.0 dB |
| Peaking | 608 Hz  |  0.71 | 6.7 dB  |
| Peaking | 1373 Hz |  1.02 | -5.5 dB |
| Peaking | 2335 Hz |  2.12 | 3.5 dB  |
| Peaking | 5296 Hz |  1.94 | 4.4 dB  |
| Peaking | 20 Hz   |  1.86 | 1.3 dB  |
| Peaking | 324 Hz  |  8.49 | 0.6 dB  |
| Peaking | 3403 Hz | 14.62 | -1.4 dB |
| Peaking | 6775 Hz |  8.78 | 1.6 dB  |
| Peaking | 8036 Hz |  2.74 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/V-Moda%20V-80%20True%20Blood/V-Moda%20V-80%20True%20Blood.png)