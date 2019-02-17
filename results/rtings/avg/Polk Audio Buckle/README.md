# Polk Audio Buckle
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.2; 23 -8.4; 25 -8.6; 28 -8.9; 31 -9.0; 34 -9.0; 37 -8.9; 41 -8.6; 45 -8.4; 49 -8.1; 54 -7.8; 60 -7.5; 66 -7.3; 72 -7.0; 79 -6.9; 87 -6.8; 96 -6.8; 106 -6.8; 116 -6.7; 128 -6.7; 141 -6.5; 155 -6.3; 170 -6.3; 187 -6.2; 206 -6.3; 227 -6.0; 249 -5.7; 274 -6.1; 302 -7.0; 332 -7.0; 365 -6.5; 402 -5.4; 442 -4.9; 486 -5.5; 535 -6.0; 588 -5.9; 647 -5.7; 712 -6.8; 783 -7.7; 861 -7.5; 947 -6.9; 1042 -6.2; 1146 -5.5; 1261 -4.7; 1387 -4.1; 1526 -3.4; 1678 -2.7; 1846 -2.3; 2031 -2.0; 2234 -1.0; 2457 -0.5; 2703 -0.6; 2973 -1.7; 3270 -2.4; 3597 -1.7; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio Buckle GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio Buckle ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 1.01 | -2.6 dB |
| Peaking | 445 Hz  | 4.58 | 1.5 dB  |
| Peaking | 856 Hz  | 3.32 | -2.1 dB |
| Peaking | 2382 Hz | 0.97 | 5.2 dB  |
| Peaking | 5189 Hz | 1.87 | 5.4 dB  |
| Peaking | 287 Hz  | 1.74 | 1.5 dB  |
| Peaking | 318 Hz  | 3.27 | -2.2 dB |
| Peaking | 6286 Hz | 6.25 | 1.6 dB  |
| Peaking | 6682 Hz | 5.48 | 1.8 dB  |
| Peaking | 7597 Hz | 1.9  | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.8 dB |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | 0.1 dB  |
| Peaking | 250 Hz   | 1.41 | 0.1 dB  |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Polk%20Audio%20Buckle/Polk%20Audio%20Buckle.png)