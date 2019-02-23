# Polk Audio UltraFit 500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.9; 60 -2.2; 66 -3.2; 72 -4.2; 79 -5.2; 87 -6.0; 96 -6.8; 106 -7.5; 116 -8.1; 128 -8.7; 141 -9.3; 155 -9.8; 170 -10.3; 187 -10.7; 206 -11.0; 227 -11.3; 249 -11.6; 274 -11.7; 302 -11.9; 332 -12.0; 365 -12.0; 402 -12.2; 442 -12.4; 486 -12.6; 535 -12.8; 588 -12.8; 647 -13.1; 712 -13.2; 783 -13.1; 861 -13.1; 947 -12.7; 1042 -11.9; 1146 -10.4; 1261 -9.3; 1387 -9.6; 1526 -8.8; 1678 -7.3; 1846 -5.3; 2031 -3.7; 2234 -2.4; 2457 -1.5; 2703 -0.6; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.9; 5267 -2.1; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFit 500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFit 500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.58 | 7.2 dB  |
| Peaking | 1080 Hz | 0.12 | -7.5 dB |
| Peaking | 2669 Hz | 0.95 | 11.1 dB |
| Peaking | 5325 Hz | 1.05 | 7.4 dB  |
| Peaking | 376 Hz  | 2.25 | 0.7 dB  |
| Peaking | 849 Hz  | 3.27 | -1.1 dB |
| Peaking | 5074 Hz | 4.84 | -3.3 dB |
| Peaking | 6429 Hz | 1.48 | 3.3 dB  |
| Peaking | 7592 Hz | 2.93 | -3.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.0 dB  |
| Peaking | 62 Hz    | 1.41 | 3.4 dB  |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | -5.0 dB |
| Peaking | 1000 Hz  | 1.41 | -6.3 dB |
| Peaking | 2000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Polk%20Audio%20UltraFit%20500/Polk%20Audio%20UltraFit%20500.png)