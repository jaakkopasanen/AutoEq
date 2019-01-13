# Westone 4R
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.5; 25 2.0; 28 1.4; 31 0.9; 34 0.4; 37 -0.0; 41 -0.5; 45 -0.9; 49 -1.2; 54 -1.7; 60 -2.1; 66 -2.6; 72 -3.1; 79 -3.5; 87 -4.1; 96 -4.6; 106 -4.9; 116 -5.2; 128 -5.6; 141 -5.8; 155 -6.0; 170 -6.1; 187 -6.2; 206 -6.2; 227 -6.1; 249 -6.1; 274 -5.9; 302 -5.7; 332 -5.4; 365 -5.0; 402 -4.6; 442 -4.1; 486 -3.8; 535 -3.2; 588 -2.3; 647 -1.6; 712 -1.1; 783 -0.3; 861 -0.0; 947 0.1; 1042 -0.1; 1146 -0.4; 1261 -0.7; 1387 -1.0; 1526 -1.1; 1678 -0.8; 1846 0.0; 2031 1.1; 2234 2.0; 2457 3.2; 2703 4.1; 2973 5.5; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -1.8; 9330 -6.2; 10263 -7.4; 11289 -2.4; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone 4R GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone 4R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 19 Hz   | 1.1  | 3.5 dB   |
| Peaking | 108 Hz  | 0.71 | -2.9 dB  |
| Peaking | 259 Hz  | 0.59 | -5.2 dB  |
| Peaking | 4594 Hz | 0.85 | 7.2 dB   |
| Peaking | 9801 Hz | 3.15 | -10.1 dB |
| Peaking | 866 Hz  | 2.75 | 1.4 dB   |
| Peaking | 1597 Hz | 2.15 | -2.0 dB  |
| Peaking | 3091 Hz | 2.06 | 2.5 dB   |
| Peaking | 4213 Hz | 1.05 | -1.5 dB  |
| Peaking | 6140 Hz | 5.39 | 2.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Westone%204R/Westone%204R.png)