# Polk Audio UltraFit 1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.7; 28 -1.5; 31 -2.4; 34 -3.4; 37 -4.3; 41 -5.4; 45 -6.2; 49 -7.2; 54 -8.4; 60 -9.2; 66 -10.2; 72 -11.2; 79 -11.7; 87 -12.6; 96 -13.6; 106 -13.9; 116 -14.6; 128 -15.0; 141 -16.0; 155 -16.0; 170 -16.5; 187 -16.7; 206 -17.1; 227 -17.4; 249 -17.4; 274 -17.3; 302 -18.1; 332 -17.6; 365 -18.0; 402 -18.3; 442 -17.5; 486 -17.4; 535 -18.1; 588 -17.6; 647 -18.1; 712 -17.5; 783 -16.6; 861 -14.9; 947 -11.7; 1042 -12.0; 1146 -9.8; 1261 -9.8; 1387 -10.1; 1526 -9.8; 1678 -8.3; 1846 -5.4; 2031 -2.8; 2234 -0.7; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFit 1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFit 1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 24 Hz   | 0.77 | 7.3 dB   |
| Peaking | 252 Hz  | 0.29 | -11.0 dB |
| Peaking | 698 Hz  | 1.33 | -5.4 dB  |
| Peaking | 1560 Hz | 3.07 | -5.1 dB  |
| Peaking | 2771 Hz | 0.56 | 8.3 dB   |
| Peaking | 188 Hz  | 4.36 | 0.2 dB   |
| Peaking | 2256 Hz | 6.32 | 1.4 dB   |
| Peaking | 3082 Hz | 1.84 | -0.9 dB  |
| Peaking | 6255 Hz | 1.86 | 6.1 dB   |
| Peaking | 7399 Hz | 1.38 | -5.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB   |
| Peaking | 62 Hz    | 1.41 | -3.1 dB  |
| Peaking | 125 Hz   | 1.41 | -7.0 dB  |
| Peaking | 250 Hz   | 1.41 | -8.5 dB  |
| Peaking | 500 Hz   | 1.41 | -10.2 dB |
| Peaking | 1000 Hz  | 1.41 | -5.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Polk%20Audio%20UltraFit%201000/Polk%20Audio%20UltraFit%201000.png)