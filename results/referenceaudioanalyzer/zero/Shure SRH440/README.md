# Shure SRH440
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -1.0; 54 -2.3; 60 -3.6; 66 -4.3; 72 -4.4; 79 -4.2; 87 -4.4; 96 -4.8; 106 -5.4; 116 -5.6; 128 -5.6; 141 -5.3; 155 -5.1; 170 -4.9; 187 -4.6; 206 -4.9; 227 -5.2; 249 -5.5; 274 -6.0; 302 -6.4; 332 -7.1; 365 -7.5; 402 -7.4; 442 -6.8; 486 -6.3; 535 -6.0; 588 -5.8; 647 -5.6; 712 -5.6; 783 -5.5; 861 -5.3; 947 -5.1; 1042 -4.9; 1146 -5.3; 1261 -5.8; 1387 -5.9; 1526 -5.9; 1678 -5.5; 1846 -4.8; 2031 -4.2; 2234 -3.7; 2457 -4.6; 2703 -6.5; 2973 -7.7; 3270 -8.1; 3597 -8.7; 3957 -9.2; 4353 -9.1; 4788 -9.8; 5267 -10.7; 5793 -11.5; 6373 -12.7; 7010 -12.3; 7711 -8.7; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH440 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH440 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.67 | 6.6 dB  |
| Peaking | 190 Hz  | 3.2  | 1.6 dB  |
| Peaking | 964 Hz  | 1.88 | 1.5 dB  |
| Peaking | 2164 Hz | 3.97 | 3.3 dB  |
| Peaking | 5946 Hz | 1.71 | -5.9 dB |
| Peaking | 375 Hz  | 4.86 | -1.5 dB |
| Peaking | 3736 Hz | 1.51 | -3.3 dB |
| Peaking | 4946 Hz | 0.67 | 2.5 dB  |
| Peaking | 6929 Hz | 4.06 | -3.7 dB |
| Peaking | 8235 Hz | 4.19 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.4 dB  |
| Peaking | 62 Hz    | 1.41 | 1.7 dB  |
| Peaking | 125 Hz   | 1.41 | 0.6 dB  |
| Peaking | 250 Hz   | 1.41 | 0.7 dB  |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.7 dB |
| Peaking | 8000 Hz  | 1.41 | -2.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Shure%20SRH440/Shure%20SRH440.png)