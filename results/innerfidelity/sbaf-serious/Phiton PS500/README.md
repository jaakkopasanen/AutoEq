# Phiton PS500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.9; 28 5.5; 31 4.6; 34 3.7; 37 2.9; 41 2.2; 45 1.7; 49 1.2; 54 0.9; 60 0.4; 66 0.0; 72 -0.2; 79 -1.0; 87 -1.5; 96 -2.1; 106 -2.4; 116 -2.7; 128 -3.2; 141 -3.3; 155 -3.2; 170 -2.9; 187 -2.9; 206 -2.5; 227 -1.9; 249 -1.2; 274 0.1; 302 1.5; 332 2.4; 365 2.8; 402 2.8; 442 2.8; 486 2.5; 535 2.5; 588 2.6; 647 2.2; 712 1.5; 783 1.3; 861 1.6; 947 0.6; 1042 -0.3; 1146 -0.9; 1261 -1.4; 1387 -2.1; 1526 -2.4; 1678 -2.6; 1846 -2.2; 2031 -0.8; 2234 1.3; 2457 4.3; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 4.2; 4788 6.0; 5267 6.0; 5793 5.2; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phiton PS500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiton PS500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 0.26 | 7.3 dB  |
| Peaking | 506 Hz  | 0.49 | 12.3 dB |
| Peaking | 620 Hz  | 0.09 | -9.4 dB |
| Peaking | 2923 Hz | 1.65 | 10.1 dB |
| Peaking | 5269 Hz | 1.23 | 9.4 dB  |
| Peaking | 192 Hz  | 3.52 | -0.7 dB |
| Peaking | 921 Hz  | 4.76 | 1.2 dB  |
| Peaking | 1778 Hz | 3.37 | -1.1 dB |
| Peaking | 2497 Hz | 9.05 | 1.5 dB  |
| Peaking | 7888 Hz | 8.05 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phiton%20PS500/Phiton%20PS500.png)