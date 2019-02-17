# Audio Technica ATH-AD2000X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.7; 72 -1.1; 79 -1.6; 87 -2.0; 96 -2.5; 106 -3.1; 116 -3.6; 128 -4.0; 141 -4.4; 155 -4.7; 170 -4.8; 187 -5.2; 206 -5.3; 227 -5.4; 249 -5.5; 274 -5.5; 302 -5.6; 332 -5.6; 365 -5.6; 402 -5.6; 442 -5.5; 486 -5.8; 535 -5.8; 588 -5.6; 647 -5.8; 712 -5.7; 783 -5.9; 861 -6.1; 947 -6.3; 1042 -6.4; 1146 -6.3; 1261 -6.0; 1387 -6.1; 1526 -5.7; 1678 -5.1; 1846 -3.4; 2031 -1.8; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -2.4; 3957 -4.0; 4353 -2.2; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-AD2000X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-AD2000X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.28 | 5.8 dB  |
| Peaking | 68 Hz    | 1.06 | 1.9 dB  |
| Peaking | 425 Hz   | 1.55 | 0.6 dB  |
| Peaking | 2628 Hz  | 1.64 | 6.4 dB  |
| Peaking | 5488 Hz  | 2.4  | 6.0 dB  |
| Peaking | 1498 Hz  | 1.87 | -0.9 dB |
| Peaking | 2064 Hz  | 5.76 | 1.6 dB  |
| Peaking | 6542 Hz  | 6.63 | 2.4 dB  |
| Peaking | 7594 Hz  | 2.6  | -1.5 dB |
| Peaking | 10252 Hz | 1.52 | -0.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 5.0 dB  |
| Peaking | 125 Hz   | 1.41 | 1.6 dB  |
| Peaking | 250 Hz   | 1.41 | 0.3 dB  |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-AD2000X/Audio%20Technica%20ATH-AD2000X.png)