# Noble Audio Trident
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.7; 23 -5.8; 25 -5.9; 28 -6.1; 31 -6.3; 34 -6.5; 37 -6.6; 41 -6.9; 45 -7.1; 49 -7.3; 54 -7.5; 60 -7.8; 66 -8.1; 72 -8.5; 79 -8.8; 87 -9.2; 96 -9.7; 106 -10.0; 116 -10.4; 128 -10.7; 141 -10.9; 155 -11.2; 170 -11.3; 187 -11.3; 206 -11.3; 227 -11.2; 249 -11.1; 274 -10.9; 302 -10.6; 332 -10.3; 365 -10.0; 402 -9.6; 442 -9.3; 486 -8.8; 535 -8.3; 588 -7.7; 647 -7.1; 712 -6.4; 783 -5.6; 861 -5.0; 947 -4.5; 1042 -4.3; 1146 -4.6; 1261 -5.0; 1387 -5.0; 1526 -4.7; 1678 -4.1; 1846 -3.5; 2031 -3.1; 2234 -2.9; 2457 -2.3; 2703 -0.7; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -3.1; 4788 -7.2; 5267 -8.2; 5793 -11.5; 6373 -14.7; 7010 -13.8; 7711 -10.4; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noble Audio Trident GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noble Audio Trident ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 124 Hz  | 0.95 | -1.9 dB  |
| Peaking | 255 Hz  | 0.55 | -4.1 dB  |
| Peaking | 934 Hz  | 1.73 | 2.4 dB   |
| Peaking | 3331 Hz | 1.02 | 7.2 dB   |
| Peaking | 6366 Hz | 2.55 | -10.8 dB |
| Peaking | 22 Hz   | 1.32 | 1.0 dB   |
| Peaking | 4118 Hz | 9.24 | 2.2 dB   |
| Peaking | 4715 Hz | 6.9  | -2.5 dB  |
| Peaking | 7408 Hz | 6.73 | -4.9 dB  |
| Peaking | 7848 Hz | 2.67 | 3.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.7 dB  |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -4.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.9 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Noble%20Audio%20Trident/Noble%20Audio%20Trident.png)