# Polk Audio UltraFit 300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.4; 23 -16.4; 25 -16.4; 28 -16.4; 31 -16.4; 34 -16.4; 37 -16.4; 41 -16.5; 45 -16.5; 49 -16.5; 54 -16.6; 60 -16.7; 66 -16.8; 72 -16.9; 79 -17.0; 87 -17.1; 96 -17.2; 106 -17.1; 116 -17.0; 128 -16.8; 141 -16.7; 155 -16.4; 170 -16.1; 187 -15.6; 206 -15.2; 227 -14.6; 249 -14.1; 274 -13.5; 302 -12.8; 332 -12.2; 365 -11.5; 402 -10.9; 442 -10.0; 486 -9.5; 535 -8.8; 588 -7.9; 647 -7.4; 712 -7.0; 783 -6.2; 861 -6.0; 947 -6.1; 1042 -6.3; 1146 -6.6; 1261 -6.9; 1387 -7.4; 1526 -8.1; 1678 -8.7; 1846 -8.7; 2031 -8.7; 2234 -8.4; 2457 -7.0; 2703 -6.2; 2973 -5.1; 3270 -3.6; 3597 -0.6; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFit 300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFit 300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.35 | -8.3 dB |
| Peaking | 129 Hz  | 0.34 | -9.5 dB |
| Peaking | 822 Hz  | 0.96 | 2.6 dB  |
| Peaking | 1985 Hz | 1.35 | -3.8 dB |
| Peaking | 4482 Hz | 1.25 | 7.4 dB  |
| Peaking | 3246 Hz | 5.1  | -0.9 dB |
| Peaking | 3570 Hz | 6.19 | 2.0 dB  |
| Peaking | 4528 Hz | 4.19 | -1.1 dB |
| Peaking | 6340 Hz | 3.09 | 4.4 dB  |
| Peaking | 7393 Hz | 1.64 | -3.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.1 dB |
| Peaking | 62 Hz    | 1.41 | -7.3 dB  |
| Peaking | 125 Hz   | 1.41 | -8.6 dB  |
| Peaking | 250 Hz   | 1.41 | -6.2 dB  |
| Peaking | 500 Hz   | 1.41 | -1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 2000 Hz  | 1.41 | -4.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Polk%20Audio%20UltraFit%20300/Polk%20Audio%20UltraFit%20300.png)