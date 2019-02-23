# Polk Audio UltraFit 2000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.8; 54 -2.1; 60 -3.7; 66 -5.2; 72 -6.4; 79 -7.5; 87 -8.5; 96 -9.4; 106 -9.9; 116 -10.1; 128 -10.2; 141 -10.2; 155 -10.0; 170 -9.7; 187 -9.3; 206 -8.9; 227 -8.5; 249 -8.0; 274 -7.5; 302 -6.9; 332 -6.4; 365 -5.9; 402 -5.3; 442 -4.5; 486 -4.1; 535 -3.4; 588 -2.5; 647 -1.9; 712 -1.9; 783 -2.6; 861 -5.2; 947 -7.9; 1042 -9.5; 1146 -10.1; 1261 -10.8; 1387 -11.1; 1526 -11.7; 1678 -12.0; 1846 -11.6; 2031 -10.5; 2234 -8.9; 2457 -6.6; 2703 -4.8; 2973 -3.3; 3270 -3.5; 3597 -5.1; 3957 -5.4; 4353 -4.1; 4788 -1.9; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -9.8; 9330 -10.8; 10263 -7.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFit 2000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFit 2000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 41 Hz   | 0.47 | 8.7 dB  |
| Peaking | 105 Hz  | 0.67 | -7.8 dB |
| Peaking | 654 Hz  | 1.48 | 6.2 dB  |
| Peaking | 1407 Hz | 1.39 | -6.6 dB |
| Peaking | 5374 Hz | 2.32 | 6.9 dB  |
| Peaking | 1987 Hz | 3.87 | -2.4 dB |
| Peaking | 3100 Hz | 2.35 | 4.9 dB  |
| Peaking | 3782 Hz | 2.23 | -2.5 dB |
| Peaking | 6498 Hz | 6.18 | 2.5 dB  |
| Peaking | 9034 Hz | 3.98 | -5.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.6 dB  |
| Peaking | 125 Hz   | 1.41 | -4.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | 5.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | -5.4 dB |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Polk%20Audio%20UltraFit%202000/Polk%20Audio%20UltraFit%202000.png)