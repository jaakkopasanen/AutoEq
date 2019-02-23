# Polk Audio UltraFit 2000 sample A
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -1.4; 66 -2.9; 72 -4.2; 79 -5.3; 87 -6.4; 96 -7.5; 106 -8.0; 116 -8.3; 128 -8.5; 141 -8.5; 155 -8.4; 170 -8.1; 187 -7.7; 206 -7.4; 227 -7.0; 249 -6.6; 274 -6.1; 302 -5.6; 332 -4.6; 365 -4.3; 402 -3.7; 442 -2.8; 486 -2.3; 535 -1.7; 588 -0.7; 647 -0.5; 712 -0.5; 783 -0.5; 861 -3.2; 947 -7.0; 1042 -10.0; 1146 -10.9; 1261 -11.6; 1387 -12.0; 1526 -12.1; 1678 -12.4; 1846 -12.8; 2031 -12.5; 2234 -11.4; 2457 -9.1; 2703 -7.2; 2973 -5.4; 3270 -5.3; 3597 -6.4; 3957 -6.8; 4353 -5.6; 4788 -3.2; 5267 -0.6; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -8.1; 8482 -13.0; 9330 -13.9; 10263 -9.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -10.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFit 2000 sample A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFit 2000 sample A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.4dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 34 Hz   | 1.1  | 7.3 dB   |
| Peaking | 695 Hz  | 1.37 | 10.1 dB  |
| Peaking | 1381 Hz | 0.86 | -8.6 dB  |
| Peaking | 5992 Hz | 1.49 | 8.0 dB   |
| Peaking | 8838 Hz | 2.94 | -10.7 dB |
| Peaking | 58 Hz   | 3.17 | 3.3 dB   |
| Peaking | 127 Hz  | 1.28 | -3.0 dB  |
| Peaking | 2162 Hz | 2.96 | -3.5 dB  |
| Peaking | 3057 Hz | 1.27 | 3.8 dB   |
| Peaking | 3982 Hz | 3.05 | -3.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 3.6 dB  |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | 6.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | -7.7 dB |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Polk%20Audio%20UltraFit%202000%20sample%20A/Polk%20Audio%20UltraFit%202000%20sample%20A.png)