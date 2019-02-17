# Steelseries Flux InEar Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.8; 23 -4.8; 25 -4.9; 28 -4.9; 31 -5.1; 34 -5.2; 37 -5.3; 41 -5.4; 45 -5.5; 49 -5.7; 54 -5.9; 60 -6.2; 66 -6.5; 72 -6.8; 79 -7.2; 87 -7.6; 96 -8.1; 106 -8.4; 116 -8.6; 128 -8.8; 141 -9.1; 155 -9.2; 170 -9.3; 187 -9.3; 206 -9.4; 227 -9.2; 249 -9.1; 274 -8.9; 302 -8.7; 332 -8.4; 365 -8.2; 402 -7.9; 442 -7.5; 486 -7.3; 535 -7.0; 588 -6.3; 647 -6.1; 712 -5.9; 783 -5.5; 861 -5.8; 947 -6.0; 1042 -6.5; 1146 -6.7; 1261 -7.2; 1387 -7.8; 1526 -8.3; 1678 -8.7; 1846 -8.8; 2031 -9.0; 2234 -8.7; 2457 -7.5; 2703 -6.1; 2973 -4.1; 3270 -2.2; 3597 -2.0; 3957 -3.9; 4353 -7.0; 4788 -6.7; 5267 -2.9; 5793 -0.5; 6373 -0.8; 7010 -3.7; 7711 -6.0; 8482 -6.2; 9330 -6.3; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -6.3; 15026 -6.3; 16529 -6.3; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Steelseries Flux InEar Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Steelseries Flux InEar Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 0.62 | 1.6 dB  |
| Peaking | 177 Hz   | 0.7  | -3.4 dB |
| Peaking | 1953 Hz  | 1.96 | -3.2 dB |
| Peaking | 3380 Hz  | 4.35 | 5.3 dB  |
| Peaking | 6062 Hz  | 4.49 | 6.6 dB  |
| Peaking | 788 Hz   | 2.77 | 1.3 dB  |
| Peaking | 1469 Hz  | 5.04 | -0.7 dB |
| Peaking | 4568 Hz  | 5.87 | -4.9 dB |
| Peaking | 4590 Hz  | 2.5  | 2.2 dB  |
| Peaking | 22050 Hz | 1.71 | 0.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.5 dB  |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.4 dB |
| Peaking | 4000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Steelseries%20Flux%20InEar%20Pro/Steelseries%20Flux%20InEar%20Pro.png)