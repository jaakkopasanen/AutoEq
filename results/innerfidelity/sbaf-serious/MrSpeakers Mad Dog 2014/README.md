# MrSpeakers Mad Dog 2014
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.1; 25 2.7; 28 2.4; 31 2.1; 34 1.8; 37 1.6; 41 1.4; 45 1.3; 49 1.1; 54 0.9; 60 0.6; 66 0.5; 72 0.4; 79 0.2; 87 -0.1; 96 -0.7; 106 -1.3; 116 -2.0; 128 -2.8; 141 -3.2; 155 -3.1; 170 -2.7; 187 -3.4; 206 -3.6; 227 -3.5; 249 -3.3; 274 -3.1; 302 -2.9; 332 -2.8; 365 -2.4; 402 -1.2; 442 -0.6; 486 -0.5; 535 1.3; 588 1.6; 647 0.1; 712 -0.1; 783 1.1; 861 0.4; 947 0.3; 1042 0.5; 1146 0.1; 1261 0.6; 1387 0.2; 1526 0.6; 1678 1.5; 1846 2.1; 2031 3.1; 2234 4.6; 2457 5.9; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 5.8; 4788 5.2; 5267 5.0; 5793 2.7; 6373 1.0; 7010 1.4; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MrSpeakers Mad Dog 2014 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Mad Dog 2014 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 0.3  | 3.9 dB  |
| Peaking | 81 Hz   | 1.36 | 2.1 dB  |
| Peaking | 187 Hz  | 0.37 | -4.0 dB |
| Peaking | 551 Hz  | 2.12 | 3.1 dB  |
| Peaking | 3330 Hz | 1    | 6.9 dB  |
| Peaking | 1471 Hz | 6.65 | -1.3 dB |
| Peaking | 2438 Hz | 5.48 | 1.6 dB  |
| Peaking | 3293 Hz | 4.19 | -0.8 dB |
| Peaking | 5077 Hz | 3.16 | 2.6 dB  |
| Peaking | 6730 Hz | 0.92 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MrSpeakers%20Mad%20Dog%202014/MrSpeakers%20Mad%20Dog%202014.png)