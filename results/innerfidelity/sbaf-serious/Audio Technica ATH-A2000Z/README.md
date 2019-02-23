# Audio Technica ATH-A2000Z
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.3; 25 -1.9; 28 -2.8; 31 -3.6; 34 -4.2; 37 -4.7; 41 -5.3; 45 -5.8; 49 -6.1; 54 -6.5; 60 -6.8; 66 -7.0; 72 -7.1; 79 -7.3; 87 -7.6; 96 -8.3; 106 -9.0; 116 -9.0; 128 -9.0; 141 -9.1; 155 -8.8; 170 -8.0; 187 -8.3; 206 -7.8; 227 -7.3; 249 -6.8; 274 -6.4; 302 -6.2; 332 -6.2; 365 -6.3; 402 -6.5; 442 -6.5; 486 -6.7; 535 -6.7; 588 -6.4; 647 -6.4; 712 -6.5; 783 -6.3; 861 -6.2; 947 -6.5; 1042 -6.1; 1146 -6.3; 1261 -6.4; 1387 -7.2; 1526 -8.8; 1678 -10.4; 1846 -11.2; 2031 -11.6; 2234 -11.4; 2457 -9.1; 2703 -6.6; 2973 -5.0; 3270 -5.1; 3597 -8.1; 3957 -9.8; 4353 -9.6; 4788 -5.7; 5267 -0.6; 5793 -0.9; 6373 -1.5; 7010 -4.1; 7711 -6.3; 8482 -6.7; 9330 -11.3; 10263 -10.2; 11289 -6.6; 12418 -6.6; 13660 -6.6; 15026 -6.6; 16529 -10.4; 18182 -8.7; 20000 -6.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-A2000Z GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-A2000Z ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 2.02 | 6.1 dB   |
| Peaking | 2033 Hz  | 2.34 | -7.2 dB  |
| Peaking | 4220 Hz  | 2.96 | -13.5 dB |
| Peaking | 4822 Hz  | 1.01 | 10.8 dB  |
| Peaking | 9473 Hz  | 2.7  | -7.0 dB  |
| Peaking | 33 Hz    | 1.8  | 1.1 dB   |
| Peaking | 129 Hz   | 1.13 | -3.0 dB  |
| Peaking | 438 Hz   | 0.2  | 0.5 dB   |
| Peaking | 1638 Hz  | 7.95 | -1.4 dB  |
| Peaking | 17085 Hz | 2.52 | -4.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.7 dB |
| Peaking | 4000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -2.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-A2000Z/Audio%20Technica%20ATH-A2000Z.png)