# Grado SR225i Goo Bowl

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 5.8; 41 5.0; 45 3.9; 49 3.2; 54 2.5; 60 1.4; 66 0.4; 72 -0.3; 79 -0.9; 87 -1.4; 96 -1.9; 106 -2.1; 116 -2.2; 128 -2.4; 141 -2.3; 155 -2.2; 170 -2.0; 187 -1.8; 206 -1.5; 227 -1.2; 249 -1.0; 274 -0.6; 302 -0.6; 332 -0.6; 365 -0.3; 402 -0.3; 442 -0.1; 486 -0.1; 535 -0.0; 588 0.3; 647 0.3; 712 0.3; 783 0.5; 861 0.2; 947 0.1; 1042 -0.2; 1146 -0.4; 1261 -0.9; 1387 -2.0; 1526 -2.9; 1678 -3.9; 1846 -5.8; 2031 -8.3; 2234 -7.1; 2457 -4.6; 2703 -3.0; 2973 -2.6; 3270 -1.4; 3597 -2.9; 3957 -1.8; 4353 -0.1; 4788 -0.5; 5267 -2.4; 5793 -0.8; 6373 -1.7; 7010 -4.8; 7711 -6.1; 8482 -7.9; 9330 -9.1; 10263 -4.4; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR225i Goo Bowl GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR225i Goo Bowl ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 29 Hz    |  0.62 | 6.9 dB  |
| Peaking | 104 Hz   |  0.74 | -3.6 dB |
| Peaking | 2061 Hz  |  2.43 | -1.3 dB |
| Peaking | 2082 Hz  |  2.45 | -6.8 dB |
| Peaking | 8747 Hz  |  2.73 | -9.4 dB |
| Peaking | 764 Hz   |  1.73 | 0.8 dB  |
| Peaking | 3643 Hz  | 10.47 | -1.9 dB |
| Peaking | 9801 Hz  |  7.02 | -3.5 dB |
| Peaking | 11062 Hz |  2.85 | 2.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR225i%20Goo%20Bowl/Grado%20SR225i%20Goo%20Bowl.png)