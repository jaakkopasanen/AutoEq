# Polk Audio UltraFit 500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.7; 41 -1.6; 45 -2.7; 49 -3.4; 54 -4.4; 60 -5.4; 66 -6.4; 72 -7.3; 79 -8.2; 87 -8.9; 96 -9.9; 106 -10.4; 116 -11.0; 128 -12.0; 141 -12.4; 155 -12.9; 170 -13.5; 187 -14.0; 206 -14.5; 227 -14.9; 249 -15.3; 274 -15.5; 302 -15.7; 332 -16.1; 365 -16.2; 402 -16.9; 442 -16.2; 486 -16.2; 535 -16.4; 588 -15.9; 647 -15.4; 712 -15.0; 783 -13.9; 861 -13.0; 947 -12.0; 1042 -10.9; 1146 -9.9; 1261 -8.7; 1387 -7.8; 1526 -6.8; 1678 -5.6; 1846 -3.9; 2031 -2.0; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFit 500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFit 500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 30 Hz   | 0.73 | 7.3 dB   |
| Peaking | 417 Hz  | 0.29 | -10.4 dB |
| Peaking | 2471 Hz | 0.83 | 8.9 dB   |
| Peaking | 5331 Hz | 2.14 | 4.5 dB   |
| Peaking | 653 Hz  | 2.85 | -0.5 dB  |
| Peaking | 1095 Hz | 3.1  | 0.6 dB   |
| Peaking | 4059 Hz | 3.33 | 1.4 dB   |
| Peaking | 6417 Hz | 4.07 | 4.3 dB   |
| Peaking | 6786 Hz | 1.28 | -2.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -7.1 dB |
| Peaking | 500 Hz   | 1.41 | -9.0 dB |
| Peaking | 1000 Hz  | 1.41 | -4.8 dB |
| Peaking | 2000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Polk%20Audio%20UltraFit%20500/Polk%20Audio%20UltraFit%20500.png)