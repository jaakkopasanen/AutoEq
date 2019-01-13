# Lear LUF 4C
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.2; 25 0.1; 28 -0.1; 31 -0.3; 34 -0.5; 37 -0.6; 41 -0.8; 45 -1.0; 49 -1.2; 54 -1.5; 60 -1.9; 66 -2.1; 72 -2.3; 79 -2.6; 87 -2.9; 96 -3.2; 106 -3.2; 116 -3.2; 128 -3.1; 141 -2.9; 155 -2.6; 170 -2.1; 187 -1.6; 206 -1.0; 227 -0.3; 249 0.3; 274 0.7; 302 1.2; 332 1.4; 365 1.6; 402 1.7; 442 1.9; 486 1.8; 535 1.8; 588 2.1; 647 1.9; 712 1.6; 783 1.6; 861 1.0; 947 0.5; 1042 -0.3; 1146 -1.0; 1261 -2.1; 1387 -3.5; 1526 -5.1; 1678 -6.3; 1846 -7.1; 2031 -8.0; 2234 -8.7; 2457 -7.7; 2703 -5.5; 2973 -2.2; 3270 -0.2; 3597 0.8; 3957 1.5; 4353 5.3; 4788 4.4; 5267 -1.9; 5793 -4.9; 6373 -2.0; 7010 0.2; 7711 -0.9; 8482 -4.7; 9330 -6.4; 10263 -3.4; 11289 -0.2; 12418 0.0; 13660 -0.4; 15026 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Lear LUF 4C GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Lear LUF 4C ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 102 Hz  | 1.24 | -3.6 dB |
| Peaking | 2147 Hz | 1.85 | -9.7 dB |
| Peaking | 4653 Hz | 2.33 | 8.1 dB  |
| Peaking | 5557 Hz | 4.59 | -8.6 dB |
| Peaking | 9240 Hz | 4.47 | -7.2 dB |
| Peaking | 170 Hz  | 2.05 | -1.6 dB |
| Peaking | 536 Hz  | 0.56 | 2.4 dB  |
| Peaking | 1499 Hz | 3.02 | -2.4 dB |
| Peaking | 6174 Hz | 7.58 | -1.3 dB |
| Peaking | 7013 Hz | 6.49 | 1.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Lear%20LUF%204C/Lear%20LUF%204C.png)