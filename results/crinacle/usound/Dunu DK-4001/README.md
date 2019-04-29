# Dunu DK-4001
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.0; 23 -5.3; 25 -5.5; 28 -5.7; 31 -5.9; 34 -6.1; 37 -6.2; 41 -6.3; 45 -6.4; 49 -6.5; 54 -6.6; 60 -6.7; 66 -6.9; 72 -7.1; 79 -7.2; 87 -7.4; 96 -7.6; 106 -7.8; 116 -7.9; 128 -8.0; 141 -7.9; 155 -8.0; 170 -8.2; 187 -8.1; 206 -8.0; 227 -7.9; 249 -7.8; 274 -7.7; 302 -7.5; 332 -7.4; 365 -7.3; 402 -7.3; 442 -7.2; 486 -7.2; 535 -7.1; 588 -7.1; 647 -7.1; 712 -7.1; 783 -7.0; 861 -7.1; 947 -7.3; 1042 -7.6; 1146 -8.4; 1261 -9.4; 1387 -10.0; 1526 -10.1; 1678 -9.7; 1846 -8.8; 2031 -7.4; 2234 -5.8; 2457 -4.2; 2703 -2.7; 2973 -1.5; 3270 -0.7; 3597 -0.5; 3957 -0.5; 4353 -0.8; 4788 -2.3; 5267 -5.0; 5793 -7.6; 6373 -8.4; 7010 -9.7; 7711 -10.2; 8482 -6.7; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -11.6; 20000 -7.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dunu DK-4001 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu DK-4001 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 176 Hz   | 0.68 | -1.6 dB |
| Peaking | 1656 Hz  | 1.19 | -7.1 dB |
| Peaking | 4053 Hz  | 0.59 | 10.1 dB |
| Peaking | 6602 Hz  | 1.35 | -9.5 dB |
| Peaking | 18622 Hz | 1.87 | -6.0 dB |
| Peaking | 20 Hz    | 1.17 | 1.4 dB  |
| Peaking | 17919 Hz | 1.8  | -0.4 dB |
| Peaking | 18151 Hz | 2.97 | 0.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -0.3 dB |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Dunu%20DK-4001/Dunu%20DK-4001.png)