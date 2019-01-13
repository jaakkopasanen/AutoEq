# Grado SR225 Comfy Pad with Hole
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.8; 34 5.2; 37 4.3; 41 3.3; 45 2.4; 49 1.7; 54 1.0; 60 0.3; 66 -0.4; 72 -1.0; 79 -1.5; 87 -1.8; 96 -2.3; 106 -2.3; 116 -2.4; 128 -2.5; 141 -2.4; 155 -2.3; 170 -2.1; 187 -2.0; 206 -1.8; 227 -1.4; 249 -1.2; 274 -0.8; 302 -0.9; 332 -0.8; 365 -0.5; 402 -0.4; 442 -0.2; 486 -0.1; 535 -0.0; 588 0.3; 647 0.4; 712 0.3; 783 0.4; 861 0.3; 947 0.1; 1042 -0.1; 1146 -0.2; 1261 -0.7; 1387 -1.6; 1526 -2.7; 1678 -3.4; 1846 -5.0; 2031 -8.8; 2234 -9.2; 2457 -6.0; 2703 -3.3; 2973 -1.6; 3270 -0.0; 3597 -1.3; 3957 0.4; 4353 2.5; 4788 2.1; 5267 0.8; 5793 3.3; 6373 3.9; 7010 0.9; 7711 -1.6; 8482 -3.7; 9330 -4.1; 10263 -0.3; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR225 Comfy Pad with Hole GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR225 Comfy Pad with Hole ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 26 Hz   | 0.82 | 6.7 dB   |
| Peaking | 110 Hz  | 0.7  | -3.1 dB  |
| Peaking | 2159 Hz | 2.9  | -10.1 dB |
| Peaking | 6509 Hz | 1.18 | 4.6 dB   |
| Peaking | 8537 Hz | 2.69 | -7.2 dB  |
| Peaking | 821 Hz  | 1.23 | 0.8 dB   |
| Peaking | 1510 Hz | 7.23 | -0.9 dB  |
| Peaking | 4486 Hz | 5.68 | 3.3 dB   |
| Peaking | 5336 Hz | 2.27 | -3.0 dB  |
| Peaking | 6111 Hz | 5.67 | 3.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR225%20Comfy%20Pad%20with%20Hole/Grado%20SR225%20Comfy%20Pad%20with%20Hole.png)