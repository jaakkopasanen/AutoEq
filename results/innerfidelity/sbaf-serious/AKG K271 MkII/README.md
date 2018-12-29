# AKG K271 MKII
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 5.9; 41 5.3; 45 4.6; 49 4.0; 54 3.3; 60 2.9; 66 2.9; 72 3.6; 79 4.7; 87 5.8; 96 5.8; 106 3.4; 116 2.4; 128 2.0; 141 1.0; 155 1.5; 170 1.7; 187 1.2; 206 1.2; 227 0.5; 249 -0.2; 274 -0.4; 302 -0.6; 332 -0.7; 365 -0.7; 402 -0.9; 442 -0.9; 486 -1.2; 535 -1.6; 588 -1.8; 647 -2.7; 712 -0.5; 783 1.3; 861 0.7; 947 0.5; 1042 -0.2; 1146 -0.5; 1261 -1.0; 1387 -1.7; 1526 -2.7; 1678 -3.2; 1846 -2.4; 2031 0.6; 2234 0.6; 2457 2.1; 2703 2.2; 2973 2.9; 3270 3.7; 3597 4.8; 3957 4.6; 4353 2.8; 4788 4.1; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 -0.3; 8482 -5.6; 9330 -7.6; 10263 -4.5; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K271 MKII GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K271 MKII ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.73 | 6.4 dB  |
| Peaking | 91 Hz   | 2.77 | 4.9 dB  |
| Peaking | 3531 Hz | 3.14 | 4.1 dB  |
| Peaking | 5882 Hz | 2.15 | 6.9 dB  |
| Peaking | 9123 Hz | 3.59 | -9.6 dB |
| Peaking | 175 Hz  | 3.93 | 1.1 dB  |
| Peaking | 678 Hz  | 1.61 | -4.4 dB |
| Peaking | 790 Hz  | 2.73 | 4.8 dB  |
| Peaking | 1716 Hz | 2.59 | -4.7 dB |
| Peaking | 2160 Hz | 2.04 | 2.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K271%20MKII/AKG%20K271%20MKII.png)