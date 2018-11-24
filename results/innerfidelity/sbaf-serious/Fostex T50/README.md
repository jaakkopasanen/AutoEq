# Fostex T50

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 6.0; 128 5.3; 141 3.8; 155 3.4; 170 3.5; 187 3.4; 206 3.2; 227 3.0; 249 2.9; 274 2.7; 302 2.4; 332 2.2; 365 1.7; 402 0.6; 442 0.7; 486 1.0; 535 0.8; 588 0.8; 647 0.7; 712 0.2; 783 0.4; 861 0.3; 947 0.3; 1042 -0.0; 1146 0.3; 1261 0.4; 1387 0.2; 1526 -0.4; 1678 -0.8; 1846 -0.7; 2031 -1.0; 2234 -0.5; 2457 0.4; 2703 1.4; 2973 1.9; 3270 3.8; 3597 3.9; 3957 3.0; 4353 4.1; 4788 5.9; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fostex T50 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex T50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.27 | 6.1 dB  |
| Peaking | 107 Hz  | 1.72 | 2.3 dB  |
| Peaking | 257 Hz  | 1.42 | 1.6 dB  |
| Peaking | 3430 Hz | 4.15 | 3.1 dB  |
| Peaking | 5423 Hz | 2.33 | 6.7 dB  |
| Peaking | 1940 Hz | 3.5  | -1.4 dB |
| Peaking | 6531 Hz | 6.68 | 2.5 dB  |
| Peaking | 7756 Hz | 2.35 | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fostex%20T50/Fostex%20T50.png)