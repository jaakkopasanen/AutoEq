# Steelseries Flux In-Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.5; 23 -7.6; 25 -7.6; 28 -7.6; 31 -7.6; 34 -7.6; 37 -7.7; 41 -7.7; 45 -7.8; 49 -7.9; 54 -7.9; 60 -8.1; 66 -8.2; 72 -8.4; 79 -8.5; 87 -8.7; 96 -8.9; 106 -8.9; 116 -8.7; 128 -8.7; 141 -8.7; 155 -8.5; 170 -8.3; 187 -7.9; 206 -7.6; 227 -7.2; 249 -6.8; 274 -6.3; 302 -5.8; 332 -5.4; 365 -4.8; 402 -4.4; 442 -3.7; 486 -3.4; 535 -3.0; 588 -2.3; 647 -2.0; 712 -1.9; 783 -1.5; 861 -1.7; 947 -1.9; 1042 -2.3; 1146 -2.7; 1261 -3.3; 1387 -4.0; 1526 -4.7; 1678 -5.2; 1846 -5.5; 2031 -5.7; 2234 -6.1; 2457 -5.8; 2703 -5.5; 2973 -5.4; 3270 -2.6; 3597 -0.8; 3957 -0.5; 4353 -1.8; 4788 -2.1; 5267 -1.3; 5793 -1.5; 6373 -2.6; 7010 -2.4; 7711 -1.9; 8482 -2.1; 9330 -2.1; 10263 -2.1; 11289 -2.1; 12418 -2.1; 13660 -3.9; 15026 -4.9; 16529 -4.4; 18182 -4.5; 20000 -2.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Steelseries Flux In-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Steelseries Flux In-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 37 Hz    | 0.24 | -5.4 dB |
| Peaking | 165 Hz   | 0.73 | -3.9 dB |
| Peaking | 2330 Hz  | 1.44 | -4.5 dB |
| Peaking | 3788 Hz  | 3.2  | 3.2 dB  |
| Peaking | 16668 Hz | 1.14 | -2.9 dB |
| Peaking | 795 Hz   | 2.02 | 1.5 dB  |
| Peaking | 1551 Hz  | 4.18 | -1.1 dB |
| Peaking | 4541 Hz  | 4.34 | -0.6 dB |
| Peaking | 5371 Hz  | 5.72 | 1.3 dB  |
| Peaking | 11324 Hz | 2.74 | 0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.4 dB |
| Peaking | 62 Hz    | 1.41 | -4.4 dB |
| Peaking | 125 Hz   | 1.41 | -5.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.9 dB |
| Peaking | 4000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -3.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Steelseries%20Flux%20In-Ear/Steelseries%20Flux%20In-Ear.png)