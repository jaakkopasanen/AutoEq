# Audeze SINE
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.2; 25 -1.8; 28 -2.5; 31 -3.0; 34 -3.4; 37 -3.7; 41 -4.1; 45 -4.3; 49 -4.5; 54 -4.8; 60 -4.9; 66 -5.1; 72 -5.3; 79 -5.6; 87 -5.9; 96 -6.4; 106 -6.6; 116 -6.8; 128 -7.1; 141 -7.3; 155 -7.4; 170 -7.4; 187 -7.6; 206 -7.6; 227 -7.5; 249 -7.2; 274 -7.2; 302 -7.2; 332 -7.2; 365 -7.0; 402 -6.8; 442 -6.7; 486 -6.5; 535 -6.1; 588 -5.6; 647 -5.1; 712 -4.8; 783 -4.7; 861 -4.7; 947 -4.9; 1042 -5.0; 1146 -4.8; 1261 -5.4; 1387 -6.3; 1526 -6.6; 1678 -7.4; 1846 -7.5; 2031 -7.4; 2234 -7.3; 2457 -6.1; 2703 -6.7; 2973 -6.5; 3270 -5.8; 3597 -6.2; 3957 -4.6; 4353 -4.1; 4788 -3.1; 5267 -1.9; 5793 -0.9; 6373 -1.7; 7010 -3.0; 7711 -5.3; 8482 -5.5; 9330 -5.6; 10263 -6.9; 11289 -5.6; 12418 -5.6; 13660 -5.6; 15026 -5.6; 16529 -7.2; 18182 -8.3; 20000 -5.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze SINE GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze SINE ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 14 Hz    | 0.67 | 6.8 dB  |
| Peaking | 189 Hz   | 0.79 | -2.2 dB |
| Peaking | 2014 Hz  | 2.22 | -2.2 dB |
| Peaking | 5762 Hz  | 2.73 | 5.0 dB  |
| Peaking | 17984 Hz | 1.66 | -3.1 dB |
| Peaking | 435 Hz   | 1.33 | -1.5 dB |
| Peaking | 1141 Hz  | 0.4  | 1.9 dB  |
| Peaking | 1561 Hz  | 1.89 | -2.0 dB |
| Peaking | 3118 Hz  | 2.38 | -1.5 dB |
| Peaking | 10253 Hz | 4.86 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.3 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -1.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20SINE/Audeze%20SINE.png)