# Phiaton Chord MS530
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.7; 23 -1.0; 25 -1.2; 28 -1.5; 31 -1.8; 34 -2.0; 37 -2.2; 41 -2.4; 45 -2.6; 49 -2.8; 54 -3.0; 60 -3.4; 66 -3.7; 72 -3.9; 79 -4.2; 87 -4.1; 96 -4.1; 106 -4.8; 116 -5.0; 128 -5.1; 141 -5.4; 155 -5.4; 170 -4.8; 187 -4.9; 206 -4.4; 227 -3.9; 249 -3.4; 274 -2.9; 302 -2.5; 332 -2.3; 365 -2.2; 402 -2.6; 442 -2.6; 486 -2.6; 535 -3.0; 588 -3.2; 647 -3.8; 712 -4.4; 783 -4.6; 861 -5.4; 947 -5.9; 1042 -6.9; 1146 -7.6; 1261 -7.7; 1387 -8.4; 1526 -6.2; 1678 -7.8; 1846 -8.2; 2031 -6.8; 2234 -5.6; 2457 -3.7; 2703 -2.3; 2973 -0.7; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phiaton Chord MS530 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton Chord MS530 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.59 | 5.5 dB  |
| Peaking | 59 Hz   | 1.03 | 1.5 dB  |
| Peaking | 411 Hz  | 0.76 | 4.4 dB  |
| Peaking | 1629 Hz | 0.98 | -3.8 dB |
| Peaking | 3822 Hz | 0.89 | 7.6 dB  |
| Peaking | 1149 Hz | 4.79 | -0.7 dB |
| Peaking | 2602 Hz | 0.34 | 0.3 dB  |
| Peaking | 3965 Hz | 4.79 | -1.2 dB |
| Peaking | 6199 Hz | 2.59 | 4.9 dB  |
| Peaking | 7491 Hz | 1.48 | -3.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.3 dB  |
| Peaking | 62 Hz    | 1.41 | 2.2 dB  |
| Peaking | 125 Hz   | 1.41 | 0.1 dB  |
| Peaking | 250 Hz   | 1.41 | 2.5 dB  |
| Peaking | 500 Hz   | 1.41 | 4.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | 8.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phiaton%20Chord%20MS530/Phiaton%20Chord%20MS530.png)