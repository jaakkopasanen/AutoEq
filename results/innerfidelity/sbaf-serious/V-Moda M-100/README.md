# V-Moda M-100

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -3.7; 23 -3.8; 25 -3.9; 28 -4.0; 31 -4.1; 34 -4.2; 37 -4.3; 41 -4.4; 45 -4.4; 49 -4.5; 54 -4.7; 60 -4.9; 66 -4.9; 72 -4.9; 79 -5.2; 87 -5.2; 96 -5.0; 106 -5.1; 116 -5.7; 128 -6.3; 141 -6.3; 155 -5.8; 170 -4.8; 187 -4.7; 206 -3.6; 227 -2.3; 249 -0.9; 274 0.4; 302 0.7; 332 2.1; 365 3.5; 402 4.3; 442 4.6; 486 4.0; 535 3.5; 588 3.3; 647 2.5; 712 1.7; 783 1.2; 861 0.6; 947 0.2; 1042 -0.1; 1146 -0.2; 1261 -0.3; 1387 -0.5; 1526 -0.8; 1678 -0.9; 1846 -0.6; 2031 -0.6; 2234 -0.5; 2457 0.0; 2703 0.1; 2973 0.9; 3270 1.1; 3597 0.9; 3957 1.3; 4353 2.3; 4788 5.7; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.1; 9330 -3.8; 10263 -3.9; 11289 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`V-Moda M-100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda M-100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.71 | -2.8 dB |
| Peaking | 64 Hz   | 0.7  | -3.3 dB |
| Peaking | 151 Hz  | 1.12 | -5.1 dB |
| Peaking | 431 Hz  | 1.44 | 5.5 dB  |
| Peaking | 5465 Hz | 2.86 | 7.1 dB  |
| Peaking | 619 Hz  | 5.07 | 0.9 dB  |
| Peaking | 1619 Hz | 1.35 | -1.2 dB |
| Peaking | 7984 Hz | 0.73 | 1.0 dB  |
| Peaking | 9713 Hz | 3.94 | -6.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/V-Moda%20M-100/V-Moda%20M-100.png)