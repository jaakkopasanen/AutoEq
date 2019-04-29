# Audio Genetic AG2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.8; 23 -4.1; 25 -4.4; 28 -4.8; 31 -5.1; 34 -5.3; 37 -5.6; 41 -5.9; 45 -6.1; 49 -6.3; 54 -6.5; 60 -6.8; 66 -7.1; 72 -7.5; 79 -7.9; 87 -8.3; 96 -8.8; 106 -9.2; 116 -9.6; 128 -10.0; 141 -10.2; 155 -10.5; 170 -10.6; 187 -10.7; 206 -10.8; 227 -10.8; 249 -10.7; 274 -10.6; 302 -10.4; 332 -10.3; 365 -10.0; 402 -9.8; 442 -9.5; 486 -9.2; 535 -8.8; 588 -8.3; 647 -7.9; 712 -7.4; 783 -6.8; 861 -6.3; 947 -6.0; 1042 -6.0; 1146 -6.5; 1261 -7.0; 1387 -7.1; 1526 -6.6; 1678 -5.8; 1846 -4.9; 2031 -3.9; 2234 -2.9; 2457 -2.6; 2703 -3.3; 2973 -2.3; 3270 -1.1; 3597 -0.6; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.1; 5793 -3.5; 6373 -4.0; 7010 -7.3; 7711 -7.3; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.8; 16529 -8.0; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Genetic AG2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Genetic AG2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 12 Hz    | 0.36 | 3.3 dB  |
| Peaking | 212 Hz   | 0.5  | -4.5 dB |
| Peaking | 2892 Hz  | 1.15 | 2.9 dB  |
| Peaking | 4607 Hz  | 1.41 | 5.3 dB  |
| Peaking | 7366 Hz  | 3.35 | -3.0 dB |
| Peaking | 949 Hz   | 1.77 | 2.9 dB  |
| Peaking | 1331 Hz  | 0.77 | -2.7 dB |
| Peaking | 2306 Hz  | 1.39 | 2.4 dB  |
| Peaking | 2739 Hz  | 6.42 | -2.1 dB |
| Peaking | 15718 Hz | 3.46 | -2.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.0 dB  |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | -1.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Audio%20Genetic%20AG2/Audio%20Genetic%20AG2.png)