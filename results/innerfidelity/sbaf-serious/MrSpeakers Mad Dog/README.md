# MrSpeakers Mad Dog
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -1.0; 72 -1.3; 79 -3.7; 87 -6.3; 96 -7.3; 106 -7.2; 116 -6.9; 128 -6.6; 141 -6.3; 155 -5.6; 170 -6.1; 187 -6.0; 206 -5.8; 227 -5.4; 249 -5.3; 274 -5.2; 302 -5.0; 332 -4.9; 365 -5.2; 402 -5.2; 442 -5.6; 486 -6.5; 535 -6.8; 588 -5.5; 647 -4.9; 712 -5.4; 783 -6.5; 861 -7.1; 947 -7.0; 1042 -6.0; 1146 -6.0; 1261 -5.7; 1387 -5.5; 1526 -5.2; 1678 -4.6; 1846 -3.6; 2031 -2.0; 2234 -1.0; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -2.2; 7010 -4.2; 7711 -6.3; 8482 -8.2; 9330 -8.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MrSpeakers Mad Dog GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Mad Dog ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.81 | 7.1 dB  |
| Peaking | 326 Hz  | 2.36 | 1.5 dB  |
| Peaking | 2527 Hz | 1.76 | 4.5 dB  |
| Peaking | 5142 Hz | 0.93 | 6.3 dB  |
| Peaking | 8608 Hz | 2.32 | -4.8 dB |
| Peaking | 37 Hz   | 2.98 | -1.6 dB |
| Peaking | 72 Hz   | 1.74 | 4.5 dB  |
| Peaking | 92 Hz   | 2.12 | -5.1 dB |
| Peaking | 663 Hz  | 5.84 | 1.5 dB  |
| Peaking | 877 Hz  | 3.54 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 4.5 dB  |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | 1.6 dB  |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MrSpeakers%20Mad%20Dog/MrSpeakers%20Mad%20Dog.png)