# Grado RS1e Bowl Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.9; 66 4.6; 72 3.1; 79 1.6; 87 0.1; 96 -1.2; 106 -2.0; 116 -2.3; 128 -2.7; 141 -2.8; 155 -2.6; 170 -2.3; 187 -1.9; 206 -1.4; 227 -0.9; 249 -0.4; 274 -0.3; 302 -1.0; 332 -0.5; 365 -0.1; 402 0.1; 442 0.5; 486 0.5; 535 0.6; 588 0.9; 647 0.9; 712 0.7; 783 0.8; 861 0.5; 947 0.2; 1042 -0.2; 1146 -0.6; 1261 -1.1; 1387 -2.1; 1526 -2.8; 1678 -5.1; 1846 -10.7; 2031 -11.1; 2234 -8.4; 2457 -4.1; 2703 -0.7; 2973 1.9; 3270 3.1; 3597 3.8; 3957 5.8; 4353 6.0; 4788 3.1; 5267 5.8; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado RS1e Bowl Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado RS1e Bowl Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 78 Hz   | 0.25 | 14.2 dB  |
| Peaking | 123 Hz  | 0.53 | -16.0 dB |
| Peaking | 2006 Hz | 2.99 | -13.3 dB |
| Peaking | 3911 Hz | 1.7  | 6.1 dB   |
| Peaking | 5958 Hz | 4.06 | 5.0 dB   |
| Peaking | 59 Hz   | 4.7  | 1.4 dB   |
| Peaking | 89 Hz   | 4.4  | -0.8 dB  |
| Peaking | 311 Hz  | 4.87 | -1.1 dB  |
| Peaking | 6693 Hz | 9.48 | 1.7 dB   |
| Peaking | 7928 Hz | 2.49 | -1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20RS1e%20Bowl%20Pads/Grado%20RS1e%20Bowl%20Pads.png)