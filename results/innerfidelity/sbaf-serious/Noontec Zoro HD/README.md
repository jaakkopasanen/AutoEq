# Noontec Zoro HD
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -3.8; 23 -3.9; 25 -4.0; 28 -4.2; 31 -4.3; 34 -4.4; 37 -4.5; 41 -4.6; 45 -4.7; 49 -4.8; 54 -4.9; 60 -5.1; 66 -5.3; 72 -5.6; 79 -5.8; 87 -6.0; 96 -6.4; 106 -6.6; 116 -6.7; 128 -6.8; 141 -6.6; 155 -6.8; 170 -6.5; 187 -6.5; 206 -6.5; 227 -6.1; 249 -5.5; 274 -4.8; 302 -4.5; 332 -4.2; 365 -3.6; 402 -3.2; 442 -2.6; 486 -2.5; 535 -1.9; 588 -1.5; 647 -1.2; 712 -0.9; 783 -0.5; 861 -0.4; 947 -0.2; 1042 0.2; 1146 0.7; 1261 1.1; 1387 0.9; 1526 0.7; 1678 0.8; 1846 1.2; 2031 1.5; 2234 1.6; 2457 2.5; 2703 2.8; 2973 2.7; 3270 1.9; 3597 3.0; 3957 5.5; 4353 6.0; 4788 6.0; 5267 4.4; 5793 5.9; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noontec Zoro HD GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontec Zoro HD ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.3  | -3.8 dB |
| Peaking | 125 Hz  | 0.74 | -3.7 dB |
| Peaking | 249 Hz  | 0.82 | -3.4 dB |
| Peaking | 4317 Hz | 1.38 | 5.4 dB  |
| Peaking | 6101 Hz | 5.17 | 3.6 dB  |
| Peaking | 1246 Hz | 3.8  | 1.1 dB  |
| Peaking | 2820 Hz | 2.03 | 2.0 dB  |
| Peaking | 3360 Hz | 3.25 | -3.5 dB |
| Peaking | 4043 Hz | 2.17 | 1.1 dB  |
| Peaking | 8415 Hz | 2.72 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noontec%20Zoro%20HD/Noontec%20Zoro%20HD.png)