# 64 Audio N8 custom sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.2; 25 -1.8; 28 -2.6; 31 -3.2; 34 -3.8; 37 -4.3; 41 -4.8; 45 -5.3; 49 -5.6; 54 -6.0; 60 -6.6; 66 -7.2; 72 -7.6; 79 -8.1; 87 -8.7; 96 -9.1; 106 -9.3; 116 -9.8; 128 -10.1; 141 -10.3; 155 -10.5; 170 -10.6; 187 -10.8; 206 -10.6; 227 -10.7; 249 -10.6; 274 -10.5; 302 -10.2; 332 -9.9; 365 -9.6; 402 -9.3; 442 -9.0; 486 -8.6; 535 -8.2; 588 -7.8; 647 -7.3; 712 -6.7; 783 -6.3; 861 -5.8; 947 -5.6; 1042 -5.8; 1146 -6.5; 1261 -7.4; 1387 -8.1; 1526 -8.3; 1678 -8.1; 1846 -7.7; 2031 -7.3; 2234 -6.6; 2457 -5.8; 2703 -4.7; 2973 -3.7; 3270 -2.9; 3597 -2.6; 3957 -3.1; 4353 -3.7; 4788 -4.3; 5267 -2.6; 5793 -0.6; 6373 -1.1; 7010 -4.1; 7711 -6.3; 8482 -6.6; 9330 -6.6; 10263 -6.6; 11289 -6.6; 12418 -6.6; 13660 -6.6; 15026 -10.0; 16529 -15.3; 18182 -16.3; 20000 -6.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8 custom sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8 custom sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 16 Hz    | 0.61 | 7.3 dB   |
| Peaking | 188 Hz   | 0.54 | -4.5 dB  |
| Peaking | 3499 Hz  | 2.74 | 4.1 dB   |
| Peaking | 5963 Hz  | 3.3  | 6.3 dB   |
| Peaking | 17681 Hz | 1.47 | -11.5 dB |
| Peaking | 939 Hz   | 2.45 | 2.0 dB   |
| Peaking | 1553 Hz  | 2.35 | -2.1 dB  |
| Peaking | 7872 Hz  | 7.2  | -1.0 dB  |
| Peaking | 12533 Hz | 3.49 | 1.1 dB   |
| Peaking | 13874 Hz | 7.42 | 2.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 16000 Hz | 1.41 | -7.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/64%20Audio%20N8%20custom%20sample%202/64%20Audio%20N8%20custom%20sample%202.png)