# JH Audio Layla Max
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.6; 23 -11.9; 25 -12.1; 28 -12.3; 31 -12.5; 34 -12.6; 37 -12.6; 41 -12.7; 45 -12.8; 49 -12.9; 54 -13.0; 60 -13.1; 66 -13.2; 72 -13.3; 79 -13.4; 87 -13.5; 96 -13.6; 106 -13.7; 116 -13.7; 128 -13.7; 141 -13.5; 155 -13.3; 170 -13.1; 187 -12.9; 206 -12.6; 227 -12.2; 249 -11.8; 274 -11.4; 302 -11.0; 332 -10.7; 365 -10.2; 402 -9.9; 442 -9.6; 486 -9.3; 535 -8.9; 588 -8.7; 647 -8.3; 712 -7.9; 783 -7.5; 861 -7.0; 947 -6.8; 1042 -7.3; 1146 -8.1; 1261 -8.4; 1387 -7.8; 1526 -6.5; 1678 -4.6; 1846 -2.6; 2031 -0.9; 2234 -0.5; 2457 -0.5; 2703 -0.6; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -8.0; 8482 -9.7; 9330 -7.2; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -11.8; 20000 -15.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JH Audio Layla Max GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JH Audio Layla Max ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 33 Hz    | 0.17 | -5.0 dB |
| Peaking | 203 Hz   | 0.3  | -3.6 dB |
| Peaking | 1317 Hz  | 2.3  | -5.0 dB |
| Peaking | 3265 Hz  | 0.43 | 7.2 dB  |
| Peaking | 8400 Hz  | 3.4  | -6.8 dB |
| Peaking | 2109 Hz  | 4.49 | 1.6 dB  |
| Peaking | 4541 Hz  | 0.5  | -0.9 dB |
| Peaking | 6002 Hz  | 2.8  | 2.7 dB  |
| Peaking | 19555 Hz | 1.24 | -9.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.7 dB |
| Peaking | 62 Hz    | 1.41 | -4.9 dB |
| Peaking | 125 Hz   | 1.41 | -6.0 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | -2.1 dB |
| Peaking | 2000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -1.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/JH%20Audio%20Layla%20Max/JH%20Audio%20Layla%20Max.png)