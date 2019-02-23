# Polk Audio Buckle
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.5; 23 -15.6; 25 -15.6; 28 -15.7; 31 -15.6; 34 -15.5; 37 -15.4; 41 -15.2; 45 -15.0; 49 -14.8; 54 -14.5; 60 -14.2; 66 -13.8; 72 -13.3; 79 -12.7; 87 -12.8; 96 -13.5; 106 -13.8; 116 -13.7; 128 -13.6; 141 -13.5; 155 -13.3; 170 -12.5; 187 -12.9; 206 -12.9; 227 -12.6; 249 -12.5; 274 -11.6; 302 -9.9; 332 -9.7; 365 -8.9; 402 -8.7; 442 -8.4; 486 -8.1; 535 -7.7; 588 -7.3; 647 -6.9; 712 -7.3; 783 -8.0; 861 -8.8; 947 -8.7; 1042 -8.6; 1146 -8.2; 1261 -7.5; 1387 -7.2; 1526 -6.8; 1678 -6.3; 1846 -5.5; 2031 -4.7; 2234 -4.3; 2457 -3.8; 2703 -3.1; 2973 -3.8; 3270 -4.1; 3597 -3.2; 3957 -1.3; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio Buckle GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio Buckle ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.7  | -7.0 dB |
| Peaking | 40 Hz   | 0.72 | -5.4 dB |
| Peaking | 159 Hz  | 0.55 | -6.1 dB |
| Peaking | 2535 Hz | 3.11 | 2.3 dB  |
| Peaking | 4973 Hz | 1.65 | 6.8 dB  |
| Peaking | 244 Hz  | 4.77 | -1.4 dB |
| Peaking | 832 Hz  | 0.53 | 1.9 dB  |
| Peaking | 1010 Hz | 1.39 | -3.7 dB |
| Peaking | 6478 Hz | 4.44 | 3.8 dB  |
| Peaking | 7245 Hz | 1.63 | -2.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.0 dB |
| Peaking | 62 Hz    | 1.41 | -4.6 dB  |
| Peaking | 125 Hz   | 1.41 | -5.6 dB  |
| Peaking | 250 Hz   | 1.41 | -4.7 dB  |
| Peaking | 500 Hz   | 1.41 | 0.4 dB   |
| Peaking | 1000 Hz  | 1.41 | -2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Polk%20Audio%20Buckle/Polk%20Audio%20Buckle.png)