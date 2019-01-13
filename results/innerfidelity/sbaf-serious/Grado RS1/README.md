# Grado RS1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.7; 49 4.8; 54 3.5; 60 2.2; 66 1.1; 72 0.0; 79 -1.0; 87 -2.0; 96 -2.7; 106 -3.2; 116 -3.3; 128 -3.4; 141 -3.3; 155 -3.1; 170 -2.8; 187 -2.5; 206 -2.2; 227 -1.6; 249 -1.7; 274 -1.6; 302 -1.3; 332 -1.0; 365 -0.6; 402 -0.9; 442 -0.6; 486 -0.5; 535 -0.2; 588 0.0; 647 0.1; 712 0.0; 783 0.4; 861 0.3; 947 0.0; 1042 -0.0; 1146 -0.1; 1261 -0.9; 1387 -2.0; 1526 -3.8; 1678 -5.1; 1846 -9.9; 2031 -8.4; 2234 -7.2; 2457 -5.4; 2703 -4.1; 2973 -1.8; 3270 -0.4; 3597 0.9; 3957 -2.3; 4353 -9.8; 4788 -8.0; 5267 -5.3; 5793 -5.2; 6373 -8.4; 7010 -10.4; 7711 -8.0; 8482 -8.5; 9330 -9.1; 10263 -2.1; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -0.0; 16529 -5.1; 18182 -7.1; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado RS1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado RS1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 1.53 | 7.5 dB  |
| Peaking | 1959 Hz  | 2.96 | -9.5 dB |
| Peaking | 7030 Hz  | 1.25 | -9.7 dB |
| Peaking | 17827 Hz | 2.37 | -8.5 dB |
| Peaking | 22050 Hz | 2.01 | -5.0 dB |
| Peaking | 136 Hz   | 1.1  | -3.9 dB |
| Peaking | 3642 Hz  | 5.42 | 4.9 dB  |
| Peaking | 4432 Hz  | 7.17 | -8.3 dB |
| Peaking | 9263 Hz  | 3.9  | -9.1 dB |
| Peaking | 10175 Hz | 1.35 | 5.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20RS1/Grado%20RS1.png)