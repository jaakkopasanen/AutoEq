# First Harmonic IEB6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.9; 34 -1.5; 37 -2.1; 41 -2.7; 45 -3.3; 49 -3.9; 54 -4.5; 60 -5.2; 66 -5.8; 72 -6.4; 79 -7.0; 87 -7.6; 96 -8.1; 106 -8.4; 116 -8.7; 128 -8.9; 141 -9.2; 155 -9.1; 170 -9.1; 187 -9.0; 206 -8.8; 227 -8.5; 249 -8.2; 274 -7.8; 302 -7.3; 332 -6.8; 365 -6.3; 402 -5.8; 442 -5.1; 486 -4.7; 535 -4.2; 588 -3.5; 647 -3.0; 712 -2.8; 783 -2.4; 861 -2.5; 947 -2.8; 1042 -3.3; 1146 -3.7; 1261 -4.2; 1387 -5.0; 1526 -5.7; 1678 -6.2; 1846 -6.4; 2031 -6.7; 2234 -7.2; 2457 -5.1; 2703 -6.8; 2973 -8.3; 3270 -7.7; 3597 -6.2; 3957 -5.8; 4353 -7.5; 4788 -8.8; 5267 -10.1; 5793 -14.0; 6373 -13.0; 7010 -8.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`First Harmonic IEB6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `First Harmonic IEB6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.54 | 6.5 dB  |
| Peaking | 148 Hz  | 0.49 | -3.6 dB |
| Peaking | 842 Hz  | 0.68 | 5.1 dB  |
| Peaking | 1730 Hz | 0.87 | -1.9 dB |
| Peaking | 5961 Hz | 4.86 | -8.8 dB |
| Peaking | 2498 Hz | 9.04 | 2.5 dB  |
| Peaking | 3059 Hz | 2.83 | -2.5 dB |
| Peaking | 3806 Hz | 3.2  | 2.8 dB  |
| Peaking | 4627 Hz | 3.17 | -1.4 dB |
| Peaking | 7569 Hz | 6.49 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | 2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | -1.6 dB |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/First%20Harmonic%20IEB6/First%20Harmonic%20IEB6.png)