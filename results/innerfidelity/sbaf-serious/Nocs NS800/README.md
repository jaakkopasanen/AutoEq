# Nocs NS800
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.6; 25 0.5; 28 0.4; 31 0.3; 34 0.3; 37 0.2; 41 0.1; 45 -0.1; 49 -0.1; 54 -0.3; 60 -0.6; 66 -0.9; 72 -1.1; 79 -1.4; 87 -1.8; 96 -2.1; 106 -2.4; 116 -2.4; 128 -2.8; 141 -2.9; 155 -3.0; 170 -3.1; 187 -3.1; 206 -3.0; 227 -2.9; 249 -2.9; 274 -2.6; 302 -2.5; 332 -2.3; 365 -2.0; 402 -1.8; 442 -1.3; 486 -1.2; 535 -0.9; 588 -0.3; 647 -0.0; 712 0.2; 783 0.5; 861 0.4; 947 0.2; 1042 -0.0; 1146 -0.2; 1261 -0.4; 1387 -0.8; 1526 -1.2; 1678 -1.3; 1846 -1.0; 2031 -0.7; 2234 -0.6; 2457 -0.3; 2703 -0.6; 2973 0.1; 3270 2.8; 3597 5.9; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 -0.3; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Nocs NS800 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nocs NS800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.63 | 0.7 dB  |
| Peaking | 176 Hz  | 0.6  | -3.3 dB |
| Peaking | 1777 Hz | 2.26 | -1.9 dB |
| Peaking | 2796 Hz | 4.02 | -3.3 dB |
| Peaking | 4450 Hz | 1.25 | 7.2 dB  |
| Peaking | 371 Hz  | 2.4  | -0.4 dB |
| Peaking | 769 Hz  | 2.41 | 0.9 dB  |
| Peaking | 3565 Hz | 8.71 | 2.0 dB  |
| Peaking | 6261 Hz | 2.92 | 6.1 dB  |
| Peaking | 6654 Hz | 1.24 | -4.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Nocs%20NS800/Nocs%20NS800.png)