# Umi Voix
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.7; 23 -12.8; 25 -12.9; 28 -12.9; 31 -13.0; 34 -13.1; 37 -13.1; 41 -13.2; 45 -13.2; 49 -13.3; 54 -13.4; 60 -13.5; 66 -13.7; 72 -13.9; 79 -14.0; 87 -14.2; 96 -14.4; 106 -14.4; 116 -14.4; 128 -14.4; 141 -14.3; 155 -14.1; 170 -14.0; 187 -13.5; 206 -13.2; 227 -12.7; 249 -12.1; 274 -11.5; 302 -10.7; 332 -9.9; 365 -9.0; 402 -8.3; 442 -7.1; 486 -6.7; 535 -6.5; 588 -5.8; 647 -6.0; 712 -6.5; 783 -6.8; 861 -7.7; 947 -8.5; 1042 -9.5; 1146 -10.3; 1261 -11.0; 1387 -11.6; 1526 -11.9; 1678 -11.3; 1846 -9.9; 2031 -7.8; 2234 -5.7; 2457 -3.1; 2703 -1.0; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -3.5; 4353 -6.5; 4788 -3.1; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Umi Voix GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Umi Voix ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 12 Hz    | 1.37 | -5.9 dB |
| Peaking | 43 Hz    | 0.32 | -5.7 dB |
| Peaking | 162 Hz   | 0.66 | -5.2 dB |
| Peaking | 3342 Hz  | 2.22 | 6.7 dB  |
| Peaking | 21314 Hz | 2.61 | 3.7 dB  |
| Peaking | 612 Hz   | 1.58 | 2.7 dB  |
| Peaking | 1515 Hz  | 1.15 | -6.1 dB |
| Peaking | 2564 Hz  | 3.16 | 4.2 dB  |
| Peaking | 4323 Hz  | 6.64 | -4.5 dB |
| Peaking | 5652 Hz  | 2.75 | 6.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.3 dB |
| Peaking | 62 Hz    | 1.41 | -5.1 dB |
| Peaking | 125 Hz   | 1.41 | -6.7 dB |
| Peaking | 250 Hz   | 1.41 | -5.2 dB |
| Peaking | 500 Hz   | 1.41 | 2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.5 dB |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Umi%20Voix/Umi%20Voix.png)