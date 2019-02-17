# Enigmatic Audio Paradox
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.4; 23 -2.7; 25 -3.0; 28 -3.4; 31 -3.6; 34 -3.8; 37 -4.0; 41 -4.1; 45 -4.1; 49 -4.2; 54 -4.4; 60 -5.1; 66 -5.3; 72 -5.4; 79 -5.4; 87 -5.7; 96 -6.7; 106 -8.2; 116 -9.2; 128 -9.8; 141 -10.0; 155 -9.8; 170 -9.6; 187 -10.4; 206 -10.3; 227 -10.2; 249 -10.0; 274 -9.7; 302 -9.3; 332 -8.8; 365 -6.9; 402 -6.3; 442 -5.9; 486 -5.8; 535 -5.8; 588 -5.4; 647 -4.2; 712 -4.5; 783 -4.7; 861 -5.1; 947 -6.0; 1042 -6.8; 1146 -6.9; 1261 -6.8; 1387 -6.8; 1526 -6.5; 1678 -5.8; 1846 -5.3; 2031 -4.0; 2234 -2.8; 2457 -1.5; 2703 -0.6; 2973 -0.5; 3270 -0.8; 3597 -1.9; 3957 -2.2; 4353 -2.2; 4788 -0.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.3; 9330 -8.8; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Enigmatic Audio Paradox GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Enigmatic Audio Paradox ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.13 | 3.7 dB  |
| Peaking | 173 Hz  | 0.64 | -5.9 dB |
| Peaking | 586 Hz  | 1.45 | 2.7 dB  |
| Peaking | 2911 Hz | 1.92 | 6.0 dB  |
| Peaking | 5466 Hz | 2.49 | 6.1 dB  |
| Peaking | 40 Hz   | 2.54 | -0.4 dB |
| Peaking | 806 Hz  | 3.65 | 1.0 dB  |
| Peaking | 1205 Hz | 2.19 | -1.3 dB |
| Peaking | 6434 Hz | 9.32 | 2.0 dB  |
| Peaking | 8951 Hz | 4.76 | -3.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.2 dB  |
| Peaking | 62 Hz    | 1.41 | 2.1 dB  |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Enigmatic%20Audio%20Paradox/Enigmatic%20Audio%20Paradox.png)