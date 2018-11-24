# 1MORE Crystal Piston

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.6dB
GraphicEQ: 21 -6.4; 23 -6.8; 25 -7.2; 28 -7.6; 31 -7.8; 34 -8.1; 37 -8.5; 41 -8.7; 45 -8.8; 49 -9.0; 54 -9.2; 60 -9.4; 66 -9.6; 72 -9.8; 79 -9.9; 87 -10.1; 96 -10.1; 106 -10.2; 116 -9.9; 128 -9.9; 141 -9.7; 155 -9.5; 170 -9.2; 187 -8.9; 206 -8.4; 227 -7.9; 249 -7.4; 274 -6.8; 302 -6.2; 332 -5.6; 365 -4.9; 402 -4.3; 442 -3.5; 486 -2.9; 535 -2.3; 588 -1.4; 647 -0.8; 712 -0.4; 783 0.3; 861 0.2; 947 0.3; 1042 0.1; 1146 0.2; 1261 0.5; 1387 0.2; 1526 -0.3; 1678 -1.4; 1846 -2.6; 2031 -2.7; 2234 -2.4; 2457 -1.8; 2703 -1.6; 2973 -1.3; 3270 -0.9; 3597 -1.2; 3957 -2.2; 4353 -4.8; 4788 -6.6; 5267 -7.5; 5793 -7.8; 6373 -5.8; 7010 -4.0; 7711 -3.9; 8482 -5.2; 9330 -4.5; 10263 -0.5; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1MORE Crystal Piston GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-6**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Crystal Piston ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 45 Hz    | 0.33 | -8.0 dB |
| Peaking | 143 Hz   | 0.72 | -5.2 dB |
| Peaking | 291 Hz   | 1.28 | -2.8 dB |
| Peaking | 5463 Hz  | 1.89 | -8.0 dB |
| Peaking | 8769 Hz  | 5.27 | -4.3 dB |
| Peaking | 469 Hz   | 2.26 | -1.0 dB |
| Peaking | 1041 Hz  | 0.69 | 1.4 dB  |
| Peaking | 2002 Hz  | 2.33 | -3.1 dB |
| Peaking | 3542 Hz  | 5.92 | 1.3 dB  |
| Peaking | 11067 Hz | 4.96 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/1MORE%20Crystal%20Piston/1MORE%20Crystal%20Piston.png)