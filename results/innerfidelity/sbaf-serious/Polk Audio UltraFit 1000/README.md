# Polk Audio UltraFit 1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -1.0; 54 -2.1; 60 -2.9; 66 -3.9; 72 -4.9; 79 -5.4; 87 -6.3; 96 -7.3; 106 -7.6; 116 -8.3; 128 -8.7; 141 -9.7; 155 -9.7; 170 -10.2; 187 -10.4; 206 -10.8; 227 -11.1; 249 -11.1; 274 -11.0; 302 -11.8; 332 -11.3; 365 -11.7; 402 -12.0; 442 -11.2; 486 -11.1; 535 -11.8; 588 -11.3; 647 -11.8; 712 -11.2; 783 -10.3; 861 -8.6; 947 -5.4; 1042 -5.7; 1146 -3.5; 1261 -3.5; 1387 -3.8; 1526 -3.5; 1678 -2.0; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFit 1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFit 1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.54 | 7.1 dB  |
| Peaking | 269 Hz  | 0.38 | -5.5 dB |
| Peaking | 675 Hz  | 2.24 | -3.6 dB |
| Peaking | 2214 Hz | 0.61 | 6.6 dB  |
| Peaking | 5279 Hz | 2.13 | 4.1 dB  |
| Peaking | 1172 Hz | 4.95 | 1.4 dB  |
| Peaking | 1475 Hz | 5.66 | -1.4 dB |
| Peaking | 3927 Hz | 2.66 | 1.2 dB  |
| Peaking | 6350 Hz | 3.99 | 4.3 dB  |
| Peaking | 7006 Hz | 1.29 | -3.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.3 dB  |
| Peaking | 62 Hz    | 1.41 | 2.7 dB  |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | -5.6 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Polk%20Audio%20UltraFit%201000/Polk%20Audio%20UltraFit%201000.png)