# AKG K701 sample A
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.9; 31 5.5; 34 5.0; 37 4.5; 41 4.0; 45 3.6; 49 3.2; 54 2.7; 60 2.2; 66 2.1; 72 2.3; 79 2.2; 87 1.8; 96 0.7; 106 -0.1; 116 -0.6; 128 -1.2; 141 -1.6; 155 -1.7; 170 -1.8; 187 -2.2; 206 -2.4; 227 -2.3; 249 -2.4; 274 -2.4; 302 -2.4; 332 -2.2; 365 -2.2; 402 -2.0; 442 -1.6; 486 -1.2; 535 -1.1; 588 -0.4; 647 0.2; 712 0.8; 783 1.1; 861 0.7; 947 0.5; 1042 0.0; 1146 0.3; 1261 0.6; 1387 0.5; 1526 0.1; 1678 -0.7; 1846 -1.5; 2031 -2.4; 2234 -2.2; 2457 -1.8; 2703 -0.7; 2973 1.3; 3270 2.9; 3597 2.2; 3957 0.9; 4353 -0.6; 4788 -0.9; 5267 -1.2; 5793 -3.5; 6373 -3.9; 7010 -1.8; 7711 -1.8; 8482 -1.9; 9330 -1.8; 10263 -0.1; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.0; 20000 -1.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K701 sample A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K701 sample A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.3  | 6.4 dB  |
| Peaking | 218 Hz  | 0.79 | -3.0 dB |
| Peaking | 2230 Hz | 3.26 | -2.9 dB |
| Peaking | 3369 Hz | 3.39 | 3.7 dB  |
| Peaking | 6255 Hz | 2.1  | -3.7 dB |
| Peaking | 126 Hz  | 5.4  | -0.6 dB |
| Peaking | 413 Hz  | 2.62 | -0.7 dB |
| Peaking | 765 Hz  | 3.2  | 1.6 dB  |
| Peaking | 1312 Hz | 5.04 | 0.9 dB  |
| Peaking | 9014 Hz | 8.08 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K701%20sample%20A/AKG%20K701%20sample%20A.png)