# Focal Clear snA1BRQE000007

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.7; 25 3.5; 28 3.2; 31 3.0; 34 2.8; 37 2.6; 41 2.4; 45 2.3; 49 2.1; 54 1.9; 60 1.7; 66 1.4; 72 1.1; 79 0.8; 87 0.5; 96 0.1; 106 -0.0; 116 -0.1; 128 -0.4; 141 -0.4; 155 -0.4; 170 -0.4; 187 -0.3; 206 -0.2; 227 -0.0; 249 0.0; 274 0.3; 302 0.4; 332 0.6; 365 0.8; 402 0.9; 442 1.1; 486 1.1; 535 1.1; 588 1.4; 647 1.3; 712 1.1; 783 1.2; 861 0.7; 947 0.3; 1042 -0.1; 1146 -0.7; 1261 -1.1; 1387 -1.2; 1526 -0.7; 1678 -0.9; 1846 -0.4; 2031 0.6; 2234 1.1; 2457 1.4; 2703 1.2; 2973 1.1; 3270 0.9; 3597 0.8; 3957 4.0; 4353 4.3; 4788 4.5; 5267 6.0; 5793 3.3; 6373 2.4; 7010 2.5; 7711 0.3; 8482 -0.6; 9330 -0.3; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Clear snA1BRQE000007 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Clear snA1BRQE000007 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.09 | 3.8 dB  |
| Peaking | 51 Hz   | 1.83 | 1.5 dB  |
| Peaking | 564 Hz  | 1.8  | 1.5 dB  |
| Peaking | 4117 Hz | 5.99 | 3.0 dB  |
| Peaking | 5253 Hz | 3.05 | 5.5 dB  |
| Peaking | 147 Hz  | 2.15 | -0.7 dB |
| Peaking | 1396 Hz | 2.66 | -1.5 dB |
| Peaking | 2472 Hz | 3.61 | 1.5 dB  |
| Peaking | 6826 Hz | 9.49 | 3.5 dB  |
| Peaking | 7447 Hz | 1.53 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Focal%20Clear%20snA1BRQE000007/Focal%20Clear%20snA1BRQE000007.png)