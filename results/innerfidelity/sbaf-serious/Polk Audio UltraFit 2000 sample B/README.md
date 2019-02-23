# Polk Audio UltraFit 2000 sample B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.9; 45 -2.0; 49 -3.2; 54 -4.6; 60 -6.1; 66 -7.4; 72 -8.5; 79 -9.6; 87 -10.6; 96 -11.4; 106 -11.8; 116 -11.9; 128 -11.9; 141 -11.9; 155 -11.7; 170 -11.3; 187 -10.9; 206 -10.5; 227 -10.0; 249 -9.5; 274 -8.9; 302 -8.1; 332 -8.2; 365 -7.5; 402 -6.8; 442 -6.2; 486 -5.8; 535 -5.1; 588 -4.3; 647 -4.0; 712 -4.1; 783 -5.1; 861 -7.2; 947 -8.8; 1042 -9.0; 1146 -9.3; 1261 -10.1; 1387 -10.1; 1526 -11.3; 1678 -11.5; 1846 -10.3; 2031 -8.5; 2234 -6.4; 2457 -4.1; 2703 -2.3; 2973 -1.2; 3270 -1.7; 3597 -3.7; 3957 -3.9; 4353 -2.6; 4788 -0.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.8; 9330 -7.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFit 2000 sample B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFit 2000 sample B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.71 | 7.5 dB  |
| Peaking | 114 Hz  | 0.79 | -7.1 dB |
| Peaking | 1619 Hz | 2    | -6.0 dB |
| Peaking | 2903 Hz | 2.45 | 5.7 dB  |
| Peaking | 5463 Hz | 2.42 | 6.6 dB  |
| Peaking | 241 Hz  | 1.78 | -1.1 dB |
| Peaking | 707 Hz  | 1.5  | 4.5 dB  |
| Peaking | 952 Hz  | 2.24 | -3.7 dB |
| Peaking | 6525 Hz | 8.45 | 2.2 dB  |
| Peaking | 8684 Hz | 2.43 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.5 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -6.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | 3.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.4 dB |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Polk%20Audio%20UltraFit%202000%20sample%20B/Polk%20Audio%20UltraFit%202000%20sample%20B.png)