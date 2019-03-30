# Beyerdynamic DT 440
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.7; 45 -1.1; 49 -1.4; 54 -1.8; 60 -2.4; 66 -2.9; 72 -3.4; 79 -3.8; 87 -4.2; 96 -4.6; 106 -5.0; 116 -5.3; 128 -5.5; 141 -5.5; 155 -5.5; 170 -5.5; 187 -5.6; 206 -5.4; 227 -5.1; 249 -4.9; 274 -4.6; 302 -4.3; 332 -4.0; 365 -3.7; 402 -3.4; 442 -3.1; 486 -2.9; 535 -3.2; 588 -3.1; 647 -2.9; 712 -3.0; 783 -3.2; 861 -3.5; 947 -4.1; 1042 -4.7; 1146 -5.2; 1261 -5.5; 1387 -5.8; 1526 -5.6; 1678 -5.8; 1846 -6.0; 2031 -6.5; 2234 -6.9; 2457 -7.3; 2703 -8.1; 2973 -9.2; 3270 -10.0; 3597 -10.6; 3957 -11.1; 4353 -12.1; 4788 -12.8; 5267 -13.2; 5793 -15.5; 6373 -17.6; 7010 -16.2; 7711 -9.1; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 440 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 440 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 31 Hz   | 0.61 | 6.5 dB   |
| Peaking | 609 Hz  | 0.65 | 3.7 dB   |
| Peaking | 6923 Hz | 1.22 | -18.0 dB |
| Peaking | 7995 Hz | 3.16 | 8.5 dB   |
| Peaking | 9425 Hz | 0.9  | 6.0 dB   |
| Peaking | 56 Hz   | 3.6  | 0.5 dB   |
| Peaking | 1208 Hz | 3    | -0.8 dB  |
| Peaking | 2356 Hz | 1.01 | 1.5 dB   |
| Peaking | 3196 Hz | 1.25 | -1.6 dB  |
| Peaking | 5316 Hz | 7.26 | 1.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.8 dB  |
| Peaking | 62 Hz    | 1.41 | 2.9 dB  |
| Peaking | 125 Hz   | 1.41 | -0.0 dB |
| Peaking | 250 Hz   | 1.41 | 0.8 dB  |
| Peaking | 500 Hz   | 1.41 | 3.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -6.4 dB |
| Peaking | 8000 Hz  | 1.41 | -3.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.9 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beyerdynamic%20DT%20440/Beyerdynamic%20DT%20440.png)