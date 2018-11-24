# Klipsch X20i

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.4; 23 -0.5; 25 -0.6; 28 -0.8; 31 -0.9; 34 -1.1; 37 -1.1; 41 -1.3; 45 -1.4; 49 -1.5; 54 -1.8; 60 -2.0; 66 -2.3; 72 -2.7; 79 -3.0; 87 -3.3; 96 -3.7; 106 -3.9; 116 -4.1; 128 -4.3; 141 -4.4; 155 -4.5; 170 -4.5; 187 -4.5; 206 -4.5; 227 -4.3; 249 -4.1; 274 -3.9; 302 -3.6; 332 -3.3; 365 -2.9; 402 -2.6; 442 -2.2; 486 -1.9; 535 -1.4; 588 -0.8; 647 -0.4; 712 -0.1; 783 0.3; 861 0.3; 947 0.2; 1042 -0.0; 1146 -0.1; 1261 -0.3; 1387 -0.8; 1526 -1.2; 1678 -1.4; 1846 -1.4; 2031 -1.3; 2234 -1.5; 2457 -1.2; 2703 -0.8; 2973 1.4; 3270 5.1; 3597 6.0; 3957 6.0; 4353 5.1; 4788 3.8; 5267 3.8; 5793 4.4; 6373 5.4; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Klipsch X20i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch X20i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 130 Hz  | 0.59 | -4.0 dB |
| Peaking | 285 Hz  | 1.2  | -2.0 dB |
| Peaking | 2558 Hz | 1.45 | -4.2 dB |
| Peaking | 3652 Hz | 1.81 | 8.3 dB  |
| Peaking | 6213 Hz | 4.74 | 4.5 dB  |
| Peaking | 484 Hz  | 1.77 | -1.0 dB |
| Peaking | 730 Hz  | 0.9  | 1.1 dB  |
| Peaking | 1582 Hz | 3.54 | -0.9 dB |
| Peaking | 8253 Hz | 4.13 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Klipsch%20X20i/Klipsch%20X20i.png)