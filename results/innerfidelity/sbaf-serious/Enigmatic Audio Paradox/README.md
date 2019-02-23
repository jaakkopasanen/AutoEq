# Enigmatic Audio Paradox
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.8; 23 -4.1; 25 -4.3; 28 -4.7; 31 -5.0; 34 -5.2; 37 -5.3; 41 -5.4; 45 -5.5; 49 -5.5; 54 -5.8; 60 -6.4; 66 -6.6; 72 -6.7; 79 -6.7; 87 -7.0; 96 -8.1; 106 -9.6; 116 -10.5; 128 -11.1; 141 -11.3; 155 -11.1; 170 -10.9; 187 -11.7; 206 -11.6; 227 -11.5; 249 -11.4; 274 -11.0; 302 -10.6; 332 -10.1; 365 -8.3; 402 -7.6; 442 -7.2; 486 -7.2; 535 -7.1; 588 -6.7; 647 -5.5; 712 -5.9; 783 -6.1; 861 -6.4; 947 -7.4; 1042 -8.1; 1146 -8.3; 1261 -8.1; 1387 -8.1; 1526 -7.8; 1678 -7.2; 1846 -6.6; 2031 -5.4; 2234 -4.1; 2457 -2.9; 2703 -1.9; 2973 -1.4; 3270 -2.1; 3597 -3.3; 3957 -3.5; 4353 -3.5; 4788 -1.6; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -8.5; 9330 -10.1; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Enigmatic Audio Paradox GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Enigmatic Audio Paradox ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.17 | 2.4 dB  |
| Peaking | 179 Hz  | 0.78 | -5.8 dB |
| Peaking | 2886 Hz | 2.91 | 4.9 dB  |
| Peaking | 5661 Hz | 1.99 | 6.5 dB  |
| Peaking | 9000 Hz | 4.24 | -5.0 dB |
| Peaking | 122 Hz  | 2.76 | -3.1 dB |
| Peaking | 125 Hz  | 1.29 | 2.0 dB  |
| Peaking | 288 Hz  | 2.39 | -1.7 dB |
| Peaking | 993 Hz  | 0.6  | 3.3 dB  |
| Peaking | 1223 Hz | 1.22 | -5.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -5.1 dB |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Enigmatic%20Audio%20Paradox/Enigmatic%20Audio%20Paradox.png)