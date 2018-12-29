# Grado HF-1 Prototype
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.9; 45 5.2; 49 4.1; 54 2.8; 60 1.7; 66 0.9; 72 -0.1; 79 -1.1; 87 -1.8; 96 -2.2; 106 -2.4; 116 -2.4; 128 -2.3; 141 -2.1; 155 -1.8; 170 -1.4; 187 -1.0; 206 -1.0; 227 -0.7; 249 -0.5; 274 -0.2; 302 0.4; 332 0.2; 365 0.5; 402 0.5; 442 0.5; 486 0.4; 535 0.6; 588 0.7; 647 0.7; 712 0.6; 783 0.7; 861 0.3; 947 0.1; 1042 -0.1; 1146 -0.3; 1261 -1.0; 1387 -2.0; 1526 -3.2; 1678 -3.9; 1846 -4.5; 2031 -5.3; 2234 -5.1; 2457 -3.8; 2703 -3.5; 2973 -1.8; 3270 -0.7; 3597 -1.3; 3957 -1.5; 4353 -6.4; 4788 -8.9; 5267 -5.0; 5793 -3.1; 6373 -4.0; 7010 -6.4; 7711 -7.3; 8482 -9.9; 9330 -11.1; 10263 -5.9; 11289 -0.2; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -1.9; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado HF-1 Prototype GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado HF-1 Prototype ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 59 Hz    | 0.19 | 11.1 dB  |
| Peaking | 107 Hz   | 0.49 | -12.8 dB |
| Peaking | 2009 Hz  | 1.93 | -5.5 dB  |
| Peaking | 4730 Hz  | 5.4  | -8.3 dB  |
| Peaking | 8756 Hz  | 2.64 | -11.5 dB |
| Peaking | 13 Hz    | 1.86 | -1.0 dB  |
| Peaking | 3549 Hz  | 6.25 | 1.2 dB   |
| Peaking | 9807 Hz  | 6.43 | -3.4 dB  |
| Peaking | 11421 Hz | 2.79 | 3.1 dB   |
| Peaking | 18477 Hz | 4.04 | -2.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20HF-1%20Prototype/Grado%20HF-1%20Prototype.png)