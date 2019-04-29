# JH Audio Angie Min
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.7; 28 -1.0; 31 -1.4; 34 -1.9; 37 -2.3; 41 -2.8; 45 -3.2; 49 -3.4; 54 -3.8; 60 -4.3; 66 -4.8; 72 -5.3; 79 -5.8; 87 -6.3; 96 -6.8; 106 -7.3; 116 -7.7; 128 -8.1; 141 -8.4; 155 -8.8; 170 -8.9; 187 -9.1; 206 -9.2; 227 -9.2; 249 -9.3; 274 -9.3; 302 -9.3; 332 -9.3; 365 -9.2; 402 -9.2; 442 -9.2; 486 -9.1; 535 -9.0; 588 -8.8; 647 -8.7; 712 -8.5; 783 -8.3; 861 -8.2; 947 -8.7; 1042 -9.8; 1146 -11.1; 1261 -12.1; 1387 -12.3; 1526 -11.6; 1678 -9.8; 1846 -7.5; 2031 -5.2; 2234 -3.4; 2457 -2.3; 2703 -2.5; 2973 -2.9; 3270 -1.8; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.4; 7711 -9.4; 8482 -10.8; 9330 -6.8; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -13.0; 20000 -18.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JH Audio Angie Min GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JH Audio Angie Min ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 0.78 | 6.1 dB   |
| Peaking | 2901 Hz  | 1.5  | 4.2 dB   |
| Peaking | 6845 Hz  | 0.6  | 15.2 dB  |
| Peaking | 8140 Hz  | 2.34 | -13.8 dB |
| Peaking | 13640 Hz | 0.01 | -5.1 dB  |
| Peaking | 864 Hz   | 1.08 | 3.8 dB   |
| Peaking | 1413 Hz  | 1.37 | -6.7 dB  |
| Peaking | 2248 Hz  | 1.3  | 4.0 dB   |
| Peaking | 2922 Hz  | 4.73 | -3.3 dB  |
| Peaking | 22050 Hz | 2.57 | 0.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | -4.1 dB |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | 8.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | -1.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/JH%20Audio%20Angie%20Min/JH%20Audio%20Angie%20Min.png)