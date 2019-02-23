# Final Audio Pandora Hope 4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.7; 23 -10.8; 25 -10.8; 28 -10.9; 31 -10.8; 34 -10.7; 37 -10.6; 41 -10.3; 45 -9.9; 49 -9.5; 54 -9.4; 60 -9.9; 66 -10.6; 72 -11.0; 79 -10.8; 87 -10.2; 96 -9.3; 106 -8.0; 116 -8.6; 128 -10.7; 141 -10.6; 155 -9.4; 170 -8.5; 187 -9.6; 206 -9.5; 227 -9.3; 249 -9.6; 274 -9.2; 302 -8.9; 332 -8.5; 365 -8.5; 402 -8.1; 442 -7.9; 486 -7.9; 535 -7.8; 588 -7.2; 647 -7.1; 712 -7.9; 783 -8.0; 861 -7.9; 947 -7.5; 1042 -7.0; 1146 -6.6; 1261 -6.5; 1387 -6.8; 1526 -7.0; 1678 -6.8; 1846 -6.3; 2031 -5.8; 2234 -5.9; 2457 -5.5; 2703 -3.6; 2973 -0.5; 3270 -3.4; 3597 -1.8; 3957 -5.7; 4353 -7.6; 4788 -5.6; 5267 -1.3; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.9; 9330 -8.6; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio Pandora Hope 4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio Pandora Hope 4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.76 | -4.3 dB |
| Peaking | 73 Hz   | 3.37 | -2.3 dB |
| Peaking | 200 Hz  | 0.43 | -2.8 dB |
| Peaking | 3017 Hz | 3.97 | 5.5 dB  |
| Peaking | 5907 Hz | 4.15 | 6.8 dB  |
| Peaking | 109 Hz  | 8.03 | 1.7 dB  |
| Peaking | 132 Hz  | 7.4  | -2.0 dB |
| Peaking | 3666 Hz | 8.84 | 3.4 dB  |
| Peaking | 4223 Hz | 7.39 | -3.7 dB |
| Peaking | 9207 Hz | 6.44 | -2.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.3 dB |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Final%20Audio%20Pandora%20Hope%204/Final%20Audio%20Pandora%20Hope%204.png)