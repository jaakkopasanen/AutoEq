# Beyerdynamic DT 240 Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.0; 23 -1.4; 25 -1.8; 28 -2.4; 31 -2.8; 34 -3.1; 37 -3.4; 41 -3.7; 45 -3.9; 49 -4.0; 54 -4.2; 60 -4.3; 66 -4.3; 72 -4.4; 79 -3.9; 87 -3.1; 96 -4.3; 106 -5.6; 116 -5.6; 128 -4.8; 141 -4.7; 155 -5.1; 170 -4.7; 187 -4.9; 206 -4.6; 227 -3.7; 249 -3.1; 274 -2.3; 302 -1.3; 332 -0.4; 365 0.0; 402 -0.7; 442 -0.7; 486 -0.9; 535 -0.6; 588 -0.1; 647 -0.2; 712 -0.5; 783 -0.4; 861 -0.5; 947 -0.3; 1042 0.2; 1146 -0.0; 1261 -0.4; 1387 -1.1; 1526 -2.0; 1678 -2.7; 1846 -2.9; 2031 -2.8; 2234 -2.4; 2457 -1.0; 2703 0.3; 2973 1.8; 3270 3.3; 3597 5.6; 3957 2.2; 4353 1.9; 4788 5.3; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.1; 9330 -1.2; 10263 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 240 Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 240 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 49 Hz   | 0.7  | -3.5 dB |
| Peaking | 153 Hz  | 0.92 | -4.6 dB |
| Peaking | 3562 Hz | 6.56 | 5.0 dB  |
| Peaking | 5588 Hz | 2.97 | 6.9 dB  |
| Peaking | 219 Hz  | 4.04 | -0.7 dB |
| Peaking | 352 Hz  | 5.88 | 1.5 dB  |
| Peaking | 1950 Hz | 1.65 | -5.5 dB |
| Peaking | 2158 Hz | 0.8  | 2.2 dB  |
| Peaking | 9017 Hz | 4.29 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20240%20Pro/Beyerdynamic%20DT%20240%20Pro.png)