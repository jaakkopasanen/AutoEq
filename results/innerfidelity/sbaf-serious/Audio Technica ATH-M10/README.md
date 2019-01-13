# Audio Technica ATH-M10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 5.6; 96 4.9; 106 3.5; 116 2.8; 128 2.1; 141 1.6; 155 1.3; 170 1.4; 187 0.7; 206 0.5; 227 0.2; 249 -0.0; 274 -0.2; 302 -0.5; 332 -0.6; 365 -0.5; 402 -0.6; 442 -0.3; 486 -0.6; 535 -0.7; 588 -0.4; 647 -0.5; 712 -1.0; 783 -1.3; 861 -2.0; 947 -2.2; 1042 0.7; 1146 1.4; 1261 -0.8; 1387 -0.7; 1526 0.1; 1678 1.8; 1846 2.9; 2031 3.4; 2234 5.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 2.9; 7010 2.4; 7711 0.3; 8482 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-M10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-M10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 54 Hz   | 0.27 | 7.3 dB  |
| Peaking | 196 Hz  | 0.49 | -3.5 dB |
| Peaking | 874 Hz  | 4.3  | -2.8 dB |
| Peaking | 1416 Hz | 4.57 | -2.8 dB |
| Peaking | 3418 Hz | 0.76 | 6.8 dB  |
| Peaking | 84 Hz   | 5.88 | 1.0 dB  |
| Peaking | 3529 Hz | 5.21 | -0.9 dB |
| Peaking | 5739 Hz | 3.1  | 3.3 dB  |
| Peaking | 7928 Hz | 1.37 | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-M10/Audio%20Technica%20ATH-M10.png)