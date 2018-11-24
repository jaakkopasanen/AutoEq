# Yutai BAS02

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.0; 23 -1.1; 25 -1.2; 28 -1.3; 31 -1.5; 34 -1.6; 37 -1.7; 41 -1.8; 45 -2.0; 49 -2.1; 54 -2.3; 60 -2.5; 66 -2.7; 72 -3.0; 79 -3.3; 87 -3.6; 96 -3.9; 106 -4.1; 116 -4.2; 128 -4.4; 141 -4.5; 155 -4.6; 170 -4.6; 187 -4.5; 206 -4.5; 227 -4.3; 249 -4.2; 274 -3.9; 302 -3.6; 332 -3.4; 365 -3.1; 402 -2.8; 442 -2.3; 486 -2.1; 535 -1.6; 588 -1.0; 647 -0.6; 712 -0.4; 783 0.1; 861 0.1; 947 -0.0; 1042 -0.1; 1146 -0.2; 1261 -0.4; 1387 -0.7; 1526 -1.0; 1678 -1.1; 1846 -0.8; 2031 -0.3; 2234 -0.2; 2457 -0.1; 2703 -0.4; 2973 0.1; 3270 3.1; 3597 5.9; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yutai BAS02 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yutai BAS02 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 65 Hz   | 0.39 | -1.6 dB |
| Peaking | 159 Hz  | 0.7  | -3.4 dB |
| Peaking | 331 Hz  | 1.33 | -1.7 dB |
| Peaking | 2569 Hz | 1.27 | -2.8 dB |
| Peaking | 4399 Hz | 1.25 | 7.8 dB  |
| Peaking | 1466 Hz | 1    | 1.4 dB  |
| Peaking | 1511 Hz | 2.12 | -2.1 dB |
| Peaking | 4586 Hz | 7.05 | -1.3 dB |
| Peaking | 6356 Hz | 3.07 | 4.2 dB  |
| Peaking | 7486 Hz | 1.78 | -3.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yutai%20BAS02/Yutai%20BAS02.png)