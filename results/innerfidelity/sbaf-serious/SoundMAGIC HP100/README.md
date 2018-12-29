# SoundMAGIC HP100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 -0.1; 25 -0.8; 28 -1.6; 31 -2.1; 34 -2.5; 37 -2.7; 41 -2.9; 45 -2.9; 49 -3.0; 54 -2.9; 60 -2.6; 66 -2.0; 72 -1.5; 79 -1.3; 87 0.1; 96 1.7; 106 2.4; 116 2.1; 128 1.1; 141 0.3; 155 2.2; 170 5.1; 187 1.7; 206 0.2; 227 -1.0; 249 -1.4; 274 -1.4; 302 -1.3; 332 -1.2; 365 -1.1; 402 -1.1; 442 -0.8; 486 -1.0; 535 -1.0; 588 -0.6; 647 -0.5; 712 -0.6; 783 -0.2; 861 -0.2; 947 0.2; 1042 -0.2; 1146 -0.3; 1261 -0.3; 1387 -0.7; 1526 -1.1; 1678 -1.4; 1846 -1.3; 2031 -1.5; 2234 -1.8; 2457 -1.5; 2703 -1.1; 2973 0.1; 3270 1.0; 3597 0.5; 3957 -0.9; 4353 -1.4; 4788 2.7; 5267 4.2; 5793 6.0; 6373 5.5; 7010 2.5; 7711 -1.0; 8482 -5.7; 9330 -6.3; 10263 -2.7; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SoundMAGIC HP100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SoundMAGIC HP100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 94 Hz   | 0.36 | -4.1 dB |
| Peaking | 105 Hz  | 1.99 | 6.2 dB  |
| Peaking | 170 Hz  | 4.36 | 7.0 dB  |
| Peaking | 6047 Hz | 3.18 | 7.3 dB  |
| Peaking | 8931 Hz | 3.78 | -8.1 dB |
| Peaking | 142 Hz  | 9.69 | -0.6 dB |
| Peaking | 2236 Hz | 1.62 | -1.9 dB |
| Peaking | 3295 Hz | 4.66 | 1.9 dB  |
| Peaking | 4382 Hz | 4.36 | -3.4 dB |
| Peaking | 4910 Hz | 6.13 | 3.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/SoundMAGIC%20HP100/SoundMAGIC%20HP100.png)